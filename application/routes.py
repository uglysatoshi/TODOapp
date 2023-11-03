from application import app, db
from flask import render_template, flash, request, redirect
from .forms import TodoForm
from datetime import datetime


@app.route("/")
def index():
    return render_template("view_todos.html")


@app.route("/add_todo", methods=["POST", "GET"])
def add_todo():
    if request.method == "POST":
        form = TodoForm(request.form)
        todo_name = form.name.data
        todo_description = form.description.data
        todo_completed = form.completed.data

        db.todo_flask.insert_one({
            "name": todo_name,
            "description": todo_description,
            "completed": todo_completed,
            "date_completed": datetime.now()
        })
        flash("Your TODO is successfully inserted", "success")
        return redirect("/")
    else:
        form = TodoForm()
        return render_template("add_todo.html", form=form)
