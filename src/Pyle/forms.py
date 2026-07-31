from decimal import Decimal

from flask_wtf import FlaskForm
from wtforms import (
    DecimalField,
    IntegerField,
    StringField,
    SubmitField
    )
from wtforms.validators import (
    DataRequired,
    NumberRange
    )

'''
Form to add new vehicle to database
'''
class NewVehicleForm(FlaskForm):
    vehicle_name = StringField('Vehicle Name', validators=[DataRequired(message='Must provide profile name.')])
    vehicle_year = IntegerField('Year')
    vehicle_make = StringField('Make/Manufacturer')
    vehicle_model = StringField('Model')
    vin = StringField('VIN or Serial #')
    mileage = DecimalField('Miles', validators=[NumberRange(min=Decimal('0.01'), message='Mileage cannot be negative.')])
    add_profile = SubmitField('Save Vehicle')

'''
Form to select new active vehicle
'''

'''
Form to add maintenance event
'''

