from flask import Flask, make_response, request, abort, session
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

class Signup(Resource):
    def post(self):
        email = request.get_json()['email']
        password = request.get_json()['password']
        if email and password:
            new_user = User(email = email)
            new_user.password_hash = password
            db.session.add(new_user)
            db.session.commit()

            session['user_id'] = new_user.id
            return new_user.to_dict(), 201
        return {'error': '422 Unprocessable Entity'}, 422

api.add_resource(Signup, '/signup', endpoint='signup')

class Login(Resource):
    def post(self):
        try:
            email = request.get_json().get('email')
            user = User.query.filter(User.email == email).first()
            print('pass', request.get_json()['password'])
            print('auth', user.authenticate(request.get_json()['password']))
            if user.authenticate(request.get_json()['password']):
                print('here3')
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
            user_id = session['user_id']
            if user_id:
                user = User.query.filter(User.id == user_id).first()
                response = make_response(
                    user.to_dict,
                    200
                )
                return response 
        except:
            abort(401, "Unauthorized")

api.add_resource(AuthorizedSession, '/auth')



if __name__ == '__main__':
    app.run(port=5555, debug=True)
