from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy import MetaData 

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class User(db.Model):
    __tablename__ = 'users' 

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(3), unique=True)
    password = db.Column(db.String(3))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    logs = db.relationship('Log', backref='log')

    def __repr__(self):
        return f'<User {self.name}>'
    
class Log(db.Model):
    __tablename__ = 'logs'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id')) 

    