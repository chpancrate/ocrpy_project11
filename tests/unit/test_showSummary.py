import server


def test_showSummary_with_valid_email(client,
                                      clubs_fix,
                                      competitions_fix,
                                      mocker):
    """
    GIVEN that you are on the index page
    WHEN you enter a valid email
    THEN the summary page is displayed
         and the past competition have no booking button
    """
    # mock of the club and competition lists
    mocker.patch.object(server, "clubs", clubs_fix)
    mocker.patch.object(server, "competitions", competitions_fix)

    post_data = {"email": "test@email1.com"}

    response = client.post('/showSummary', data=post_data)
    response_data = response.data.decode()

    # we are on the summary page
    assert "Welcome, test@email1.com" in response_data


def test_showSummary_with_invalid_email(client,
                                        clubs_fix,
                                        competitions_fix,
                                        mocker):
    """
    GIVEN that you are on the index page
    WHEN you enter an invalid email
    THEN you stay on the index page and an error message is displayed
    """
    # mock of the club and competition lists
    mocker.patch.object(server, "clubs", clubs_fix)
    mocker.patch.object(server, "competitions", competitions_fix)

    post_data = {"email": "errorTest@email1.com"}

    response = client.post('/showSummary',
                           data=post_data,
                           follow_redirects=True)
    response_data = response.data.decode()

    assert "Unknown email" in response_data


def test_cannot_book_competition_in_past(client,
                                         clubs_fix,
                                         competitions_fix,
                                         mocker):
    """
    GIVEN that you are on the index page
    WHEN you enter a valid email
    THEN the summary page is displayed
         and the past competition have no booking button
    """
    # mock of the club and competition lists
    mocker.patch.object(server, "clubs", clubs_fix)
    mocker.patch.object(server, "competitions", competitions_fix)

    post_data = {"email": "test@email1.com"}

    response = client.post('/showSummary', data=post_data)
    response_data = response.data.decode()

    # we are on the summary page
    assert "Welcome, test@email1.com" in response_data
    # competition in the past has no booking button
    assert ("<a href=\"/book/Competition 3/Test Name 1\""
            ">Book Places</a>" not in response_data)
