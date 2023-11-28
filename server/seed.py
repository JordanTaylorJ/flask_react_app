from app import app
from models import db, User 

with app.app_context():
    User.query.delete()

    users=[]
    user = User(username="Admin", password="123")
    users.append(user)
    user2 = User(username="Jordan", password='123')
    users.append(user2)
    
    db.session.add_all(users)
    db.session.commit()

print('seeded')