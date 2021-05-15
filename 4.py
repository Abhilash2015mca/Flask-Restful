# used argument parsing
import string
from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

items = []


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("name", type=string, help="Please Enter the Name of the Item")
    parser.add_argument("price", type=float, help="Please Enter the Price of the Item")

    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {" item": item}, 200 if item is not None else 404
        # print single item

    def delete(self, name):
        global items
        if next(filter(lambda x: x['name'] == name, items), None):
            items = list(filter(lambda x: x['name'] != name, items))
            return {name: "is deleted"}, 200
        return {name: "not found"}, 404
        # delete the requested item


class addItem(Resource):
    def post(self):
        data = Item.parser.parse_args()
        if next(filter(lambda x: x['name'] == data["name"], items), None):
            return {" item": "Already Present"}
        item = {"name": data["name"], "price": data["price"]}
        items.append(item)
        return {item["name"]: "inserted"}, 201
        # Add a single item at a time and returns that

    def put(self):
        data = Item.parser.parse_args()
        item = next(filter(lambda x: x['name'] == data["name"], items), None)
        if item is None:
            item = {"name": data["name"], "price": data["price"]}
            items.append(item)
            return {item["name"]: "inserted"}, 201
            # add item if item is not present
        else:
            item.update(data)
            return {item["name"]: "updated"}, 200
            # update item


class itemList(Resource):
    def get(self):
        return {"items": items}, 200
    # returns the full item list


api.add_resource(Item, '/item/<string:name>/')
api.add_resource(addItem, '/add/')
api.add_resource(itemList, '/items/')
if __name__ == '__main__':
    app.run(debug=True)
