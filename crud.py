
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

from model import db, Teacher, Student, Classroom, connect_to_db 


def create_teacher(fname, lname, teacher_email, password):

    
    new_teacher = Teacher(fname=fname, lname=lname, teacher_email=teacher_email, password=password)
    
    return new_teacher 

def get_users():
    """Return all users"""

    return Teacher.query.all()

def get_teacher_by_email(email):

    return Teacher.query.filter(Teacher.teacher_email == email).first()


def create_student(fname, classroom_id, teacher_id):
    
    
    new_student = Student(fname=fname, classroom_id=classroom_id, teacher_id=teacher_id) 
    
    return new_student

def get_all_students():
    """Return all students"""

    return Student.query.all()

def get_student_by_id():
    Student.query.get(1)

def create_classroom(classroom_name, classroom_description, teacher_id):
    new_classroom = Classroom(classroom_name=classroom_name, classroom_description=classroom_description, teacher_id=teacher_id)
    
    

    return new_classroom       

def get_classrooms():
    """Return all classrooms"""

    return Classroom.query.all()

def get_classrooms_by_teacher_id(teacher_id):
    return Classroom.query.filter_by(teacher_id=teacher_id).all()

def get_classrooms_by_classroom_id(classroom_id):
    return Classroom.query.filter_by(classroom_id=classroom_id).first()


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
if __name__ == '__main__':
 
    from server import app
    app.app_context().push()
    connect_to_db(app, "classroom")