from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,FieldList,RadioField,IntegerField,EmailField

class UserForm(Form):
    
    nombre=StringField("nombre")
    apellido=StringField("apellido")
    matricula=StringField("matricula")
    email=EmailField("email")