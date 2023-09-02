import telebot
from telegram_bot_calendar import DetailedTelegramCalendar, LSTEP
import datetime
from datetime import date
import bot_database
import create_post
import get_post
import get_products_from_page
import verification
import time

bot = telebot.TeleBot('6508472057:AAHdRDqUbaVjn7sstEtnHPMmKAXXAPp6_og')


@bot.message_handler(content_types=['text'])
def get_text_message(message):
    match message.text:
        case "/get_products_from_page":
            get_products_from_page.init_bot(message, bot)
        case "/get_product":
            get_products_from_page.init_bot(message, bot)
        case "/verification":
            verification.init_bot(message, bot)
        case "/create_post":
            create_post.init_bot(message, bot)
        case "/get_post":
            get_post.init_bot(message, bot)
        case "/help":
            bot.send_message(message.from_user.id, "Список команд:")
        case _:
            bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


while True:
    # Получаем текущее время
    now = date.today()
    current_date_time = datetime.datetime.now()
    current_time = current_date_time.time()
    print(now)
    print(current_time)

    bot_database.autoposting_date(now, current_time)
    # # Проходим по всем чатам в словаре
    # for chat_id in delayed_messages:
    #     # Проходим по всем сообщениям в списке
    #     for time, text in delayed_messages[chat_id]:
    #         # Если время отправки наступило или прошло
    #         if time <= now:
    #             # Отправляем сообщение в чат
    #             bot.send_message(chat_id, text)
    #             # Удаляем сообщение из списка
    #             delayed_messages[chat_id].remove((time, text))
    # # Делаем небольшую паузу, чтобы не перегружать процессор
    time.sleep(5)

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
    verification.init_bot(call.message)


@bot.callback_query_handler(func=lambda call: True and call.data.split('|')[0] == 'create_post_platform')
def callback_inline(call):
    publication_platform = call.data.split('|')[1]
    create_post.get_publication_platform(call.message, publication_platform)


@bot.callback_query_handler(func=lambda call: True and call.data.split('|')[0] == 'choice')
def callback_inline(call):
    create_post.record_data(call.data.split('|')[1])


@bot.callback_query_handler(func=lambda call: True and call.data.split('|')[0] == 'get_post_platform')
def callback_inline(call):
    publication_platform = call.data.split('|')[1]
    get_post.get_publication_platform(call.message, publication_platform)


bot.polling(none_stop=True, interval=0)
