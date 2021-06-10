from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo


class MineInfoForm(FlaskForm):
    mine_name = StringField('Mine site', validators=[DataRequired(), Length(1, 64)])
    mine_mineral = StringField('Mineral', validators=[DataRequired(), Length(1, 64)])
    submit = SubmitField('Submit')
