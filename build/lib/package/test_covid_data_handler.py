from covid_data_handler import *
""" Testing for the module coivd_data_handling.py"""
def test_parse_csv_data():
    """tests whether the file is opened correctly"""
    data = parse_csv_data('nation_2021-10-28.csv')
    assert len(data) == 639

def test_process_covid_csv_data():
    """tests whether the variables were processed correctly"""
    last7days_cases , current_hospital_cases , total_deaths = \
        process_covid_csv_data(parse_csv_data('nation_2021-10-28.csv'))
    assert last7days_cases == 240299
    assert current_hospital_cases == 7019
    assert total_deaths == 141544

def test_covid_API_request():
    """tests whether the API returns a list"""    
    data = covid_API_request()
    assert isinstance(data, list)

def test_national_covid_API_request():
    """tests whether the national API return a list"""
    data = national_covid_API_request()
    assert isinstance(data, list)

def test_schedule_covid_updates():
    """tests whether the sheduler schedules updates"""
    schedule_covid_updates(update_interval=10, update_name='update test')

def test_national_schedule_covid_updates():
    """tests whether the scheduler shedules updates"""
    national_schedule_covid_updates(update_interval=10, update_name='update test')

