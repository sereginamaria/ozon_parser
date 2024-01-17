import datetime
from datetime import date
import time
import bot_database

def autop():
    while True:
        today_date = date.today()
        today_time = datetime.datetime.now().time()
        today_time_hour = today_time.hour
        today_time_minute =today_time.minute

        if today_time_hour < 10:
            today_time_hour = "0" + str(today_time_hour)

        if today_time_minute < 10:
            today_time_minute = "0" + str(today_time_minute)


        current_time = str(today_time_hour) + ':' + str(today_time_minute)

        print(current_time)
        bot_database.autoposting_date(today_date, current_time)

        time.sleep(2400)
