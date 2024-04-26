def seed_database()
    db.drop_all()
    db.create_all()
    

    
teacher1 = Teacher(fname="John", lname="Doe", teacher_email="john.doe@example.com")    
teacher2 = Teacher(fname="Jane")