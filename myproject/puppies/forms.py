# forms.py puppies
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class AddForm(FlaskForm):

    name = StringField('Name of Puppy: ')
    color = StringField('Add Color: ')
    breed = StringField('Type of breed: ')
    submit = SubmitField('Add Puppy')
    


class DelForm(FlaskForm):

    id = IntegerField("Id Number of Puppy to Remove: ")
    submit = SubmitField("Remove Puppy")


