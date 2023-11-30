from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy_serializer import SerializerMixin

from config import db, bcrypt 

class User(db.Model, SerializerMixin):
    __tablename__ = 'users' 

    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(3), unique=True)
    password = db.Column(db.String(3))
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    logs = db.relationship('Log', back_populates='user')

    serialize_rules = ('-logs.user',) 

    def __repr__(self):
        return f'<User {self.first_name} {self.last_name}>'
    
class Log(db.Model, SerializerMixin):
    __tablename__ = 'logs'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id')) 
    aircraft_id = db.Column(db.Integer, db.ForeignKey('aircrafts.id'))
    date = db.Column(db.String)
    from_to = db.Column(db.Text)
    remarks_and_endorsements = db.Column(db.Text)
    takeoffs = db.Column(db.Float)
    landings = db.Column(db.Float)
    single_engine_land = db.Column(db.Float)
    multi_engine_land = db.Column(db.Float)
    night = db.Column(db.Float)
    actual_instrument = db.Column(db.Float)
    simulated_instrument = db.Column(db.Float)
    cross_country = db.Column(db.Float)
    flight_instructor = db.Column(db.Float)
    dual_received = db.Column(db.Float)
    pilot_in_command = db.Column(db.Float)
    total_duration = db.Column(db.Float)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    user = db.relationship('User', back_populates='logs')
    aircraft = db.relationship('Aircraft', back_populates='logs')
    
    serialize_rules = ('-user.logs', '-aircraft.logs',)

    def __repr__(self):
        return f'<Log {self.date}, {self.total_duration}>'

class Aircraft(db.Model, SerializerMixin):
    __tablename__='aircrafts'

    id = db.Column(db.Integer, primary_key=True)
    aircraft_type = db.Column(db.String)
    ident = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    logs = db.relationship('Log', back_populates='aircraft')

    serialize_rules = ('-log.aircraft',)

    def __repr__(self):
        return f'<Aircraft {self.aircraft_type} {self.ident}>'