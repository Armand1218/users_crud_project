from flask import Flask, render_template, request, redirect
from flask_app import app
from flask_app.models.user import User

@app.route('/')
def index():
    return redirect('/all_user')

@app.route('/all_user')
def all_user():
    return render_template("user.html", all_users = User.get_all())

@app.route('/add/user')
def add_user():
    return render_template("index.html", user = User.get_one_db)

@app.route('/create/user', methods=['POST'])
def create_user():
    User.save_db(request.form)
    return redirect('/all_user')

@app.route('/edit/user/<int:id>')
def edit(id):
    data = {
        "id": id
    }
    return render_template("user_edit.html", user = User.get_one_db(data))

@app.route('/update/user', methods=['POST'])
def update_user():
    User.update_db(request.form)
    return redirect('/all_user')

@app.route('/show_page/user/<int:id>')
def show_user(id):
    data = {
        "id": id
    }
    return render_template("user_info.html", user = User.get_one_db(data))

@app.route('/delete/user/<int:id>')
def delete_user(id):
    data = {
        "id": id
    }
    User.delete_db(data)
    return redirect('/all_user')