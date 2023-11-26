from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate 

app = Flask(__name__)

@app.route("/")
def index():
    return "bing bong!"