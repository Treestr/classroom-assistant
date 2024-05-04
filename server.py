from flask import Flask, render_template, request, flash, session, redirect, jsonify
import crud 
from model import connect_to_db, db, Student #add all classes here specifically?



from jinja2 import StrictUndefined



app = Flask(__name__)
app.secret_key = "dev"

app.jinja_env.undefined = StrictUndefined ##RESEARCH strict undefined


@app.route('/')
def homepage():
    """View homepage."""

    return render_template('homepage.html')


# REGISTER USER/SIGN-UP
@app.route('/register')
def register():
    """View registration page"""

    return render_template('register.html')

@app.route ("/users", methods= ["POST"])                               
def register_user():

    email = request.form.get("email")
    password = request.form.get("password")
    fname = request.form.get("fname")
    lname = request.form.get("lname")
    user = crud.get_teacher_by_email(email)
    
    if user:
        flash("This email is already in use. Please Try again.")
    else:
        teacher = crud.create_teacher(fname, lname, email, password)
        db.session.add(teacher)
        db.session.commit()
        flash("Success! Account Created. Please log in.")
    return redirect("/login")

@app.route ("/login")
def login_page():
    return render_template("login.html")


@app.route ("/login_user", methods=["POST"])
def login_user():
    email=request.form.get("email")
    password=request.form.get("password")
    teacher = crud.get_teacher_by_email(email)
    if password == teacher.password:
        session["teacher_id"]=teacher.teacher_id

        print(teacher.teacher_id)
        print(session)
        
        return redirect("/add_classroom")
    flash ("Not logged in.")
    return redirect("/login")

@app.route ("/add_classroom")
def add_classroom():
    return render_template("add_classroom.html")

@app.route("/addclassroom", methods=["POST"])
def addclassroom():
    classroom_name = request.form.get("classroom_name")
    classroom_description= request.form.get("classroom_description")
    classroom=crud.create_classroom(classroom_name, classroom_description, session["teacher_id"])
    db.session.add(classroom)
    db.session.commit()
    session["classroom_id"]=classroom.classroom_id
    return redirect("/add_students")

@app.route('/add_students')
def student_page():
    # students = []
    return render_template('addstudents.html')
    
    
    
#ADD STUDENTS TO CLASSROOM
# @app.route('/add_student', methods=['POST'])
# def add_student():
    # data = request.json
    # fname = data.get('fname')
    # new_student = {'fname': fname}
    # students.append(new_student)

#NEW FILE, ADD STUDENTS TO CLASSROOM, NEED STUDENTS TO BELONG TO A CLASSROOM
@app.route('/addstudents', methods=['POST'])
def add_student():
    fname = request.form.get("fname")
    student=crud.create_student(fname, session["classroom_id"], session["teacher_id"])    
    db.session.add(student)
    db.session.commit()
    print(student)
    flash("Student Created!")
    return redirect("/dashboard")

@app.route('/dashboard')
def show_dashboard():
    #get all students to pass to template & display*jinja, boostrap - cards *get all students *query database *review crud!!!!
    return render_template("dashboard.html")
                              
            
# return jsonify(new_student)
# 
        # return redirect("/")  
# 
     
    

# @app.route("/students/<student_id>)
# def show_students(student_id):
# 
    # student = crud.get_students_by_id(student_id)
    # return render_template("all_students.html"), student==student




if __name__ == "__main__":
    connect_to_db(app, "classroom")
    app.run(host="0.0.0.0", debug=True)