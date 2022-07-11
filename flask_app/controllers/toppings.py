from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.burger import Burger
from flask_app.models.restaurant import Restaurant
from flask_app.models.topping import Topping



@app.route('/toppings/')
def toppings():
    all_toppings = Topping.get_all_toppings()
    print('all_toppings '*5)
    print(all_toppings)
    return render_template("toppings.html", all_toppings=all_toppings)
