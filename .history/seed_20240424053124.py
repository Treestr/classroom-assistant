def seed_database()
    db.drop_all()
    db.create_all()
    

    
teacher1 = Teacher(fname="John", lname="Doe", teacher_email="john.doe@example.com")    
teacher2 = Teacher(fname="Jane:, lname="Doe", teacher_email="jane.doe@example.com")
db.session.add(teacher1)
db.session.add(teacher2)

homeroom1 = Homeroom((homeroom_name="Homerooom A",))