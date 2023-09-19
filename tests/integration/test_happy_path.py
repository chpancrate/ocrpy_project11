def test_user_happy_path(client):
    """
    This tests the following path :
    - user arrive on index page
    - user logs in
    - user book places in a competition
    - user is back on summary page
    """

    login_data = {"email": "Test@email1.com"}
    booking_data = {"club": "Test Name 1",
                    "competition": "Test competition 1",
                    "places": "10"}

    # go to the index page
    client.get('/')
    # connect to the application
    client.post('/showSummary', data=login_data)
    # go to a booking page
    client.get('/book/Test competition 1/Test Name 1')
    # book a competition

    response = client.post('/purchasePlaces', data=booking_data)
    response_data = response.data.decode()

    print(response_data)

    # the page displayed is the summary
    assert "Welcome, Test@email1.com" in response_data
    # a message is displayed to assert booking
    assert "Great-booking complete!" in response_data
    # number of available points should be initial - booked places:
    # 15 - 10 = 5
    assert "Points available: 5" in response_data
    # number of remaining places should be initial = booked places:
    # 25 - 10 = 15
    assert "Number of Places: 15" in response_data
