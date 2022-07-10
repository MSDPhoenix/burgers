from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.restaurant import Restaurant

@app.route('/')
def index():
    restaurants = Restaurant.get_all()
    for restaurant in restaurants:
        month=restaurant.created_at.strftime('%B')
        date=restaurant.created_at.strftime('%d')
        year=restaurant.created_at.strftime('%Y')
        if date[0] == "0":
            date = date[1:]
        restaurant.created_at=month+' '+date+', '+year
    return render_template('index.html', restaurants=restaurants)

@app.route('/new_restaurant_form/')
def new_restaurant_form():
    return render_template('new_restaurant.html')

@app.route('/save_restaurant/',methods=['POST'])
def save_restaurant():
    data = {
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'email':request.form['email'],
    }
    id=restaurant.save_restaurant(data)
    return redirect('/show_one_restaurant/'+str(id))

@app.route('/show_one_restaurant/<int:id>/')
def show_one_restaurant(id):
    data = {
        'id':id
    }
    restaurant=restaurant.get(data)
    month=restaurant.created_at.strftime('%B')
    date=restaurant.created_at.strftime('%d')
    year=restaurant.created_at.strftime('%Y')
    if date[0] == "0":
        date = date[1:]
    created_at=month+' '+date+', '+year
    month=restaurant.updated_at.strftime('%B')
    date=restaurant.updated_at.strftime('%d')
    year=restaurant.updated_at.strftime('%Y')
    time=restaurant.updated_at.strftime('%I:%M')
    am_pm=restaurant.updated_at.strftime('%p').lower()
    if time[0] == "0":
        time = time[1:]
    if date[0] == "0":
        date = date[1:]
    updated_at=month+' '+date+', '+year+' at '+time+' '+am_pm
    return render_template('show_one_restaurant.html',restaurant=restaurant,created_at=created_at,updated_at=updated_at)

@app.route('/edit_restaurant_page/<int:id>/')
def edit_restaurant_page(id):
    data = {
        'id':id
    }
    restaurant=restaurant.get(data)
    return render_template('edit_restaurant.html',restaurant=restaurant)

@app.route('/delete_restaurant/<int:id>/')
def delete_restaurant(id):
    data = {
        'id':id
    }
    Restaurant.delete(data)
    return redirect('/')

@app.route('/update_restaurant/<int:id>/',methods=['POST'])
def update_restaurant(id):
    data = {
        'id':id,
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'email':request.form['email'],
    }
    Restaurant.update(data)
    return redirect('/show_one_restaurant/'+str(id))

    session.modified = True # By default, it's set to False


