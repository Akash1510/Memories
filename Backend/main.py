from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS 

# initialize the flask application
app = Flask(__name__)
CORS(app)

# SetUp SQLAlchemy Configuration
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///local.db'
app.config['SQLALCHEMY_BINDS'] = {
    'users': 'sqlite:///users.db', 
    'friends': 'sqlite:///friends.db'
}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'Akash@3412323'

# Initialize SqlAlchemy
db = SQLAlchemy(app)

# Import routes
from Router.auth import *
from Router.box_router import *

# Create the database tables
with app.app_context(): 
    db.metadata.create_all(bind=db.get_engine(app, bind='users'))
    db.metadata.create_all(bind=db.get_engine(app, bind='friends'))

if __name__ == "__main__":
    app.run(debug=True)




