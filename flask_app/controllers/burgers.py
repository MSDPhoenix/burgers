from operator import concat
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.burger import Burger
from flask_app.models.restaurant import Restaurant
from flask_app.models.topping import Topping



@app.route('/')
def index():
    return render_template("index.html",restaurants=Restaurant.get_all())

@app.route('/create',methods=['POST'])
def create():
    data = {
        "name":request.form['name'],
        "bun": request.form['bun'],
        "meat": request.form['meat'],
        "calories": request.form['calories'],
        "restaurant_id": request.form['restaurant_id'],
    }
    Burger.save(data)
    return redirect('/burgers')




@app.route('/burgers/')
def burgers():
    return render_template("results.html",all_burgers=Burger.get_all())


@app.route('/show/<int:burger_id>')
def detail_page(burger_id):
    data = {
        'id': burger_id
    }
    return render_template("details_page.html",burger=Burger.get_one(data),restaurant=Restaurant.get_by_burger_id(Restaurant,data))

@app.route('/edit_page/<int:burger_id>')
def edit_page(burger_id):
    data = {
        'id': burger_id
    }
    burger = Burger.get_one(data)
    all_toppings=Topping.get_all_toppings()
    burger_toppings_ids = []
    for x in burger.toppings:
        burger_toppings_ids.append(x.id)
    remaining_toppings = []
    for topping in all_toppings:
        if topping.id not in burger_toppings_ids:
            remaining_toppings.append(topping)
    return render_template("edit_page.html", burger=burger,remaining_toppings=remaining_toppings)

@app.route('/update/<int:burger_id>', methods=['POST'])
def update(burger_id):
    data = {
        'id': burger_id,
        "name":request.form['name'],
        "bun": request.form['bun'],
        "meat": request.form['meat'],
        "calories": request.form['calories']
    }
    Burger.update(data)
    return redirect(f"/show/{burger_id}")

@app.route('/delete/<int:burger_id>')
def delete(burger_id):
    data = {
        'id': burger_id,
    }
    Burger.destroy(data)
    return redirect('/burgers')

@app.route('/burger_add_topping/<int:burger_id>/',methods=['POST'])
def burger_add_topping(burger_id):
    print(request.form)
    data = {
        'burger_id': burger_id,
        'topping_id' : request.form['topping_id']
    }
    Burger.add_topping(data)
    return redirect('/edit_page/'+str(burger_id))

@app.route('/burger_remove_topping/<int:burger_id>/',methods=['POST'])
def burger_remove_topping(burger_id):
    print(request.form)
    data = {
        'burger_id': burger_id,
        'topping_id' : request.form['topping_id']
    }
    Burger.remove_topping(data) 
    return redirect('/edit_page/'+str(burger_id))

burger_remove_topping