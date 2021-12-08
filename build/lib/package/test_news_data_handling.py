from covid_news_handling import *

def test_news_API_request():
    """ checks if the news articles are gotten from the news API"""
    assert news_API_request()
    """checks that the covid articles are gotten from covid terms"""
    assert news_API_request(data["covid_terms"]) == news_API_request()

def test_update_news():
    """tests whether the scheduler shedules updates"""
    update_news('test')
