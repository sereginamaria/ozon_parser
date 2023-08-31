from telebot import types
from telegram_bot_calendar import DetailedTelegramCalendar, LSTEP
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

def post_post():
    print('post')
# def create_card_message get_post_date_of_publication_message(message):
#     product_list = db.create_card_db(get_post_publication_category_post)
#     main_menu = types.InlineKeyboardMarkup()
#     k = 1
#     for product_id_list in product_list:
#         product_id, product_name, product_article, product_sizes, product_price, product_price_with_ozon_card, product_images = product_id_list
#         key = types.InlineKeyboardButton(text=k, callback_data='choice' + '|' + str(product_id) + '|' + str(k))
#         main_menu.add(key)
#         k = k + 1
#
#     bot.send_message(message.chat.id, 'Выберите нужные карточки', reply_markup=main_menu)


