from server import loadClubs
import json


def test_should_correctly_open_club_file(mocker):

    data = {"clubs": [
            {
                "name": "test name",
                "email": "test@email",
                "points": "13"
            }
            ]}
    expected_value = [
            {
                "name": "test name",
                "email": "test@email",
                "points": "13"
            }
            ]

    read_data = json.dumps(data)
    mock_opener = mocker.mock_open(read_data=read_data)
    mocker.patch('builtins.open', mock_opener)
    result = loadClubs()

    assert result == expected_value


def test_should_give_message_for_file_unknown(mocker):

    expected_value = "Fichier clubs non trouvé"
    mock_opener = mocker.mock_open()
    mock_opener.side_effect = FileNotFoundError
    mocker.patch('builtins.open', mock_opener)
    result = loadClubs()
    print("R:", result)
    print("EV:", expected_value)

    assert result == "Fichier clubs non trouvé"


def test_should_give_message_for_file_empty(mocker):
    data = ""
    expected_value = "Le fichier clubs est vide"

    read_data = json.dumps(data)
    mock_opener = mocker.mock_open(read_data=read_data)
    mocker.patch('builtins.open', mock_opener)
    result = loadClubs()

    assert result == expected_value
