from threading import Thread
import telebot
from telegram_bot_calendar import DetailedTelegramCalendar, LSTEP
import datetime
from datetime import date
import bot_database
import create_post
import get_post
import get_products_from_page
import get_product
import verification
import autoposting
import time

bot = telebot.TeleBot('6508472057:AAHdRDqUbaVjn7sstEtnHPMmKAXXAPp6_og')

th_1 = Thread(target=autoposting.autop)
# th_1.start()

@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if message.text == "/get_products_from_page":
        get_products_from_page.init_bot(message, bot)
    elif message.text == "/get_product":
        get_product.init_bot(message, bot)
    elif message.text == "/verification":
        verification.init_bot(message, bot)
    elif message.text == "/create_post":
        create_post.init_bot(message, bot)
    elif message.text == "/get_post":
        get_post.init_bot(message, bot)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Список команд:")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


@bot.callback_query_handler(func=DetailedTelegramCalendar.func(calendar_id=1))
def call(call):
    result, key, step = DetailedTelegramCalendar(calendar_id=1, locale='ru').process(call.data)
    if not result and key:
        bot.edit_message_text(f"Select {LSTEP[step]}",
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=key)
    elif result:
        create_post.get_date_of_publication(call.message, result)


@bot.callback_query_handler(func=DetailedTelegramCalendar.func(calendar_id=2))
def call(call):
    result, key, step = DetailedTelegramCalendar(calendar_id=2, locale='ru').process(call.data)
    if not result and key:
        bot.edit_message_text(f"Select {LSTEP[step]}",
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=key)
    elif result:
        get_post.get_date_of_publication(call.message, result)


@bot.callback_query_handler(func=lambda call: True and call.data.split('|')[0] == 'verification')
def callback_inline(call):
    bot_database.callback_verification(call.data)
    verification.init_bot(call.message, bot)


@bot.callback_query_handler(func=lambda call: True and call.data.split('|')[0] == 'create_post_platform')
def callback_inline(call):
    publication_platform = call.data.split('|')[1]
    create_post.get_publication_platform(call.message, publication_platform)


@bot.callback_query_handler(func=lambda call: True and call.data.split('|')[0] == 'choice')
def callback_inline(call):
    create_post.record_data(call.message, call.data.split('|')[1], call.data.split('|')[2])


@bot.callback_query_handler(func=lambda call: True and call.data.split('|')[0] == 'get_post_platform')
def callback_inline(call):
    publication_platform = call.data.split('|')[1]
    get_post.get_publication_platform(call.message, publication_platform)


bot.polling(none_stop=True, interval=0)
