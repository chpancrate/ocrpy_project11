import pytest
import json


def test_showSummary(client, mocker):
    """
    GIVEN that you are on the index page
    WHEN you enter a valid email
    THEN the summary page is displayed
    """
    clubs_data = {"clubs": [
        {
            "name": "Test Name 1",
            "email": "Test@email1.com",
            "points": "12"
        },
        {
            "name": "Test Name 2",
            "email": "Test@email2.com",
            "points": "4"
        },
    ]}

    competitions_data = [
        {
            "name": "Test competition 1",
            "date": "2020-03-27 10:00:00",
            "numberOfPlaces": "25"
        },
        {
            "name": "Test competition 2",
            "date": "2020-10-22 13:30:00",
            "numberOfPlaces": "13"
        }
    ]
    post_data = {"email": "Test@email1.com"}
    # post_data = {"email": "john@simplylift.co"}
    """
    mock_opener = mocker.mock_open()
    mock_opener.side_effect = [
                     mocker.mock_open(
                        read_data=json.dumps(clubs_data)
                     ).return_value,
                     mocker.mock_open(
                        read_data=json.dumps(
                            {"competitions": competitions_data}
                            )
                     ).return_value
                     ]
    print("XXX-SE:", mock_opener.side_effect)
    mocker.patch('builtins.open', mock_opener)
    """
    response = client.post('/showSummary', data=post_data)
    response_data = response.data.decode()
    print("XXX-RD:", response_data)

    assert "Welcome, Test@email1.com" in response_data
    # assert "Welcome, john@simplylift.co" in response_data
