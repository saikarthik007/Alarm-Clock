"""
Application to set alarm based on date and time
Developed by : Karthik C
"""
import time
from datetime import datetime
from playsound import playsound


class AlarmClock:
    """class to set alarm on time based on user input"""
    def __init__(self, alarm_date, alarm_time):
        """ init function"""
        self.alarm_time = alarm_time
        self.alarm_date = alarm_date

    def set_alarm(self):
        """ function to trigger alarm"""

        while True:
            time.sleep(1)
            current_time = datetime.now()
            now = current_time.strftime("%H:%M:%S")
            date = current_time.strftime("%d/%m/%Y")
            if date == self.alarm_date and now == self.alarm_time:
                print("Time to Wake up")
                playsound('alarm.mp3')
                break

    def verify_user_input(self):
        """verify user given date and time is not in past"""
        current_time = datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        if self.alarm_date < date:
            print("Entered date is in past cant set alarm!")
            status = False
        elif self.alarm_date > date and (self.alarm_time < now or self.alarm_time > now):# or (self.alarm_date > date and self.alarm_time > now):
            status = True
        elif self.alarm_date == date and self.alarm_time < now:
            print("Entered time is in past cant set alarm!")
            status = False
        else:
            status = True
        return status


if __name__ == "__main__":
    # get date from user to set alarm on particular date
    ALARM_DAY = input("Enter the date to set alarm : DD/MM/YYYY\n")
    # get time from user to set alarm on time
    ALARM_TIME = input("Enter the time to set alarm : HH:MM:SS\n")
    # verify user given date and time is not in past
    INSTANCE = AlarmClock(ALARM_DAY, ALARM_TIME)
    VALIDATION = INSTANCE.verify_user_input()
    if VALIDATION:
        print("Setting up alarm...")
        INSTANCE.set_alarm()
