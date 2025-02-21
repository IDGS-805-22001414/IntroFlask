from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, RadioField, SubmitField
from wtforms.validators import DataRequired, NumberRange, Email

class UserForm(FlaskForm):
    nombre= StringField("Nombre", validators=[DataRequired()])
    apellido = StringField("Apellido", validators=[DataRequired()])
    matricula = StringField("Matrícula", validators=[DataRequired()])
    email = StringField("Correo", validators=[DataRequired(), Email()])

class ZodiacoForm(FlaskForm):  
    nombre = StringField("Nombre", validators=[DataRequired()])
    apellido = StringField("Apellidos", validators=[DataRequired()])
    dia = IntegerField("Día de nacimiento", validators=[DataRequired(), NumberRange(1, 31)])
    mes = IntegerField("Mes de nacimiento", validators=[DataRequired(), NumberRange(1, 12)])
    anio = IntegerField("Año de nacimiento", validators=[DataRequired(), NumberRange(1900, 2025)])
    
    sexo = RadioField("Sexo", choices=[('M', 'Masculino'), ('F', 'Femenino')], validators=[DataRequired()])
    
    submit = SubmitField("Calcular Signo")


