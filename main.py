from flask import Flask, render_template, request, redirect, url_for

import db
from models import Tasks

app = Flask(__name__)


@app.route("/")
def home():
    all_task = db.session.query(Tasks).all()#BBDD Query
    return render_template("index.html", task_list=all_task)

@app.route('/new-task', methods=['POST'])
def create_task():
    task = Tasks(content=request.form['task_content'], completed=False)

    db.session.add(task)#add the object from Task to database
    db.session.commit()#Execute
    return redirect(url_for('home'))

@app.route('/delete-task/<id>')
def delete(id):
    task = db.session.query(Tasks).filter_by(id=int(id)).delete()#looking for id inside database
    db.session.commit() #execute
    return redirect(url_for('home'))

@app.route('/task-completed/<id>')
def completed(id):
    task = db.session.query(Tasks).filter_by(id=int(id)).first()
    task.completed = not(task.completed)
    db.session.commit() #execute
    return redirect(url_for('home'))

if __name__=="__main__":

    # Here we instruct SQLAlchemy to create tables for each model in models.py, if it doesn't exist
    db.Base.metadata.create_all(db.engine)
    app.run(debug=True)#debug=True means that everytime the server is restarted or something is to be modified
    #the Flask's server will restart itself
