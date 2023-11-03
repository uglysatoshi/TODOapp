from application import app, db
from flask import render_template, flash, request, redirect
from .forms import TodoForm
from datetime import datetime


@app.route("/")
def get_todos():
    todos = []
    for todo in db.todo_flask.find().sort("date_created", -1):
        todo["_id"] = str(todo["_id"])
        todo["date_created"] = todo["date_created"].strftime("%d.%b.%Y %H:%M:%S")
        todos.append(todo)

    return render_template("view_todos.html", todos=todos)


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
            "date_created": datetime.now()
        })
        flash("Your TODO is successfully inserted", "success")
        return redirect("/")
    else:
        form = TodoForm()
        return render_template("add_todo.html", form=form)
