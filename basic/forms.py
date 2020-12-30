from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email


class ExampleForm(FlaskForm):
    name = StringField("Name",validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    subject = StringField("Subject",validators=[DataRequired()])
    message = TextAreaField("Message",validators=[DataRequired()])
    submit_email = SubmitField("Send")