from flask import Flask, make_response, request, abort, session
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

class Login(Resource):
    def post(self):
        print('here')
        print(request.get_json())
        try:
            email = request.get_json().get('email')
            print('email', email)
            user = User.query.filter(User.email == email).first()
            print('here2')
            if user.authenticate(request.get_json()['password']):
                print(user, 'user')
                session['user_id'] = user.id 
                response = make_response(
                    user.to_dict(),
                    200
                )
                return response
        except: 
            abort:(401, "Incorrect email or password.")

api.add_resource(Login, '/login')

class AuthorizedSession(Resource):
    def get(self):
        try:
            user = User.query.filter_by(id =session['user_id']).first()
            response = make_response(
                user.to_dict,
                200
            )
        except:
            abort(401, "Unauthorized")

api.add_resource(AuthorizedSession, '/auth')



if __name__ == '__main__':
    app.run(port=5555, debug=True)
