from flask_app import app
from flask_app.controllers import burgers
from flask_app.controllers import restaurants
from flask_app.controllers import toppings



if __name__=="__main__":
    app.run(debug=True,port=5001)