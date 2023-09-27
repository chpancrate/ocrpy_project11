import server


def test_logout(client,
                clubs_fix,
                competitions_fix,
                mocker):
    """
    GIVEN you are on the summary page
    WHEN you press logout
    THEN the index page appears
    """
    # mock of the club and competition lists
    mocker.patch.object(server, "clubs", clubs_fix)
    mocker.patch.object(server, "competitions", competitions_fix)

    response = client.get('/logout', follow_redirects=True)
    response_data = response.data.decode()

    assert "Welcome to the GUDLFT Registration Portal!" in response_data
    assert response.status_code == 200
