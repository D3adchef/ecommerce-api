from flask import request, jsonify
from app import app
from models import db, User, Product, Order
from schemas import UserSchema, ProductSchema, OrderSchema
from datetime import datetime

# Schemas
user_schema = UserSchema()
users_schema = UserSchema(many=True)

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)

# =======================
# USER ROUTES
# =======================
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify(users_schema.dump(users)), 200

@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify(user_schema.dump(user)), 200

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(
        name=data['name'],
        email=data['email'],
        address=data['address']
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify(user_schema.dump(new_user)), 201

@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    user = User.query.get_or_404(id)
    data = request.get_json()
    user.name = data.get('name', user.name)
    user.email = data.get('email', user.email)
    user.address = data.get('address', user.address)
    db.session.commit()
    return jsonify(user_schema.dump(user)), 200

@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get_or_404(id)
    for order in user.orders:
        db.session.delete(order)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User and related orders deleted"}), 200

# =======================
# PRODUCT ROUTES
# =======================
@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify(products_schema.dump(products)), 200

@app.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    product = Product.query.get_or_404(id)
    return jsonify(product_schema.dump(product)), 200

@app.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    new_product = Product(
        product_name=data['product_name'],
        description=data['description'],
        price=data['price'],
        stock_quantity=data['stock_quantity']
    )
    db.session.add(new_product)
    db.session.commit()
    return jsonify(product_schema.dump(new_product)), 201

@app.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    product = Product.query.get_or_404(id)
    data = request.get_json()
    product.product_name = data.get('product_name', product.product_name)
    product.description = data.get('description', product.description)
    product.price = data.get('price', product.price)
    product.stock_quantity = data.get('stock_quantity', product.stock_quantity)
    db.session.commit()
    return jsonify(product_schema.dump(product)), 200

@app.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({"message": "Product deleted"}), 200

# =======================
# ORDER ROUTES
# =======================
@app.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    user_id = data.get('user_id')
    order = Order(order_date=datetime.utcnow(), user_id=user_id)
    db.session.add(order)
    db.session.commit()
    return jsonify(order_schema.dump(order)), 201

@app.route('/orders', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    return jsonify(orders_schema.dump(orders)), 200

@app.route('/orders/<int:order_id>/add_product/<int:product_id>', methods=['PUT'])
def add_product_to_order(order_id, product_id):
    order = Order.query.get_or_404(order_id)
    product = Product.query.get_or_404(product_id)
    if product not in order.products:
        order.products.append(product)
        db.session.commit()
        return jsonify({"message": "Product added to order"}), 200
    return jsonify({"message": "Product already in order"}), 200

@app.route('/orders/<int:order_id>/remove_product/<int:product_id>', methods=['DELETE'])
def remove_product_from_order(order_id, product_id):
    order = Order.query.get_or_404(order_id)
    product = Product.query.get_or_404(product_id)
    if product in order.products:
        order.products.remove(product)
        db.session.commit()
        return jsonify({"message": "Product removed from order"}), 200
    return jsonify({"message": "Product not in order"}), 404

@app.route('/orders/user/<int:user_id>', methods=['GET'])
def get_orders_for_user(user_id):
    orders = Order.query.filter_by(user_id=user_id).all()
    return jsonify(orders_schema.dump(orders)), 200

@app.route('/orders/<int:order_id>/products', methods=['GET'])
def get_products_for_order(order_id):
    order = Order.query.get_or_404(order_id)
    return jsonify(products_schema.dump(order.products)), 200

@app.route('/orders/<int:id>', methods=['DELETE'])
def delete_order(id):
    order = Order.query.get_or_404(id)
    db.session.delete(order)
    db.session.commit()
    return jsonify({"message": "Order deleted"}), 200
