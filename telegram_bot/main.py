import telebot
from telebot import types
import bot_database
from telegram_bot_calendar import DetailedTelegramCalendar, LSTEP
import bot_requests
import get_post

bot = telebot.TeleBot('6508472057:AAHdRDqUbaVjn7sstEtnHPMmKAXXAPp6_og')

@bot.message_handler(content_types=['text'])
def get_text_message(message):

    match message.text:
        case "/get_products_from_page":
            bot.send_message(message.from_user.id, "Введите название категории для публикации")
            bot.register_next_step_handler(message, get_page_url_message)
        case "/get_product":
            bot.send_message(message.from_user.id, "Введите название категории для публикации")
            bot.register_next_step_handler(message, get_product_url_message)
        case "/verification":
            verification_message(message)
        case "/create_post":
            publication_category_message(message)
        case "/get_post":
            global get_postt
            get_postt = True
            get_post.init_bot(message, bot)
            # get_post_publication_category_message(message)
        case "/help":
            bot.send_message(message.from_user.id, "Список команд:")
        case _:
            bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


def get_page_url_message(message):
    publication_category_page = message.text
    bot.send_message(message.from_user.id, "Введите ссылку на категорию/список страниц с товарами")
    bot.register_next_step_handler(message, get_products_from_page_message, publication_category_page)


def get_products_from_page_message(message, publication_category_page):
    bot_requests.get_products_from_page_request(message, publication_category_page)
    bot.send_message(message.from_user.id, "Выполнение завершено!")


def get_product_url_message(message):
    publication_category_product = message.text
    bot.send_message(message.from_user.id, "Введите ссылку на товар")
    bot.register_next_step_handler(message, get_product_message, publication_category_product)


def get_product_message(message, publication_category_product):
    bot_requests.get_product_request(message, publication_category_product)
    bot.send_message(message.from_user.id, "Выполнение завершено!")


def verification_message(message):
    products = bot_database.verification_db()
    product_list = products.fetchall()
    if product_list:
        for product in product_list:
            product_id, product_images = product
            main_menu = types.InlineKeyboardMarkup()
            key1 = types.InlineKeyboardButton(text='Да',
                                              callback_data='verification' + '|' + 'yes' + '|' + str(product_id))
            key2 = types.InlineKeyboardButton(text='Нет',
                                              callback_data='verification' + '|' + 'no' + '|' + str(product_id))
            main_menu.add(key1, key2)

            bot.send_photo(chat_id=message.chat.id, photo=product_images.split(',')[0],
                           caption='Оставляем?\nАртикул: ' + str(product_id),
                           reply_markup=main_menu)

    else:
        bot.send_message(message.chat.id, "Все товары проверифицированы")


def publication_category_message(message):
    bot.send_message(message.chat.id, 'Введите категорию для публикации:')
    bot.register_next_step_handler(message, publishing_platform_message)


def publishing_platform_message(message):
    global publication_category_post
    publication_category_post = message.text

    main_menu = types.InlineKeyboardMarkup()
    key1 = types.InlineKeyboardButton(text='Вконтакте', callback_data='platform' + '|' + 'vk')
    key2 = types.InlineKeyboardButton(text='Телеграмм', callback_data='platform' + '|' + 'tg')
    key3 = types.InlineKeyboardButton(text='Инстаграмм', callback_data='platform' + '|' + 'inst')
    main_menu.add(key1, key2, key3)
    bot.send_message(message.chat.id, 'Выберите платформу для публикации', reply_markup=main_menu)


def date_of_publication_message(message):
    calendar, step = DetailedTelegramCalendar().build()
    bot.send_message(message.chat.id,
                     f"Select {LSTEP[step]}",
                     reply_markup=calendar)

def create_card_message(message):
    product_list = bot_database.create_card_db(publication_category_post)
    main_menu = types.InlineKeyboardMarkup()
    k = 1
    for product_id_list in product_list:
        product_id, product_name, product_article, product_sizes, product_price, product_price_with_ozon_card, product_images = product_id_list
        key = types.InlineKeyboardButton(text=k, callback_data='choice' + '|' + str(product_id) + '|' + str(k))
        main_menu.add(key)
        k = k + 1

    bot.send_message(message.chat.id, 'Выберите нужные карточки', reply_markup=main_menu)

def get_post_publication_category_message(message):
    bot.send_message(message.chat.id, 'Введите категорию поста:')

    bot.register_next_step_handler(message, get_post_publishing_platform_message)


def get_post_publishing_platform_message(message):
    global get_post_publication_category_post
    get_post_publication_category_post = message.text

    main_menu = types.InlineKeyboardMarkup()
    key1 = types.InlineKeyboardButton(text='Вконтакте', callback_data='get_post_platform' + '|' + 'vk')
    key2 = types.InlineKeyboardButton(text='Телеграмм', callback_data='get_post_platform' + '|' + 'tg')
    key3 = types.InlineKeyboardButton(text='Инстаграмм', callback_data='get_post_platform' + '|' + 'inst')
    main_menu.add(key1, key2, key3)
    bot.send_message(message.chat.id, 'Выберите платформу поста', reply_markup=main_menu)


def get_post_date_of_publication_message(message):
    calendar, step = DetailedTelegramCalendar().build()

    bot.send_message(message.chat.id,
                     f"Select {LSTEP[step]}",
                     reply_markup=calendar)

# def get_post_create_card_message(message):
#     product_list = bot_database.get_post_create_card_db(get_post_publication_category_post, get_post_publishing_platform, get_post_date_of_publication)
#
#
#     bot.send_message(message.chat.id, 'Вот ваш пост: ' + get_post_publication_category_post + get_post_publishing_platform + str(get_post_date_of_publication))


@bot.callback_query_handler(func=DetailedTelegramCalendar.func(calendar_id=2))
def call(call):
    print('1')
    result, key, step = DetailedTelegramCalendar().process(call.data)
    if not result and key:
        print('2')
        bot.edit_message_text(f"Select {LSTEP[step]}",
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=key)
    elif result:
            get_post.get_date_of_publication(call.message, result)
#
#
# @bot.callback_query_handler(func=lambda call: True)
# def callback_inline(call):
#     if call.data.split('|')[0] == "verification":
#         bot_database.callback_verification(call.data)
#         verification_message(call.message)
#
#     if call.data.split('|')[0] == 'platform':
#         global publishing_platform
#         publishing_platform = call.data.split('|')[1]
#         print(publishing_platform)
#         date_of_publication_message(call.message)
#
#     if call.data.split('|')[0] == 'choice':
#         bot_database.choice_db(date_of_publication, publishing_platform, call.data)
#
#     if call.data.split('|')[0] == 'get_post_platform':
#         global get_post_publishing_platform
#         get_post_publishing_platform = call.data.split('|')[1]
#         print(get_post_publishing_platform)
#         get_post_date_of_publication_message(call.message)

@bot.callback_query_handler(func=lambda call: True and call.data.split('|')[0] == 'get_post_platform')
def callback_inline(call):
    publication_platform = call.data.split('|')[1]
    get_post.get_publication_platform(call.message, publication_platform)

bot.polling(none_stop=True, interval=0)
