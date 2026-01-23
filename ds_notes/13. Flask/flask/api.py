'''
This code demonstrates the working with APIs (JSON) and several HTTP requests like GET, POST, PUT, DELETE (HTTP Verbs)
'''

'''Creating a To-Do list'''

from flask import Flask, request, jsonify

app = Flask(__name__)


## Initial Data in my to do list
items = [
    {"id":1, "name":"Item 1", "description":"This is the Item 1"},
    {"id":2, "name":"Item 2", "description":"This is the Item 2"}
]


## If we do not set manually, all the methods by default are set to GET
@app.route('/')
def home():
    return "<html><H1>Welcome to the sample To-Do list App!</H1></html>"


## GET: To retrieve all the items
@app.route('/items')
def get_items():
    return jsonify(items)


## GET: To retrieve a specific item using the item_id
@app.route('/items/<int:item_id>')
def get_specific_item(item_id):
    ## Using iterator which returns None if not found for any match
    item = next((item for item in items if item["id"]==item_id), None)
    if item is None:
        return jsonify({"error":"Item not found !"})
    return jsonify(item)
    

## POST: To create a new_item in the To-Do list     //--API
@app.route('/items', methods=['POST'])
def create_item():
    ## Check if the request has json and that json request has name field and if not, throw the error
    if not request.json or not "name" in request.json:
        return jsonify({"error": "Item not found"})
    else:
        new_item={
            ## if there are existing items, take the last item_id in the items and add 1, otherwise start from 1
            "id":items[-1]["id"]+1 if items else 1,
            ## take name field from the input json body
            "name":request.json["name"],
            ## take description field from the input json body
            "description":request.json["description"]
        }
        ## add the new_item to the items
        items.append(new_item)
        ## display the added item
        return jsonify(new_item)



'''
Difference between POST and PUT is that:
POST: Used to create a new item
PUT: Used to update an existing item
'''
## PUT: To update an item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    ## search for the matching item_id
    item = next((item for item in items if item["id"]==item_id), None)
    if item is None:
        ## error if not found
        return jsonify({"error": "Item not found !"})
    else:
        ## since we are handling with PUT method, to update the field, we must use get to POST i.e., to pass the parameter and capture it like POST method
        ## to get name from the json and update item
        item["name"]=request.json.get("name", item["name"])
        ## to get description from the json and update item
        item["description"]=request.json.get("description", item["description"])
        return jsonify(item)


## DELETE: Delete an item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    ## make the items global inorder to observe the change after delete operation
    global items
    ## store all the items that are not matching with item_id
    items = [item for item in items if item["id"]!=item_id]
    return jsonify({"result":"Item deleted !"})



if __name__=='__main__':
    app.run(debug=True)