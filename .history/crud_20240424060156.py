from model import db, Teacher, Student, Homeroom, Attendance, Location, MovementLog, Group, GroupMembership, connect_to_db 

if __name__ == '__main__':
    from server import app
    connect_to_db(app)


from model import db, User, Movie, Rating, connect_to_db

from flask import Flask, request, jsonifyfrom models import db,Teacher, Student, Homeroom, Location, MovementLog, Attendance 
from datetime import datetime
app = Flask







 