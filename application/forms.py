from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired

class TodoForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    description = TextAreaField("Description", validators=[DataRequired()])
    completed = SelectField("Completed", choices=[("False", "False"), ("True", "True")], validators=[DataRequired()])
    submit = SubmitField("Add TODO")
