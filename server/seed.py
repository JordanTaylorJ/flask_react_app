from app import app
from models import db, User, Log, Aircraft

with app.app_context():
    User.query.delete()

    users=[]
    user = User(email="admin@hello.com", password="123")
    users.append(user)
    user2 = User(email="jordan@hello.com", password='123')
    users.append(user2)
    
    db.session.add_all(users)
    db.session.commit()

print('seeded')