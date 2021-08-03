"""A test module to test input values from user.
"""

from alarm_clock import AlarmClock


def test_date_time_input():
    input_date = "03/08/2021"
    input_time = "05:05:00"
    output = AlarmClock(input_date, input_time).verify_user_input()
    print("output = ", output)
    assert output is not False, "Given date and time is invalid."


test_date_time_input()
