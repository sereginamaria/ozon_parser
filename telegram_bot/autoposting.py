# # Импортируем необходимые библиотеки
# import telebot # для работы с Telegram API
# import datetime # для работы с датой и временем
#
# # Создаем объект бота с помощью токена, полученного от @BotFather
# bot = telebot.TeleBot("YOUR_TOKEN")
#
# # Создаем словарь, где будем хранить отложенные сообщения
# # Ключ - идентификатор чата, значение - список кортежей (время, текст)
# delayed_messages = {}
#
# # Обрабатываем команду /start
# @bot.message_handler(commands=["start"])
# def start(message):
#     # Приветствуем пользователя и объясняем, как пользоваться ботом
#     bot.send_message(message.chat.id, "Привет, я бот для создания отложенных сообщений. Чтобы отправить сообщение позже, напиши его в формате:\n\n[год]-[месяц]-[день] [час]:[минута] [текст]\n\nНапример:\n\n2023-09-01 15:00 Привет, как дела?\n\nБот отправит это сообщение в указанное время. Можешь создать несколько отложенных сообщений для одного или разных чатов.")
#
# # Обрабатываем все остальные сообщения
# @bot.message_handler(func=lambda m: True)
# def delay(message):
#     # Пытаемся распарсить сообщение по формату
#     try:
#         # Разделяем сообщение на две части: время и текст
#         time, text = message.text.split(maxsplit=1)
#         # Преобразуем строку с временем в объект datetime
#         time = datetime.datetime.strptime(time, "%Y-%m-%d %H:%M")
#         # Проверяем, что время не прошло
#         if time > datetime.datetime.now():
#             # Добавляем сообщение в словарь отложенных сообщений
#             if message.chat.id not in delayed_messages:
#                 delayed_messages[message.chat.id] = []
#             delayed_messages[message.chat.id].append((time, text))
#             # Сообщаем пользователю, что сообщение запланировано
#             bot.send_message(message.chat.id, f"Сообщение '{text}' запланировано на {time}")
#         else:
#             # Сообщаем пользователю, что время неверное
#             bot.send_message(message.chat.id, "Нельзя отправить сообщение в прошлое. Попробуй еще раз.")
#     except:
#         # Сообщаем пользователю, что формат неверный
#         bot.send_message(message.chat.id, "Неверный формат сообщения. Попробуй еще раз.")
#
# # Создаем бесконечный цикл, в котором будем проверять отложенные сообщения
# while True:
#     # Получаем текущее время
#     now = datetime.datetime.now()
#     # Проходим по всем чатам в словаре
#     for chat_id in delayed_messages:
#         # Проходим по всем сообщениям в списке
#         for time, text in delayed_messages[chat_id]:
#             # Если время отправки наступило или прошло
#             if time <= now:
#                 # Отправляем сообщение в чат
#                 bot.send_message(chat_id, text)
#                 # Удаляем сообщение из списка
#                 delayed_messages[chat_id].remove((time, text))
#     # Делаем небольшую паузу, чтобы не перегружать процессор
#     time.sleep(1)

import datetime
from datetime import date
import time
import bot_database

def autop():
    while True:
        today_date = date.today()
        today_time = datetime.datetime.now().time()
        today_time_hour = today_time.hour
        today_time_minute =today_time.minute
        print(today_date)
        print(today_time)

        if today_time_hour < 10:
            today_time_hour = "0" + str(today_time_hour)

        if today_time_minute < 10:
            today_time_minute = "0" + str(today_time_minute)


        current_time = str(today_time_hour) + ':' + str(today_time_minute)

        print(current_time)
        bot_database.autoposting_date(today_date, current_time)

        time.sleep(5)