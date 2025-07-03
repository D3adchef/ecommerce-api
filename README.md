A full-featured RESTful API built with Flask, SQLAlchemy, Marshmallow, and MySQL, designed to manage users, products, and orders for an online store.

🔧 Technologies Used
Python

Flask

SQLAlchemy (ORM)

Marshmallow (Serialization & Validation)

MySQL

Postman (for testing)

📦 Features
👤 User Endpoints
GET /users: Get all users

GET /users/<id>: Get a user by ID

POST /users: Create a user

PUT /users/<id>: Update a user

DELETE /users/<id>: Delete a user

📦 Product Endpoints
GET /products: Get all products

GET /products/<id>: Get product by ID

POST /products: Add a product

PUT /products/<id>: Update a product

DELETE /products/<id>: Delete a product

🧾 Order Endpoints
POST /orders: Create an order with user ID

PUT /orders/<order_id>/add_product/<product_id>: Add a product to an order

DELETE /orders/<order_id>/remove_product/<product_id>: Remove product from order

GET /orders/user/<user_id>: Get all orders for a user

GET /orders/<order_id>/products: Get all products in an order

🗂 Database Schema
One-to-Many: A user can have many orders

Many-to-Many: Orders and Products have a many-to-many relationship

⚙️ Setup Instructions
Clone this repo

bash
Copy
Edit
git clone https://github.com/d3adchef/ecommerce-api.git
cd ecommerce-api
Create virtual environment and activate it

bash
Copy
Edit
python -m venv venv
venv\Scripts\activate    # Windows
# OR
source venv/bin/activate # macOS/Linux
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Set up MySQL Database

Open MySQL Workbench

Create a database called ecommerce_api

Update your app.py connection string:

python
Copy
Edit
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:<your_password>@localhost/ecommerce_api'
Run the app

bash
Copy
Edit
flask run
Test with Postman

Import and use the Postman collection

Make requests to http://localhost:5000

📸 Screenshots (optional)
You can add Postman screenshots here later.

👤 Author
GitHub: @d3adchef

