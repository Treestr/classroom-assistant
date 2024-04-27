
# MOVIE RATINGS EXAMPLES:

# def create_user(email, password):
    # """Create and return a new user."""
# 
    # user = __blank__(email=__blank__, password=__blank__)
# 
    # return user
# 
# def create_movie(title, overview, release_date, poster_path):
    # """Create and return a new movie."""
# 
    # movie = Movie(
        # title=title,
        # overview=overview,
        # release_date=release_date,
        # poster_path=poster_path,
    # )
# 
    # return movie
#END MOVIE RATINGS EXAMPLES   


#MISC

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
#END MISC

"""CRUD operations"""

from model import db, Teacher, Student, Homeroom, Attendance, Location, MovementLog, Group, GroupMembership, connect_to_db 

if __name__ == '__main__':
    from server import app
    connect_to_db(app)


def create_user(fname, lname, teacher_email):

    teacher = Teacher(
    """Create and return a new user."""
    new_user = Teacher(fname, lname=lname, teacher_email=teacher_email)
    db.session.add(new_user)
    db.session.commit()
    )
    return new_user() 

def get_users()
    """Return all users"""

    return User.query.all()

def create_student(fname, lname, student_id):

    student = Student(
    """Create and return a new user."""
    new_student = Student(fname, lname=lname, student_id=student_id) 
    db.session.add(new_student)
    db.session.commit()
    )
    return new_student()

def get_all_students():
    """Return all students"""

    return Student.query.all()

def get_student_by_id():
    Student.query.get(1)

def create_classroom():
    classroom = Classroom(
        new_classroom = Classroom()
        db.session.add(new_classroom)
        db.session.commit()    
    )
    return new_classroom()

def get_classrooms()
    """Return all classrooms"""

    return Classroom.query.all()


# def get_all_teachers():
    return Teacher.query.all()
# 
# def get_teacher_by_id(teacher_id):
    # return Teacher.query.get(teacher_id)
# 
# def update_teacher(teacher_id, fname, lname, teacher_email)
    # teacher = Teacher.query.get(teacher_id)
    # if teacher:
        # teacher.fname = fname
        # teacher.lname = lname
        # teacher.teacher_email = teacher_email
        # db.session.commit()
# 
    # return teacher
# 
# def delete_teacher(teacher_id):
    # teacher = Teacher.query.get(teacher_id)
    # if teacher:
        # db.session.delete(teacher)
        # db.session.commit()
        # 
    # return teacher

#CHECK IF CORRECT, COMPLETE FOR OTHER CLASSES


 