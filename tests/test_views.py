import json

def test_hello_endpoint(app_client):
    """
    Make a request to the home endpoint and verify the status code is 200,
    and that the 'message' key is present in the response dict
    """

    response = app_client.get('/')
    data = json.loads(response.data)
    
    assert response.status_code == 200
    assert 'message' in data
