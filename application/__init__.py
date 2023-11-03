from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://127.0.0.1:27017"
app.config["SECRET_KEY"] = "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"

mongodb_client = PyMongo(app)
db = mongodb_client.db

from application import routes
