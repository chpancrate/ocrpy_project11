import pytest


def test_showSummary_with_valid_email(client):
    """
    GIVEN that you are on the index page
    WHEN you enter a valid email
    THEN the summary page is displayed
    """

    post_data = {"email": "Test@email1.com"}

    response = client.post('/showSummary', data=post_data)
    response_data = response.data.decode()

    assert "Welcome, Test@email1.com" in response_data


def test_showSummary_with_invalid_email(client):
    """
    GIVEN that you are on the index page
    WHEN you enter an invalid email
    THEN you stay on the index page and an error message is displayed
    """

    post_data = {"email": "errorTest@email1.com"}

    response = client.post('/showSummary', data=post_data)
    response_data = response.data.decode()

    assert "Unknown email" in response_data
