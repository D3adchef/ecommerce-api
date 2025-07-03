from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from models import db, User, Product, Order

app = Flask(__name__)

# Connect to your MySQL database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:Sp%40uld%21ng80@localhost/ecommerce_api'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize after app is configured
db.init_app(app)
ma = Marshmallow(app)

# ✅ Import routes BEFORE running app
from routes import *

if __name__ == '__main__':
    app.run(debug=True)
