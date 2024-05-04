from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import Table, Column, Integer, ForeignKey, String
# from sqlalchemy.orm import relationship
db = SQLAlchemy()

class Teacher(db.Model):

    __tablename__ = "teachers"

    teacher_id = db.Column(db.Integer, primary_key=True, autoincrement=True,)
    fname = db.Column(db.String(20), nullable = False, unique = True)
    lname = db.Column(db.String(20), nullable = False, unique = True)
    teacher_email = db.Column(db.String(50), nullable = False, unique = True)
    students = db.relationship('Student', back_populates='teacher')
    password = db.Column(db.String(20))
                         

    def __repr__(self):
        return f"<Teacher(teacher_id={self.teacher_id} fname=self{self.fname} lname=self{self.lname} teacher_email={self.email}>"
     

class Student(db.Model):
    
    __tablename__ = "students"

    student_id = db.Column(db.Integer, primary_key=True, autoincrement=True) 
    fname = db.Column(db.String(20), nullable=False, unique=True)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.teacher_id'), nullable=False)
    teacher = db.relationship('Teacher', back_populates='students')
    classroom_id = db.Column(db.Integer, db.ForeignKey('classroom.classroom_id'), nullable=False)
    classroom = db.relationship('Classroom', back_populates='students')
    #groups = db.relationship('GroupMembership', back_populates = 'student')

    def __repr__(self):
        return f"<Student(student_id={self.student_id} fname=self{self.fname}/>"



#COMBINE FIRST AND LAST NAME

# class Student:
    # def __init__(self, fname, lname):
        # self.fname = fname
        # self.lname = lname
    # 
    # def full_name(self):
        # return f"{self.fname} {self.lname}"
# 
# Create a student object
# student = Student("John", "Wick")
# 
# 
# print(student.full_name())  



class Classroom(db.Model):
    
    __tablename__ = "classroom"
    
    classroom_id = db.Column(db.Integer, primary_key=True, autoincrement=True) 
    classroom_name = db.Column(db.String(20), nullable=False, unique=True)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.teacher_id'), nullable=False)
    students = db.relationship('Student', back_populates='classroom') 
    classroom_description=db.Column(db.Text)
    
    def __repr__(self):
        return f"<Classroom(classroom_id={self.teacher_id} fname ='self{self.fname}'lname ='self{self.lname} teacher_email ={self.email}/>"
    
                                             
# class Attendance(db.Model):
    # __tablename__ = "attendance"
    # attendance_id = db.Column(db.Integer, primary_key=True)
    # date = db.Column(db.Date, nullable=False)
    # status = db.Column(db.String(10), nullable=False) #present or absent
    # student_id = db.Column(db.Integer, db.ForeignKey('students.student_id'))
    # student = db.relationship('Student', back_populates='attendance_records')
# 
    # def __repr__(self):
        # return f"<Attendance(attendance_id={self.attendance_id}, status = 'self{self.status}>"
                                                    #  
# 
# class Location(db.Model):
    # 
    # __tablename__ = "locations"
# 
    # location_id = db.Column(db.Integer, primary_key=True, autoincrement=True) 
    # location_name = db.Column(db.String(20), nullable=False, unique=True)
    #  add: flag(students not allowed at same time)
# 
# class MovementLog(db.Model): #MovementRecord??
#    __tablename__ = "movement_log"
#    log_id = db.Column (db.Integer, primary_key=True)
#    student_id = db.Column(db.Integer, db.ForeignKey('students.student_id'))
#    location_id = db.Column(db.Integer, db.ForeignKey('locations.location_id'))
#    time_out = db.Column(db.DateTime, nullable = False)
#    time_in = db.Column(db.DateTime) 
#    student = db.relationship('Student')

# class Group(db.Model):
# 
    # __tablename__ = "groups"
# 
    # group_id = db.Column(db.Integer, primary_key=True, autoincrement=True,)#is comma correct check
    # group_name = db.Column(db.String(20), unique=True)
    # students = db.relationship('GroupMembership', back_populates="groups")
    # classroom_id = db.Column(db.Integer, db.ForeignKey('classroom.classroom_id'))
    # FK class_id
# 
    # 
# 
# ADD group membership record?
# add connector class Group_member
# class GroupMembership(db.Model):
    # __tablename__ = "group_memberships"
    # student_id = db.Column(db.Integer, db.ForeignKey('students.student_id'), primary_key=True)
    # group_id = db.Column(db.Integer, db.ForeignKey('groups.group_id'), primary_key=True)
    # student = db.relationship("Student", back_populates="groups")
    # group = db.relationship("Group", back_populates="students")
# 
    # 
# class Assignment(db.Model):
    # 
    # __tablename__ = "assignments"
# 
    # assignment_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # assignment_title = db.Column(db.String(20))
    # assignment_desc = db.Column(db.String(100))
    #due_date
    #FK teacher_id, student_id
    #add columns: title, description, due_date, teacher_id FK


##CREATE A CLASS: CONNECTOR FOR STUDENTS/ASSIGNMENTS

#SUBMIT ASSIGNMENTS
# class Submission(db.Model):
    # 
    # __tablename__ = "submissions"
# 
    # submission_id = db.Column((db.Integer, primary_key=True, autoincrement=True)
# add: date, text_field, assignment_id FK, student_id FK
    # 


def connect_to_db(app, db_name):

    app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql:///{db_name}"
    app.config["SQLALCHEMY_ECHO"] = True
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    from server import app
    app.app_context().push()
    connect_to_db(app, "classroom")   
   
   



   




 
    