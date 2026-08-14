import pytest

from flask import current_app # will eventully pull DB name (minus extension) from config
from sqlalchemy import (create_engine)
from sqlalchemy.exc import (OperationalError, ProgrammingError)

from src.Pyle.app import create_app
from src.Pyle.config import TestConfig

DB_NAME = 'sqlite:///pyle_test.db'

'''
Test App
'''
@pytest.fixture(scope='session')
def app():
    app = create_app(TestConfig)

    yield app

'''
Test Client
'''
@pytest.fixture(scope='session')
def client(app):
    return app.test_client()

'''
Test Database Connection
'''
@pytest.fixture(scope='module')
def db_session():
    conn = create_engine.conenct()
    pass

'''
Test 'Vehicle' object for adding vehicle
'''
@pytest.fixture(scope='session')
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
Test 'Vehicle' object for updating vehicle
'''
@pytest.fixture(scope='session')
def test_updated_vehicle():
    vehicle = {
        'vehicle_name' : 'Test Vehicle',
        'vehicle_year' : '1972',
        'vehicle_make' : 'AMC',
        'vehicle_model' : 'Gremlin',
        'mileage' : '555,089',
        'vin' : 'TOH4M0l3MAN',
        'engine_type' : 'V8',
        'engine_volume_liters' : '5.0',
        'transmission_model' : 'Chrysler TorqueFlite',
        'transmission_speed' : '3',
        'transmission_type' : 'automatic',
        'oil_type' : 'ZDDP',
        'oil_weight' : '10W-30',
        'oil_volume_qt' : '6.0'
        }

'''
Test 'Maintenance' object for adding a new maintenance record
'''
@pytest.fixture(scope='session')
def test_maintenance():
    maintenance = {
        # NOTE Will add logic later for incrementing a uuid for use as vehicle id
        # 'vehicle_id' : '1001',
        'vehicle_name' : 'Test Vehicle',
        'date' : '2025-10-31',
        'miles' : '550,089',
        'technician' : 'Otto',
        'service_name' : 'Oil Change',
        'service_notes' : 'Drain/fill oil, replace filter, new crush washer',
        'replacement_part' : 'Valvoline VR1 10W-30',
        'lifespan_miles' :'5000',
        'lifespan_months' : '12'
        }

'''
Test 'Maintenance' object for updating an existing record
'''
@pytest.fixture(scope='session')
def test_maintenance_update():
    maintenance = {
        'vehicle_id' : '1001',
        'date' : '2025-10-31',
        'miles' : '550,089',
        'technician' : 'Otto',
        'service_name' : 'Oil Change',
        'service_notes' : 'Drain/fill oil, replace filter, new crush washer',
        'replacement_part' : 'Valvoline VR1 10W-30',
        'lifespan_miles' :'3000',
        'lifespan_months' : '12',
        }