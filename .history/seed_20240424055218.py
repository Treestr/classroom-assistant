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

movement_log_entry = MovementLog(student=student1, location=location1, time_out=datetime.now()time_in=datetime.now()#time elapsed
movement_log_entry = MovementLog(student=student2, location=location2, time_out=datetime.now()time_in=datetime.now()#time elapsed
db.session.add(movement_log_entry1) #CHANGE NAME
db.session.add(movement_log_entry2) #CHANGE NAME



homeroom1 = Homeroom(homeroom_name="Homeroom A", teacher=teacher1)
homeroom2 = Homeroom(homeroom_name="Homeroom B", teacher=teacher2)
db.session.add(homeroom1)
db.session.add(homeroom2)

attendance1 = Attendance(date=datetime.today(), status="present", student=student1)
attendance2 = Attendance(date=datetime.today(), status="present", student=student1)
db.session.add(attendance1)
db.session.add(attendance2)




                     