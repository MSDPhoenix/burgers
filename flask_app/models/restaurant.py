from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.topping import Topping
from flask_app.models.burger import Burger
# from flask_app.models import topping


class Restaurant:

    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.burgers = []

    @classmethod
    def get(cls,data):
        query = '''
                SELECT * FROM restaurants 
                LEFT JOIN burgers ON restaurants.id = burgers.restaurant_id
                WHERE restaurants.id=%(id)s;
                '''
        results = connectToMySQL('burgers').query_db(query,data)
        restaurant = cls(results[0])
        print('A'*50)
        if results[0]['burgers.id']:
        #     print('***',results[0]['burgers.id'])
        # else:
        #     print('hello')

            for result in results:
                burger_data = {
                    'id' : result['burgers.id'],
                    'name' :result['burgers.name'],
                    'bun' : result['bun'],
                    'meat' : result['meat'],
                    'calories' : result['calories'],
                    'created_at' : result['burgers.created_at'],
                    'updated_at' : result['burgers.updated_at'],
                }
                this_burger = Burger(burger_data)
                # print(this_burger.id)
                # print(this_burger.name)
                # print(this_burger.bun)
                # print(this_burger.meat)
                # print(this_burger.calories)
                restaurant.burgers.append(this_burger)
                toppings = Topping.get_toppings(burger_data)
                for topping in toppings:
                    this_burger.toppings.append(topping)
        return restaurant

    def get_by_burger_id(cls,data):
        query = '''
                SELECT * FROM restaurants 
                LEFT JOIN burgers ON restaurants.id = burgers.restaurant_id
                WHERE burgers.id=%(id)s;
                '''
        results = connectToMySQL('burgers').query_db(query,data)
        restaurant = cls(results[0])
        for result in results:
            data = {
                'id' : result['burgers.id'],
                'name' :result['burgers.name'],
                'bun' : result['bun'],
                'meat' : result['meat'],
                'calories' : result['calories'],
                'created_at' : result['burgers.created_at'],
                'updated_at' : result['burgers.updated_at'],
            }
            this_burger = Burger(data)
            restaurant.burgers.append(this_burger)
            toppings = Topping.get_toppings(data)
            for topping in toppings:
                this_burger.toppings.append(topping)
            return restaurant

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM restaurants;'
        results = connectToMySQL('burgers').query_db(query)
        restaurants = []
        for restaurant in results:
            restaurants.append(cls(restaurant))
        return restaurants

    @classmethod
    def save_restaurant(cls,data):
        query = """
                INSERT INTO restaurants (name)
                VALUES (%(name)s)
                """
        return connectToMySQL('burgers').query_db(query,data)

    @classmethod
    def delete(cls,data):
        query = 'DELETE FROM restaurants WHERE id=%(id)s;'
        connectToMySQL('burgers').query_db(query,data)

    @classmethod
    def update(cls,data):
        query = """
                UPDATE restaurants 
                SET name=%(name)s
                WHERE id=%(id)s;
                """
        connectToMySQL('burgers').query_db(query,data)
