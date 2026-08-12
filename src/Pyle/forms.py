from decimal import Decimal

from flask_wtf import FlaskForm
from wtforms import (
    DateTimeLocalField,
    DecimalField,
    IntegerField,
    StringField,
    SubmitField,
    TextAreaField
    )
from wtforms.validators import (
    DataRequired,
    Length,
    NumberRange
    )

'''
Form to add new vehicle to database
'''
class NewVehicleForm(FlaskForm):
    vehicle_name = StringField(
        'Vehicle Name',
        validators=[DataRequired(message='Must provide profile name.')]
        )
    vehicle_year = IntegerField('Year')
    vehicle_make = StringField('Make/Manufacturer')
    vehicle_model = StringField('Model')
    vin = StringField('VIN or Serial #')
    mileage = DecimalField(
        'Miles',
        validators=[NumberRange(min=Decimal('0.01'), message='Mileage cannot be negative.')]
        )
    
    add_profile = SubmitField('Save Vehicle')

'''
Form to select new active vehicle
'''

'''
Form to add maintenance Record
'''
class NewRecordForm(FlaskForm):
    vehicle_name = StringField(
        'Vehicle Name',
        validators=[DataRequired(message='Must provide profile name.')]
        )
    date = DateTimeLocalField(
        'Date/Time',
        validators=[DataRequired(message='Must add the date.')]
        )
    mileage = DecimalField(
        'Miles',
        validators=[NumberRange(min=Decimal('0.01'), message='Mileage cannot be negative.')]
        )
    technician = StringField(
        'Technician',
        validators=[DataRequired(message='Must provide technician name.')]
        )
    service_name = StringField(
        'Service Name',
        validators=[DataRequired(message='Must provide service name.')]
        )
    service_notes = TextAreaField(
        'Service Notes',
        validators=[Length(max=500, message='Note is too long.')]
        )
    replacement_part = StringField('Replacement Part')
    lifespan_miles = IntegerField(
        'Lifespan (Miles)',
        validators=[NumberRange(min=0, message='Mileage cannot be negative.')]
        )
    lifespan_months = IntegerField(
            'Lifespan (Months)',
            validators=[NumberRange(min=0, message='Months cannot be negative.')]
            )
    
    add_record = SubmitField('Save Record')
