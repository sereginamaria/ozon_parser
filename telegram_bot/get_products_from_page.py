import bot_requests


def init_bot(message, telegram_bot):
    global bot
    bot = telegram_bot
    get_products_from_page(message)


def get_products_from_page(message):
    bot.send_message(message.from_user.id, "Введите название категории для публикации")
    bot.register_next_step_handler(message, get_publication_category)


def get_publication_category(message):
    publication_category = message.text
    bot.send_message(message.from_user.id, "Введите ссылку на категорию/список страниц с товарами")
    bot.register_next_step_handler(message, get_link, publication_category)


def get_link(message, publication_category):
    bot_requests.get_products_from_page(message, publication_category)
    bot.send_message(message.from_user.id, "Выполнение завершено!")
