from flask import Flask, make_response
from flask import request, session 
from flask_migrate import Migrate 
#from flask_restful import Resource 

from models import db, User

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db, render_as_batch=True)

db.init_app(app)

@app.route('/')
def index():
    response= make_response(
        '<h1>Hello World</h1>',
        200
    )
    return response

@app.route('/users/<int:id>')
def user_by_id(id):
    user = User.query.filter(User.id == id).first()

    if not user:
        response_body = '<h1>404 user not found</h1>'
        response = make_response(response_body, 404)
        return response 

    response_body = f'''
        <h1> User:{user.username} </h1>
    '''
    response = make_response(response_body, 200)
    return response 

if __name__ == '__main__':
    app.run(port=5555, debug=True)
