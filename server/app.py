from flask import Flask, make_response
from flask_migrate import Migrate 
from flask_restful import Resource 

from config import app, db, api 
from models import User

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

    if user:
        body = user.to_dict()
        status = 200
    else:
        body = {'message': f'404: {id} not found'}
        status = 404
    
    return make_response(body, status)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
