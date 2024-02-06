from telebot import types
from telegram_bot_calendar import DetailedTelegramCalendar, LSTEP
import bot_database
import bot_requests


def init_bot(message, telegram_bot):
    global bot
    bot = telegram_bot
    get_post(message)


def get_post(message):


    bot.send_message(message.chat.id, 'Введите категорию поста:')
    bot.register_next_step_handler(message, get_publication_category)


def get_publication_category(message):
    global publication_category
    publication_category = message.text

    menu = types.InlineKeyboardMarkup()
    key1 = types.InlineKeyboardButton(text='Вконтакте', callback_data='get_post_platform' + '|' + 'vk')
    key2 = types.InlineKeyboardButton(text='Телеграмм', callback_data='get_post_platform' + '|' + 'tg')
    key3 = types.InlineKeyboardButton(text='Инстаграмм', callback_data='get_post_platform' + '|' + 'inst')
    menu.add(key1, key2, key3)

    bot.send_message(message.chat.id, 'Выберите платформу поста', reply_markup=menu)


def get_publication_platform(message, callback_publication_platform):
    global publication_platform
    publication_platform = callback_publication_platform

    calendar, step = DetailedTelegramCalendar(calendar_id=2, locale='ru').build()
    bot.send_message(message.chat.id, f"Select {LSTEP[step]}", reply_markup=calendar)


def get_date_of_publication(message, callback_date_of_publication):
    global date_of_publication
    date_of_publication = callback_date_of_publication
    bot.send_message(message.chat.id, 'Формируется пост: ' + publication_category + publication_platform + str(date_of_publication)
                     + '. Ожидайте...')

    bot_database.get_post_from_db(publication_category, publication_platform, date_of_publication)

    mass = ['1', '2', '3', '4', '5', '6', '7']

    bot_requests.create_video(mass)

    video = open('/home/masha/ozon_parser/video_maker/output1.mp4', 'rb')
    bot.send_video(message.chat.id, video, timeout=10)