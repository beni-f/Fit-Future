from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, IntegerField, PasswordField, SubmitField, BooleanField, SelectField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Length, Email, NumberRange, EqualTo, ValidationError
from fitfuture.db_models import User

class Registration(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired(), Length(min=6, max=20)])
    height = IntegerField('Height', validators=[DataRequired(), NumberRange(max=300)])
    weight = IntegerField('Weight', validators=[DataRequired(), NumberRange(max=700)])
    gender_choices = [('male', 'Male'), ('female', 'Female'), ('other', 'Rather not to say')]
    gender = SelectField('Gender', choices=gender_choices, validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=32)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username Already Exists.')
    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('Email Already Exists.')
        

class Login(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=32)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
    
class UpdateAccount(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=6, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Username Already Exists.')
    def validate_email(self, email):
        if email.data != current_user.email:
            user_email = User.query.filter_by(email=email.data).first()
            if user_email:
                raise ValidationError('Email Already Exists.')