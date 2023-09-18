from server import loadCompetitions
import json


def test_should_correctly_open_club_file(mocker):
    """
    GIVEN that you have a json file with competition data
    WHEN you run the load function
    THEN the data are correctly loaded
    """

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
    """
    GIVEN that you do NOT have a competition json file
    WHEN you run the load function
    THEN the program stops and display an error message stating the reason
    """

    expected_value = "competitions.json file not found"
    mock_open = mocker.mock_open()
    mock_open = mocker.mock_open.side_effect = FileNotFoundError
    mocker.patch('builtins.open', mock_open)
    result = loadCompetitions()
    print("R:", result)
    print("EV:", expected_value)

    assert result == expected_value


def test_should_give_message_for_file_empty(mocker):
    """
    GIVEN that you have an empty competition json file
    WHEN you run the load function
    THEN the program stops and display an error message stating the reason
    """

    data = ""
    expected_value = "The competitions.json file is empty"

    read_data = json.dumps(data)
    mock_open = mocker.mock_open(read_data=read_data)
    mocker.patch('builtins.open', mock_open)
    result = loadCompetitions()

    assert result == expected_value
