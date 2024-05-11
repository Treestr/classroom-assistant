from flask import Flask, render_template, request, flash, session, redirect, jsonify
import crud 
from model import connect_to_db, db, Student #add all classes here specifically?
#what is Celery??


from jinja2 import StrictUndefined



app = Flask(__name__)
app.secret_key = "dev"

app.jinja_env.undefined = StrictUndefined 


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
        
        return redirect("/dashboard")
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
    return redirect(f'/classroom/{session["classroom_id"]}')

@app.route('/dashboard')
def show_dashboard():
    if 'teacher_id' not in session:
        flash("Please log in to view your dashboard.")
        return redirect("/login")
    
    teacher_id = session['teacher_id']
    classrooms = crud.get_classrooms_by_teacher_id(teacher_id)
    if not classrooms:
        flash("No classrooms available yet. Please add a classroom.")

    return render_template("dashboard.html", classrooms=classrooms)    
        
# @app.task
# def check_time_limits():
    # now = datetime.utcnow()
    # active_movements = MovementLog.query.filter(MovementLog.time_in.is_(None)).join(Location).all()      
    # for movement in active_movements:
        # if movement.location.time_limit and now> movement.time_out +timedelta(minutes=movement.location.time_limit):
            # send_notification(movement.student_id, movement.location_id)   
# 
# def send_notification(student_id, location_id):
# 
    # print(f"Student {student_id} has exceeded time limit at location {location_id}")            
        # 
    #get all students to pass to template & display*jinja, boostrap - cards *get all students *query database *review crud!!!! return render_template("dashboard.html")
                              
            
# return jsonify(new_student)
# 
        # return redirect("/")  

        #
#DRAG/DROP students into groups DRAFT JS

@app.route('/classroom/<int:classroom_id>/display_students')
def display_students(classroom_id):
    classroom = Classroom.query.get(classroom_id)
    if not classroom:
        flash("Classroom not found.")
        return redirect("/dashboard")
    
    students = classroom.students
    return render_template("display_students.html", students=students, classroom=classroom)


# @app.route(__________)#time in time out 
# def (attendance_id):
    # attendance = crud.get_attendance_by_id(attendance_id)
    # new_status = 'out_pass' 
    # if attendance.status =='in_class' else 'in_class'
    # updated_attendance = crud.update_attendance_status(attendance_id, new_status)
    # return redirect#___________________
# 
# 
    #  
    

@app.route("/classroom/<classroom_id>")
def show_classroom(classroom_id):
    session["classroom_id"]=classroom_id
    classroom = crud.get_classrooms_by_classroom_id(classroom_id)
    return render_template("class.html", classroom=classroom)
# 




if __name__ == "__main__":
    connect_to_db(app, "classroom")
    app.run(host="0.0.0.0", debug=True)