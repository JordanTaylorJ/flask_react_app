from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy import MetaData 

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)

class User(db.Model):
    __tablename__ = 'users' 

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(3), unique=True)
    password = db.Column(db.String(3))

    def __repr__(self):
        return f'<User {self.name}>'
    