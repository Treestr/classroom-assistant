def seed_database()
    db.drop_all()
    db.create_all()
    

    
teacher1 = Teacher(fname="John", lname="Doe", teacher_email="john.doe@example.com")    
teacher2 = Teacher(fname="Jane:, lname="Doe", teacher_email="jane.doe@example.com")
db.session.add(teacher1)
db.session.add(teacher2)

student1 = Student(fname="Alex", lname="Anderson", teacher=teacher1, homeroom=homeroom1)
student1 = Student(fname="Becca", lname="Boyd", teacher=teacher1, homeroom=homeroom2)
db.session.add(student1)
db.session.add(student2)

location1 = Location(location_name="Library")
location1 = Location(location_name="Nurse")
db.session.add(location1)
db.session.add(location2)

movement_log_entry = MovementLog(student=student1, location=location1, time_out=date)




homeroom1 = Homeroom(homeroom_name="Homeroom A", teacher=teacher1)
homeroom2 = Homeroom(homeroom_name="Homeroom B", teacher=teacher2)
db.session.add(homeroom1)
db.session.add(homeroom2)
                     