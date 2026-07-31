import pytest

from src.Pyle.app import create_app
from src.Pyle.config import TestConfig

'''
Test App creation
'''
@pytest.fixture()
def app():
    app = create_app(TestConfig)

    yield app

'''
Test Client configuration
'''
@pytest.fixture()
def client(app):
    return app.test_client()

'''
Test Vehicle object
'''
@pytest.fixture()
def test_vehicle():
    vehicle = []