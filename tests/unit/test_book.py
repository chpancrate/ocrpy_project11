import server


def test_book_page_with_correct_data(clubs_fix,
                                     competitions_fix,
                                     client,
                                     mocker):
    """
    GIVEN that the competition and the club in the url exist
    WHEN you arrive on the url
    THEN the places available for the competition are displayed
    """
    # mock of the club and competition lists
    mocker.patch.object(server, "clubs", clubs_fix)
    mocker.patch.object(server, "competitions", competitions_fix)

    response = client.get('/book/Competition 1/Test Name 1')
    response_data = response.data.decode()

    assert "Competition 1" in response_data
    assert "Places available: 25" in response_data


def test_book_page_with_wrong_club(clubs_fix,
                                   competitions_fix,
                                   client,
                                   mocker):
    """
    GIVEN that the club in the url does not exist
    WHEN you arrive on the url
    THEN the welcome page is displayed with an error message"
    """
    # mock of the club and competition lists
    mocker.patch.object(server, "clubs", clubs_fix)
    mocker.patch.object(server, "competitions", competitions_fix)

    response = client.get('/book/Competition 1/wrong club')
    response_data = response.data.decode()

    assert "<h1>Page not found</h1>" in response_data


def test_book_page_with_wrong_competition(clubs_fix,
                                          competitions_fix,
                                          client,
                                          mocker):
    """
    GIVEN that the competition in the url does not exist
    WHEN you arrive on the url
    THEN the welcome page is displayed with an error message"
    """
    # mock of the club and competition lists
    mocker.patch.object(server, "clubs", clubs_fix)
    mocker.patch.object(server, "competitions", competitions_fix)

    response = client.get('/book/wrong competition/Test Name 1')
    response_data = response.data.decode()

    assert "<h1>Page not found</h1>" in response_data


def test_book_page_with_full_data(clubs_fix,
                                  competitions_fix,
                                  client,
                                  mocker):
    """
    GIVEN that the competition and the club in the url exist
    WHEN you arrive on the url
    THEN the places available for the competition are displayed
    """
    # mock of the club and competition lists
    mocker.patch.object(server, "clubs", clubs_fix)
    mocker.patch.object(server, "competitions", competitions_fix)

    response = client.get('/book/Competition 1/Test Name 1')
    response_data = response.data.decode()

    assert "Competition 1" in response_data
    assert "Places available: 25" in response_data
    assert "Points available: 15" in response_data
    assert "Return to list" in response_data


def test_book_page_places_already_purchased(clubs_fix,
                                            competitions_fix,
                                            client,
                                            mocker):
    """
    GIVEN that the competition and the club in the url exist
    WHEN you arrive on the url
    THEN the number of places already booked for the competition are displayed
    """
    # mock of the club and competition lists
    mocker.patch.object(server, "clubs", clubs_fix)
    mocker.patch.object(server, "competitions", competitions_fix)

    response = client.get('/book/Competition 3/Test Name 3')
    response_data = response.data.decode()

    assert "Competition 3" in response_data
    assert "Places already reserved: 2" in response_data
