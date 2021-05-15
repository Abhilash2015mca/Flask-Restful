from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = []


class Item(Resource):
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item
        return {"Item not found"}, 404
        # print single item

    def post(self, name):
        item = {"name": name, "price": 112.00}
        items.append(item)
        return item, 201
    # Add a single item at a time and returns that


class itemList(Resource):
    def get(self):
        return {"items": items}, 200
    # returns the full item list


api.add_resource(Item, '/item/<string:name>/')
api.add_resource(itemList, '/items/')
if __name__ == '__main__':
    app.run(debug=True)
