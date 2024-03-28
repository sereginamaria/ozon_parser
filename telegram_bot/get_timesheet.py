from datetime import date
import datetime as datetime2
from telebot import types
from telegram_bot_calendar import DetailedTelegramCalendar, LSTEP
import bot_database


def init_bot(message, telegram_bot):
    global bot
    bot = telegram_bot
    # get_timesheet(message)
    date_t = date.today()
    get_date_of_publication(message, date_t)

def get_timesheet(message):
    bot.send_message(message.chat.id, 'Введите дату:')

    calendar, step = DetailedTelegramCalendar(calendar_id=5, locale='ru').build()
    bot.send_message(message.chat.id, f"Select {LSTEP[step]}", reply_markup=calendar)


def get_date_of_publication(message, callback_date_of_publication):
    global date_of_publication
    timesheet = {
        'Monday': {
            "Украшения": '6:00',
            "Верхняя Одежда": '8:00',
            "Кофта": '10:00',
            "Брюки": '12:00',
            "Топ": '14:00',
            "Платье": '16:00',
            "Пиджак": '18:00',
            "Сумка": '20:00',
        },
        'Tuesday': {
            "Аксессуары": '6:00',
            "Верхняя Одежда": '8:00',
            "Футболка": '10:00',
            "Кофта": '12:00',
            "Костюм": '14:00',
            "Юбка": '16:00',
            "Блузка": '18:00',
            "Обувь": '20:00',
        },
        'Wednesday': {
            "Украшения": '6:00',
            "Верхняя Одежда": '8:00',
            "Рубашка": '10:00',
            "Платье": '12:00',
            "Пиджак": '14:00',
            "Брюки": '16:00',
            "Топ": '18:00',
            "Сумка": '20:00',
        },
        'Thursday': {
            "Аксессуары": '6:00',
            "Верхняя Одежда": '8:00',
            "Кофта": '10:00',
            "Юбка": '12:00',
            "Блузка": '14:00',
            "Джинсы": '16:00',
            "Футболка": '18:00',
            "Обувь": '20:00',
        },
        'Friday': {
            "Украшения": '6:00',
            "Верхняя Одежда": '8:00',
            "Пиджак": '10:00',
            "Брюки": '12:00',
            "Обувь": '14:00',
            "Топ": '16:00',
            "Платье": '18:00',
            "Сумка": '20:00',
        },
        'Saturday': {
            "Домашняя Одежда": '6:00',
            "Верхняя Одежда": '8:00',
            "Рубашка": '10:00',
            "Джинсы": '12:00',
            "Футболка": '14:00',
            "Пиджак": '16:00',
            "Брюки": '18:00',
            "Обувь": '20:00',
        },
        'Sunday': {
            "Украшения": '6:00',
            "Верхняя Одежда": '8:00',
            "Кофта": '10:00',
            "Топ": '12:00',
            "Платье": '14:00',
            "Костюм": '16:00',
            "Юбка": '18:00',
            "Сумка": '20:00',
        }
    }

    date_of_publication = callback_date_of_publication
    bot.send_message(message.chat.id, 'Готовится расписание. Ожидайте...')

    time_array = ['6:00', '8:00', '10:00', '12:00', '14:00', '16:00', '18:00', '20:00']

    i = 1
    while i <= 7:
        timesheet_text = str(date_of_publication)
        for time in time_array:
            product_list = bot_database.get_timesheet(date_of_publication, time)

            # bot.send_message(message.chat.id, time)
            # bot.send_message(message.chat.id, len(product_list))
            # bot.send_message(message.chat.id, str(product_list))
            publication_category = ''
            sub_category = ''
            if len(product_list) > 0:
                publication_category = ''.join(product_list[0][0])
                sub_category = ''.join(product_list[0][1])
            else:
                date_name = date_of_publication.strftime("%A")
                for k, v in timesheet[date_name].items():
                    if v == time:
                        publication_category = k

            # bot.send_message(message.chat.id, publication_category)
            if (publication_category == 'Верхняя Одежда' or publication_category == 'Кофта'):
                if len(product_list) == 6:
                    timesheet_text += '\n' + time + ' ' + publication_category + ' ' + sub_category + '  ✅️'
                else:
                    timesheet_text += ('\n' + time + ' ' + publication_category + ' ' + sub_category + ' ❌' + 'Нужно еще '
                                       + str(6 - len(product_list)))
            else:
                if len(product_list) == 6:
                    timesheet_text += '\n' + time + ' ' + publication_category + '  ✅️'
                else:
                    timesheet_text += ('\n' + time + ' ' + publication_category + ' ❌' + 'Нужно еще '
                                       + str(6 - len(product_list)))

            # i = 1
            # for product in product_list:
            #     publication_category = ''.join(product[0])
            #     timesheet += '\n' + str(i) + '. ' + publication_category
            #     i += 1
        i += 1
        date_of_publication += datetime2.timedelta(days=1)
        bot.send_message(message.chat.id, timesheet_text)
        timesheet_text = ''

