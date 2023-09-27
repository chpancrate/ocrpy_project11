import pytest
import os


@pytest.fixture
def test_file():
    # Create a temporary file for testing
    filename = 'clubs_test.json'
    yield filename
    # Clean up: Remove the temporary file after the test
    if os.path.exists(filename):
        os.remove(filename)


def test_should_correctly_save_data_to_file(mocker, test_file):
    """
    GIVEN that you have a json dictionnary with clubs data
    WHEN you run the save function
    THEN the data are correctly saved
    """
    """
    clubs = {"clubs": [
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
    """
    pass


def test_handle_error_from_save_data_to_file(mocker):
    """
    GIVEN that you have a json dictionnary with clubs data
    WHEN you run the save function and somethings gets wrong
    THEN a message is displayer to warn the user
    """
    pass
