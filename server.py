from flask import Flask, render_template, request, flash, session, redirect, jsonify
from model import connect_to_db, db, Student #add all classes here specifically?
import crud
 
import crud

from jinja2 import StrictUndefined



app = Flask(__name__)
app.secret_key = "dev"

app.jinja_env.undefined = StrictUndefined ##RESEARCH strict undefined



@app.route('/')
def homepage():
    """View homepage."""

    return render_template('homepage.html')

@app.route('/register')
def register():
    """View registration page"""

    return render_template('register.html')

@app.route ("/users", methods= ["POST"])                               
def register_user():
    
"""Create a new user"""

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    if user:
        flash("This email is already in use. Please Try again.")
    else:
        user = crud.create_user(email, password)
        db.session.add(user)
        db.session.commit()
        flash("Success! Account Created. Please log in.")

    return redirect("/")  

    students = []

    @app.route('/')
    def index():
        return render_template('add_students.html')
    @app.route('/add_student', methods=['POST'])
    def add_student():
     data = request.json
     fname = data.get('fname')
     lname = data.get('lname')

    new_student = Student(fname, lname)
    students.append(new_student)

    return jsonify({'fname': fname, 'lname': lname})





# @app.route("/students/<student_id>)
# def show_students(student_id):
# 
    # student = crud.get_students_by_id(student_id)
    # return render_template("all_students.html"), student==student




if __name__ == "__main__":

app.run(host="0.0.0.0", debug=True)