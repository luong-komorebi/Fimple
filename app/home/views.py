from flask import render_template, request
from app import db
from app.models import Category, Priority, Todo
from . import home

@home.route('/')
def list_all():
    categories = Category.query.all()
    todos = Todo.query.join(Priority).order_by(Priority.value.desc())
    return render_template('list.html', categories=categories, todos=todos)

@home.route('/new-task', methods=['POST'])
def new():
    if request.method == 'POST':
        category = Category.query.filter_by(id=request.form['category']).first()
        priority = Priority.query.filter_by(id=request.form['priority']).first()
        todo = Todo(category, priority, request.form['description'])
        db.session.add(todo)
        db.session.commit()
        return redirect('/')
    else:
        categories = Category.query.all()
        priorities = Priority.query.all()
        return render_template(
            'new-task.html',
            page='new-task',
            categories=categories,
            priorities=priorities)

@home.route('/<name>')
def list_todos(name):
    category = Category.query.filter_by(name=name).first()
    categories = Category.query.all()
    return render_template(
        'list.html',
        todos=Todo.query.filter_by(category=category).all(),
        categories=categories)

@home.route('/<int:todo_id>', methods=['GET', 'POST'])
def update_todo(todo_id):
    todo = Todo.query.get(todo_id)
    categories = Category.query.all()
    if request.method == 'GET':
        return render_template(
            'new-task.html',
            todo=todo,
            categories=categories)
    else:
        category = Category.query.filter_by(id=request.form['category']).first()
        description = request.form['description']
        todo.category = category
        todo.description = description
        db.session.commit()
        return redirect('/')


@home.route('/new-category', methods=['GET', 'POST'])
def new_category():
    if request.method == 'POST':
        category = Category(name=request.form['category'])
        db.session.add(category)
        db.session.commit()
        return redirect('/')
    else:
        return render_template(
            'new-category.html',
            page='new-category.html')


@home.route('/edit_category/<int:category_id>', methods=['GET', 'POST'])
def edit_category(category_id):
    category = Category.query.get(category_id)
    if request.method == 'GET':
        return render_template(
            'new-category.html',
            category=category)
    else:
        category_name = request.form['category']
        category.name = category_name
        db.session.commit()
        return redirect('/')


@home.route('/delete-category/<int:category_id>', methods=['POST'])
def delete_category(category_id):
    if request.method == 'POST':
        category = Category.query.get(category_id)
        if not category.todos:
            db.session.delete(category)
            db.session.commit()
        else:
            flash('You have TODOs in that category. Remove them first.')
        return redirect('/')


@home.route('/delete-todo/<int:todo_id>', methods=['POST'])
def delete_todo(todo_id):
    if request.method == 'POST':
        todo = Todo.query.get(todo_id)
        db.session.delete(todo)
        db.session.commit()
        return redirect('/')


@home.route('/mark-done/<int:todo_id>', methods=['POST'])
def mark_done(todo_id):
    if request.method == 'POST':
        todo = Todo.query.get(todo_id)
        todo.is_done = True
        db.session.commit()
        return redirect('/')
