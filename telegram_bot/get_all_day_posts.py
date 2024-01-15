from telebot import types
from telegram_bot_calendar import DetailedTelegramCalendar, LSTEP
import bot_database


def init_bot(message, telegram_bot):
    global bot
    bot = telegram_bot
    get_all_day_posts(message)


def get_all_day_posts(message):
    print('get_all_day_posts')

    menu = types.InlineKeyboardMarkup()
    key1 = types.InlineKeyboardButton(text='Вконтакте', callback_data='get_all_day_posts_platform' + '|' + 'vk')
    key2 = types.InlineKeyboardButton(text='Телеграмм', callback_data='get_all_day_posts_platform' + '|' + 'tg')
    key3 = types.InlineKeyboardButton(text='Инстаграмм', callback_data='get_all_day_posts_platform' + '|' + 'inst')
    menu.add(key1, key2, key3)

    bot.send_message(message.chat.id, 'Выберите платформу поста', reply_markup=menu)


def get_publication_platform(message, callback_publication_platform):
    global publication_platform
    publication_platform = callback_publication_platform

    calendar, step = DetailedTelegramCalendar(calendar_id=4, locale='ru').build()
    bot.send_message(message.chat.id, f"Select {LSTEP[step]}", reply_markup=calendar)


def get_date_of_publication(message, callback_date_of_publication):
    global date_of_publication
    date_of_publication = callback_date_of_publication
    bot.send_message(message.chat.id, 'Формируется пост: ' + publication_platform + str(date_of_publication)
                     + '. Ожидайте...')
    bot_database.get_all_day_posts_from_db(publication_platform, date_of_publication)