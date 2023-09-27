import server


def test_purchasePlaces_with_correct_values(client,
                                            clubs_fix,
                                            competitions_fix,
                                            mocker):
    """
    GIVEN that you enter :
        -ok- a number of place required <= your available points
        -ok- a number of place required <= 12
        -ok- a number of place required <= the available places in competition
        and that the club and competition hidden field are correct
    WHEN you send the request
    THEN the place are booked
    """
    # data from club and competition comes from json test files
    # club initial points : 15
    # competition initial places : 25

    # mock of the club and competition lists
    mocker.patch.object(server, "clubs", clubs_fix)
    mocker.patch.object(server, "competitions", competitions_fix)

    post_data = {"club": "Test Name 1",
                 "competition": "Competition 1",
                 "places": "1"}

    response = client.post('/purchasePlaces', data=post_data)
    response_data = response.data.decode()

    # print(response_data)

    # the page displayed is the summary
    assert "Welcome, test@email1.com" in response_data
    # a message is displayed to assert booking
    assert "Great-booking complete!" in response_data
    # number of available points should be initial - booked places:
    # 15 - 1 = 14
    assert "Points available: 14" in response_data
    # number of remaining places should be initial - booked places:
    # 25 - 1 = 24
    assert "Number of Places: 24" in response_data


def test_purchasePlaces_with_places_required_gt_available_points(
        client,
        clubs_fix,
        competitions_fix,
        mocker):
    """
    GIVEN that you enter :
        -Er- a number of place required > your available points
        -ok- a number of place required <= 12
        -ok- a number of place required <= the available places in competition
        and that the club and competition hidden field are correct
    WHEN you send the request
    THEN an error message is displayed
    """
    # data from club and competition comes from json test files
    # club initial points : 4
    # competition initial places : 7

    # mock of the club and competition lists
    mocker.patch.object(server, "clubs", clubs_fix)
    mocker.patch.object(server, "competitions", competitions_fix)

    post_data = {"club": "Test Name 2",
                 "competition": "Competition 2",
                 "places": "6"}

    response = client.post('/purchasePlaces', data=post_data)
    response_data = response.data.decode()

    # print(response_data)

    # the page displayed is the booking page
    assert "How many places?" in response_data
    # an error message is displayed
    assert "You do not have enough points." in response_data


def test_purchasePlaces_with_places_required_gt_12(
        client,
        clubs_fix,
        competitions_fix,
        mocker):
    """
    GIVEN that you enter :
        -ok- a number of place required <= your available points
        -Er- a number of place required > 12
        -ok- a number of place required <= the available places in competition
        and that the club and competition hidden field are correct
    WHEN you send the request
    THEN an error message is displayed
    """
    # data from club and competition comes from json test files
    # club initial points : 14
    # competition initial places : 24

    # mock of the club and competition lists
    mocker.patch.object(server, "clubs", clubs_fix)
    mocker.patch.object(server, "competitions", competitions_fix)

    post_data = {"club": "Test Name 1",
                 "competition": "Competition 1",
                 "places": "13"}

    response = client.post('/purchasePlaces', data=post_data)
    response_data = response.data.decode()

    # print(response_data)

    # the page displayed is the booking page
    assert "How many places?" in response_data
    # an error message is displayed
    assert "You cannot book more than 12 places." in response_data


def test_purchasePlaces_with_places_required_gt_available_places(
        client,
        clubs_fix,
        competitions_fix,
        mocker):
    """
    GIVEN that you enter :
        -ok- a number of place required <= your available points
        -ok- a number of place required <= 12
        -Er- a number of place required > the available places in competition
        and that the club and competition hidden field are correct
    WHEN you send the request
    THEN an error message is displayed
    """
    # data from club and competition comes from json test files
    # club initial points : 15
    # competition initial places : 7

    # mock of the club and competition lists
    mocker.patch.object(server, "clubs", clubs_fix)
    mocker.patch.object(server, "competitions", competitions_fix)

    post_data = {"club": "Test Name 1",
                 "competition": "Competition 2",
                 "places": "10"}

    response = client.post('/purchasePlaces', data=post_data)
    response_data = response.data.decode()

    # print(response_data)

    # the page displayed is the booking page
    assert "How many places?" in response_data
    # an error message is dispalyed
    assert "There is not enough places in the competition." in response_data


def test_purchasePlaces_with_wrong_club(
        client,
        clubs_fix,
        competitions_fix,
        mocker):
    """
    GIVEN that you enter :
        - a number of place required <= your available points
        - a number of place required <= 12
        - a number of place required <= the available places in the competition
        and that the club hidden field is incorrect
    WHEN you send the request
    THEN an error message is displayed
    """
    # data from club and competition comes from json test files
    # club initial points : 15
    # competition initial places : 25

    # mock of the club and competition lists
    mocker.patch.object(server, "clubs", clubs_fix)
    mocker.patch.object(server, "competitions", competitions_fix)

    post_data = {"club": "wrong club",
                 "competition": "Competition 1",
                 "places": "10"}

    response = client.post('/purchasePlaces', data=post_data)
    response_data = response.data.decode()

    # print(response_data)

    # the error 500 page is displayed
    assert "<h1>An internal server error occured</h1>" in response_data


def test_purchasePlaces_with_wrong_competition(
        client,
        clubs_fix,
        competitions_fix,
        mocker):
    """
    GIVEN that you enter :
        - a number of place required <= your available points
        - a number of place required <= 12
        - a number of place required <= the available places in the competition
        and that the competition hidden field is incorrect
    WHEN you send the request
    THEN an error message is displayed
    """
    # data from club and competition comes from json test files
    # club initial points : 15
    # competition initial places : 25

    # mock of the club and competition lists
    mocker.patch.object(server, "clubs", clubs_fix)
    mocker.patch.object(server, "competitions", competitions_fix)

    post_data = {"club": "Test Name 1",
                 "competition": "wrong competition",
                 "places": "10"}

    response = client.post('/purchasePlaces', data=post_data)
    response_data = response.data.decode()

    # print(response_data)

    # the error 500 page is displayed
    assert "<h1>An internal server error occured</h1>" in response_data
