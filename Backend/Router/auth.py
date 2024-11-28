from main import app,db
from Model.User import User
from flask import request,jsonify
from flask_bcrypt import Bcrypt
from validations.validators import user_validation
from flask_jwt_extended import JWTManager,create_access_token,jwt_required,get_jwt_identity
from datetime import timedelta

bcrypt = Bcrypt(app)
jwt = JWTManager(app)

@app.route('/api/signup',methods=['POST'])

def signup():
    try:
        data = request.get_json()

        # check the data
        for field in data:
            if field not in ['name','email','password']:
                return jsonify({'error':'Invalid data'}),400

        name = data.get('name')
        email = data.get('email')
        password = data.get('password')

        # now vaidate all data from the body
        if(not name or not password or not email):
            return jsonify({'message':'Required to Filled the Details'})
        
        # Now Validate email
        # if(not user_validation(email=email)):
        #     return jsonify({'message':'Invalid Email'})
        # Check wheher email already exist or not in database
        
        user = User.query.filter_by(email=email).first()
        if(user):
            return jsonify({'message':'User Already Exist'})
        hash_password = bcrypt.generate_password_hash(password).decode('utf-8')
        # Now insert data into database
        New_user = User(name=name,email=email,password=hash_password)
        db.session.add(New_user)
        db.session.commit()

        return jsonify({'message':'User Created Successfully'}),200        
    except Exception as e:
        db.session.rollback()
        return jsonify({'message':"Error in Data"}),500



@app.route('/api/login',methods=['POST'])

def login():
    try:
        data = request.get_json()
        if not data or not 'email'in data or not 'password' in data:
            return jsonify({'message':'Email and password are requied'})
        email = data.get('email')
        password = data.get('password')

        user = User.query.filter_by(email=email).first()
        if(not user):
            return jsonify({'message':'User Not Found'})
        if(not bcrypt.check_password_hash(user.password,password)):
            return jsonify({'message':'Invalid Password'})
        # Create the JWT token
        access_token = create_access_token(identity={'email':user.email},expires_delta=timedelta(minutes=20))
        return jsonify({access_token:access_token},{email:user.email}),200

    except Exception as e:
        db.session.rollback()
        return jsonify({'message':"Error in Data"}),500
        

# FOr the Authentication 
@app.route('/api/protected',methods=['GET'])
@jwt_required()
def protected():
    # Access the identity of the current user
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user),200


@app.route('/api/users',methods=['GET'])

def getAll():
    users = User.query.all()
    output = [user.to_json() for user in users]
    return jsonify(output)
