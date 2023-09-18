import pytest


def test_book_page_with_correct_data(client):
    """
    GIVEN that the competition and the club in the url exist
    WHEN you arrive on the url
    THEN the places available for the competition are displayed
    """

    response = client.get('/book/Test competition 1/Test Name 1')
    response_data = response.data.decode()

    assert "Test competition 1" in response_data
    assert "Places available: 25" in response_data


def test_book_page_with_wrong_club(client):
    """
    GIVEN that the club in the url does not exist
    WHEN you arrive on the url
    THEN the welcome page is displayed with an error message"
    """
    response = client.get('/book/Test competition 1/wrong club')
    response_data = response.data.decode()

    assert "Page not found" in response_data


def test_book_page_with_wrong_competition(client):
    """
    GIVEN that the competition in the url does not exist
    WHEN you arrive on the url
    THEN the welcome page is displayed with an error message"
    """
    response = client.get('/book/wrong competition/Test Name 1')
    response_data = response.data.decode()

    assert "Page not found" in response_data
