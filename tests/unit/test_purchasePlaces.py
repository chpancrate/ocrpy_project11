def test_purchasePlaces_with_correct_values():
    """
    GIVEN that you enter :
        - a number of place required <= your available points
        - a number of place required <= 12
        - a number of place required <= the available places in the competition
        and that the club and competition hidden field are correct
    WHEN you send the request
    THEN the place are booked
    """
    pass


def test_purchasePlaces_with_places_required_gt_available_points():
    """
    GIVEN that you enter :
        - a number of place required > your available points
        - a number of place required <= 12
        - a number of place required <= the available places in the competition
        and that the club and competition hidden field are correct
    WHEN you send the request
    THEN an error message is displayed
    """
    pass


def test_purchasePlaces_with_places_required_gt_12():
    """
    GIVEN that you enter :
        - a number of place required <= your available points
        - a number of place required > 12
        - a number of place required <= the available places in the competition
        and that the club and competition hidden field are correct
    WHEN you send the request
    THEN an error message is displayed
    """
    pass


def test_purchasePlaces_with_places_required_gt_available_places():
    """
    GIVEN that you enter :
        - a number of place required <= your available points
        - a number of place required <= 12
        - a number of place required > the available places in the competition
        and that the club and competition hidden field are correct
    WHEN you send the request
    THEN an error message is displayed
    """
    pass


def test_purchasePlaces_with_wrong_club():
    """
    GIVEN that you enter :
        - a number of place required <= your available points
        - a number of place required <= 12
        - a number of place required <= the available places in the competition
        and that the club hidden field is incorrect
    WHEN you send the request
    THEN an error message is displayed
    """
    pass


def test_purchasePlaces_with_wrong_competition():
    """
    GIVEN that you enter :
        - a number of place required <= your available points
        - a number of place required <= 12
        - a number of place required <= the available places in the competition
        and that the competition hidden field is incorrect
    WHEN you send the request
    THEN an error message is displayed
    """
    pass
