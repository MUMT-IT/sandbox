from datetime import datetime

import pandas as pd
import pytest
from otcalculator import (caldate, create_datetime,
                          calculate_ot_hours, round_hours)


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


def test_create_datetime():
    t1 = datetime(2019,8,22,7,30,0)
    dt = create_datetime(t1, 8, 30)
    assert dt == datetime(2019,8,22,8,30,0)


def test_round_hour_negative():
    assert round_hours(-0.5) == 0
    assert round_hours(-1.4) == -1


def test_calculate_ot_one_hour_early():
    t1 = datetime(2019,8,22,7,30,0)
    t2 = datetime(2019,8,22,8,30,0)
    scantimes = pd.Series([t1, t2])
    ot_hours = calculate_ot_hours(scantimes, 8,30)
    assert ot_hours[0] == -1


def test_calculate_ot_one_hour_late():
    t1 = datetime(2019,8,22,7,30,0)
    t2 = datetime(2019,8,22,9,30,0)
    scantimes = pd.Series([t1, t2])
    ot_hours = calculate_ot_hours(scantimes, 8,30)
    assert ot_hours[1] == 1


def test_calculate_ot_40min_early():
    t1 = datetime(2019,8,22,7,50,0)
    t2 = datetime(2019,8,22,9,30,0)
    scantimes = pd.Series([t1, t2])
    ot_hours = calculate_ot_hours(scantimes, 8,30)
    assert ot_hours[0] == 0
