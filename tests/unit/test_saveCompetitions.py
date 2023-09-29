import pytest
import server
from server import save_competitions
import json
from werkzeug.exceptions import HTTPException


def test_should_correctly_save_data_to_file(mocker,
                                            competitions_fix):
    """
    GIVEN that you have a json dictionnary with competitions data
    WHEN you run the save function
    THEN the data are correctly saved
    """
    mocker.patch.object(server,
                        "COMPETITIONS_JSON_FILE_NAME",
                        'competitions_test.json')

    save_competitions(competitions_fix)

    with open('competitions_test.json') as competitions_test_file:
        competitions = json.load(competitions_test_file)

        assert competitions == {"competitions": competitions_fix}


def test_handle_error_from_save_data_to_file(mocker, competitions_fix):
    """
    GIVEN that you have a json dictionnary with clubs data
    WHEN you run the save function and somethings gets wrong
    THEN a message is displayer to warn the user
    """
    mocker.patch.object(server,
                        "COMPETITIONS_JSON_FILE_NAME",
                        'competitions_test.json')

    # mock the open fuction to simulate a file not found error
    mock_opener = mocker.mock_open()
    mock_opener.side_effect = FileNotFoundError
    mocker.patch('builtins.open', mock_opener)

    with pytest.raises(HTTPException) as http_error:
        save_competitions(competitions_fix)

    assert http_error.value.code == 500
    assert http_error.value.description == "cannot write competitions file"
