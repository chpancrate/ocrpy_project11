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
