import pytest
from server import create_app


@pytest.fixture()
def client():
    app = create_app()
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


@pytest.fixture
def clubs_fix():
    return [
        {
            "name": "Test Name 1",
            "email": "test@email1.com",
            "points": "15",
            "reservations": []

        },
        {
            "name": "Test Name 2",
            "email": "test@email1.com",
            "points": "4",
            "reservations": []
        },
        {
            "name": "Test Name 3",
            "email": "test@email3.com",
            "points": "12",
            "reservations": [
                {
                    "competition": "Competition 3",
                    "places": 2
                }
            ]

        }
    ]


@pytest.fixture
def competitions_fix():
    return [
        {
            "name": "Competition 1",
            "date": "2024-03-27 10:00:00",
            "numberOfPlaces": "25"
        },
        {
            "name": "Competition 2",
            "date": "2023-10-22 13:30:00",
            "numberOfPlaces": "7"
        },
        {
            "name": "Competition 3",
            "date": "2023-07-22 13:30:00",
            "numberOfPlaces": "20"
        }
    ]
