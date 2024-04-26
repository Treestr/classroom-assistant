from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Teacher(db.Model):

    __tablename__ = "teachers"

    teacher_id = db.Column(db.Integer, primary_key=True, autoincrement=True,)
    fname = db.Column(db.String(20), nullable = False, unique = True)
    lname = db.Column(db.String(20), nullable = False, unique = True)
    teacher_email = db.Column(db.String(50), nullable = False, unique = True)
    students = db.relationship('Student', back_populates='teacher')

    def __repr__(self):
        return f"<Teacher(teacher_id={self.teacher_id}, 
    fname='self{self.fname}', 
    lname='self{self.lname},
    teacher_email='{self.email}')>"
     

class Student(db.Model):

    __tablename__ = "students"

    student_id = db.Column(db.Integer, primary_key=True, autoincrement=True) 
    fname = db.Column(db.String(20), nullable=False, unique=True)
    lname = db.Column(db.String(20), nullable = False, unique = True)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.teacher_id'), nullable=False)
    teacher = db.relationship('Teacher', back_populates='students')
    homeroom_id = db.Column(db.Integer, db.ForeignKey('homeroom.homeroom_id'), nullable=False)
    homeroom = db.relationship('Homeroom', back_populates='students')

    def __repr__(self):
        return f"<Student(student_id={self.student_id}, 
    fname='self{self.fname}', 
    lname='self{self.lname},

    

##TO DO REVISE & ADD CONNECTOR CLASS: STUDENT/HOMEROOM


class Homeroom(db.Model):#Homeroom =
    
    __tablename__ = "homeroom"
    
    homeroom_id = db.Column(db.Integ, primary_key=True, autoincrement=True) 
    homeroom_name = db.Column(db.Str(20), nullable=False, unique=True)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.teacher_id'), nullable=False)
    students = db.relationship('Student', back_populates='homeroom') 
    
    def __repr__(self):
    return f"<Homeroom(homeroom_id={self.teacher_id}, 
fname='self{self.fname}', 
lname='self{self.lname},
teacher_email='{self.email}')>"
    
    class Location(db.Model):
    
    __tablename__ = "locations"

    student_locations_id = db.Column(db.Integer, primary_key=True,)
    location_name = db.Column(db.String(20), nullable=False, unique=True)

                                             
class Attendance(db.Model):
    __tablename__ = "attendance"
    attendance_id = db.Column(db.Integer, primary_key=True)

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

     class Location(db.Model):
 
 __tablename__ = "locations"
 student_locations_id = db.Column(db.Integer, primary_key=True,)
 location_name = db.Column(db.String(20), nullable=False, unique=True)

class Submission(db.Model):
    
    __tablename__ = "submissions"

    submission_id = db.Column((db.Integer, primary_key=True, autoincrement=True)
#add: date, text_field, assignment_id FK, student_id FK
    


def connect_to_db(app, db_name):

    app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql:///{db_classroom}"
    app.config["SQLALCHEMY_ECHO"] = True
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

\
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    from server import app as flask app



 
    