from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime

# create the app
app = Flask(__name__)

# config database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
db = SQLAlchemy(app)


# portfolio model
class Portfolio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    date = db.Column(db.DateTime, default=datetime.datetime.now)
    description = db.Column(db.String(240), nullable=False)
    skills = db.Column(db.String(180), nullable=False)
    githuburl = db.Column(db.String(240), nullable=False)

    def __init__(self, title, date, description, skills, githuburl):
        self.title = title
        self.date = date
        self.description = description
        self.skills = skills
        self.githuburl = githuburl

    def __repr__(self):
        return f'''<Portfolio %r>' (Title: {self.title}
        Date: {self.date}
        Description: {self.description}
        Skills: {self.skills}
        Github: {self.githuburl}
        )'''

#function to take a date string in format YYYY-MM-DD and return a datetime object

def get_datetime_from_date_string(date_string: str) -> datetime:
    date_format = "%Y-%m-%d"
    date = datetime.datetime.strptime(date_string, date_format)
    return date