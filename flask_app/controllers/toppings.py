from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.burger import Burger
from flask_app.models.restaurant import Restaurant
from flask_app.models.topping import Topping

@app.route('/toppings/')
def toppings():
    all_toppings = Topping.get_all_toppings()
    return render_template("toppings.html", all_toppings=all_toppings)

@app.route('/new_topping/',methods=['POST'])
def new_topping():
    Topping.save(request.form)
    return redirect("/toppings/")

@app.route('/update_topping/',methods=['POST'])    
def update_topping():
    Topping.update_topping(request.form)
    return redirect("/toppings/")

@app.route('/delete_topping/<int:topping_id>/')     
def delete_topping(topping_id):
    Topping.delete_topping(data={'topping_id' : topping_id})    
    return redirect("/toppings/")

@app.route('/edit_topping_name/<int:topping_id>/')
def edit_topping_name(topping_id):
    all_toppings = Topping.get_all_toppings()
    for topping in all_toppings:
        if topping.id == topping_id:
            all_toppings.remove(topping)
    data = {'topping_id':topping_id}
    topping_to_edit = Topping.get(data)
    return render_template("edit_toppings.html", all_toppings=all_toppings,topping_to_edit=topping_to_edit)



