def test_logout(client):
    """
    GIVEN you are on the summary page
    WHEN you press logout
    THEN the index page appears
    """
    response = client.get('/logout', follow_redirects=True)
    response_data = response.data.decode()

    assert "Welcome to the GUDLFT Registration Portal!" in response_data
    assert response.status_code == 200
