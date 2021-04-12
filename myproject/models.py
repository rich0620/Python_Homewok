# Models.py
# set up db inside the __init__.py under myproject folder

from myproject import db

class Puppy(db.Model):

    __tablename__ = 'puppies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    color = db.Column(db.Text)
    breed = db.Column(db.Text)
    owner = db.relationship('Owner', backref='puppy', uselist=False)

    def __init__(self, name, color, breed):
        self.name = name
        self.color = color
        self.breed = breed

    def __repr__(self):
        if self.owner:
            return f"Puppy name is {self.name} which is a {self.color} {self.breed} and the owner is {self.owner.name}"
        else:
            return f"Puppy name is {self.name} which is a {self.color} {self.breed} and has no owner!"


class Owner(db.Model):

    __tablename__ = 'owners'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer, db.ForeignKey('puppies.id'))

    def __init__(self, name, puppy_id):
        self.name = name
        self.puppy_id = puppy_id

    def __repr__(self):
        return f"Owner Name: {self.name}"

db.create_all()
