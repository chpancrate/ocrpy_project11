import pytest
import server
from server import save_clubs
import json
from werkzeug.exceptions import HTTPException


def test_should_correctly_save_data_to_file(mocker,
                                            clubs_fix):
    """
    GIVEN that you have a json dictionnary with clubs data
    WHEN you run the save function
    THEN the data are correctly saved in the clubs.json file
    """
    mocker.patch.object(server, "CLUBS_JSON_FILE_NAME", 'clubs_test.json')

    save_clubs(clubs_fix)

    with open('clubs_test.json') as clubs_test_file:
        clubs = json.load(clubs_test_file)

        assert clubs == {"clubs": clubs_fix}


def test_handle_error_from_save_data_to_file(mocker,
                                             clubs_fix):
    """
    GIVEN that you have a json dictionnary with clubs data
    WHEN you run the save function and somethings gets wrong
    THEN a message is displayer to warn the user
    """
    mocker.patch.object(server, "CLUBS_JSON_FILE_NAME", 'clubs_test.json')

    # mock the open function to simulate a file not found error
    mock_opener = mocker.mock_open()
    mock_opener.side_effect = FileNotFoundError
    mocker.patch('builtins.open', mock_opener)

    with pytest.raises(HTTPException) as http_error:
        save_clubs(clubs_fix)

    assert http_error.value.code == 500
    assert http_error.value.description == "cannot write clubs file"
