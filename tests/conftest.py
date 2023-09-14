import pytest
import json
from server import app
import server


@pytest.fixture
def client(mocker):
    app.config["TESTING"] = True

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
    mocker.patch('server.loadClubs', return_value=clubs_data)
    mocker.patch('server.loadCompetitions', return_value=competitions_data)

    with app.test_client() as client:
        yield client
