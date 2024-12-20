from telebot import types
from telegram_bot_calendar import DetailedTelegramCalendar, LSTEP
import bot_database


def init_bot(message, telegram_bot):
    global bot, count, mass
    count = 0
    mass = []
    bot = telegram_bot
    create_single_post(message)


def create_single_post(message):
    bot.send_message(message.chat.id, 'Введите категорию для публикации:')
    bot.register_next_step_handler(message, get_publication_category)


def get_publication_category(message):
    global publication_category
    publication_category = message.text

    menu = types.InlineKeyboardMarkup()
    key1 = types.InlineKeyboardButton(text='Вконтакте', callback_data='create_single_post_platform' + '|' + 'vk')
    key2 = types.InlineKeyboardButton(text='Телеграмм', callback_data='create_single_post_platform' + '|' + 'tg')
    key3 = types.InlineKeyboardButton(text='Инстаграмм', callback_data='create_single_post_platform' + '|' + 'inst')
    menu.add(key1, key2, key3)

    bot.send_message(message.chat.id, 'Выберите платформу для публикации', reply_markup=menu)


def get_publication_platform(message, callback_publication_platform):
    global publication_platform
    publication_platform = callback_publication_platform

    calendar, step = DetailedTelegramCalendar(calendar_id=3, locale='ru').build()
    bot.send_message(message.chat.id, f"Select {LSTEP[step]}", reply_markup=calendar)


def get_date_of_publication(message, callback_date_of_publication):
    global date_of_publication
    date_of_publication = callback_date_of_publication

    bot.send_message(message.chat.id, 'Введите время публикации (в формате 12:00)')
    bot.register_next_step_handler(message, get_time_of_publication)

def get_time_of_publication(message):
    global time_of_publication
    time_of_publication = message.text

    bot.send_message(message.chat.id, 'Ожидайте...')
    product_list = bot_database.create_single_card(publication_category)


    if len(product_list) < 1:
        bot.send_message(message.chat.id, 'В базе данных недостаточно товаров для данной категории')
    else:
        menu = types.InlineKeyboardMarkup()
        k = 1
        for product_id_list in product_list:
            product_id, product_name, product_article, product_sizes, product_price, \
                product_price_with_ozon_card, product_images, publication_category_i, product_url = product_id_list
            key = types.InlineKeyboardButton(text=k, callback_data='choice_single' + '|' + str(product_id) + '|' + str(k))
            menu.add(key)
            k = k + 1

        bot.send_message(message.chat.id, 'Выберите нужные карточки', reply_markup=menu)

def record_data(message, product_id, k):
    global count, mass

    if k not in mass:
        mass.append(k)
        count = count + 1
    if count == 1:
        bot_database.create_single_post(date_of_publication, time_of_publication, publication_platform, product_id)
        bot.send_message(message.chat.id, 'Вы выбрали карточку, пост создан')
    else:
        bot.send_message(message.chat.id, 'Вы выбрали карточку, пост создан')
