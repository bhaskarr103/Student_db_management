from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///student.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Student(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300), nullable=False)
    std = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(500), nullable=False)
    phone = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"


@app.route('/', methods=['GET', 'POST'])
def help():
    if request.method == 'POST':
        name = request.form['name']
        std = request.form['std']
        email = request.form['email']
        phone = request.form['phone']
        student = Student(name=name, std=std, email=email, phone=phone)
        db.session.add(student)
        db.session.commit()

    allStudent = Student.query.all()
    return render_template('index.html', allStudent=allStudent)


@app.route('/show')
def products():
    allStudent = Student.query.all()
    return 'This is products page'

# It looks like you are trying to render the template with " allStudent "
# as a parameter, but it is not defined in the route function.
# You need to query the database to get the student data and pass it
# to the template.


@app.route('/delete/<int:sno>')
def delete(sno):
    todo_to_delete = Student.query.filter_by(sno=sno).first()
    db.session.delete(todo_to_delete)
    db.session.commit()
    return redirect('/')

@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    todo_to_update = Student.query.get(sno)

    if request.method == 'POST':
        todo_to_update.title = request.form['name']
        todo_to_update.desc = request.form['std']
        todo_to_update.title = request.form['email']
        todo_to_update.title = request.form['phone']
        db.session.commit()
        return redirect('/')

    return render_template('update.html', todo=todo_to_update)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run()

# After defining your models, you need to create the corresponding tables
# in the SQLite database. You can do this by using the 'db.create_all()' method.
# Add the following lines of code after defining the ' Student ' class:
