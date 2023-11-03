from application import app, db
from flask import render_template, flash, request, redirect, url_for
from .forms import TodoForm
from datetime import datetime
from bson import ObjectId


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


@app.route("/update_todo/<id>", methods=["POST", "GET"])
def update_todo(id):
    if request.method == "POST":
        form = TodoForm(request.form)
        todo_name = form.name.data
        todo_description = form.description.data
        todo_completed = form.completed.data

        db.todo_flask.find_one_and_update({"_id": ObjectId(id)}, {"$set": {
            "name": todo_name,
            "description": todo_description,
            "completed": todo_completed,
            "date_created": datetime.now()
        }})

        flash("Todo is successfully updated", "success")
        return redirect("/")

    else:
        form = TodoForm()
        todo = db.todo_flask.find_one_or_404({"_id": ObjectId(id)})
        print(todo)
        form.name.data = todo.get("name", None)
        form.description.data = todo.get("description", None)
        form.completed.data = todo.get("completed", None)

    return render_template("add_todo.html", form=form)
