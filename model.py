from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Teacher(db.Model):

    __tablename__ = "teachers"

    teacher_id = db.Column(db.Integer, primary_key=True, autoincrement=True,)
    fname = db.Column(db.String(20), nullable = False, unique = True)
    lname - db.Column(db.String(20), nullable = False, unique = True)
    teacher_email = db.Column(db.String(50), nullable = False, unique = True)
    #foreign key relationships

class Student(db.Model):

    __tablename__ = "students"

    student_id = db.Column(db.Integer, primary_key=True, autoincrment=True) 
    fname = db.Column(db.String(20), nullable=False, unique=True)
    lname = db.Column(db.String(20), nullable = False, unique = True)
    #icon, qr/barcode, flags (not allowed same time)
    #foreign key relationships
   

##ADD CONNECTOR CLASS: STUDENT/HOMEROOM

class Location(db.Model):                       

    __tablename__ = "locations"

    student_locations_id = db.Column(db.Integer, primary_key=True,)
    location_name = db.Column(db.String(20), nullable=False, unique=True)


class HomeRoom(db.Model):#Homeroom = "class" py/school context naming challenge
    
    __tablename__ = "homeroom"
    
    homeroom_id = db.Column(db.Integer, primary_key=True, autoincrement=True,)
    homeroom_name = db.Column(db.String), nullable=False
    # teacher_id = db.relationship('Teacher', ADDDDDDD (back-populates?))
    # student_id = db.relationship                                                  


class Group(db.Model):

    __tablename__ = "groups"

    group_id = db.Column(db.Integer, primary_key=True, autoincrement=True,)#is comma correct check
    group_name = db.Column(db.String(20), unique=True)
    #FK class_id
    

    #membership_record is a CONNECTOR table

    ###HELP WITH BELOW

# class Group_Member(db.Model): #membership_record is a CONNECTOR table
# 
    # __tablename__ = "group_members" #check syntax
# group_id = db.Column(db.Integer, primary_key=True, autoincrement=True,)

class Assignment(db.Model):
    
    __tablename__ = "assignments"

    assignment_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    assignment_title = db.Column(db.String(20)
    assignment_desc = db.Column(db.String(100))
    #due_date
    #FK teacher_id, student_id
    #add columns: title, description, due_date, teacher_id FK

##CREATE A CLASSS: CONNECTOR FOR STUDENTS/ASSIGNMENTS

class Leave_Record(db.Model):
    __tablename__ = "leave_records"

    leave_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    leave_time = 
    return_time = 
    #FK: location_id, student_id
    

class Location(db.Model):
    
    __tablename__ = "locations"

    location_id = db.Column((db.Integer, primary_key=True, autoincrement=True)
    #add: location_name, flag(students not allowed at same time)

class Submission(db.Model):
    
    __tablename__ = "submissions"

    submission_id = db.Column((db.Integer, primary_key=True, autoincrement=True)
#add: date, text_field, assignment_id FK, student_id FK
    


def connect_to_db(app, db_name):

    app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql:///{db_classroom}"
    app.config["SQLALCHEMY_ECHO"] = True
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    from server import app as flask app


