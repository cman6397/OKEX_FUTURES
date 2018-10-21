from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, DecimalField
from wtforms.validators import DataRequired, Optional, Length, InputRequired, NumberRange


class LoginForm(FlaskForm):
	username = StringField('Username', validators=[InputRequired(),Length(max=50)])
	password = PasswordField('Password', validators=[InputRequired(),Length(max=50)])
	submit = SubmitField('Sign In')


		


