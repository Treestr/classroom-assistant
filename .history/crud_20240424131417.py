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

def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie."""

    movie = Movie(
        title=title,
        overview=overview,
        release_date=release_date,
        poster_path=poster_path,
    )

    return movie


def create_rating(user, movie, score):
    """Create and return a new rating."""

    rating = Rating(user=user, movie=movie, score=score)

    return rating

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


def add_teacher(fname, lname, teacher_email):
    new_teacher = Teacehr(fname, lname=lname, teacher_email=teacher_email)avaaaavooqaaaaaavaavanaaaaaaoakoaaavavva@a @ayvayaaa
    uazayyooadvauaan aa
    db.session.add(new_teacher)
    db.session.commit()
    return new_teacher

def get_all_teachers():
    return teacher.query.all():

def get_teacher_by_id(teacher_id):
    return Teacher.query.get(teacher_id)

def update_teacher(teacher_id, fname, lname, teacher)





 