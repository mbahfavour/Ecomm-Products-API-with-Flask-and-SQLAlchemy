from email import message
from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tmp/database.db'
db = SQLAlchemy(app)

class ProductModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(300), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Products(name = {name} ,description = {description}, category = {category}, image= {image}, price = {price})"



products_post_args = reqparse.RequestParser()
products_post_args.add_argument(
    "name", type=str, help="Post name of product", required=True)
products_post_args.add_argument(
    "description", type=str, help="Post description of product", required=True)
products_post_args.add_argument(
    "image", type=str, help="Post image of product", required=True)
products_post_args.add_argument(
    "category", type=str, help="Post category of product", required=True)
products_post_args.add_argument(
    "price", type=int, help="Post price of product", required=True)

products_update_args = reqparse.RequestParser()
products_update_args.add_argument(
    "name", type=str, help="Post name of product")
products_update_args.add_argument(
    "description", type=str, help="Post description of product")
products_update_args.add_argument(
    "image", type=str, help="Post image of product")
products_update_args.add_argument(
    "category", type=str, help="Post category of product")
products_update_args.add_argument(
    "price", type=int, help="Post price of product")


resource_fields = {
    "id" : fields.Integer,
    "name": fields.String,
    "description": fields.String,
    "image": fields.String,
    "category": fields.String,
    "price": fields.Integer
}

class Products(Resource):
    @marshal_with(resource_fields)
    def get(self, product_id):
        result = ProductModel.query.filter_by(id=product_id).first()
        if not result:
            abort(404, "Could not find video with that id")
        return result
    
    @marshal_with(resource_fields)
    def post(self, product_id):
        args = products_post_args.parse_args()
        result = ProductModel.query.filter_by(id=product_id).first()
        if result:
            abort(409, "ID taken already")
        product = ProductModel(id=product_id, name=args['name'], description=args['description'], image=args['image'], category=args['category'], price=args['price'])
        db.session.add(product)
        db.session.commit()
        return product, 201
    
    @marshal_with(resource_fields)
    def put(self, product_id):
        args = products_update_args.parse_args()
        result = ProductModel.query.filter_by(id=product_id).first()
        if not result:
            abort(404, "Could not find video with that id. Cannot update")
        if args['name']:
            result.name = args['name']
        if args['description']:
            result.description = args['description']
        if args['category']:
            result.category = args['category']
        if args['image']:
            result.image = args['image']
        if args['price']:
            result.price = args['price']

        db.session.commit()
        return result
    
    # def delete(self, product_id):
    #     result = ProductModel.query.filter_by(id=product_id).first()
    #     # if not result:
    #     #     abort(404, "Could not find video with that id")
    #     db.session.delete(result)
    #     db.session.commit()
    #     return "", 204



api.add_resource(Products, "/products/<int:product_id>")

if __name__ == "__main__":
    app.run(debug=True)
