import telebot as telebot
import sys
import logging

logger = logging.getLogger('telegram_stilist_bot')
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)

bot = telebot.TeleBot('7075281827:AAFFGJ-vPc0DDQ-VmMakxFqYjafNUjxxynI')
