from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Teacher(db.Model):

    __tablename__ = "teachers"

    teacher_id = db.Column(db.Integer, primary_key=True, autoincrement=True,)
#add class: fname, lname (or full name???), teacher_email

class Student(db.Model):

    __tablename__ = "students"

    student_id = db.Column(db.Integer, primary_key=True, autoincrment=True) 
    #add class: fname, lname (or name??), icon, qr/barcode, flag (students not allowed out at same time)

##ADD CONNECTOR CLASS: STUDENT/HOMEROOM

class Location(db.Model):

    __tablename__ = "locations"

    student_locations_id = db.Column(db.Integer, primary_key=True,)
##add class: location_name

class HomeRoom(db.Model):#Homeroom = "class" py/school context naming challenge
    
    __tablename__ = "homeroom"
    
    homeroom_id = db.Column(db.Integer, primary_key=True, autoincrement=True,)
    #homeroom_name, teacher_id FK, student_id FK

class Group(db.Model):

    __tablename__ = "groups"

    group_id = db.Column(db.Integer, primary_key=True, autoincrement=True,)#is comma correct check
    #add: group_name, class_id FK, ((assignment_id????))

    #membership_record is a CONNECTOR table

    ###HELP WITH BELOW

# class Group_Member(db.Model): #membership_record is a CONNECTOR table
# 
    # __tablename__ = "group_members" #check syntax
# group_id = db.Column(db.Integer, primary_key=True, autoincrement=True,)

class Assignment(db.Model):
    
    __tablename__ = "assignments"

    assignment_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    #add columns: title, description, due_date, teacher_id FK

##CREATE A CLASSS: CONNECTOR FOR STUDENTS/ASSIGNMENTS

class Leave_Record(db.Model):
    __tablename__ = "leave_records"

    leave_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ##remaining columns: student_id FK, leave_start_time, leave_end_time, location_id Fk

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


