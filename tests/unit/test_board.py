import server


def test_board_page_access(client,
                           clubs_fix,
                           competitions_fix,
                           mocker):
    """
    GIVEN that you are on the index page
    WHEN you enter press view more
    THEN the clubs points board is displayed
    """

    # mock of the club and competition lists
    mocker.patch.object(server, "clubs", clubs_fix)
    mocker.patch.object(server, "competitions", competitions_fix)

    response = client.get('/board')
    data = response.data.decode()

    assert "<h2>Clubs points board</h2>" in data
    assert response.status_code == 200


def test_board_page_with_json_file_error(client, mocker):
    """
    GIVEN the application is launched but a json file is missing or empty
    WHEN you go to the '/board/' url
    THEN the 500 error page is displayed
    """
    clubs_data = []
    competitions_data = []
    # mock of the club and competition lists
    mocker.patch.object(server, "clubs", clubs_data)
    mocker.patch.object(server, "competitions", competitions_data)

    response = client.get('/board', follow_redirects=True)
    data = response.data.decode()

    assert "<h1>An internal server error occured</h1>" in data
    assert "json files missing or empty" in data
