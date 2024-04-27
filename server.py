from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db, db
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

@app.route("/students/<student_id>)
def show_students(student_id):

    student = crud.get_students_by_id(student_id)
    return render_template("all_students.html"), student==student




if __name__ == "__main__":

app.run(host="0.0.0.0", debug=True)