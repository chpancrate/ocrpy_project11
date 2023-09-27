import server


def test_index_page_on_arrival(client,
                               clubs_fix,
                               competitions_fix,
                               mocker):
    """
    GIVEN the application is launched
    WHEN you go to the '/' url
    THEN the index page
    """
    # mock of the club and competition lists
    mocker.patch.object(server, "clubs", clubs_fix)
    mocker.patch.object(server, "competitions", competitions_fix)

    response = client.get('/')
    data = response.data.decode()

    assert "Welcome to the GUDLFT Registration Portal!" in data
    assert response.status_code == 200


def test_index_page_has_summary(client,
                                clubs_fix,
                                competitions_fix,
                                mocker):
    """
    GIVEN the application is launched
    WHEN you go to the '/' url
    THEN the index page is diplayed with the list of clubs
    """
    # mock of the club and competition lists
    mocker.patch.object(server, "clubs", clubs_fix)
    mocker.patch.object(server, "competitions", competitions_fix)

    response = client.get('/')
    data = response.data.decode()

    assert "Welcome to the GUDLFT Registration Portal!" in data
    assert "<th>Clubs</td>" in data
    assert response.status_code == 200
