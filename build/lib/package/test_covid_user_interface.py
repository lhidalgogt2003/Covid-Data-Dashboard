from covid_user_interface import*

""" Tests for the module covid_user_interface"""

def test_calculate_time():
    """tests whether time is converted from string to int"""
    data = calculate_time("12:30")
    assert isinstance(data, int)

def test_news_removal():
    """tests whether the news removed are returned in a list"""
    data = news_removal()
    assert isinstance(data, list)

def test_update_removal():
    """tests whether the updates removed are returned in a list"""
    data = update_removal()
    assert isinstance(data, list)

def test_schedule_event():
    """tests whether the request is returned as an int"""
    data = schedule_event()
    assert isinstance(data[0], int)
    assert isinstance(data[1], int)
    assert isinstance(data[2], int)
    assert isinstance(data[3], int)