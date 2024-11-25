from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS 



# initialize the flask application
app = Flask(__name__)
CORS(app)

# SetUp SQLAlchemy Configuration

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///friends.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Initialize SqlAlchemy
db = SQLAlchemy(app)


from Router.box_router import *
# Create the database tables 
with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)

