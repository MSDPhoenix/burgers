from flask_app.config.mysqlconnection import connectToMySQL

class Restaurant:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get(cls,data):
        query = 'SELECT * FROM restaurants WHERE id=%(id)s;'
        result = connectToMySQL('burgers').query_db(query,data)
        print("result[0] = ",result[0])
        restaurant = cls(result[0])
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
