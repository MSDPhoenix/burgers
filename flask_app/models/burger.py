from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import topping

class Burger:
    def __init__(self,data):
        self.id = data['id']
        self.name= data['name']
        self.bun = data['bun']
        self.meat = data['meat']
        self.calories = data['calories']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.toppings = []

    @classmethod
    def save(cls,data):
        query = "INSERT INTO burgers (name,bun,meat,calories,restaurant_id) VALUES (%(name)s,%(bun)s,%(meat)s,%(calories)s,%(restaurant_id)s)"
        return connectToMySQL('burgers').query_db(query,data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM burgers;"
        burgers_from_db =  connectToMySQL('burgers').query_db(query)
        burgers =[]
        for b in burgers_from_db:
            burgers.append(cls(b))
        return burgers

    @classmethod
    def get_one(cls,data):
        print('D'*50)
        print(data)
        query = """
                SELECT * FROM burgers
                LEFT JOIN add_ons ON burgers.id = add_ons.burger_id
                LEFT JOIN toppings ON toppings.id = add_ons.topping_id
                WHERE burgers.id = %(id)s;
                """
        # query = "SELECT * FROM burgers WHERE burgers.id = %(id)s;"
        results = connectToMySQL('burgers').query_db(query,data)
        burger = cls(results[0])
        # print('B'*50)
        # for result in results[0].items():
        #     print(result)
        for result in results:
            data = {
                'id' : result['topping_id'],
                'topping_name' : result['topping_name'],
                'created_at' : result['toppings.created_at'],
                'updated_at' : result['toppings.updated_at'],
            }
            this_topping = topping.Topping(data)
            burger.toppings.append(this_topping)


        return burger

    @classmethod
    def update(cls,data):
        query = "UPDATE burgers SET name=%(name)s, bun=%(bun)s, meat=%(meat)s, calories=%(calories)s,updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL('burgers').query_db(query,data)

    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM burgers WHERE id = %(id)s;"
        return connectToMySQL('burgers').query_db(query,data)

    @classmethod
    def get_burger_with_toppings(cls,data):
        query = """
                SELECT * FROM burgers
                LEFT JOIN add_ons ON add_ons.burger_id = burger.id 
                LEFT JOIN toppings ON add_ons.topping_id = toppings.id WHERE burgers.id = %(id)s;
                """
        return connectToMySQL('burgers').query_db(query,data)




