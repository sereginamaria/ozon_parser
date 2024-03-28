from telebot import types
from telebot.types import InputMediaPhoto
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

    mass = ['2', '3', '4', '5', '6', '7']

    from PIL import Image

    for num in mass:
        image = Image.open("/home/masha/ozon_parser/card_creator/cards/card" + str(num) + ".png")
        image_copy = image.copy()
        image_copy.save('/home/masha/ozon_parser/card_creator/cards_copyes/card' + str(num) + ".png")

    media_group = []
    # media_group.append(
    #     InputMediaPhoto(open("/home/masha/ozon_parser/card_creator/cards_copyes/card_title" + ".png", "rb")))

    media_group.append(
        InputMediaPhoto(open("/home/masha/ozon_parser/card_creator/cards_copyes/card_inst" + ".png", "rb")))
    for num in mass:
        # bot.send_message(message.chat.id, len(new_product_images[num]))
        # bot.send_message(message.chat.id, len('https://cdn1.ozone.ru/s3/multimedia-l/6822645671.jpg'))
        media_group.append(
            InputMediaPhoto(open("/home/masha/ozon_parser/card_creator/cards_copyes/card" + str(num) + ".png", "rb")))

    mass.insert(0, '_inst')
    # for i in range(3):
    #     mass.append('_qr_code')

    # bot.send_message(message.chat.id, mass)

    bot_requests.create_video(mass)

    # video_maker.generate_video()

    video = open('/home/masha/ozon_parser/video_maker/output1.mp4', 'rb')

    bot.send_video(message.chat.id, video, timeout=10)
    bot.send_media_group(chat_id=message.chat.id, media=media_group)