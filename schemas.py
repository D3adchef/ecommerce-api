from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from models import User, Product, Order

class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True

class ProductSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Product
        load_instance = True
        include_fk = True

    product_name = fields.Str(required=True)
    description = fields.Str(required=True)
    price = fields.Float(required=True)
    stock_quantity = fields.Int(required=True)

class OrderSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Order
        load_instance = True
        include_fk = True

    # Include nested product data when serializing
    products = fields.Nested(ProductSchema, many=True)
