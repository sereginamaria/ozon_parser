import telebot
from telebot import types
import requests
from connect_db import verification

bot = telebot.TeleBot('6508472057:AAHdRDqUbaVjn7sstEtnHPMmKAXXAPp6_og')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/get_products_from_page":
        bot.send_message(message.from_user.id, "Введите ссылку на категорию/список страниц с товарами")
        bot.register_next_step_handler(message, get_page_url)
    elif message.text == "/get_product":
        bot.send_message(message.from_user.id, "Введите ссылку на товар")
        bot.register_next_step_handler(message, get_product_url)
    elif message.text == "/verification":
        bot.send_message(message.from_user.id, "Хочу верифицировать")
        bot.register_next_step_handler(message, verification)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Список команд:")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


def get_product_url(message):
    requests.post("http://127.0.0.1:5000/get_product", message.text)
    bot.send_message(message.from_user.id, "Выполнение завершено!")
def get_page_url(message):
    requests.post("http://127.0.0.1:5000/get_products_from_page", message.text)
    bot.send_message(message.from_user.id, "Выполнение завершено!")


# Кнопки меню в сообщеиях
# def inline_key(a):
#     if a.text == "Inline_menu":
#         mainmenu = types.InlineKeyboardMarkup()
#         key1 = types.InlineKeyboardButton(text='Кнопка 1', callback_data='key1')
#         key2 = types.InlineKeyboardButton(text='Кнопка 2', callback_data='key2')
#         mainmenu.add(key1, key2)
#         bot.send_message(a.chat.id, 'Это главное меню!', reply_markup=mainmenu)



@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "mainmenu":
        mainmenu = types.InlineKeyboardMarkup()
        key1 = types.InlineKeyboardButton(text='Кнопка 1', callback_data='key1')
        key2 = types.InlineKeyboardButton(text='Кнопка 2', callback_data='key2')
        mainmenu.add(key1, key2)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=mainmenu)
    elif call.data == "key1":
        next_menu = types.InlineKeyboardMarkup()
        key3 = types.InlineKeyboardButton(text='Кнопка 3', callback_data='key3')
        back = types.InlineKeyboardButton(text='Назад', callback_data='mainmenu')
        next_menu.add(key3, back)
        bot.edit_message_text('Это меню уровня 2, для кнопки1!', call.message.chat.id, call.message.message_id,
                              reply_markup=next_menu)
    elif call.data == "key2":
        next_menu2 = types.InlineKeyboardMarkup()
        key4 = types.InlineKeyboardButton(text='Кнопка 4', callback_data='key4')
        back = types.InlineKeyboardButton(text='Назад', callback_data='mainmenu')
        next_menu2.add(key4, back)
        bot.edit_message_text('Это меню уровня 2, для кнопки2!', call.message.chat.id, call.message.message_id,
                              reply_markup=next_menu2)


bot.polling(none_stop=True, interval=0)
