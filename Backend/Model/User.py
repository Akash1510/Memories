from main import db

class User(db.Model):
    __bind_key__ ='users'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80),nullable=False)
    email = db.Column(db.String(80),unique=True,nullable=False)
    password = db.Column(db.String(80),nullable=False)

    def to_json(self):
        return {
            "id":self.id,
            "name":self.name,
            "email":self.email,
            "password":self.password
        }
