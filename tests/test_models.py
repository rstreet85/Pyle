'''
Test the Vehicle model
'''
def test_add_vehicle(client, test_vehicle):
    response = client.post('/add_vehicle', data=test_vehicle)
    # Read back database entry
    assert False

'''
Test the Record model
'''
def test_add_record(client, test_maintenance):
    response = client.post('/add_record', data=test_maintenance)
    # Read back database entry
    assert False