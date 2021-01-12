from flask_wtf import Form
from wtforms import IntegerField, TextField, DateTimeField, TextAreaField, StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, InputRequired, Email, Length

class TodoForm(Form):
    text = TextField('text', validators=[DataRequired()])
    date = DateTimeField('date', format='%m-%d-%y %H:%M', validators=[DataRequired()])
    desc = TextAreaField('desc')

class LogInForm(Form):
    username = StringField('username', validators=[DataRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])

class RegisterForm(Form):
    email = StringField('email', validators=[DataRequired(), Length(min=4, max=50)])
    username = StringField('username', validators=[DataRequired(), Length(min=4, max=50)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])

class BlogPostForm(Form):
    title = TextField('title', validators=[DataRequired()])
    blogBody = TextAreaField('blogBody', validators=[DataRequired()])
