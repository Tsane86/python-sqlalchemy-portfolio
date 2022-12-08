from models import db, Portfolio, app, get_datetime_from_date_string
from flask import (render_template, request, redirect, url_for, flash)


#home route
@app.route('/')
def home():
    portfolio_items = Portfolio.query.all()
    return render_template('index.html', portfolio_items=portfolio_items)

#create route
@app.route('/new', methods=['GET', 'POST'])
def create():
    print(request.form)
    if request.form:
            dateToUse = get_datetime_from_date_string(
                request.form['date'] + "-01")
            portfolio = Portfolio(title=request.form['title'], date=dateToUse, description=request.form['desc'], skills=request.form['skills'], githuburl=request.form['github'])
            db.session.add(portfolio)
            db.session.commit()
            return redirect(url_for('home'))
    return render_template('projectform.html')

#detail route
@app.route('/<id>')
def detail(id):
    portfolio_item = Portfolio.query.get(id)
    return render_template('detail.html', portfolio_item=portfolio_item)

#edit route
@app.route('/<id>/edit', methods=['GET', 'POST'])
def edit(id):
    portfolio_item = Portfolio.query.get(id)
    if request.form:
        dateToUse = get_datetime_from_date_string(
            request.form['date'] + "-01")
        portfolio_item.title = request.form['title']
        portfolio_item.date = dateToUse
        portfolio_item.description = request.form['desc']
        portfolio_item.skills = request.form['skills']
        portfolio_item.githuburl = request.form['github']
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', portfolio_item=portfolio_item)

#delete route
@app.route('/<id>/delete', methods=['GET', 'POST'])
def delete(id):
    portfolio = Portfolio.query.get(id)
    db.session.delete(portfolio)
    db.session.commit()
    return redirect(url_for('home'))

#dunder main
if __name__ == '__main__':
    #run the app
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000, host='127.0.0.1')