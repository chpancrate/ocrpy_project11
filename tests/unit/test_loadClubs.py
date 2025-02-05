from server import loadClubs
import json


def test_should_correctly_open_club_file(mocker):
    """
    GIVEN that you have a json file with clubs data
    WHEN you run the load function
    THEN the data are correctly loaded
    """

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
    """
    GIVEN that you do NOT have a club json file
    WHEN you run the load function
    THEN the program stops and display an error message stating the reason
    """

    expected_value = []
    mock_opener = mocker.mock_open()
    mock_opener.side_effect = FileNotFoundError
    mocker.patch('builtins.open', mock_opener)
    result = loadClubs()

    assert result == expected_value


def test_should_give_message_for_file_empty(mocker):
    """
    GIVEN that you have an empty club json file
    WHEN you run the load function
    THEN the program stops and display an error message stating the reason
    """

    data = ""
    expected_value = []

    mock_opener = mocker.mock_open(read_data=data)
    mocker.patch('builtins.open', mock_opener)
    result = loadClubs()

    assert result == expected_value
