from telebot import types
from telebot.types import InputMediaPhoto
from telegram_bot_calendar import DetailedTelegramCalendar, LSTEP
import bot_database
import bot_requests
from PIL import Image
import asyncio

def init_bot(message, telegram_bot):
    global bot, count, mass
    count = 0
    mass = []
    bot = telegram_bot
    create_post(message)


def create_post(message):
    # mass = ['1', '2', '3', '4', '5', '6', '7']
    # bot_requests.create_video(mass)
    #
    # video = open('/home/masha/ozon_parser/video_maker/video.mp4', 'rb')
    # bot.send_video(message.chat.id, video, timeout=10)

    bot.send_message(message.chat.id, 'Введите категорию для публикации:')
    bot.register_next_step_handler(message, get_publication_category)


def get_publication_category(message):
    global publication_category
    publication_category = message.text

    menu = types.InlineKeyboardMarkup()
    key1 = types.InlineKeyboardButton(text='Вконтакте', callback_data='create_post_platform' + '|' + 'vk')
    key2 = types.InlineKeyboardButton(text='Телеграмм', callback_data='create_post_platform' + '|' + 'tg')
    key3 = types.InlineKeyboardButton(text='Инстаграмм', callback_data='create_post_platform' + '|' + 'inst')
    menu.add(key1, key2, key3)

    bot.send_message(message.chat.id, 'Выберите платформу для публикации', reply_markup=menu)


def get_publication_platform(message, callback_publication_platform):
    global publication_platform
    publication_platform = callback_publication_platform

    calendar, step = DetailedTelegramCalendar(calendar_id=1, locale='ru').build()
    bot.send_message(message.chat.id, f"Select {LSTEP[step]}", reply_markup=calendar)


def get_date_of_publication(message, callback_date_of_publication):
    global date_of_publication
    date_of_publication = callback_date_of_publication

    bot.send_message(message.chat.id, 'Введите время публикации (в формате 12:00)')
    bot.register_next_step_handler(message, get_time_of_publication)

def get_time_of_publication(message):
    global time_of_publication
    # print(message.text)
    # bot.send_message(message.chat.id, message.text)
    time_of_publication = message.text

    bot.send_message(message.chat.id, 'Ожидайте...')
    product_list = bot_database.create_test_card(publication_category)

    # print(publication_category)
    # print(product_list)
    # bot.send_message(message.chat.id, publication_category)
    # bot.send_message(message.chat.id, product_list)

    if len(product_list) < 6:
        print(product_list)
        bot.send_message(message.chat.id, 'В базе данных недостаточно товаров для данной категории')
    else:
        menu = types.InlineKeyboardMarkup()
        k = 1
        for product_id_list in product_list:
            product_id, product_name, product_article, product_sizes, product_price, \
                product_price_with_ozon_card, product_images, publication_category_i, product_url = product_id_list
            key = types.InlineKeyboardButton(text=k, callback_data='choice' + '|' + str(product_id) + '|' + str(k))
            menu.add(key)
            k = k + 1

        bot.send_message(message.chat.id, 'Выберите нужные карточки', reply_markup=menu)


def record_data(message, product_id, k):
    global count, mass, product_id_first

    if k not in mass:
        mass.append(k)
        count = count + 1

    if count == 1:
        product_id_first = product_id

    if count < 6:
        bot_database.create_post(date_of_publication, time_of_publication, publication_platform, product_id)
    elif count == 6:
        bot_database.create_post(date_of_publication, time_of_publication, publication_platform, product_id)
        bot.send_message(message.chat.id, 'Вы выбрали 6 карточек, пост создан на ' + str(date_of_publication) + ' ' + str(time_of_publication))

        for num in mass:
            image = Image.open("/home/masha/ozon_parser/card_creator/cards/card" + str(num) + ".png")
            image_copy = image.copy()
            image_copy.save('/home/masha/ozon_parser/card_creator/cards_copyes/card' + str(num) + ".png")

        bot_database.product_for_only_title_card(product_id_first)
        media_group = []
        media_group.append(
            InputMediaPhoto(open("/home/masha/ozon_parser/card_creator/cards_copyes/card_title" + ".png", "rb")))

        media_group.append(
            InputMediaPhoto(open("/home/masha/ozon_parser/card_creator/cards_copyes/card_inst" + ".png", "rb")))
        for num in mass:
            # bot.send_message(message.chat.id, len(new_product_images[num]))
            # bot.send_message(message.chat.id, len('https://cdn1.ozone.ru/s3/multimedia-l/6822645671.jpg'))
            media_group.append(
                InputMediaPhoto(open("/home/masha/ozon_parser/card_creator/cards_copyes/card" + str(num) + ".png", "rb")))



        mass.insert(0,'_inst')
        # for i in range(3):
        #     mass.append('_qr_code')

        # bot.send_message(message.chat.id, mass)

        bot_requests.create_video(mass)

        # video_maker.generate_video()

        video = open('/home/masha/ozon_parser/video_maker/output1.mp4', 'rb')

        bot.send_video(message.chat.id, video, timeout=10)
        bot.send_media_group(chat_id=message.chat.id, media=media_group)

    else:
        bot.send_message(message.chat.id, 'Вы выбрали 6 карточек, пост создан')

