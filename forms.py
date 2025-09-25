from flask_wtf import FlaskForm
from pyexpat.errors import messages
from wtforms.fields.simple import StringField, PasswordField, SubmitField
from wtforms.validators import data_required, input_required, EqualTo, length
from wtforms import fields


class registrationForm(FlaskForm):
    username = StringField (label='Username :',validators=[data_required(message='username is required'),input_required(message='username is required'),length(min =3,message='the name must be up then 3 character')])
    password =  PasswordField(label='Password',validators=[data_required(message='password is required'),input_required(message='password is required'),length(min=8,max=16, message='the password must be under then 16 character and  up then 8 character')])
    confirm = PasswordField(label='Confirm Password',validators=[data_required(message='confirme password is required'),input_required(message='confirme password is required'),EqualTo('password',message='password must match')])
    submit = SubmitField(label='Submit')

class loginForm(FlaskForm):
    username = StringField(label='Username :', validators=[data_required(message='username is required'),input_required(message='username is required'), length(min=3, message='the name must be up then 3 character')])
    password = PasswordField(label='Password', validators=[data_required(message='password is required'),input_required(message='password is required'),length(min=8, max=16, message='the password must be under then 16 character and  up then 8 character')])
    submit = SubmitField(label='Submit')