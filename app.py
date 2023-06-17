from flask import Flask, request
app = Flask(__name__)

stores = [{"name": "my-store", 'items': [{"name": "my-item", "price": 299}]}]

#get all the stores
@app.get("/store")
def get_stores():
    return {"stores": stores}

# get specific store
@app.get("/store/<string:name>")
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return store
    return {"message": "Store not found"}, 404

# create new store
@app.post("/store")
def create_Store():
    request_data = request.get_json()
    new_store = {"name": request_data['name'], "items": []}
    stores.append(new_store)
    return new_store, 201

# create new item associate with store
@app.post("/store/<string:name>/item")
def create_item(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {"name": request_data['name'], "price": request_data['price']}
            store["items"].append(new_item)
            return new_item
    return {"message": "store not found"}, 404


# get the itmes withing the store
@app.get("/store/<string:name>/item")
def get_items_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            return {"items": store['items']}
    return {"message": "Store Not Found"}


app.run()