from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class ModelePredictionForm(FlaskForm):
    TV = StringField("TV", validators=[DataRequired()])
    Radio = StringField("Radio", validators=[DataRequired()])
    Newspaper = StringField("Newspaper", validators=[DataRequired()])

    submit = SubmitField("Prédire")

