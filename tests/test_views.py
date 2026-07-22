'''
Test if Main Menu page is loading
'''
def test_index(client):
    response = client.get('/')
    assert response.status_code == 200

    assert b'<title>Pyle - Main</title>' in response.data
    assert b'<h1>Main Menu</h1>' in response.data

    response = client.get('/index')
    assert response.status_code == 200

    response = client.get('/main')
    assert response.status_code == 200

    response = client.get('/home')
    assert response.status_code == 200

'''
Test if Vehicle Details page is loading
'''
def test_details(client):
    response = client.get('/details')

    assert response.status_code == 200
    assert b'<h1>Vehicle Details</h1>' in response.data

'''
Test if Vehicle History page is loading
'''
def test_history(client):
    response = client.get('/history')

    assert response.status_code == 200
    assert b'<h1>Maintenance History</h1>' in response.data

'''
Test if Vehicle Status page is loading
'''
def test_status(client):
    response = client.get('/status')

    assert response.status_code == 200
    assert b'<h1>Vehicle Status</h1>' in response.data

