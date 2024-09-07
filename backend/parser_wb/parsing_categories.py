from parser_wb import get_products

def parse_trousers():
    # БРЮКИ
    # Все цвета, кроме черного
    # Вечернаяя мода
    get_products.parse_page('Брюки',
                           'https://www.wildberries.ru/catalog/zhenshchinam/odezhda/bryuki-i-shorty?sort=popular&page=1&xsubject=11&fcolor=16119260%3B16777215%3B11393254%3B16776960%3B32768%3B10824234%3B16711680%3B16753920%3B16761035%3B8421504%3B255%3B15631086&f23796=31142')

    # Выпускной, новый год, свадьба
    get_products.parse_page('Брюки',
                           'https://www.wildberries.ru/catalog/zhenshchinam/odezhda/bryuki-i-shorty?sort=popular&page=1&xsubject=11&fcolor=16119260%3B16777215%3B11393254%3B16776960%3B32768%3B10824234%3B16711680%3B16753920%3B16761035%3B8421504%3B255%3B15631086&f23796=31137%3B31138%3B31136')

    # Офис
    get_products.parse_page('Брюки',
                           'https://www.wildberries.ru/catalog/zhenshchinam/odezhda/bryuki-i-shorty?sort=popular&page=1&xsubject=11&fcolor=16119260%3B16777215%3B11393254%3B16776960%3B32768%3B10824234%3B16711680%3B16753920%3B16761035%3B8421504%3B255%3B15631086&f23796=31140')

    # Повседневное
    get_products.parse_page('Брюки',
                           'https://www.wildberries.ru/catalog/zhenshchinam/odezhda/bryuki-i-shorty?sort=popular&page=1&xsubject=11&fcolor=16119260%3B16777215%3B11393254%3B16776960%3B32768%3B10824234%3B16711680%3B16753920%3B16761035%3B8421504%3B255%3B15631086&f23796=31141')

    # ВСЕ категории, ЧЕРНЫЙ
    get_products.parse_page('Брюки',
                           'https://www.wildberries.ru/catalog/zhenshchinam/odezhda/bryuki-i-shorty?sort=popular&page=1&xsubject=11&fcolor=0')
def parse_home_clothes():
    # ДОМАШНЯЯ ОДЕЖДА
    # Пижамы
    get_products.parse_page('Домашняя Одежда',
                           'https://www.wildberries.ru/catalog/0/search.aspx?search=Одежда%20для%20дома&page=1')
    # Тапочки
    get_products.parse_page('Домашняя Одежда',
                           'https://www.wildberries.ru/catalog/0/search.aspx?search=домашние%20тапочки%20женские&page=1')

def parse_jewelry():
    # УКРАШЕНИЯ
    # Бижутерия
    # Браслеты
    get_products.parse_page('Украшения',
                            'https://www.wildberries.ru/catalog/aksessuary/bizhuteriya/braslety?sort=popular&page=1&fkind=2')

    # Броши
    get_products.parse_page('Украшения',
                           'https://www.wildberries.ru/catalog/aksessuary/bizhuteriya/broshi?sort=popular&page=1&fkind=2')

    # Бусы
    get_products.parse_page('Украшения',
                            'https://www.wildberries.ru/catalog/aksessuary/bizhuteriya/busy?sort=popular&page=1&fkind=2')

    # Колье
    get_products.parse_page('Украшения',
                            'https://www.wildberries.ru/catalog/aksessuary/bizhuteriya/kole?sort=popular&page=1&fkind=2')

    # Кольца
    get_products.parse_page('Украшения',
                            'https://www.wildberries.ru/catalog/aksessuary/bizhuteriya/koltsa?sort=popular&page=1&fkind=2')

    # Комплекты
    get_products.parse_page('Украшения',
                            'https://www.wildberries.ru/catalog/aksessuary/bizhuteriya/komplekty?sort=popular&page=1&fkind=2')

    # Подвески
    get_products.parse_page('Украшения',
                            'https://www.wildberries.ru/catalog/aksessuary/bizhuteriya/podveski?sort=popular&page=1&fkind=2')

    # Серьги
    get_products.parse_page('Украшения',
                            'https://www.wildberries.ru/catalog/aksessuary/bizhuteriya/sergi?sort=popular&page=1&fkind=2')

    # Цепочки
    get_products.parse_page('Украшения',
                            'https://www.wildberries.ru/catalog/aksessuary/bizhuteriya/tsepochki')

    # Чокеры
    get_products.parse_page('Украшения',
                            'https://www.wildberries.ru/catalog/aksessuary/bizhuteriya/chokery?sort=popular&page=1&fkind=2')

    # Ювелирные украшения
    get_products.parse_page('Украшения',
                            'https://www.wildberries.ru/catalog/0/search.aspx?page=1&sort=popular&search=ювелирные+украшения&xsubject=202%3B24%3B203%3B452%3B299%3B300%3B206%3B54%3B207%3B205%3B2035%3B2679&priceU=6300%3B500000&fkind=2')


def parse_bag():
    for i in range(4):
        # СУМКА
        # Клатчи
        get_products.parse_page('Сумка',
                               'https://www.wildberries.ru/catalog/aksessuary/sumki-i-ryukzaki/klatchi?sort=popular&page=1&fkind=2')

        # СУМКА НЕ черная
        get_products.parse_page('Сумка',
                               'https://www.wildberries.ru/catalog/aksessuary/sumki-i-ryukzaki/sumki?sort=popular&page=1&xsubject=50&fcolor=16119260%3B16777215%3B11393254%3B16776960%3B32768%3B10824234%3B16711680%3B16761035%3B16753920%3B8421504%3B255%3B15631086&fkind=2')

        # СУМКА черная
        get_products.parse_page('Сумка',
                                'https://www.wildberries.ru/catalog/aksessuary/sumki-i-ryukzaki/sumki?sort=popular&page=1&xsubject=50&fcolor=0&fkind=2')

def parse_tshirts():
    # ФУТБОЛКА
    # Все цвета кроме белого и черного
    # Вечернее, праздничное
    get_products.parse_page('Футболка',
                           'https://www.wildberries.ru/catalog/zhenshchinam/odezhda/futbolki-i-topy?sort=popular&page=1&xsubject=192%3B219&fcolor=16119260%3B11393254%3B16776960%3B32768%3B10824234%3B16711680%3B16753920%3B16761035%3B8421504%3B255%3B15631086&f23796=31142%3B31137%3B31138%3B67470%3B31136')

    # Офис
    get_products.parse_page('Футболка',
                           'https://www.wildberries.ru/catalog/zhenshchinam/odezhda/futbolki-i-topy?sort=popular&page=1&xsubject=192%3B219&fcolor=16119260%3B11393254%3B16776960%3B32768%3B10824234%3B16711680%3B16753920%3B16761035%3B8421504%3B255%3B15631086&f23796=31140')

    # Повседневное
    get_products.parse_page('Футболка',
                           'https://www.wildberries.ru/catalog/zhenshchinam/odezhda/futbolki-i-topy?sort=popular&page=1&xsubject=192%3B219&fcolor=16119260%3B11393254%3B16776960%3B32768%3B10824234%3B16711680%3B16753920%3B16761035%3B8421504%3B255%3B15631086&f23796=31141')

    # ВСЕ категории, БЕЛОЕ И ЧЕРНОЕ
    get_products.parse_page('Футболка',
                           'https://www.wildberries.ru/catalog/zhenshchinam/odezhda/futbolki-i-topy?sort=popular&page=1&xsubject=192%3B219&fcolor=16777215%3B0')

def parse_shirts():
    for i in range(4):
        # РУБАШКИ
        get_products.parse_page('Рубашка',
                               'https://www.wildberries.ru/catalog/zhenshchinam/odezhda/bluzki-i-rubashki?sort=popular&page=1&xsubject=184')

def parse_blouse():
    for i in range(4):
        # БЛУЗКИ
        get_products.parse_page('Блузка',
                            'https://www.wildberries.ru/catalog/zhenshchinam/odezhda/bluzki-i-rubashki?sort=popular&page=1&xsubject=1429%3B41')

def parse_jeans():
    for i in range(4):
        # ДЖИНСЫ
        get_products.parse_page('Джинсы',
                               'https://www.wildberries.ru/catalog/zhenshchinam/odezhda/dzhinsy-dzhegginsy')

def parse_jacket():
    # ПИДАЖАК
    # Все цвета кроме черного
    # Вечерние
    get_products.parse_page('Пиджак',
                            'https://www.wildberries.ru/catalog/zhenshchinam/odezhda/pidzhaki-i-zhakety?sort=popular&page=1&fcolor=16119260%3B16777215%3B11393254%3B16776960%3B32768%3B10824234%3B16711680%3B16753920%3B16761035%3B8421504%3B255%3B15631086&f23796=31142%3B31137%3B31494%3B31136%3B67470')

    # Офис
    get_products.parse_page('Пиджак',
                            'https://www.wildberries.ru/catalog/zhenshchinam/odezhda/pidzhaki-i-zhakety?sort=popular&page=1&fcolor=16119260%3B16777215%3B11393254%3B16776960%3B32768%3B10824234%3B16711680%3B16753920%3B16761035%3B8421504%3B255%3B15631086&f23796=31140')

    # Повседневное
    get_products.parse_page('Пиджак',
                            'https://www.wildberries.ru/catalog/zhenshchinam/odezhda/pidzhaki-i-zhakety?sort=popular&page=1&fcolor=16119260%3B16777215%3B11393254%3B16776960%3B32768%3B10824234%3B16711680%3B16753920%3B16761035%3B8421504%3B255%3B15631086&f23796=31141')

    # ПИДАЖАК
    # ВСЕ категории, ЧЕРНЫЙ
    get_products.parse_page('Пиджак',
                            'https://www.wildberries.ru/catalog/zhenshchinam/odezhda/pidzhaki-i-zhakety?sort=popular&page=1&fcolor=0')

def parse_dress():
    #ЛЕТО (НУЖНО БУДЕТ ИЗМЕНИТЬ ССЫЛКИ)
    # # ПЛАТЬЕ
    # # Все цвета, кроме черного
    # # Вечерняя мода
    # get_products.parse_page('Платье',
    #                         'https://www.wildberries.ru/catalog/zhenshchinam/odezhda/platya?sort=popular&page=1&fcolor=16119260%3B16777215%3B11393254%3B16776960%3B32768%3B10824234%3B16711680%3B16753920%3B16761035%3B8421504%3B255%3B15631086&f23796=31142')
    #
    # # Выпускной, новый год, символ года
    # get_products.parse_page('Платье',
    #                         'https://www.wildberries.ru/catalog/zhenshchinam/odezhda/platya?sort=popular&page=1&fcolor=16119260%3B16777215%3B11393254%3B16776960%3B32768%3B10824234%3B16711680%3B16753920%3B16761035%3B8421504%3B255%3B15631086&f23796=31137%3B31138%3B67470')
    #
    # # Офис
    # get_products.parse_page('Платье',
    #                         'https://www.wildberries.ru/catalog/zhenshchinam/odezhda/platya?sort=popular&page=1&fcolor=16119260%3B16777215%3B11393254%3B16776960%3B32768%3B10824234%3B16711680%3B16753920%3B16761035%3B8421504%3B255%3B15631086&f23796=31140')
    #
    # # Повседневное
    # get_products.parse_page('Платье',
    #                         'https://www.wildberries.ru/catalog/zhenshchinam/odezhda/platya?sort=popular&page=1&fcolor=16119260%3B16777215%3B11393254%3B16776960%3B32768%3B10824234%3B16711680%3B16753920%3B16761035%3B8421504%3B255%3B15631086&f23796=31141')
    #
    # # Свадьба
    # get_products.parse_page('Платье',
    #                         'https://www.wildberries.ru/catalog/zhenshchinam/odezhda/platya?sort=popular&page=1&fcolor=16119260%3B16777215%3B11393254%3B16776960%3B32768%3B10824234%3B16711680%3B16753920%3B16761035%3B8421504%3B255%3B15631086&f23796=31136')
    #
    # # Все категории, ЧЕРНОЕ
    # get_products.parse_page('Платье',
    #                         'https://www.wildberries.ru/catalog/zhenshchinam/odezhda/platya?sort=popular&page=1&fcolor=0')


    #ОСЕНЬ
    # ПЛАТЬЕ
    # Все цвета, кроме черного
    # Вечерняя мода
    get_products.parse_page('Платье',
                            'https://www.wildberries.ru/catalog/0/search.aspx?page=1&sort=popular&search=Платье+женское+осень&xsubject=69&fcolor=16119260%3B16777215%3B11393254%3B16776960%3B32768%3B10824234%3B16711680%3B16753920%3B16761035%3B8421504%3B255%3B15631086&fkind=2&f23796=31142')

    # Выпускной, новый год, символ года
    get_products.parse_page('Платье',
                            'https://www.wildberries.ru/catalog/0/search.aspx?page=1&sort=popular&search=Платье+женское+осень&xsubject=69&fcolor=16119260%3B16777215%3B11393254%3B16776960%3B32768%3B10824234%3B16711680%3B16753920%3B16761035%3B8421504%3B255%3B15631086&fkind=2&f23796=31137%3B31138%3B67470')

    # Офис
    get_products.parse_page('Платье',
                            'https://www.wildberries.ru/catalog/0/search.aspx?page=1&sort=popular&search=Платье+женское+осень&xsubject=69&fcolor=16119260%3B16777215%3B11393254%3B16776960%3B32768%3B10824234%3B16711680%3B16753920%3B16761035%3B8421504%3B255%3B15631086&fkind=2&f23796=31140')

    # Повседневное
    get_products.parse_page('Платье',
                            'https://www.wildberries.ru/catalog/0/search.aspx?page=1&sort=popular&search=Платье+женское+осень&xsubject=69&fcolor=16119260%3B16777215%3B11393254%3B16776960%3B32768%3B10824234%3B16711680%3B16753920%3B16761035%3B8421504%3B255%3B15631086&fkind=2&f23796=31141')

    # Свадьба
    get_products.parse_page('Платье',
                            'https://www.wildberries.ru/catalog/0/search.aspx?page=1&sort=popular&search=Платье+женское+осень&xsubject=69&fcolor=16119260%3B16777215%3B11393254%3B16776960%3B32768%3B10824234%3B16711680%3B16753920%3B16761035%3B8421504%3B255%3B15631086&fkind=2&f23796=31136')

    # Все категории, ЧЕРНОЕ
    get_products.parse_page('Платье',
                            'https://www.wildberries.ru/catalog/0/search.aspx?page=1&sort=popular&search=Платье+женское+осень&xsubject=69&fcolor=0&fkind=2')

def parse_shoes():
    # ОБУВЬ
    # Ботильоны не ЧЕРНЫЕ
    get_products.parse_page('Обувь',
                            'https://www.wildberries.ru/catalog/obuv/zhenskaya/botinki-i-polubotinki?sort=popular&page=1&xsubject=343&fcolor=16119260%3B16777215%3B11393254%3B16776960%3B32768%3B10824234%3B16711680%3B16753920%3B16761035%3B8421504%3B255%3B15631086')

    # Ботильоны черные
    get_products.parse_page('Обувь',
                            'https://www.wildberries.ru/catalog/obuv/zhenskaya/botinki-i-polubotinki?sort=popular&page=1&xsubject=343&fcolor=0')

    # Полуботинки
    get_products.parse_page('Обувь',
                            'https://www.wildberries.ru/catalog/obuv/zhenskaya/botinki-i-polubotinki?sort=popular&page=1&xsubject=2956')

    # Ботинки не черные
    get_products.parse_page('Обувь',
                            'https://www.wildberries.ru/catalog/obuv/zhenskaya/botinki-i-polubotinki?sort=popular&page=1&xsubject=94&fcolor=16119260%3B16777215%3B11393254%3B16776960%3B32768%3B10824234%3B16711680%3B16761035%3B16753920%3B8421504%3B255%3B15631086')

    # Ботинки черные
    get_products.parse_page('Обувь',
                            'https://www.wildberries.ru/catalog/obuv/zhenskaya/botinki-i-polubotinki?sort=popular&page=1&xsubject=94&fcolor=0')


    # Кеды не белые и не черные
    get_products.parse_page('Обувь',
                            'https://www.wildberries.ru/catalog/obuv/zhenskaya/kedy-i-krossovki?sort=popular&page=1&xsubject=104&fcolor=16119260%3B11393254%3B16776960%3B32768%3B10824234%3B16711680%3B16753920%3B16761035%3B255%3B15631086%3B8421504')

    # Кроссовки не белые и не черные
    get_products.parse_page('Обувь',
                            'https://www.wildberries.ru/catalog/obuv/zhenskaya/kedy-i-krossovki?sort=popular&page=1&xsubject=105&fcolor=16119260%3B11393254%3B16776960%3B32768%3B10824234%3B16711680%3B16753920%3B16761035%3B255%3B15631086%3B8421504')

    # Слипоны
    get_products.parse_page('Обувь',
                            'https://www.wildberries.ru/catalog/obuv/zhenskaya/kedy-i-krossovki?sort=popular&page=1&xsubject=396')

    # Кроссовки черные и белые
    get_products.parse_page('Обувь',
                            'https://www.wildberries.ru/catalog/obuv/zhenskaya/kedy-i-krossovki?sort=popular&page=1&xsubject=105&fcolor=16777215%3B0')

    # Кеды белые и черные
    get_products.parse_page('Обувь',
                            'https://www.wildberries.ru/catalog/obuv/zhenskaya/kedy-i-krossovki?sort=popular&page=1&xsubject=104&fcolor=16777215%3B0')

    # Лоферы не ЧЕРНЫЕ
    get_products.parse_page('Обувь',
                            'https://www.wildberries.ru/catalog/obuv/zhenskaya/tufli-lofery?sort=popular&page=1&xsubject=1664&fcolor=16119260%3B16777215%3B11393254%3B16776960%3B32768%3B10824234%3B16711680%3B16753920%3B16761035%3B8421504%3B255%3B15631086')

    # Туфли не черные
    get_products.parse_page('Обувь',
                            'https://www.wildberries.ru/catalog/obuv/zhenskaya/tufli-lofery?sort=popular&page=1&xsubject=100&fcolor=16119260%3B16777215%3B11393254%3B16776960%3B32768%3B10824234%3B16711680%3B16753920%3B16761035%3B8421504%3B255%3B15631086')

    # Лоферы черные
    get_products.parse_page('Обувь',
                            'https://www.wildberries.ru/catalog/obuv/zhenskaya/tufli-lofery?sort=popular&page=1&xsubject=1664&fcolor=0')

    # Туфли черные
    get_products.parse_page('Обувь',
                            'https://www.wildberries.ru/catalog/obuv/zhenskaya/tufli-lofery?sort=popular&page=1&xsubject=100&fcolor=0')

def parse_top():
    # ТОП
    # Все цвета, кроме черного и белого
    # Вечерняя мода
    get_products.parse_page('Топ',
                            'https://www.wildberries.ru/catalog/zhenshchinam/odezhda/futbolki-i-topy?sort=popular&page=1&xsubject=185&fcolor=16119260%3B11393254%3B16776960%3B32768%3B10824234%3B16711680%3B16753920%3B16761035%3B8421504%3B255%3B15631086&f23796=31142')

    # Выпускной, свадьба, символ года, новый год
    get_products.parse_page('Топ',
                            'https://www.wildberries.ru/catalog/zhenshchinam/odezhda/futbolki-i-topy?sort=popular&page=1&xsubject=185&fcolor=16119260%3B11393254%3B16776960%3B32768%3B10824234%3B16711680%3B16753920%3B16761035%3B8421504%3B255%3B15631086&f23796=31137%3B31138%3B31136%3B67470')

    # Повседневное
    get_products.parse_page('Топ',
                            'https://www.wildberries.ru/catalog/zhenshchinam/odezhda/futbolki-i-topy?sort=popular&page=1&xsubject=185&fcolor=16119260%3B11393254%3B16776960%3B32768%3B10824234%3B16711680%3B16753920%3B16761035%3B8421504%3B255%3B15631086&f23796=31141')

    # Офис
    get_products.parse_page('Топ',
                            'https://www.wildberries.ru/catalog/zhenshchinam/odezhda/futbolki-i-topy?sort=popular&page=1&xsubject=185&fcolor=16119260%3B11393254%3B16776960%3B32768%3B10824234%3B16711680%3B16753920%3B16761035%3B8421504%3B255%3B15631086&f23796=31140')

    # Все категории, ЧЕРНОЕ И БЕЛОЕ
    get_products.parse_page('Топ',
                            'https://www.wildberries.ru/catalog/zhenshchinam/odezhda/futbolki-i-topy?sort=popular&page=1&xsubject=185&fcolor=16777215%3B0&f23796=31136%3B31137%3B31138%3B31140%3B31141%3B31142%3B67470')

def parse_skirt():
    # ЛЕТО
    # # ЮБКА
    # # Все цвета, кроме черного
    # # Вечернее
    # get_products.parse_page('Юбка',
    #                         'https://www.wildberries.ru/catalog/zhenshchinam/odezhda/yubki?sort=popular&page=1&fcolor=16119260%3B16777215%3B11393254%3B16776960%3B32768%3B10824234%3B16711680%3B16753920%3B16761035%3B8421504%3B255%3B15631086&f23796=31142%3B31137%3B31138%3B31136%3B67470')
    #
    # # Офис
    # get_products.parse_page('Юбка',
    #                         'https://www.wildberries.ru/catalog/zhenshchinam/odezhda/yubki?sort=popular&page=1&fcolor=16119260%3B16777215%3B11393254%3B16776960%3B32768%3B10824234%3B16711680%3B16753920%3B16761035%3B8421504%3B255%3B15631086&f23796=31140')
    #
    # # Повседневное
    # get_products.parse_page('Юбка',
    #                         'https://www.wildberries.ru/catalog/zhenshchinam/odezhda/yubki?sort=popular&page=1&fcolor=16119260%3B16777215%3B11393254%3B16776960%3B32768%3B10824234%3B16711680%3B16753920%3B16761035%3B8421504%3B255%3B15631086&f23796=31141')
    #
    # # Все категории, ЧЕРНОЕ
    # get_products.parse_page('Юбка',
    #                         'https://www.wildberries.ru/catalog/zhenshchinam/odezhda/yubki?sort=popular&page=1&fcolor=0')


    # ОСЕНЬ
    # ЮБКА
    # Все цвета, кроме черного
    # Вечернее
    get_products.parse_page('Юбка',
                            'https://www.wildberries.ru/catalog/0/search.aspx?page=1&sort=popular&search=Юбка+женская+осень&xsubject=38&fcolor=16119260%3B16777215%3B11393254%3B16776960%3B32768%3B10824234%3B16711680%3B16753920%3B16761035%3B8421504%3B255%3B15631086&fkind=2&f23796=31137%3B31142%3B31138%3B31136%3B67470')

    # Офис
    get_products.parse_page('Юбка',
                            'https://www.wildberries.ru/catalog/0/search.aspx?page=1&sort=popular&search=Юбка+женская+осень&xsubject=38&fcolor=16119260%3B16777215%3B11393254%3B16776960%3B32768%3B10824234%3B16711680%3B16753920%3B16761035%3B8421504%3B255%3B15631086&fkind=2&f23796=31140')

    # Повседневное
    get_products.parse_page('Юбка',
                            'https://www.wildberries.ru/catalog/0/search.aspx?page=1&sort=popular&search=Юбка+женская+осень&xsubject=38&fcolor=16119260%3B16777215%3B11393254%3B16776960%3B32768%3B10824234%3B16711680%3B16753920%3B16761035%3B8421504%3B255%3B15631086&fkind=2&f23796=31141')

    # Все категории, ЧЕРНОЕ
    get_products.parse_page('Юбка',
                            'https://www.wildberries.ru/catalog/0/search.aspx?page=1&sort=popular&search=Юбка+женская+осень&xsubject=38&fcolor=0&fkind=2')



    # ТВИДОВАЯ
    get_products.parse_page('Юбка',
                            'https://www.wildberries.ru/catalog/0/search.aspx?search=Юбка%20женская%20твидовая')

def parse_suit():
    # КОСТЮМ
    # КОСТЮМ, все цвета, кроме черного
    # Офис брючный
    get_products.parse_page('Костюм',
                            'https://www.wildberries.ru/catalog/0/search.aspx?search=%D0%96%D0%B5%D0%BD%D1%81%D0%BA%D0%B8%D0%B9%20%D0%B1%D1%80%D1%8E%D1%87%D0%BD%D1%8B%D0%B9%20%D0%BA%D0%BE%D1%81%D1%82%D1%8E%D0%BC%20%D0%BE%D1%84%D0%B8%D1%81')


    # Офис юбка
    get_products.parse_page('Костюм',
                            'https://www.wildberries.ru/catalog/0/search.aspx?search=%D0%96%D0%B5%D0%BD%D1%81%D0%BA%D0%B8%D0%B9%20%D1%8E%D0%B1%D0%BA%D0%B0%20%D0%BA%D0%BE%D1%81%D1%82%D1%8E%D0%BC%20%D0%BE%D1%84%D0%B8%D1%81')


    # Осень юбка
    get_products.parse_page('Костюм',
                            'https://www.wildberries.ru/catalog/0/search.aspx?search=%D0%96%D0%B5%D0%BD%D1%81%D0%BA%D0%B8%D0%B9%20%D1%8E%D0%B1%D0%BA%D0%B0%20%D0%BA%D0%BE%D1%81%D1%82%D1%8E%D0%BC%20%D0%BE%D1%81%D0%B5%D0%BD%D1%8C')

    # Осень брюки
    get_products.parse_page('Костюм',
                            'https://www.wildberries.ru/catalog/0/search.aspx?search=%D0%96%D0%B5%D0%BD%D1%81%D0%BA%D0%B8%D0%B9%20%D0%B1%D1%80%D1%8E%D0%BA%D0%B8%20%D0%BA%D0%BE%D1%81%D1%82%D1%8E%D0%BC%20%D0%BE%D1%81%D0%B5%D0%BD%D1%8C')

    # Твидовый
    get_products.parse_page('Костюм',
                            'https://www.wildberries.ru/catalog/0/search.aspx?search=%D0%96%D0%B5%D0%BD%D1%81%D0%BA%D0%B8%D0%B9%20%D0%BA%D0%BE%D1%81%D1%82%D1%8E%D0%BC%20%D1%82%D0%B2%D0%B8%D0%B4%D0%BE%D0%B2%D1%8B%D0%B9')

    # Твидовый брюки
    get_products.parse_page('Костюм',
                            'https://www.wildberries.ru/catalog/0/search.aspx?search=%D0%96%D0%B5%D0%BD%D1%81%D0%BA%D0%B8%D0%B9%20%D0%B1%D1%80%D1%8E%D0%BA%D0%B8%20%D0%BA%D0%BE%D1%81%D1%82%D1%8E%D0%BC%20%D1%82%D0%B2%D0%B8%D0%B4%D0%BE%D0%B2%D1%8B%D0%B9')

def parse_corset():
        # КОРСЕТ
        # НЕ черный
        get_products.parse_page('Корсет',
                               'https://www.wildberries.ru/catalog/0/search.aspx?page=1&sort=popular&search=%D0%9A%D0%BE%D1%80%D1%81%D0%B5%D1%82+%D0%B6%D0%B5%D0%BD%D1%81%D0%BA%D0%B8%D0%B9&xsubject=74&fcolor=15631086%3B255%3B8421504%3B16761035%3B16753920%3B16711680%3B10824234%3B32768%3B16776960%3B11393254%3B16777215%3B16119260')

        # Черный
        get_products.parse_page('Корсет',
                               'https://www.wildberries.ru/catalog/0/search.aspx?page=1&sort=popular&search=%D0%9A%D0%BE%D1%80%D1%81%D0%B5%D1%82+%D0%B6%D0%B5%D0%BD%D1%81%D0%BA%D0%B8%D0%B9&xsubject=74&fcolor=0')

def parse_accessories():
    # АКСЕССУАРЫ
    # Для волос
    get_products.parse_page('Аксессуары',
                            'https://www.wildberries.ru/catalog/aksessuary/aksessuary-dlya-volos?sort=popular&page=1&xsubject=383%3B8515%3B1683%3B404%3B1856%3B1854%3B1860%3B1853%3B324%3B2842')
    # Галстуки, бабочки
    get_products.parse_page('Аксессуары',
                            'https://www.wildberries.ru/catalog/aksessuary/galstuki-i-babochki?sort=popular&page=1&xsubject=62%3B454')

    # Бейсболка
    get_products.parse_page('Аксессуары',
                            'https://www.wildberries.ru/catalog/aksessuary/golovnye-ubory?sort=popular&page=1&xsubject=84&fkind=2')

    # Кепи, фуражка, берет
    get_products.parse_page('Аксессуары',
                            'https://www.wildberries.ru/catalog/aksessuary/golovnye-ubory?sort=popular&page=1&xsubject=2150%3B83%3B2460&fkind=2')

    # Повязка на голову
    get_products.parse_page('Аксессуары',
                            'https://www.wildberries.ru/catalog/aksessuary/golovnye-ubory?sort=popular&page=1&xsubject=256&fkind=2')

    # Воротник
    get_products.parse_page('Аксессуары',
                            'https://www.wildberries.ru/catalog/aksessuary/platki-i-sharfy?sort=popular&page=1&xsubject=431')

    # Палантин
    get_products.parse_page('Аксессуары',
                            'https://www.wildberries.ru/catalog/aksessuary/platki-i-sharfy?sort=popular&page=1&xsubject=58')

    # Платок
    get_products.parse_page('Аксессуары',
                            'https://www.wildberries.ru/catalog/aksessuary/platki-i-sharfy?sort=popular&page=1&xsubject=56')

    # Ремень
    get_products.parse_page('Аксессуары',
                            'https://www.wildberries.ru/catalog/aksessuary/remni-i-poyasa?sort=popular&page=1&xsubject=51&fkind=2')

    # Часы
    get_products.parse_page('Аксессуары',
                            'https://www.wildberries.ru/catalog/aksessuary/chasy-i-remeshki?sort=popular&page=1&xsubject=60&fkind=2')

    # Платок
    get_products.parse_page('Аксессуары',
                            'https://www.wildberries.ru/catalog/aksessuary/platki-i-sharfy?sort=popular&page=1&xsubject=56')

def parse_shorts():
    #ШОРТЫ ОСЕНЬ
    # Не черные офис
    get_products.parse_page('Шорты',
                            'https://www.wildberries.ru/catalog/0/search.aspx?page=1&sort=popular&search=%D0%96%D0%B5%D0%BD%D1%81%D0%BA%D0%B8%D0%B5+%D1%88%D0%BE%D1%80%D1%82%D1%8B+%D0%BE%D1%81%D0%B5%D0%BD%D1%8C+%D0%BE%D1%84%D0%B8%D1%81&fcolor=16119260%3B16777215%3B11393254%3B16776960%3B32768%3B10824234%3B16711680%3B16753920%3B16761035%3B8421504%3B255%3B15631086')

    # Черные офис
    get_products.parse_page('Шорты',
                            'https://www.wildberries.ru/catalog/0/search.aspx?page=1&sort=popular&search=%D0%96%D0%B5%D0%BD%D1%81%D0%BA%D0%B8%D0%B5+%D1%88%D0%BE%D1%80%D1%82%D1%8B+%D0%BE%D1%81%D0%B5%D0%BD%D1%8C+%D0%BE%D1%84%D0%B8%D1%81&fcolor=0')

def parse_kofta():
    # Водолазка не черная
     get_products.parse_page('Кофта',
                           'https://www.wildberries.ru/catalog/zhenshchinam/odezhda/dzhempery-i-kardigany?sort=popular&page=1&xsubject=153&fcolor=16119260%3B16777215%3B11393254%3B16776960%3B32768%3B10824234%3B16711680%3B16753920%3B16761035%3B8421504%3B255%3B15631086')

    # Водолазка черная
     get_products.parse_page('Кофта',
                           'https://www.wildberries.ru/catalog/zhenshchinam/odezhda/dzhempery-i-kardigany?sort=popular&page=1&xsubject=153&fcolor=0')

    # Джемпер
     get_products.parse_page('Кофта',
                           'https://www.wildberries.ru/catalog/zhenshchinam/odezhda/dzhempery-i-kardigany?sort=popular&page=1&xsubject=215')

    # Кардиган
     get_products.parse_page('Кофта',
                           'https://www.wildberries.ru/catalog/zhenshchinam/odezhda/dzhempery-i-kardigany?sort=popular&page=1&xsubject=191')

    # Кофта
     get_products.parse_page('Кофта',
                           'https://www.wildberries.ru/catalog/zhenshchinam/odezhda/dzhempery-i-kardigany?sort=popular&page=1&xsubject=161')

    # Пуловер
     get_products.parse_page('Кофта',
                           'https://www.wildberries.ru/catalog/zhenshchinam/odezhda/dzhempery-i-kardigany?sort=popular&page=1&xsubject=160')

    # Свитер
     get_products.parse_page('Кофта',
                           'https://www.wildberries.ru/catalog/zhenshchinam/odezhda/dzhempery-i-kardigany?sort=popular&page=1&xsubject=163')

    # Лонгслив черный
     get_products.parse_page('Кофта',
                           'https://www.wildberries.ru/catalog/zhenshchinam/odezhda/longslivy?sort=popular&page=1&fcolor=0')

    # Лонгслив не черный
     get_products.parse_page('Кофта',
                           'https://www.wildberries.ru/catalog/zhenshchinam/odezhda/longslivy?sort=popular&page=1&fcolor=15631086%3B255%3B8421504%3B16761035%3B16753920%3B16711680%3B10824234%3B32768%3B16776960%3B11393254%3B16777215%3B16119260')

    # Свитшот
     get_products.parse_page('Кофта',
                           'https://www.wildberries.ru/catalog/zhenshchinam/odezhda/tolstovki?sort=popular&page=1&xsubject=159')

    # Толстовка
     get_products.parse_page('Кофта',
                           'https://www.wildberries.ru/catalog/zhenshchinam/odezhda/tolstovki?sort=popular&page=1&xsubject=233')

    # Худи
     get_products.parse_page('Кофта',
                           'https://www.wildberries.ru/catalog/zhenshchinam/odezhda/tolstovki?sort=popular&page=1&xsubject=1724')

    # Боди черное
     get_products.parse_page('Кофта',
                           'https://www.wildberries.ru/catalog/0/search.aspx?page=1&sort=popular&search=%D0%B6%D0%B5%D0%BD%D1%81%D0%BA%D0%BE%D0%B5+%D0%B1%D0%BE%D0%B4%D0%B8&fcolor=0')

    # Боди не черное
     get_products.parse_page('Кофта',
                           'https://www.wildberries.ru/catalog/0/search.aspx?page=1&sort=popular&search=%D0%B6%D0%B5%D0%BD%D1%81%D0%BA%D0%BE%D0%B5+%D0%B1%D0%BE%D0%B4%D0%B8&fcolor=15631086%3B255%3B8421504%3B16761035%3B16753920%3B16711680%3B10824234%3B32768%3B16776960%3B11393254%3B16777215%3B16119260')

def parse_outer_wear():
    # ОСЕНЬ
    # ВЕРХНЯЯ ОДЕЖДА
    # Бомберы Не черные
    get_products.parse_page('Верхняя Одежда',
                                'https://www.wildberries.ru/catalog/zhenshchinam/odezhda/verhnyaya-odezhda?sort=popular&page=1&xsubject=1635&fcolor=16777215%3B11393254%3B16776960%3B32768%3B10824234%3B16711680%3B16753920%3B16761035%3B8421504%3B255%3B15631086%3B16119260')

    # Бомберы черные
    get_products.parse_page('Верхняя Одежда',
                            'https://www.wildberries.ru/catalog/zhenshchinam/odezhda/verhnyaya-odezhda?sort=popular&page=1&xsubject=1635&fcolor=0')

    # Ветровка
    get_products.parse_page('Верхняя Одежда',
                            'https://www.wildberries.ru/catalog/zhenshchinam/odezhda/verhnyaya-odezhda?sort=popular&page=1&xsubject=172')

    # Дубленка
    get_products.parse_page('Верхняя Одежда',
                            'https://www.wildberries.ru/catalog/zhenshchinam/odezhda/verhnyaya-odezhda?sort=popular&page=1&xsubject=322')

    # Косуха Не черная
    get_products.parse_page('Верхняя Одежда',
                            'https://www.wildberries.ru/catalog/zhenshchinam/odezhda/verhnyaya-odezhda?sort=popular&page=1&xsubject=2110&fcolor=16119260%3B16777215%3B11393254%3B16776960%3B32768%3B10824234%3B16711680%3B16753920%3B16761035%3B255%3B15631086%3B8421504')

    # Косуха черная
    get_products.parse_page('Верхняя Одежда',
                            'https://www.wildberries.ru/catalog/zhenshchinam/odezhda/verhnyaya-odezhda?sort=popular&page=1&xsubject=2110&fcolor=0')

    # Куртка не черная демисезон
    get_products.parse_page('Верхняя Одежда',
                            'https://www.wildberries.ru/catalog/zhenshchinam/odezhda/verhnyaya-odezhda?sort=popular&page=1&xsubject=168&fcolor=16119260%3B16777215%3B11393254%3B16776960%3B32768%3B10824234%3B16711680%3B16753920%3B16761035%3B8421504%3B255%3B15631086&fseason=50')

    # Куртка черная демисезон
    get_products.parse_page('Верхняя Одежда',
                            'https://www.wildberries.ru/catalog/zhenshchinam/odezhda/verhnyaya-odezhda?sort=popular&page=1&xsubject=168&fcolor=0&fseason=50')

    # Пальто не черное
    get_products.parse_page('Верхняя Одежда',
                            'https://www.wildberries.ru/catalog/zhenshchinam/odezhda/verhnyaya-odezhda?sort=popular&page=1&xsubject=170&fcolor=16777215%3B11393254%3B16776960%3B32768%3B10824234%3B16711680%3B16753920%3B16761035%3B8421504%3B255%3B15631086%3B16119260')

    # Пальто черное
    get_products.parse_page('Верхняя Одежда',
                            'https://www.wildberries.ru/catalog/zhenshchinam/odezhda/verhnyaya-odezhda?sort=popular&page=1&xsubject=170&fcolor=0')

    # Плащ не черный
    get_products.parse_page('Верхняя Одежда',
                            'https://www.wildberries.ru/catalog/zhenshchinam/odezhda/verhnyaya-odezhda?sort=popular&page=1&xsubject=171&fcolor=16119260%3B16777215%3B11393254%3B16776960%3B32768%3B10824234%3B16711680%3B16753920%3B16761035%3B8421504%3B255%3B15631086')

    # Плащ черный
    get_products.parse_page('Верхняя Одежда',
                            'https://www.wildberries.ru/catalog/zhenshchinam/odezhda/verhnyaya-odezhda?sort=popular&page=1&xsubject=171&fcolor=0')

    # Полупальто
    get_products.parse_page('Верхняя Одежда',
                            'https://www.wildberries.ru/catalog/zhenshchinam/odezhda/verhnyaya-odezhda?sort=popular&page=1&xsubject=1641')
    # Тренч
    get_products.parse_page('Верхняя Одежда',
                            'https://www.wildberries.ru/catalog/zhenshchinam/odezhda/verhnyaya-odezhda?sort=popular&page=1&xsubject=193')


if __name__ == "__main__":
    parse_trousers()
    parse_home_clothes()
    # parse_jewelry()
    # parse_bag()
    parse_tshirts()
    parse_shirts()
    parse_jeans()
    parse_jacket()
    # parse_dress()
    # parse_top()
    # parse_skirt()
    # parse_suit()
    # parse_corset()
    # parse_accessories()
    parse_blouse()
    parse_shorts()
    # parse_kofta()
    # parse_outer_wear()
    # parse_shoes()
