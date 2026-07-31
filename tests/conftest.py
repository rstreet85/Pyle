import pytest

from src.Pyle.app import create_app
from src.Pyle.config import TestConfig

'''
Test App
'''
@pytest.fixture()
def app():
    app = create_app(TestConfig)

    yield app

'''
Test Client
'''
@pytest.fixture()
def client(app):
    return app.test_client()

'''
Test 'New Vehicle' object
'''
@pytest.fixture()
def test_vehicle():
    vehicle = {
        'vehicle_name' : 'Test Vehicle',
        'vehicle_year' : '1972',
        'vehicle_make' : 'AMC',
        'vehicle_model' : 'Gremlin',
        'mileage' : '555,089',
        'vin' : 'TOH4M0l3MAN'
        }

'''
Test 'New Maintenance Record' object
'''
@pytest.fixture()
def test_maintenance():
    maintenance = {
        'date':'2026-01-',
        'vehicle_id':'1001',
        'miles':'550,089',
        'technician':'Otto',
        'service_name':'Oil Change',
        'service_notes':'Drain/fill oil, replace filter, new crush washer',
        'replacement_part':'Valvoline VR1 10W-30',
        'lifespan_miles':'5000',
        'lifespan_months':''
        }
