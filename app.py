from models import db, Portfolio, app, get_datetime_from_date_string
from flask import (render_template, request, redirect, url_for, flash)


#home route
@app.route('/')
def home():
    portfolio_items = Portfolio.query.all()
    return render_template('index.html', portfolio_items=portfolio_items)
    #return render_template('index.html', portfolio=Portfolio.query.all())

#create route
@app.route('/new', methods=['GET', 'POST'])
def create():
    print(request.form)
    #if form has has title, date, description, skills and github link then submit to database
    if request.form:
            dateToUse = get_datetime_from_date_string(
                request.form['date'] + "-01")
            portfolio = Portfolio(title=request.form['title'], date=dateToUse, description=request.form['desc'], skills=request.form['skills'], githuburl=request.form['github'])
            db.session.add(portfolio)
            db.session.commit()
            return redirect(url_for('home'))
    return render_template('projectform.html')

#detail route
@app.route('/details')
def detail():
    #portfolio = Portfolio.query.get(id)
    #return render_template('detail.html', portfolio=portfolio)
    return render_template('detail.html')

#edit route
@app.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit(id):
    portfolio = Portfolio.query.get(id)
    if request.method == 'POST':
        portfolio.title = request.form['title']
        portfolio.description = request.form['description']
        portfolio.image = request.form['image']
        db.session.commit()
        return redirect(url_for('home'))
    #return render_template('edit.html', portfolio=portfolio)

#delete route
@app.route('/<int:id>/delete', methods=['GET', 'POST'])
def delete(id):
    portfolio = Portfolio.query.get(id)
    db.session.delete(portfolio)
    db.session.commit()
    flash('Deleted Record!')
    return redirect(url_for('home'))

#dunder main
if __name__ == '__main__':
    #run the app
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000, host='127.0.0.1')