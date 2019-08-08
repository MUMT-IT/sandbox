from datetime import datetime
import pytest
from otcalculator import caldate


def test_first():
    checkin_time = datetime(2019,8,8,8,30,0)
    message = caldate(checkin_time, checkin_time, setin='08:30:00')
    assert message == 'Work on time/late'


def test_early():
    checkin_time = datetime(2019,8,8,8,00,0)
    message = caldate(checkin_time, checkin_time, setin='08:30:00')
    assert message == 'Work early'


def test_early_checkout_later_date():
    checkin_time = datetime(2019,8,9,8,00,0)
    checkout_time = datetime(2019,8,10,8,00,0)
    message = caldate(checkin_time, checkout_time, setin='08:30:00')
    assert message == 'Check out date more than check in date'


def test_no_checkout():
    checkin_time = datetime(2019,8,8,8,30,0)
    with pytest.raises(Exception):
        assert caldate(checkin_time, None, setin='08:30:00')

