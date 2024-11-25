from main import app, db 
from Model.box import Friend 
from flask import request, jsonify


@app.route('/',methods=['GET'])
def show():
    return "<h1>Hello World</h1>"

@app.route("/api/friends", methods=['GET']) 
def get_friends(): 
    friends = Friend.query.all() 
    result = [friend.to_json() for friend in friends]
    return jsonify(result)