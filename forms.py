from flask_wtf import FlaskForm
import flask_wtf
from wtforms import StringField, FloatField
from wtforms.validators import InputRequired, Optional, Email
from models import default_img

class AddCupcakeForm(FlaskForm):
    """Form for adding cupcakes"""

    flavor = StringField('Flavor', validators=[InputRequired(message='Must add flavor')])
    size = StringField('Size', validators=[InputRequired(message='Must add size')])
    rating = FloatField('Rating', validators=[InputRequired(message='Must add rating')])
    image = StringField('Image', default=default_img)
