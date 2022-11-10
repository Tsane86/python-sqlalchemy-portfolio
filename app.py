from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import datetime
import time

from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# create the app
app = Flask(__name__)


#config database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
db = SQLAlchemy(app)


#portfolio model
class Portfolio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(120), nullable=False)
    image = db.Column(db.String(120), nullable=False)

    def __init__(self, title, description, image):
        self.title = title
        self.description = description
        self.image = image

    def __repr__(self):
        return '<Portfolio %r>' % self.name % self.description

#home route
@app.route('/')
def home():
    return render_template('index.html')

#create route
@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        if not request.form['title'] or not request.form['description'] or not request.form['image']:
            flash('Please enter all the fields', 'error')
        else:
            portfolio = Portfolio(request.form['title'], request.form['description'], request.form['image'])

            db.session.add(portfolio)
            db.session.commit()
            flash('Record was successfully added')
            return redirect(url_for('home'))
    return render_template('create.html')

#detail route
@app.route('/detail/<int:id>')
def detail(id):
    portfolio = Portfolio.query.get(id)
    return render_template('detail.html', portfolio=portfolio)

#add route


#edit route
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    portfolio = Portfolio.query.get(id)
    if request.method == 'POST':
        portfolio.title = request.form['title']
        portfolio.description = request.form['description']
        portfolio.image = request.form['image']

        db.session.commit()
        flash('Record was successfully updated')
        return redirect(url_for('home'))
    return render_template('edit.html', portfolio=portfolio)

#delete route
@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    portfolio = Portfolio.query.get(id)
    db.session.delete(portfolio)
    db.session.commit()
    flash('Record was successfully deleted')
    return redirect(url_for('home'))

#dunder main
if __name__ == '__main__':
    #run the app
    app.run(debug=True)