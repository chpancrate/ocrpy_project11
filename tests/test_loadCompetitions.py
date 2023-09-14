from server import loadCompetitions
import json


def test_should_correctly_open_club_file(mocker):

    data = {"competitions": [
            {
                "name": "test name",
                "date": "2020-03-27 10:00:00",
                "points": "20"
            }
            ]}
    expected_value = [
            {
                "name": "test name",
                "date": "2020-03-27 10:00:00",
                "points": "20"
            }
            ]

    read_data = json.dumps(data)
    mock_open = mocker.mock_open(read_data=read_data)
    mocker.patch('builtins.open', mock_open)
    result = loadCompetitions()

    assert result == expected_value


def test_should_give_message_for_file_unknown(mocker):

    expected_value = "Fichier competitions non trouvé"
    mock_open = mocker.mock_open()
    mock_open = mocker.mock_open.side_effect = FileNotFoundError
    mocker.patch('builtins.open', mock_open)
    result = loadCompetitions()
    print("R:", result)
    print("EV:", expected_value)

    assert result == expected_value


def test_should_give_message_for_file_empty(mocker):
    data = ""
    expected_value = "Le fichier competition est vide"

    read_data = json.dumps(data)
    mock_open = mocker.mock_open(read_data=read_data)
    mocker.patch('builtins.open', mock_open)
    result = loadCompetitions()

    assert result == expected_value
