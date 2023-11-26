from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy import MetaData 

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)

class User(db.Model):
    __tablename__ = 'users' 

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String)
    password = db.Column(db.String)