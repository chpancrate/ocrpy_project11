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


def test_index_page_with_json_file_error(client, mocker):
    """
    GIVEN the application is launched but a json file is missig or empty
    WHEN you go to the '/' url
    THEN the 500 error page is displayed
    """
    clubs_data = []
    competitions_data = []
    # mock of the club and competition lists
    mocker.patch.object(server, "clubs", clubs_data)
    mocker.patch.object(server, "competitions", competitions_data)

    response = client.get('/', follow_redirects=True)
    data = response.data.decode()

    assert "<h1>An internal server error occured</h1>" in data
    assert "json files missing or empty" in data
