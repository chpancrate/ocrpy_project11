def test_showSummary_with_valid_email(client):
    """
    GIVEN that you are on the index page
    WHEN you enter a valid email
    THEN the summary page is displayed
         and the past competition have no booking button
    """

    post_data = {"email": "john@simplylift.co"}

    response = client.post('/showSummary', data=post_data)
    response_data = response.data.decode()

    # we are on the summary page
    assert "Welcome, john@simplylift.co" in response_data
    # competition in the past has no booking button
    assert ("<a href=\"/book/Summer Beach Festival/Simply Lift\""
            ">Book Places</a>" not in response_data)


def test_showSummary_with_invalid_email(client):
    """
    GIVEN that you are on the index page
    WHEN you enter an invalid email
    THEN you stay on the index page and an error message is displayed
    """

    post_data = {"email": "errorTest@email1.com"}

    response = client.post('/showSummary', data=post_data)
    response_data = response.data.decode()

    assert "Unknown email" in response_data
