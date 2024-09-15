from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
db = SQLAlchemy(app)
# Define a project model


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    link = db.Column(db.String(200), nullable=False)
    # Create the database and add sample data


@app.before_first_request
def create_db():
    db.create_all()
    if Project.query.count() == 0:  # Add data if empty
        project1 = Project(title="Weather Service API", description="Weather service using Flask.", link="https://github.com/Mohashalaby/weather-api")
        project2 = Project(title="Maze Game", description="Interactive maze game with random generation.", link="https://github.com/Mohashalaby/maze-game")
        db.session.add_all([project1, project2])
        db.session.commit()

# Serve the portfolio homepage
@app.route('/')
def home():
    projects = Project.query.all()
    return render_template('index.html', projects=projects)
    return render_template('index.html')

# Handle contact form submissions
@app.route('/contact', methods=['POST'])


def contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    
    # Here you can process the data (e.g., send an email, save to a database)
    return jsonify({"status": "success", "message": "Message sent!"})

if __name__ == '__main__':
    app.run(debug=True)
