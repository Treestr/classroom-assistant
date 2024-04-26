def seed_database()
    db.drop_all()
    db.create_all()
    

    
teacher1 = Teacher(fname="John", lname="Doe", teacher_email="john.doe@example.com")    
teacher2 = Teacher(fname="Jane:, lname="Doe", teacher_email="jane.doe@example.com")
db.session.add(teacher1)
db.session.add(teacher2)

student1 = Student(fname="Alex", lname="")


homeroom1 = Homeroom(homeroom_name="Homeroom A", teacher=teacher1)
homeroom2 = Homeroom(homeroom_name="Homeroom B", teacher=teacher2)
db.session.add(homeroom1)
db.session.add(homeroom2)
                     