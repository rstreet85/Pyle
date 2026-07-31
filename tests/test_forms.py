'''
Test the Add New Vehicle form
'''
def test_new_vehicle(client, test_vehicle):
    response = client.post('/add_vehicle', data=test_vehicle)
    assert response.status_code == 200

'''
Test the Update Vehicle form
'''

'''
Test the Add Maintenance Record form
'''
def test_new_maintenance_record(client, test_maintenance):
    response = client.post('/add_maintenance', data=test_maintenance)
    assert response.status_code == 200

'''
Test the Update Maintenance Record form
'''