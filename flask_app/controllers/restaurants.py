from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.restaurant import Restaurant

@app.route('/restaurants/')
def restaurants():
    restaurants = Restaurant.get_all()
    return render_template('restaurants.html', restaurants=restaurants)

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

@app.route('/restaurant/<int:id>/')
def show_one_restaurant(id):
    data = {
        'id':id
    }
    restaurant=Restaurant.get(data)
    return render_template('restaurant.html',restaurant=restaurant)

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



