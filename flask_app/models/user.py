from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get(cls,data):
        query = 'SELECT * FROM users WHERE id=%(id)s;'
        result = connectToMySQL('users').query_db(query,data)
        print("result[0] = ",result[0])
        user = cls(result[0])
        return user

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM users;'
        results = connectToMySQL('users').query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def save_user(cls,data):
        query = """
                INSERT INTO users (first_name, last_name, email)
                VALUES (%(first_name)s,%(last_name)s,%(email)s)
                """
        return connectToMySQL('users').query_db(query,data)

    @classmethod
    def delete(cls,data):
        query = 'DELETE FROM users WHERE id=%(id)s;'
        connectToMySQL('users').query_db(query,data)

    @classmethod
    def update(cls,data):
        query = """
                UPDATE users 
                SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s 
                WHERE id=%(id)s;
                """
        connectToMySQL('users').query_db(query,data)
