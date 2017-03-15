# Fimple : Simple Todolist App made with Flask

![](demo.png) 

### About

This is a simple todolist web app made with Flask framework and some additionals middlewares/tools. It can be run in any browser with ease. 

### Requirements

This app is developed with:
- Python 3.5
- Pip 9.0.1
- PostgreSQL 9.5.6
    - appdirs==1.4.3
    - click==6.7
    - Flask==0.12
    - Flask-Migrate==2.0.3
    - Flask-Script==2.0.5
    - Flask-SQLAlchemy==2.2
    - itsdangerous==0.24
    - Jinja2==2.9.5
    - Mako==1.0.6
    - MarkupSafe==1.0
    - packaging==16.8
    - psycopg2==2.7
    - pyparsing==2.2.0
    - python-editor==1.0.3
    - six==1.10.0
    - SQLAlchemy==1.1.6
    - Werkzeug==0.12

### How to run it locally

1. Create a working directory and cd into it. 
`mkdir workspace && cd workspace`  

2. Create a virtual environment.   
`virtualenv venv`
 _You should know what is virtualenv and how it works_  

3. Use python inside virtualenv   
`source venv/bin/activate`  

4. Install requirements   
`pip install -r requirements.txt`  

5. Install PostgreSQL  
https://www.postgresql.org/download/  

6. Switch to Postgre account  
`sudo su - postgres`  

7. Run Postgre  
`psql`  

8. Create a datbase user with a password  
`create user $user_name_here with password $'pass_word_here';`  

9. Create database instance  
`create database $app_name_here owner $user_name_here encoding 'utf-8';`  

10. You may wish to change the config in instace/config.py  
`SQLALCHEMY_DATABASE_URI = 'postgresql://$user_name_here:$password_here@localhost/$app_name_here'`  

11. Run the app  
```bash
export FLASK_CONFIG=development
export FLASK_APP=run.py
flask run
```  

12. Recreate Migration folder if you want 
```bash
flask db init
flask db migrate
flask db upgrade
```
  
### License

MIT License




