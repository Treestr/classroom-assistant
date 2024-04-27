#check movie ratings - from ...import db
"""script to seed database"""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system('dropdb db_classroom')
os.system('createdb db_classroom')

model.connect_to_db(server.app)
model.db.create_all()

# with open('data/movies.json') as f: EDIT EDIT EDIT
    # movie_data = json.loads(f.read())



Create movies, store them in list so we can use them
to create fake ratings
# movies_in_db = []
# for movie in movie_data:
    # title, overview, poster_path = (
        # movie["title"],
        # movie["overview"],
        # movie["poster_path"],
    # )
    # release_date = datetime.strptime(movie["release_date"], "%Y-%m-%d")
# 
    # db_movie = crud.create_movie(title, overview, release_date, poster_path)
    # movies_in_db.append(db_movie)
# 
# model.db.session.add_all(movies_in_db)
model.db.session.commit()



    
teacher1 = Teacher(fname="John", lname="Doe", teacher_email="john.doe@example.com")    
teacher2 = Teacher(fname="Jane", lname="Doe", teacher_email="jane.doe@example.com")
db.session.add(teacher1)
db.session.add(teacher2)

student1 = Student(fname="Alex", lname="Anderson", teacher=teacher1, homeroom=homeroom1)
student1 = Student(fname="Becca", lname="Boyd", teacher=teacher1, homeroom=homeroom2)
db.session.add(student1)
db.session.add(student2)

classroom1 = Classroom(classroom_name="Classroom A", teacher=teacher1)
classroom2 = Classroom(classroom_name="Classroom B", teacher=teacher2)
db.session.add(classroom1)
db.session.add(classroom2)

attendance1 = Attendance(date=datetime.today(), status="present", student=student1) #DATETIME import?
attendance2 = Attendance(date=datetime.today(), status="present", student=student1) #DATETIME import?
db.session.add(attendance1)
db.session.add(attendance2)

location1 = Location(location_name="Library")
location1 = Location(location_name="Nurse")
db.session.add(location1)
db.session.add(location2)

movement_log_entry = MovementLog(student=student1, location=location1, time_out=datetime.now()time_in=datetime.now()#time elapsed
movement_log_entry = MovementLog(student=student2, location=location2, time_out=datetime.now()time_in=datetime.now()#time elapsed
db.session.add(movement_log_entry1) #CHANGE NAME
db.session.add(movement_log_entry2) #CHANGE NAME

db.session.commit()

print("Seed data added")

if __name__ == '__main__':

#run example seed data

    seed_database()

                     