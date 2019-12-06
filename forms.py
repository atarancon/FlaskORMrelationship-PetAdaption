from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddOwner(FlaskForm): 
    name = StringField("Name of owner:")
    id = IntegerField("Which puppy do you want?, Enter ID:")
    submit = SubmitField("Add owner")

class AddForm(FlaskForm):
    name = StringField("Name of pup:")
    submit = SubmitField("Add puppy")

class DelForm(FlaskForm):
    id = IntegerField("ID of Puppy to be removed:")
    submit = SubmitField("Remove Puppy")
