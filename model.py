from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Teacher(db.Model):

    __tablename__ = "teachers"

    teacher_id = db.Column(db.Integer, primary_key=True, autoincrement=True,)

class Student(db.Model):

    __tablename__ = "students"

    student_id = db.Column(db.Integer, primary_key=True, autoincrment=True) 

    class Location(db.Model):

        __tablename__ "locations"

        student_locations_id = db.Column(db.Integer, primary_key=True,
                                )
    


def connect_to_db(app, db_name):



    app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql:///{db_classroom}"
    app.config["SQLALCHEMY_ECHO"] = True
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = app
    db.init_app(app)




if __name__ == "__main__":
    from server import app as flask app


