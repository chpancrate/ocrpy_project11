import server
import json


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

    # mock the jso file name to use test files
    mocker.patch.object(server,
                        "COMPETITIONS_JSON_FILE_NAME",
                        'competitions_test.json')
    mocker.patch.object(server, "CLUBS_JSON_FILE_NAME", 'clubs_test.json')

    post_data = {"club": "Test Name 1",
                 "competition": "Competition 1",
                 "places": "1"}

    response = client.post('/purchasePlaces', data=post_data)
    response_data = response.data.decode()
    competition = [c for c in competitions_fix if c['name']
                   == "Competition 1"][0]
    club = [c for c in clubs_fix if c['name']
            == "Test Name 1"][0]

    # the page displayed is the summary
    assert "Welcome, test@email1.com" in response_data
    # a message is displayed to assert booking
    assert "Great-booking complete!" in response_data
    # number of available points should be initial - booked places:
    # 15 - 1 = 14
    assert club['points'] == 14
    # number of remaining places should be initial - booked places:
    # 25 - 1 = 24
    assert competition['numberOfPlaces'] == 24


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
        -Er- a number of place required + place already booked > 12
        -ok- a number of place required <= the available places in competition
        and that the club and competition hidden field are correct
    WHEN you send the request
    THEN an error message is displayed
    """
    # data from club and competition comes from json test files
    # club initial points : 12
    # competition initial places : 20

    # mock of the club and competition lists
    mocker.patch.object(server, "clubs", clubs_fix)
    mocker.patch.object(server, "competitions", competitions_fix)

    post_data = {"club": "Test Name 3",
                 "competition": "Competition 3",
                 "places": "11"}

    response = client.post('/purchasePlaces', data=post_data)
    response_data = response.data.decode()

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

    # the error 500 page is displayed
    assert "<h1>An internal server error occured</h1>" in response_data


def test_purchasePlaces_write_in_json_files(client,
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

    # mock the jso file name to use test files
    mocker.patch.object(server,
                        "COMPETITIONS_JSON_FILE_NAME",
                        'competitions_test.json')
    mocker.patch.object(server, "CLUBS_JSON_FILE_NAME", 'clubs_test.json')

    post_data = {"club": "Test Name 1",
                 "competition": "Competition 1",
                 "places": "1"}

    client.post('/purchasePlaces', data=post_data)

    with open('clubs_test.json') as clubs_test_file:
        saved_clubs = json.load(clubs_test_file)['clubs']

    with open('competitions_test.json') as competitions_test_file:
        saved_competitions = json.load(competitions_test_file)['competitions']

    result_club = [c for c in saved_clubs if c['name'] == "Test Name 1"][0]
    result_competition = [c for c in saved_competitions
                          if c['name'] == "Competition 1"][0]

    assert result_club['points'] == 14
    assert result_competition['numberOfPlaces'] == 24


def test_purchasePlaces_with_places_already_reserved(client,
                                                     clubs_fix,
                                                     competitions_fix,
                                                     mocker):
    """
    GIVEN that places are already reserved and that you enter :
        -ok- a number of place required <= your available points
        -ok- a number of place required <= 12 - places already reserved
        -ok- a number of place required <= the available places in competition
        and that the club and competition hidden field are correct
    WHEN you send the request
    THEN the places are booked and the total places is correct
    """
    # data from club and competition comes from json test files
    # club initial points : 12
    # places already reserved : 2
    # competition initial places : 20

    # mock of the club and competition lists
    mocker.patch.object(server, "clubs", clubs_fix)
    mocker.patch.object(server, "competitions", competitions_fix)

    # mock the jso file name to use test files
    mocker.patch.object(server,
                        "COMPETITIONS_JSON_FILE_NAME",
                        'competitions_test.json')
    mocker.patch.object(server, "CLUBS_JSON_FILE_NAME", 'clubs_test.json')

    post_data = {"club": "Test Name 3",
                 "competition": "Competition 3",
                 "places": "2"}

    response = client.post('/purchasePlaces', data=post_data)
    response_data = response.data.decode()
    competition = [c for c in competitions_fix if c['name']
                   == "Competition 3"][0]
    club = [c for c in clubs_fix if c['name']
            == "Test Name 3"][0]
    reservations = club['reservations']
    club_reservation = [resa for resa in reservations
                        if (resa['competition']
                            == "Competition 3")][0]
    # the page displayed is the summary
    assert "Welcome, test@email3.com" in response_data
    # a message is displayed to assert booking
    assert "Great-booking complete!" in response_data
    # number of available points should be initial - booked places:
    # 12 - 2 = 10
    assert club['points'] == 10
    # total number of places reserved should be equal to
    # already reserved + booked places
    # 2 + 2 = 4
    assert club_reservation['places'] == 4
    # number of remaining places should be initial - booked places:
    # 20 - 2 = 18
    assert competition['numberOfPlaces'] == 18
