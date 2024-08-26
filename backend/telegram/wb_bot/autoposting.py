import datetime
from datetime import datetime
import time
import requests
from main_config import BASE_URL
def send_post(category):
    new_product = {
        "category": category,
    }

    requests.post("http://" + BASE_URL + ":5001/wb/send_post", json=new_product)

def get_publishing_time(time_str):
    return datetime.strptime(time_str, '%H:%M').time()

def in_time(time_start, current_time, time_end):
    return get_publishing_time(time_start) < current_time < get_publishing_time(time_end)

def autop():
    while True:
        current_day_of_week = datetime.now().strftime('%A')
        current_time = datetime.now().time()

        if ((current_day_of_week == 'Monday' and in_time('8:00', current_time, '8:59')) or
                (current_day_of_week == 'Wednesday' and in_time('8:00', current_time, '8:59')) or
                (current_day_of_week == 'Friday' and in_time('8:00', current_time, '8:59')) or
                (current_day_of_week == 'Saturday' and in_time('8:00', current_time, '8:59')) or
                (current_day_of_week == 'Sunday' and in_time('8:00', current_time, '8:59'))):
            send_post('Верхняя Одежда')

        # if ((current_day_of_week == 'Monday' and in_time('10:00', current_time, '10:59')) or
        #         (current_day_of_week == 'Tuesday' and in_time('12:00', current_time, '12:59')) or
        #         (current_day_of_week == 'Wednesday' and in_time('10:00', current_time, '10:59')) or
        #         (current_day_of_week == 'Friday' and in_time('10:00', current_time, '10:59')) or
        #         (current_day_of_week == 'Sunday' and in_time('10:00', current_time, '10:59'))):
        #     send_post('Кофта')
        #
        # if ((current_day_of_week == 'Monday' and in_time('16:00', current_time, '16:59')) or
        #         (current_day_of_week == 'Friday' and in_time('18:00', current_time, '18:59')) or
        #         (current_day_of_week == 'Sunday' and in_time('14:00', current_time, '14:59'))):
        #     send_post('Платье')
        #
        # if ((current_day_of_week == 'Tuesday' and in_time('16:00', current_time, '16:59')) or
        #         (current_day_of_week == 'Thursday' and in_time('12:00', current_time, '12:59')) or
        #         (current_day_of_week == 'Sunday' and in_time('18:00', current_time, '18:59'))):
        #     send_post('Юбка')
        #
        # if ((current_day_of_week == 'Wednesday' and in_time('18:00', current_time, '18:59')) or
        #         (current_day_of_week == 'Friday' and in_time('16:00', current_time, '16:59'))):
        #     send_post('Топ')
        #
        # if ((current_day_of_week == 'Wednesday' and in_time('12:00', current_time, '12:59')) or
        #         (current_day_of_week == 'Thursday' and in_time('18:00', current_time, '18:59')) or
        #         (current_day_of_week == 'Saturday' and in_time('14:00', current_time, '14:59'))):
        #     send_post('Футболка')
        #
        # if ((current_day_of_week == 'Tuesday' and in_time('14:00', current_time, '14:59')) or
        #         (current_day_of_week == 'Thursday' and in_time('10:00', current_time, '10:59')) or
        #         (current_day_of_week == 'Sunday' and in_time('16:00', current_time, '16:59'))):
        #     send_post('Костюм')
        #
        # if ((current_day_of_week == 'Thursday' and in_time('14:00', current_time, '14:59')) or
        #         (current_day_of_week == 'Saturday' and in_time('10:00', current_time, '10:59'))):
        #     send_post('Рубашка')
        #
        # if ((current_day_of_week == 'Tuesday' and in_time('18:00', current_time, '18:59')) or
        #         (current_day_of_week == 'Sunday' and in_time('12:00', current_time, '12:59'))):
        #     send_post('Блузка')
        #
        # if ((current_day_of_week == 'Monday' and in_time('12:00', current_time, '12:59')) or
        #         (current_day_of_week == 'Wednesday' and in_time('16:00', current_time, '16:59')) or
        #         (current_day_of_week == 'Friday' and in_time('12:00', current_time, '12:59')) or
        #         (current_day_of_week == 'Saturday' and in_time('18:00', current_time, '18:59'))):
        #     send_post('Брюки')
        #
        # if ((current_day_of_week == 'Monday' and in_time('18:00', current_time, '18:59')) or
        #         (current_day_of_week == 'Tuesday' and in_time('10:00', current_time, '10:59')) or
        #         (current_day_of_week == 'Wednesday' and in_time('14:00', current_time, '14:59')) or
        #         (current_day_of_week == 'Saturday' and in_time('16:00', current_time, '16:59'))):
        #     send_post('Пиджак')
        #
        # if ((current_day_of_week == 'Monday' and in_time('14:00', current_time, '14:59')) or
        #         (current_day_of_week == 'Thursday' and in_time('16:00', current_time, '16:59')) or
        #         (current_day_of_week == 'Saturday' and in_time('12:00', current_time, '12:59'))):
        #     send_post('Джинсы')
        #
        # if current_day_of_week == 'Saturday' and in_time('6:00', current_time, '6:59'):
        #     send_post('Домашняя Одежда')
        #
        # if current_day_of_week == 'Tuesday' and in_time('8:00', current_time, '8:59'):
        #     send_post('Шорты')
        #
        # if current_day_of_week == 'Thursday' and in_time('8:00', current_time, '8:59'):
        #     send_post('Корсет')
        #
        # if ((current_day_of_week == 'Tuesday' and in_time('20:00', current_time, '20:59')) or
        #         (current_day_of_week == 'Thursday' and in_time('20:00', current_time, '20:59')) or
        #         (current_day_of_week == 'Friday' and in_time('14:00', current_time, '14:59')) or
        #         (current_day_of_week == 'Saturday' and in_time('20:00', current_time, '20:59'))):
        #     send_post('Обувь')
        #
        # if ((current_day_of_week == 'Monday' and in_time('20:00', current_time, '20:59')) or
        #         (current_day_of_week == 'Wednesday' and in_time('20:00', current_time, '20:59')) or
        #         (current_day_of_week == 'Friday' and in_time('20:00', current_time, '20:59')) or
        #         (current_day_of_week == 'Sunday' and in_time('20:00', current_time, '20:59'))):
        #     send_post('Сумка')
        #
        # if ((current_day_of_week == 'Tuesday' and in_time('6:00', current_time, '6:59')) or
        #         (current_day_of_week == 'Thursday' and in_time('6:00', current_time, '6:59'))):
        #     send_post('Аксессуары')
        #
        # if ((current_day_of_week == 'Monday' and in_time('6:00', current_time, '6:59')) or
        #         (current_day_of_week == 'Wednesday' and in_time('6:00', current_time, '6:59')) or
        #         (current_day_of_week == 'Friday' and in_time('6:00', current_time, '6:59')) or
        #         (current_day_of_week == 'Sunday' and in_time('6:00', current_time, '6:59'))):
        #     send_post('Украшения')

        time.sleep(3600)
