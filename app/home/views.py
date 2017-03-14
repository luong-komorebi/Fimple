from flask import render_template, request, redirect, url_for, flash
from app import db
from app.models import Category, Priority, Todo
from app.home import home

@home.route('/')
def list_all():
    return render_template(
        'list.html',
        categories=Category.query.all(),
        todos=Todo.query.all())


@home.route('/<name>')
def list_todos(name):
    category = Category.query.filter_by(name=name).first()
    return render_template(
        'list.html',
        todos=Todo.query.filter_by(category=category).all(),# .join(Priority).order_by(Priority.value.desc()),
        categories=Category.query.all())


@home.route('/new-task', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        category = Category.query.filter_by(id=request.form['category']).first()
        todo = Todo(category=category, description=request.form['description'])
        db.session.add(todo)
        db.session.commit()
        return redirect(url_for('home.list_all'))
    else:
        return render_template(
            'new-task.html',
            page='new-task',
            categories=Category.query.all())



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
        todos = Todo.query.filter_by(category_id=category_id).all()
        if not todos:
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
