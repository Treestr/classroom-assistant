from model import db, Teacher, Student, Homeroom, Attendance, Location, connect_to_db #ADD Teacher, Student, Group, Homeroom, etc..

if __name__ == '__main__':
    from server import app
    connect_to_db(app)


from model import db, User, Movie, Rating, connect_to_db







 