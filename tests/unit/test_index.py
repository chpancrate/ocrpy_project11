def test_index_page_on_arrival(client):
    """
    GIVEN the application is launched
    WHEN you go to the '/' url
    THEN the index page
    """

    response = client.get('/')
    data = response.data.decode()

    assert "Welcome to the GUDLFT Registration Portal!" in data
    assert response.status_code == 200


def test_index_page_has_summary(client):
    """
    GIVEN the application is launched
    WHEN you go to the '/' url
    THEN the index page is diplayed with the list of clubs
    """

    response = client.get('/')
    data = response.data.decode()

    assert "Welcome to the GUDLFT Registration Portal!" in data
    assert "<th>Clubs</td>" in data
    assert response.status_code == 200
