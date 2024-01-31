import datetime
from datetime import date
import time
import bot_database
import requests

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

        # get_updates()
        time.sleep(1800)

# token = '6508472057:AAHdRDqUbaVjn7sstEtnHPMmKAXXAPp6_og'
# url = 'https://api.telegram.org/botf'
#
# def get_updates(offset=0):
#     result = requests.get(f'{url}{token}/getUpdates?offset={offset}').json()
#     print(result)
    # return result
    # requests.get(f'{url}{token}/getUpdates?offset={offset}').json()