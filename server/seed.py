from app import app
from models import db, User, Log, Aircraft   

users_list = [
    {'email': "admin@hello.com", 'password': "123", 'first_name': 'Admin', 'last_name':'Admin'},
    {'email': "jordan@hello.com", 'password':'123', 'first_name': 'Jordan', 'last_name': 'Joseph'}
]

def make_users():
    User.query.delete()
    db.session.commit()
    users = []
    
    for user_dict in users_list:
        user = User(
            email = user_dict["email"],
            first_name = user_dict['first_name'],
            last_name = user_dict['last_name']
        )
        user.password_hash = user_dict['password']
        users.append(user)
    
    db.session.add_all(users)
    db.session.commit()

print('users created')

logs_list = [
    {'user_id': 1, 'aircraft_id': 1, 'date': "05/26/2023", 'from_to': '', 'remarks_and_endorsements': '', 'takeoffs': 1, 'landings': 1, 'single_engine_land': 0.9, 'multi_engine_land': 0, 'night':0, 'actual_instrument':0, 'simulated_instrument':0, 'cross_country':0, 'flight_instructor':0, 'dual_received': 0.9, 'pilot_in_command': 0.9, 'total_duration': 0.9},
    {'user_id': 2, 'aircraft_id': 1, 'date': "05/27/2023", 'from_to': '', 'remarks_and_endorsements': '', 'takeoffs': 3, 'landings': 3, 'single_engine_land': 1.4, 'multi_engine_land': 0, 'night':0, 'actual_instrument':0, 'simulated_instrument':0, 'cross_country':0, 'flight_instructor':0, 'dual_received': 1.4, 'pilot_in_command': 1.4, 'total_duration': 1.4},
    {'user_id': 2, 'aircraft_id': 2, 'date': "05/28/2023", 'from_to': '', 'remarks_and_endorsements': '', 'takeoffs': 2, 'landings': 2, 'single_engine_land': 1.2, 'multi_engine_land': 0, 'night':0, 'actual_instrument':0, 'simulated_instrument':0, 'cross_country':0, 'flight_instructor':0, 'dual_received': 1.2, 'pilot_in_command': 1.2, 'total_duration': 1.2}
]

def make_logs():
    Log.query.delete()
    db.session.commit()
    
    logs = []

    for log_dict in logs_list:
        log = Log(
            user_id = log_dict['user_id'],
            aircraft_id = log_dict['aircraft_id'],
            date = log_dict['date'],
            from_to = log_dict['from_to'],
            remarks_and_endorsements = log_dict['remarks_and_endorsements'],
            takeoffs = log_dict['takeoffs'],
            landings = log_dict['landings'],
            single_engine_land = log_dict['single_engine_land'],
            multi_engine_land = log_dict['multi_engine_land'],
            night = log_dict['night'],
            actual_instrument = log_dict['actual_instrument'],
            simulated_instrument = log_dict['simulated_instrument'],
            cross_country = log_dict['cross_country'],
            flight_instructor = log_dict['flight_instructor'],
            dual_received = log_dict['dual_received'],
            pilot_in_command = log_dict['pilot_in_command'],
            total_duration = log_dict['total_duration']
        )
        logs.append(log)
    
    db.session.add_all(logs)
    db.session.commit()

print('logs created')

aircraft_list = [
    {'aircraft_type':'C182', 'ident':'N4741N'},
    {'aircraft_type':'C172', 'ident':'N4842O'},
    {'aircraft_type':'C210', 'ident':'N4943P'}
]

def make_aircrafts():
    Aircraft.query.delete()
    db.session.commit()
    
    aircrafts = []
    
    for aircraft_dict in aircraft_list:    
        aircraft = Aircraft(
            aircraft_type = aircraft_dict['aircraft_type'],
            ident = aircraft_dict['ident'],
        )
        aircrafts.append(aircraft)
    
    db.session.add_all(aircrafts)
    db.session.commit()

print('aircraft created')

with app.app_context():
    db.drop_all()
    db.create_all()
    make_users()
    make_logs()
    make_aircrafts()

print('seeded')