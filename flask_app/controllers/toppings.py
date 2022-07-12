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
    all_toppings = Topping.get_all_toppings()
    return render_template("toppings.html", all_toppings=all_toppings)

@app.route('/edit_topping_name/<int:topping_id>/',methods=['POST','GET'])
def edit_topping_name(topping_id):
    all_toppings = Topping.get_all_toppings()
    print("A"*40)
    print("***",topping_id)
    for topping in all_toppings:
        print(topping.id)
        if topping.id == topping_id:
            print('yes')
            all_toppings.remove(topping)
    for topping in all_toppings:
        print(topping.id)
    # print(all_toppings)
    data = {'topping_id':topping_id}
    topping_to_edit = Topping.get(data)
    # print("B"*40)
    # print(topping_to_edit)
    # for topping in all_toppings:
    # print(all_toppings)
    return render_template("edit_toppings.html", all_toppings=all_toppings,topping_to_edit=topping_to_edit)



/update/{{topping_to_edit.id}}