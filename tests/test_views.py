'''
Test if Main Menu page is loading
'''
def test_index(client):
    response = client.get('/')
    assert response.status_code == 200

'''
Test Main Menu content
'''
def test_index_content(client):
    response = client.get('/')
    assert b'<h1>Main Menu</h1>' in response.data

'''
Test if Vehicle Details page is loading
'''
def test_details(client):
    response = client.get('/details')
    assert response.status_code == 200

'''
Test Vehicle Details page content
'''
def test_details_content(client):
    response = client.get('/details')
    assert b'<h1>Vehicle Details</h1>' in response.data

'''
Test if Vehicle History page is loading
'''
def test_history(client):
    response = client.get('/history')
    assert response.status_code == 200
    assert b'<h1>Maintenance History</h1>' in response.data

'''
Test Vehicle History content
'''
def test_history_content(client):
    response = client.get('/history')
    assert b'<h1>Maintenance History</h1>' in response.data

'''
Test if Vehicle Status page is loading
'''
def test_status(client):
    response = client.get('/status')

    assert response.status_code == 200
    
    assert b'<h1>Vehicle Status</h1>' in response.data

'''
Test Vehicle Status content
'''
def test_status_content(client):
    response = client.get('/status')
    assert b'<h1>Vehicle Status</h1>' in response.data

