from main import app, db 
from Model.box import Friend 
from flask import request, jsonify
from validations.validators import get_avatar_url


@app.route('/',methods=['GET'])
def index():
    return "<h1>Hello Welcomes to Friends Book</h1>"
@app.route("/api/friends", methods=['GET']) 
def get_friends(): 
    friends = Friend.query.all() 
    result = [friend.to_json() for friend in friends]
    return jsonify(result)

@app.route("/api/create",methods=['POST'])

def create_post():
   try:
       data = request.get_json()

    # validations
       required_field = ['name','role','description','gender']
       for field in required_field:
           if field not in data or not data.get(field):
               return jsonify({"error":f"Missing the required Field{field}"})
        
       name = data.get('name')
       role= data.get('role')
       description = data.get('description')
       gender = data.get('gender')

       img_url = get_avatar_url(gender,name)

       new_friend= Friend(name=name,role=role,description=description,gender=gender,img_url=img_url)
       db.session.add(new_friend)
       db.session.commit()

       return jsonify(new_friend.to_json()),200

   except Exception as e:
       db.session.rollback()
       return jsonify({"Not valid Data":str(e)}),500
       


#    delete the freind
@app.route("/api/friends/<int:id>",methods=["DELETE"])

def delete_friend(id):
    try:
        user = Friend.query.get(id)
        if(user):
            db.session.delete(user)
            db.session.commit()
            return jsonify({"message":"Freind is Deleted Successfully"}),200

        else:
            return jsonify({'message':'User Not Found'}),404
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"error":"Not Vaild Id"},e),500
    

# Update the Friend

@app.route('/api/friends/<int:id>',methods=['PATCH'])

def Update_freind(id):
    try:
        user = Friend.query.get(id)

        if(not user):
            return jsonify({'message':'User Not Found'}),404
        data = request.get_json()

        user.name = data.get('name',user.name)
        user.role = data.get('role',user.role)
        user.description = data.get('description',user.description)
        user.gender = data.get('gender',user.gender)
        user.img_url = get_avatar_url(user.gender,user.name)
        
        db.session.commit()
        return jsonify({'message':"Friend Updated SuccessFully"}),200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error":str(e)}),500