import server
from server import loadClubs, loadCompetitions


def test_user_happy_path(client, mocker):
    """
    This tests the following path :
    - user arrive on index page
    - user logs in
    - user book places in a competition
    - user is back on summary page
    """

    login_data = {"email": "aklon.IntegTest@mail.com"}
    booking_data = {"club": "Aklon Weightlifting IntegTest",
                    "competition": "Spring Festival IntegTest",
                    "places": "10"}

    mocker.patch.object(server,
                        "CLUBS_JSON_FILE_NAME",
                        './tests/integration/clubs_test.json')
    mocker.patch.object(server,
                        "COMPETITIONS_JSON_FILE_NAME",
                        './tests/integration/competitions_test.json')
    clubs_result = loadClubs()
    competitions_result = loadCompetitions()

    # mock of the club and competition lists  using the data give previously
    mocker.patch.object(server, "clubs", clubs_result)
    mocker.patch.object(server, "competitions", competitions_result)

    # go to the index page
    response = client.get('/')
    response_data = response.data.decode()

    assert "Aklon Weightlifting IntegTest" in response_data

    # connect to the application
    response = client.post('/showSummary', data=login_data)
    response_data = response.data.decode()

    assert "Welcome, aklon.IntegTest@mail.com" in response_data

    # go to a booking page
    response = client.get('/book/Spring Festival IntegTest/Aklon Weightlifting IntegTest')
    response_data = response.data.decode()

    assert "Spring Festival IntegTest" in response_data

    # book a competition
    response = client.post('/purchasePlaces', data=booking_data)
    response_data = response.data.decode()

    competition = [c for c in competitions_result if c['name']
                   == "Spring Festival IntegTest"][0]
    club = [c for c in clubs_result if c['name']
            == "Aklon Weightlifting IntegTest"][0]

    # the page displayed is the summary
    assert "Welcome, aklon.IntegTest@mail.com" in response_data
    # a message is displayed to assert booking
    assert "Great-booking complete!" in response_data
    # number of available points should be initial - booked places:
    # 15 - 10 = 5
    assert club['points'] == 5
    # number of remaining places should be initial - booked places:
    # 25 - 10 = 15
    assert competition['numberOfPlaces'] == 15
