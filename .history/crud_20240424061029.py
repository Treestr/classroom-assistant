"""CRUD operations"""

from model import db, Teacher, Student, Homeroom, Attendance, Location, MovementLog, Group, GroupMembership, connect_to_db 

if __name__ == '__main__':
    from server import app
    connect_to_db(app)

MOVIE RATINGS EXAMPLES:

def create_user(email, password):
    """Create and return a new user."""

    user = __blank__(email=__blank__, password=__blank__)

    return user





# from model import db, User, Movie, Rating, connect_to_db
# 
# from flask import Flask, request, jsonifyfrom models import db,Teacher, Student, Homeroom, Location, MovementLog, Attendance 
# from datetime import datetime
# app = Flask(__name__)
# 
# app.config[SQLALCHEMY_DATABASE_URI'] = sqlite://mydatabase.db]
# db.init_app(app)
# 
# app.route('/create_student', methods['POST'])
    # data
        #    








 