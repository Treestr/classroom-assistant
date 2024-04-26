from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db, 
import crud



app = Flask(__name__)



app.jinja_env.undefined = StrictUndefined ##RESEARCH strict undefined


#PLACEHOLDER
@app.route('/')
def homepage():
    """View homepage."""

    return render_template('homepage.html')
#PLACEHOLDER


#PLACEHOLDER
@app.route("/ADD>")
def show_students(student_id):
    """Show details of a particular student.""


    student?? = crud.get_student_by_id(student_id)

    return render_template("student_information.html", ADD=ADD)
   
    
      ##PLACEHOLDER





if __name__ == "__main__":

app.run(host="0.0.0.0", debug=True)