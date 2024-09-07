from parser_ozon import get_products

def parse_trousers():
    # БРЮКИ
    # Все цвета, кроме черного
    # Повседневный
    get_products.parse_page('Брюки',
                           'https://www.ozon.ru/category/bryuki-zhenskie-7512/?color=100955528%2C100955546%2C100955530%2C100955529%2C100955540%2C100955527%2C100966307%2C100955534%2C100955532%2C100955535%2C100966310%2C100955536%2C100955537%2C100955542%2C100955544%2C100955545%2C101097990%2C100955541%2C100955547&opened=styleapparel%2Ccolor%2Ctype&styleapparel=55228&type=37300')

    # Офис
    get_products.parse_page('Брюки',
                           'https://www.ozon.ru/category/bryuki-zhenskie-7512/?color=100955528%2C100955546%2C100955530%2C100955529%2C100955540%2C100955527%2C100966307%2C100955534%2C100955532%2C100955535%2C100966310%2C100955536%2C100955537%2C100955542%2C100955544%2C100955545%2C101097990%2C100955541%2C100955547&opened=type%2Cstyleapparel%2Ccolor&styleapparel=58692&type=37300')

    # Вечерний
    get_products.parse_page('Брюки',
                           'https://www.ozon.ru/category/bryuki-zhenskie-7512/?color=100955528%2C100955546%2C100955530%2C100955529%2C100955540%2C100955527%2C100966307%2C100955534%2C100955532%2C100955535%2C100966310%2C100955536%2C100955537%2C100955542%2C100955544%2C100955545%2C101097990%2C100955541%2C100955547&opened=type%2Cstyleapparel%2Ccolor&styleapparel=57396&type=37300')

    # Спортивный
    get_products.parse_page('Брюки',
                           'https://www.ozon.ru/category/bryuki-zhenskie-7512/?color=100955528%2C100955546%2C100955530%2C100955529%2C100955540%2C100955527%2C100966307%2C100955534%2C100955532%2C100955535%2C100966310%2C100955536%2C100955537%2C100955542%2C100955544%2C100955545%2C101097990%2C100955541%2C100955547&opened=color%2Ctype%2Cstyleapparel&styleapparel=55224&type=37300')

    # ВСЕ категории, ЧЕРНЫЕ
    get_products.parse_page('Брюки',
                           'https://www.ozon.ru/category/bryuki-zhenskie-7512/?color=100955526&opened=styleapparel%2Ccolor%2Ctype&type=37300')

def parse_home_clothes():
    # ДОМАШНЯЯ ОДЕЖДА
    # Пижамы
    get_products.parse_page('Домашняя Одежда',
                           'https://www.ozon.ru/category/domashnyaya-odezhda-zhenskaya-7541/')

    # Тапочки
    get_products.parse_page('Домашняя Одежда',
                           'https://www.ozon.ru/category/tapochki-zhenskie-7655/')

def parse_jewelry():
    # УКРАШЕНИЯ
    # Ювелирные
    get_products.parse_page('Украшения',
                            'https://www.ozon.ru/category/yuvelirnye-ukrasheniya-50001/?category_was_predicted=true&currency_price=139.000%3B4000.000&deny_category_prediction=true&from_global=true&text=ювелирные+украшения')

    # Браслеты
    get_products.parse_page('Украшения',
                           'https://www.ozon.ru/category/braslety-bizhuternye-zhenskie-17031/')

    # Броши и значки
    get_products.parse_page('Украшения',
                            'https://www.ozon.ru/category/broshi-bizhuternye-zhenskie-17034/')

    # Колье и бусы
    get_products.parse_page('Украшения',
                            'https://www.ozon.ru/category/kole-i-ozherelya-bizhuternye-zhenskie-17027/')

    # Кольца
    get_products.parse_page('Украшения',
                            'https://www.ozon.ru/category/koltsa-bizhuternye-zhenskie-17023/')

    # Комплекты
    get_products.parse_page('Украшения',
                            'https://www.ozon.ru/category/komplekty-bizhuternyh-ukrasheniy-zhenskie-17032/')

    # Подвески и кулоны
    get_products.parse_page('Украшения',
                            'https://www.ozon.ru/category/podveski-i-kulony-bizhuternye-zhenskie-17029/')

    # Серьги
    get_products.parse_page('Украшения',
                            'https://www.ozon.ru/category/sergi-bizhuternye-17024/')

    # Цепочки
    get_products.parse_page('Украшения',
                            'https://www.ozon.ru/category/tsepochki-bizhuternye-zhenskie-17030/')

def parse_bag():
    for i in range(4):
        # СУМКА
        # Клатчи
        get_products.parse_page('Сумка',
                               'https://www.ozon.ru/category/klatchi-zhenskie-17007/')

        # СУМКА ЧЕРНАЯ
        get_products.parse_page('Сумка',
                               'https://www.ozon.ru/category/sumki-na-plecho-zhenskie-17002/?color=100955526')

        # СУМКА НЕ черная
        get_products.parse_page('Сумка',
                               'https://www.ozon.ru/category/sumki-na-plecho-zhenskie-17002/?color=100955546%2C100955529%2C100955527%2C100955528%2C100955540%2C100955534%2C100955530%2C100955547%2C100955535%2C100955542%2C100955532%2C100966310%2C100955537%2C100955536%2C100966307%2C100955544%2C100955545%2C100955541%2C101097990&opened=color')

def parse_tshirts():
    # ФУТБОЛКА
    # Все цвета, кроме черного
    # Повседневный
    get_products.parse_page('Футболка',
                           'https://www.ozon.ru/category/futbolki-i-topy-zhenskie-7505/?color=100955527%2C100955528%2C100955530%2C100955534%2C100955540%2C100955546%2C100966310%2C100955544%2C100955532%2C100955529%2C100955535%2C100955537%2C100955536%2C100955542%2C100955545%2C100966307%2C100955541%2C101097990%2C100955547&opened=styleapparel%2Ccolor%2Ctype&styleapparel=55228&type=37283%2C55242')

    # Спортивный
    get_products.parse_page('Футболка',
                            'https://www.ozon.ru/category/futbolki-i-topy-zhenskie-7505/?color=100955527%2C100955528%2C100955530%2C100955534%2C100955540%2C100955546%2C100966310%2C100955544%2C100955532%2C100955529%2C100955535%2C100955537%2C100955536%2C100955542%2C100955545%2C100966307%2C100955541%2C101097990%2C100955547&opened=styleapparel%2Ccolor%2Ctype&styleapparel=55224&type=37283%2C55242')

    # Офисный
    get_products.parse_page('Футболка',
                            'https://www.ozon.ru/category/futbolki-i-topy-zhenskie-7505/?color=100955527%2C100955528%2C100955530%2C100955534%2C100955540%2C100955546%2C100966310%2C100955544%2C100955532%2C100955529%2C100955535%2C100955537%2C100955536%2C100955542%2C100955545%2C100966307%2C100955541%2C101097990%2C100955547&opened=color%2Ctype%2Cstyleapparel&styleapparel=58692&type=37283%2C55242')

    # Вечерний, свадебный
    get_products.parse_page('Футболка',
                            'https://www.ozon.ru/category/futbolki-i-topy-zhenskie-7505/?color=100955527%2C100955528%2C100955530%2C100955534%2C100955540%2C100955546%2C100966310%2C100955544%2C100955532%2C100955529%2C100955535%2C100955537%2C100955536%2C100955542%2C100955545%2C100966307%2C100955541%2C101097990%2C100955547&opened=styleapparel%2Ccolor%2Ctype&styleapparel=79761%2C57396&type=37283%2C55242')

    # ВСЕ категории, ЧЕРНЫЙ
    get_products.parse_page('Футболка',
                            'https://www.ozon.ru/category/futbolki-i-topy-zhenskie-7505/?color=100955526&opened=type%2Cstyleapparel%2Ccolor&type=37283%2C55242')


def parse_shirts():
    for i in range(4):
        # РУБАШКА
        get_products.parse_page('Рубашка',
                               'https://www.ozon.ru/category/bluzy-i-rubashki-zhenskie-7511/?type=37307')

def parse_blouse():
    for i in range(4):
        get_products.parse_page('Блузка',
                                'https://www.ozon.ru/category/bluzy-i-rubashki-zhenskie-7511/?type=101121374%2C39030')

def parse_jeans():
    for i in range(4):
        # ДЖИНСЫ
        get_products.parse_page('Джинсы',
                               'https://www.ozon.ru/category/dzhinsy-zhenskie-7503/')

def parse_jacket():
    # ПИДАЖАК
    # ВСЕ цвета, кроме черного
    # Повседневный
    get_products.parse_page('Пиджак',
                            'https://www.ozon.ru/category/zhakety-i-zhilety-zhenskie-7535/?color=100955546%2C100955530%2C100955528%2C100955540%2C100955529%2C100955534%2C100955547%2C100966307%2C100955535%2C100955532%2C100955536%2C100955537%2C100966310%2C100955542%2C100955544%2C100955545%2C101097990%2C100955541%2C100955527&opened=color%2Cstyleapparel&styleapparel=55228')

    # Офис
    get_products.parse_page('Пиджак',
                            'https://www.ozon.ru/category/zhakety-i-zhilety-zhenskie-7535/?color=100955546%2C100955530%2C100955528%2C100955540%2C100955529%2C100955534%2C100955547%2C100966307%2C100955535%2C100955532%2C100955536%2C100955537%2C100966310%2C100955542%2C100955544%2C100955545%2C101097990%2C100955541%2C100955527&opened=color%2Cstyleapparel&styleapparel=58692')

    # Вечерний
    get_products.parse_page('Пиджак',
                            'https://www.ozon.ru/category/zhakety-i-zhilety-zhenskie-7535/?color=100955546%2C100955530%2C100955528%2C100955540%2C100955529%2C100955534%2C100955547%2C100966307%2C100955535%2C100955532%2C100955536%2C100955537%2C100966310%2C100955542%2C100955544%2C100955545%2C101097990%2C100955541%2C100955527&opened=color%2Cstyleapparel&styleapparel=57396')

    # Все категории, ЧЕРНЫЙ
    get_products.parse_page('Пиджак',
                            'https://www.ozon.ru/category/zhakety-i-zhilety-zhenskie-7535/?color=100955526')

def parse_dress():
    # ЛЕТО (НУЖНО МЕНЯТЬ)
    # # ПЛАТЬЕ
    # # Все цвета, кроме черного
    # # Бохо и восточный
    # get_products.parse_page('Платье',
    #                         'https://www.ozon.ru/category/platya-zhenskie-7502/?category_was_predicted=true&color=100955530%2C100955540%2C100955527%2C100955534%2C100955535%2C100955528%2C100955546%2C100955532%2C100955547%2C100955537%2C100955536%2C100955529%2C100966307%2C100966310%2C100955542%2C100955545%2C100955544%2C100955541%2C101097990&deny_category_prediction=true&from_global=true&opened=color%2Cmodelclothing%2Cstyleapparel&styleapparel=100374527%2C277449&text=женское+платье')
    #
    # # Офис, классический, вечерний
    # get_products.parse_page('Платье',
    #                         'https://www.ozon.ru/category/platya-zhenskie-7502/?category_was_predicted=true&color=100955530%2C100955540%2C100955527%2C100955534%2C100955535%2C100955528%2C100955546%2C100955532%2C100955547%2C100955537%2C100955536%2C100955529%2C100966307%2C100966310%2C100955542%2C100955545%2C100955544%2C100955541%2C101097990&deny_category_prediction=true&from_global=true&opened=modelclothing%2Cstyleapparel%2Ccolor&styleapparel=55225%2C148380%2C57396&text=женское+платье')
    #
    # # Винтаж
    # get_products.parse_page('Платье',
    #                         'https://www.ozon.ru/category/platya-zhenskie-7502/?category_was_predicted=true&color=100955530%2C100955540%2C100955527%2C100955534%2C100955535%2C100955528%2C100955546%2C100955532%2C100955547%2C100955537%2C100955536%2C100955529%2C100966307%2C100966310%2C100955542%2C100955545%2C100955544%2C100955541%2C101097990&deny_category_prediction=true&from_global=true&opened=color%2Cmodelclothing%2Cstyleapparel&styleapparel=56425&text=женское+платье')
    #
    # # Коктейльное, Выпускное, свадебное, праздничное
    # get_products.parse_page('Платье',
    #                         'https://www.ozon.ru/category/platya-zhenskie-7502/?category_was_predicted=true&color=100955530%2C100955540%2C100955527%2C100955534%2C100955535%2C100955528%2C100955546%2C100955532%2C100955547%2C100955537%2C100955536%2C100955529%2C100966307%2C100966310%2C100955542%2C100955545%2C100955544%2C100955541%2C101097990&deny_category_prediction=true&from_global=true&opened=styleapparel%2Ccolor%2Cmodelclothing&styleapparel=106037%2C79761%2C101124545%2C164217&text=женское+платье')
    #
    # # Все категории, ЧЕРНОЕ
    # get_products.parse_page('Платье',
    #                         'https://www.ozon.ru/category/platya-zhenskie-7502/?category_was_predicted=true&color=100955526&deny_category_prediction=true&from_global=true&text=женское+платье')
    #


    # ОСЕНЬ
    # ПЛАТЬЕ
    # Все цвета, кроме черного, все кроме лета
    # Вечернее, праздничный, свадебный, выпускной
    get_products.parse_page('Платье',
                            'https://www.ozon.ru/category/platya-zhenskie-7502/?color=100955530%2C100955546%2C100955540%2C100955527%2C100955528%2C100955534%2C100955529%2C100955535%2C100955532%2C100966310%2C100966307%2C100955537%2C100955536%2C100955542%2C100955544%2C100955545%2C101097990%2C100955541%2C100955547&opened=styleapparel%2Ccolor&season=33889%2C31827%2C82950%2C33890&styleapparel=57396%2C106037%2C101124545%2C79761')

    # Офис, классический
    get_products.parse_page('Платье',
                            'https://www.ozon.ru/category/platya-zhenskie-7502/?color=100955530%2C100955546%2C100955540%2C100955527%2C100955528%2C100955534%2C100955529%2C100955535%2C100955532%2C100966310%2C100966307%2C100955537%2C100955536%2C100955542%2C100955544%2C100955545%2C101097990%2C100955541%2C100955547&opened=color%2Cstyleapparel&season=33889%2C31827%2C82950%2C33890&styleapparel=148380%2C58692')

    # Повседневное
    get_products.parse_page('Платье',
                            'https://www.ozon.ru/category/platya-zhenskie-7502/?color=100955530%2C100955546%2C100955540%2C100955527%2C100955528%2C100955534%2C100955529%2C100955535%2C100955532%2C100966310%2C100966307%2C100955537%2C100955536%2C100955542%2C100955544%2C100955545%2C101097990%2C100955541%2C100955547&opened=styleapparel%2Ccolor&season=33889%2C31827%2C82950%2C33890&styleapparel=55228')

    # Все категории, ЧЕРНОЕ
    get_products.parse_page('Платье',
                            'https://www.ozon.ru/category/platya-zhenskie-7502/?color=100955526&opened=styleapparel%2Ccolor&season=33889%2C31827%2C82950%2C33890')

    # Все цвета, кроме черного, зима, демисезон
    get_products.parse_page('Платье',
                            'https://www.ozon.ru/category/platya-zhenskie-7502/?color=100955530%2C100955546%2C100955540%2C100955528%2C100955527%2C100955529%2C100955534%2C100955547%2C100955535%2C100955532%2C100966307%2C100966310%2C100955537%2C100955536%2C100955542%2C100955545%2C100955544%2C101097990&opened=color%2Cstyleapparel&season=31827%2C33889')

    # Все категории, ЧЕРНЫЙ, зима, демисезон
    get_products.parse_page('Платье',
                            'https://www.ozon.ru/category/platya-zhenskie-7502/?color=100955526&opened=styleapparel%2Ccolor&season=31827%2C33889')


def parse_shoes():
    # ОБУВЬ

    # ВСЕСЕЗОННОЕ
    # Кроссовки, БЕЛЫЕ и ЧЕРНЫЕ
    get_products.parse_page('Обувь',
                            'https://www.ozon.ru/category/krossovki-i-kedy-zhenskie-36484/?color=100955527%2C100955526&type=31863')

    # Кеды, БЕЛЫЕ и ЧЕРНЫЕ
    get_products.parse_page('Обувь',
                            'https://www.ozon.ru/category/krossovki-i-kedy-zhenskie-36484/?color=100955527%2C100955526&type=31953')

    # Кроссовки, кроме белых и черных
    get_products.parse_page('Обувь',
                            'https://www.ozon.ru/category/krossovki-i-kedy-zhenskie-36484/?color=100955546%2C100955528%2C100955530%2C100955540%2C100955534%2C100955529%2C100955547%2C100955535%2C100955536%2C100955532%2C100955537%2C100955542%2C100955544%2C100966307%2C100966310%2C100955545%2C100955541%2C101097990&opened=color&type=31863')

    # Кеды, кроме белых и черных
    get_products.parse_page('Обувь',
                            'https://www.ozon.ru/category/krossovki-i-kedy-zhenskie-36484/?color=100955546%2C100955528%2C100955530%2C100955540%2C100955534%2C100955529%2C100955547%2C100955535%2C100955536%2C100955532%2C100955537%2C100955542%2C100955544%2C100966307%2C100966310%2C100955545%2C100955541%2C101097990&opened=color&type=31953')

    # Туфли, ЧЕРНЫЕ
    get_products.parse_page('Обувь',
                            'https://www.ozon.ru/category/tufli-zhenskie-7644/?color=100955526&type=31864')

    # Туфли НЕ черные
    get_products.parse_page('Обувь',
                            'https://www.ozon.ru/category/tufli-zhenskie-7644/?color=100955546%2C100955529%2C100955527%2C100955528%2C100955540%2C100955530%2C100955534%2C100955547%2C100966307%2C100955535%2C100955536%2C100955537%2C100966310%2C100955532%2C100955544%2C100955545%2C100955542%2C100955541%2C101097990&opened=color&type=31864')

    # Лоферы, ЧЕРНЫЕ
    get_products.parse_page('Обувь',
                            'https://www.ozon.ru/category/tufli-zhenskie-7644/?color=100955526&type=38756')

    # Лоферы НЕ черные
    get_products.parse_page('Обувь',
                            'https://www.ozon.ru/category/tufli-zhenskie-7644/?color=100955546%2C100955527%2C100955529%2C100955534%2C100955530%2C100955540%2C100955528%2C100955535%2C100955544%2C100955537%2C100966307%2C100955536%2C100955547%2C100955545%2C100955532%2C100966310%2C100955542%2C101097990%2C100955541&opened=color&type=38756')


    # # ЛЕТО (НАДО МЕНЯТЬ)
    # # Босоножки и сандалии ЧЕРНЫЕ
    # get_products.parse_page('Обувь',
    #                         'https://www.ozon.ru/category/bosonozhki-zhenskie-7645/?category_was_predicted=true&color=100955526&deny_category_prediction=true&from_global=true&opened=color&text=Женская+обувь')
    #
    # # Босоножки и сандалии ВСЕ ЦВЕТА
    # get_products.parse_page('Обувь',
    #                         'https://www.ozon.ru/category/bosonozhki-zhenskie-7645/?category_was_predicted=true&color=100955527%2C100955546%2C100955529%2C100955534%2C100955530%2C100955535%2C100955540%2C100955528%2C100955537%2C100955544%2C100966307%2C100955536%2C100955542%2C100955532%2C100955547%2C100966310%2C100955541%2C101097990%2C100955545&deny_category_prediction=true&from_global=true&opened=color&text=Женская+обувь')

    # ЛЕТО + ОСЕНЬ
    # Слипоны
    get_products.parse_page('Обувь',
                            'https://www.ozon.ru/category/krossovki-i-kedy-zhenskie-36484/?type=56542')
    # Мюли
    get_products.parse_page('Обувь',
                            'https://www.ozon.ru/category/sabo-i-myuli-zhenskie-7646/?type=151532')

    # Сабо
    get_products.parse_page('Обувь',
                            'https://www.ozon.ru/category/sabo-i-myuli-zhenskie-7646/?type=32107')

    # Балетки
    get_products.parse_page('Обувь',
                            'https://www.ozon.ru/category/tufli-zhenskie-7644/?type=31975')

    # ОСЕНЬ
    # Полуботинки
    get_products.parse_page('Обувь',
                            'https://www.ozon.ru/category/botinki-zhenskie-7651/?type=31939')

    # ОСЕНЬ + ЗИМА
    # Ботинки ЧЕРНЫЕ
    get_products.parse_page('Обувь',
                            'https://www.ozon.ru/category/botinki-zhenskie-7651/?color=100955526&type=31961')

    # Ботинки, НЕ черные
    get_products.parse_page('Обувь',
                            'https://www.ozon.ru/category/botinki-zhenskie-7651/?color=100955546%2C100955529%2C100955528%2C100955527%2C100955530%2C100955540%2C100966307%2C100955535%2C100966310%2C100955534%2C100955536%2C100955537%2C100955544%2C100955532%2C100955547%2C100955542%2C100955545%2C101097990%2C100955541&opened=color&type=31961')

    # Ботильоны, ЧЕРНЫЕ
    get_products.parse_page('Обувь',
                            'https://www.ozon.ru/category/botinki-zhenskie-7651/?color=100955526&type=32038')

    # Ботильоны, НЕ черные
    get_products.parse_page('Обувь',
                            'https://www.ozon.ru/category/botinki-zhenskie-7651/?color=100955528%2C100955546%2C100955530%2C100955529%2C100955540%2C100955527%2C100966307%2C100955534%2C100955532%2C100955535%2C100966310%2C100955536%2C100955537%2C100955542%2C100955544%2C100955545%2C101097990%2C100955541%2C100955547&type=32038')


    # Казаки, ботфорты
    get_products.parse_page('Обувь',
                            'https://www.ozon.ru/category/sapogi-i-polusapogi-zhenskie-7652/?type=34492%2C164229')

    # Сапоги, демисезон, еврозима
    get_products.parse_page('Обувь',
                            'https://www.ozon.ru/category/sapogi-i-polusapogi-zhenskie-7652/?season=82950%2C33889&type=31978')

   # Полусапоги
    get_products.parse_page('Обувь',
                            'https://www.ozon.ru/category/sapogi-i-polusapogi-zhenskie-7652/?type=31998')


def parse_top():
    # ТОП
    # Все цвета, кроме черного
    # Повседневный
    get_products.parse_page('Топ',
                            'https://www.ozon.ru/category/futbolki-i-topy-zhenskie-7505/?color=100955527%2C100955528%2C100955530%2C100955534%2C100955540%2C100955546%2C100966310%2C100955544%2C100955532%2C100955529%2C100955535%2C100955537%2C100955536%2C100955542%2C100955545%2C100966307%2C100955541%2C101097990%2C100955547&opened=styleapparel%2Ccolor%2Ctype&styleapparel=55228&type=38835%2C38833%2C178570%2C71937')

    # Вечерний
    get_products.parse_page('Топ',
                            'https://www.ozon.ru/category/futbolki-i-topy-zhenskie-7505/?color=100955527%2C100955528%2C100955530%2C100955534%2C100955540%2C100955546%2C100966310%2C100955544%2C100955532%2C100955529%2C100955535%2C100955537%2C100955536%2C100955542%2C100955545%2C100966307%2C100955541%2C101097990%2C100955547&opened=type%2Cstyleapparel%2Ccolor&styleapparel=57396&type=38835%2C38833%2C178570%2C71937')

    # Офис
    get_products.parse_page('Топ',
                            'https://www.ozon.ru/category/futbolki-i-topy-zhenskie-7505/?color=100955527%2C100955528%2C100955530%2C100955534%2C100955540%2C100955546%2C100966310%2C100955544%2C100955532%2C100955529%2C100955535%2C100955537%2C100955536%2C100955542%2C100955545%2C100966307%2C100955541%2C101097990%2C100955547&opened=type%2Cstyleapparel%2Ccolor&styleapparel=58692&type=38835%2C38833%2C178570%2C71937')

    # Все категории, ЧЕРНОЕ
    get_products.parse_page('Топ',
                            'https://www.ozon.ru/category/futbolki-i-topy-zhenskie-7505/?color=100955526&opened=color%2Ctype%2Cstyleapparel&type=38835%2C38833%2C178570%2C71937')

def parse_skirt():
    # ЛЕТО (НАДО МЕНЯТЬ)
    # # ЮБКА
    # # ЮБКА, все цвета, кроме черного
    # # Бохо и восточный
    # get_products.parse_page('Юбка',
    #                         'https://www.ozon.ru/category/yubki-zhenskie-7504/?category_was_predicted=true&color=100955530%2C100955527%2C100955528%2C100955540%2C100955546%2C100955529%2C100955534%2C100955535%2C100966307%2C100955547%2C100955532%2C100955536%2C100955542%2C100955537%2C100955544%2C100955545%2C100955541%2C101097990%2C100966310&deny_category_prediction=true&from_global=true&opened=color%2Cstyleapparel&styleapparel=100374527%2C277449&text=женская+юбка')
    #
    # # Офис, классический, вечерний
    # get_products.parse_page('Юбка',
    #                         'https://www.ozon.ru/category/yubki-zhenskie-7504/?category_was_predicted=true&color=100955530%2C100955527%2C100955528%2C100955540%2C100955546%2C100955529%2C100955534%2C100955535%2C100966307%2C100955547%2C100955532%2C100955536%2C100955542%2C100955537%2C100955544%2C100955545%2C100955541%2C101097990%2C100966310&deny_category_prediction=true&from_global=true&opened=styleapparel%2Ccolor&styleapparel=57396%2C148380%2C55225&text=женская+юбка')
    #
    # # Винтаж
    # get_products.parse_page('Юбка',
    #                         'https://www.ozon.ru/category/yubki-zhenskie-7504/?category_was_predicted=true&color=100955530%2C100955527%2C100955528%2C100955540%2C100955546%2C100955529%2C100955534%2C100955535%2C100966307%2C100955547%2C100955532%2C100955536%2C100955542%2C100955537%2C100955544%2C100955545%2C100955541%2C101097990%2C100966310&deny_category_prediction=true&from_global=true&opened=styleapparel%2Ccolor&styleapparel=56425&text=женская+юбка')
    #
    # # Коктейльное, Выпускное, свадебное, праздничное
    # get_products.parse_page('Юбка',
    #                         'https://www.ozon.ru/category/yubki-zhenskie-7504/?category_was_predicted=true&color=100955530%2C100955527%2C100955528%2C100955540%2C100955546%2C100955529%2C100955534%2C100955535%2C100966307%2C100955547%2C100955532%2C100955536%2C100955542%2C100955537%2C100955544%2C100955545%2C100955541%2C101097990%2C100966310&deny_category_prediction=true&from_global=true&opened=styleapparel%2Ccolor&styleapparel=164217%2C79761%2C101124545%2C106037&text=женская+юбка')
    #
    # # Все категории, ЧЕРНОЕ
    # get_products.parse_page('Юбка',
    #                         'https://www.ozon.ru/category/yubki-zhenskie-7504/?category_was_predicted=true&color=100955526&deny_category_prediction=true&from_global=true&text=женская+юбка')


    # ОСЕНЬ
    # ЮБКА
    # Все цвета, кроме черногоб все кроме лета
    # Повседневный
    get_products.parse_page('Юбка',
                            'https://www.ozon.ru/category/yubki-zhenskie-7504/?color=100955530%2C100955528%2C100955546%2C100955527%2C100955529%2C100955540%2C100955547%2C100955534%2C100955535%2C100966307%2C100955532%2C100955542%2C100966310%2C100955537%2C100955544%2C100955545%2C101097990%2C100955541%2C100955536&opened=styleapparel%2Ccolor&season=33890%2C33889%2C31827%2C82950&styleapparel=55228&type=336542%2C38829')

    # Офисный
    get_products.parse_page('Юбка',
                            'https://www.ozon.ru/category/yubki-zhenskie-7504/?color=100955530%2C100955528%2C100955546%2C100955527%2C100955529%2C100955540%2C100955547%2C100955534%2C100955535%2C100966307%2C100955532%2C100955542%2C100966310%2C100955537%2C100955544%2C100955545%2C101097990%2C100955541%2C100955536&opened=color%2Cstyleapparel&season=33890%2C33889%2C31827%2C82950&styleapparel=58692&type=336542%2C38829')

    # Вечерний
    get_products.parse_page('Юбка',
                            'https://www.ozon.ru/category/yubki-zhenskie-7504/?color=100955530%2C100955528%2C100955546%2C100955527%2C100955529%2C100955540%2C100955547%2C100955534%2C100955535%2C100966307%2C100955532%2C100955542%2C100966310%2C100955537%2C100955544%2C100955545%2C101097990%2C100955541%2C100955536&opened=color%2Cstyleapparel&season=33890%2C33889%2C31827%2C82950&styleapparel=57396&type=336542%2C38829')

    # Все категории, ЧЕРНОЕ, все кроме лета
    get_products.parse_page('Юбка',
                            'https://www.ozon.ru/category/yubki-zhenskie-7504/?color=100955526&season=33890%2C33889%2C31827%2C82950&type=336542%2C38829')

    # Все категории, ЧЕРНОЕ, зима, демисезон
    get_products.parse_page('Юбка',
                            'https://www.ozon.ru/category/yubki-zhenskie-7504/?color=100955526&season=33889%2C31827&type=336542%2C38829')

    # ТВИДОВАЯ
    get_products.parse_page('Юбка',
                            'https://www.ozon.ru/category/zhenskaya-odezhda-7501/?category_was_predicted=true&deny_category_prediction=true&from_global=true&text=Юбка+женская+твидовая')

def parse_suit():
    # КОСТЮМ
    # Все категории, ЧЕРНЫЙ, все кроме лета
    get_products.parse_page('Костюм',
                            'https://www.ozon.ru/category/kostyumy-i-komplekty-odezhdy-zhenskie-7536/?color=100955526&opened=setapparel%2Cstyleapparel&season=33890%2C33889%2C82950%2C31827&styleapparel=55228%2C58692%2C57396%2C55224%2C164217%2C79761')

    # Все категории, ЧЕРНЫЙ, зима, демисезон
    get_products.parse_page('Костюм',
                            'https://www.ozon.ru/category/kostyumy-i-komplekty-odezhdy-zhenskie-7536/?color=100955526&opened=setapparel%2Cstyleapparel&season=33889%2C31827&styleapparel=55228%2C58692%2C57396%2C55224%2C164217%2C79761')

    # Все категории, кроме ЧЕРНОГО, все крмое лета
    # Повседневный
    get_products.parse_page('Костюм',
                            'https://www.ozon.ru/category/kostyumy-i-komplekty-odezhdy-zhenskie-7536/?color=100955528%2C100955530%2C100955527%2C100955540%2C100955546%2C100955534%2C100955547%2C100955529%2C100955535%2C100966307%2C100955536%2C100955532%2C100966310%2C100955542%2C100955545%2C100955544%2C101097990%2C100955541%2C100955537&opened=color%2Csetapparel%2Cstyleapparel&season=33890%2C33889%2C31827%2C82950&styleapparel=55228')

    # Офисный
    get_products.parse_page('Костюм',
                            'https://www.ozon.ru/category/kostyumy-i-komplekty-odezhdy-zhenskie-7536/?color=100955528%2C100955530%2C100955527%2C100955540%2C100955546%2C100955534%2C100955547%2C100955529%2C100955535%2C100966307%2C100955536%2C100955532%2C100966310%2C100955542%2C100955545%2C100955544%2C101097990%2C100955541%2C100955537&opened=setapparel%2Cstyleapparel%2Ccolor&season=33890%2C33889%2C31827%2C82950&styleapparel=58692')

    # Коктейльное, свадебное, вечернее
    get_products.parse_page('Костюм',
                            'https://www.ozon.ru/category/kostyumy-i-komplekty-odezhdy-zhenskie-7536/?color=100955528%2C100955530%2C100955527%2C100955540%2C100955546%2C100955534%2C100955547%2C100955529%2C100955535%2C100966307%2C100955536%2C100955532%2C100966310%2C100955542%2C100955545%2C100955544%2C101097990%2C100955541%2C100955537&opened=setapparel%2Cstyleapparel%2Ccolor&season=33890%2C33889%2C31827%2C82950&styleapparel=57396%2C164217%2C79761')

    # Твидовый
    get_products.parse_page('Костюм',
                            'https://www.ozon.ru/category/zhenskaya-odezhda-7501/?category_was_predicted=true&deny_category_prediction=true&from_global=true&text=костюм+женский+твидовый')

def parse_corset():
    for i in range(4):
        # КОРСЕТ
        get_products.parse_page('Корсет',
                               'https://www.ozon.ru/category/korsety-zhenskie-36462/?opened=styleapparel&type=311046')

def parse_accessories():
    # АКСЕССУАРЫ

    # ВЕСНА, ЛЕТО
    # Очки


    # ВСЕСЕЗОННОЕ
    # ДЛЯ ВОЛОС
    # Заколки
    get_products.parse_page('Аксессуары',
                            'https://www.ozon.ru/category/zakolki-i-grebni-zhenskie-17048/?opened=type&type=105928%2C169002%2C105927')

    # Ободки
    get_products.parse_page('Аксессуары',
                            'https://www.ozon.ru/category/obodki-zhenskie-36096/?opened=type&type=326426%2C105926%2C163671%2C100261338%2C100371056%2C69351%2C100503714')

    # Резинки
    get_products.parse_page('Аксессуары',
                            'https://www.ozon.ru/category/rezinki-zhenskie-17050/')

    # Галстуки и бабочки
    get_products.parse_page('Аксессуары',
                            'https://www.ozon.ru/category/galstuki-i-babochki-zhenskie-35308/')

    # ГОЛОВНЫЕ УБОРЫ
    # Бандана косынка
    get_products.parse_page('Аксессуары',
                            'https://www.ozon.ru/category/bandany-i-kosynki-zhenskie-17012/?type=40542%2C40550')

    # Кепка
    get_products.parse_page('Аксессуары',
                            'https://www.ozon.ru/category/shapki-zhenskie-36513/?opened=type&type=40548')

    # Ремень, пояс
    get_products.parse_page('Аксессуары',
                            'https://www.ozon.ru/category/remni-poyasa-i-portupei-zhenskie-31983/?type=40559%2C40558')

    # Часы
    get_products.parse_page('Аксессуары',
                            'https://www.ozon.ru/category/chasy-zhenskie-17037/?opened=type&type=32931%2C309840%2C38178')


    # ОСЕНЬ
    # ГОЛОВНЫЕ УБОРЫ
    # Чепчик
    get_products.parse_page('Аксессуары',
                            'https://www.ozon.ru/category/shapki-zhenskie-36513/?opened=type&type=42160')

    # Берет
    get_products.parse_page('Аксессуары',
                            'https://www.ozon.ru/category/shlyapy-zhenskie-36514/?type=40543')


    # Платки
    get_products.parse_page('Аксессуары',
                            'https://www.ozon.ru/category/platki-i-palantiny-17055/')

    # Шарфы
    get_products.parse_page('Аксессуары',
                            'https://www.ozon.ru/category/sharfy-zhenskie-17057/?type=40556%2C272969')

    # Перчатки, ЧЕРНЫЕ
    get_products.parse_page('Аксессуары',
                            'https://www.ozon.ru/category/perchatki-i-varezhki-zhenskie-17060/?color=100955526&opened=type&type=40342')

    # Перчатки, НЕ черные
    get_products.parse_page('Аксессуары',
                            'https://www.ozon.ru/category/perchatki-i-varezhki-zhenskie-17060/?color=100955528%2C100955546%2C100955529%2C100955527%2C100955534%2C100955530%2C100955540%2C100955535%2C100955532%2C100966310%2C100955547%2C100955542%2C100955537%2C100955536%2C100966307%2C100955544%2C100955545%2C100955541%2C101097990&opened=type%2Ccolor&type=40342')


def parse_kofta():
    # КОФТА
    # Свитер, ЧЕРНЫЙ и БЕЖЕВЫЙ
    get_products.parse_page('Кофта',
                           'https://www.ozon.ru/category/svitery-dzhempery-i-kardigany-zhenskie-7537/?color=100955546%2C100955526&type=39149')

    # Джепер, ЧЕРНЫЙ и БЕЖЕВЫЙ
    get_products.parse_page('Кофта',
                           'https://www.ozon.ru/category/svitery-dzhempery-i-kardigany-zhenskie-7537/?color=100955546%2C100955526&type=37309')

    # Кардиган, ЧЕРНЫЙ и БЕЖЕВЫЙ
    get_products.parse_page('Кофта',
                           'https://www.ozon.ru/category/svitery-dzhempery-i-kardigany-zhenskie-7537/?color=100955526%2C100955546&type=38842')

    # Свитер, все кроме черного и бежевого
    get_products.parse_page('Кофта',
                           'https://www.ozon.ru/category/svitery-dzhempery-i-kardigany-zhenskie-7537/?color=100955527%2C100955528%2C100955530%2C100955540%2C100955534%2C100955529%2C100955547%2C100955535%2C100955532%2C100966307%2C100955536%2C100955537%2C100966310%2C100955545%2C100955544%2C100955541%2C101097990%2C100955542&opened=color&type=39149')

    # Джемпер, все кроме черного и бежевого
    get_products.parse_page('Кофта',
                           'https://www.ozon.ru/category/svitery-dzhempery-i-kardigany-zhenskie-7537/?color=100955527%2C100955528%2C100955540%2C100955530%2C100955534%2C100955529%2C100955547%2C100955535%2C100955532%2C100966307%2C100955536%2C100955537%2C100966310%2C100955542%2C100955545%2C100955544%2C101097990%2C100955541&opened=color&type=37309')

    # Кардиган, все кроме черного и бежевого
    get_products.parse_page('Кофта',
                           'https://www.ozon.ru/category/svitery-dzhempery-i-kardigany-zhenskie-7537/?color=100955528%2C100955527%2C100955530%2C100955540%2C100955534%2C100955547%2C100955529%2C100955532%2C100955535%2C100966307%2C100955537%2C100955536%2C100966310%2C100955542%2C100955545%2C100955544%2C101097990%2C100955541&opened=color&type=38842')

    # Водолазка
    get_products.parse_page('Кофта',
                           'https://www.ozon.ru/category/svitery-dzhempery-i-kardigany-zhenskie-7537/?type=39145')

    # Пуловер
    get_products.parse_page('Кофта',
                           'https://www.ozon.ru/category/svitery-dzhempery-i-kardigany-zhenskie-7537/?type=39150')

    # Боди, ЧЕРНОЕ
    get_products.parse_page('Кофта',
                           'https://www.ozon.ru/category/bodi-i-korsazhi-zhenskie-31309/?color=100955526')

    # Боди, НЕ черное
    get_products.parse_page('Кофта',
                            'https://www.ozon.ru/category/bodi-i-korsazhi-zhenskie-31309/?color=100955527%2C100955546%2C100955535%2C100955529%2C100955534%2C100955528%2C100955530%2C100955540%2C100955536%2C100955532%2C100966310%2C100955547%2C100966307%2C100955542%2C100955537%2C100955544%2C100955545%2C101097990%2C100955541&opened=color')

    # Толстовка
    get_products.parse_page('Кофта',
                            'https://www.ozon.ru/category/tolstovki-i-olimpiyki-zhenskie-7788/?type=37308')

    # Свитшот
    get_products.parse_page('Кофта',
                            'https://www.ozon.ru/category/tolstovki-i-olimpiyki-zhenskie-7788/?type=38589')

    # Худи
    get_products.parse_page('Кофта',
                            'https://www.ozon.ru/category/tolstovki-i-olimpiyki-zhenskie-7788/?type=39148')

def parse_outer_wear():
    # ВЕРХНЯЯ ОДЕЖДА ВЕСЕННЯЯ (НАДО МЕНЯТЬ)
    # #Куртка весенняя
    # get_products.parse_page('Верхняя Одежда',
    #                            'https://www.ozon.ru/category/zhenskaya-odezhda-7501/?category_was_predicted=true&deny_category_prediction=true&from_global=true&text=Женская+весенняя+куртка')
    #
    # #Плащ
    # get_products.parse_page('Верхняя Одежда',
    #                        'https://www.ozon.ru/category/zhenskaya-odezhda-7501/?category_was_predicted=true&deny_category_prediction=true&from_global=true&text=Женский+весенний+плащ')
    #
    # #Пальто
    # get_products.parse_page('Верхняя Одежда',
    #                        'https://www.ozon.ru/category/zhenskaya-odezhda-7501/?category_was_predicted=true&deny_category_prediction=true&text=женское+весеннее+пальто')
    #
    # # Дубленка
    # get_products.parse_page('Верхняя Одежда',
    #                        'https://www.ozon.ru/category/zhenskaya-odezhda-7501/?text=Женская+весенняя+дубленка')
    #
    # # Бомбер
    # get_products.parse_page('Верхняя Одежда',
    #                         'https://www.ozon.ru/category/zhenskaya-odezhda-7501/?category_was_predicted=true&deny_category_prediction=true&from_global=true&text=Женский+бомбер')
    #
    # # Верхняя одежда летняя
    # get_products.parse_page('Верхняя Одежда',
    #                         'https://www.ozon.ru/search/?text=Верхняя+одежда+летняя+женская&from_global=true')

    # ОСЕНЬ
    # ВЕРХНЯЯ ОДЕЖДА
    # Дубленка
    get_products.parse_page('Верхняя Одежда',
                               'https://www.ozon.ru/category/dublenki-i-shuby-zhenskie-7534/?type=55235%2C101017999')

    # Шуба
    get_products.parse_page('Верхняя Одежда',
                           'https://www.ozon.ru/category/dublenki-i-shuby-zhenskie-7534/?type=39156%2C101018000')

    # Жилет
    get_products.parse_page('Верхняя Одежда',
                           'https://www.ozon.ru/category/zhilety-zhenskie-7529/')

    # Пальто, ЧЕРНОЕ
    get_products.parse_page('Верхняя Одежда',
                           'https://www.ozon.ru/category/palto-zhenskie-7531/?color=100955526&type=39155')

    # Пальто, НЕ черное
    get_products.parse_page('Верхняя Одежда',
                            'https://www.ozon.ru/category/palto-zhenskie-7531/?color=100955528%2C100955546%2C100955529%2C100955530%2C100955540%2C100955527%2C100966307%2C100955534%2C100955535%2C100955536%2C100955547%2C100955532%2C100955537%2C100966310%2C100955542%2C100955545%2C100955541%2C100955544%2C101097990&opened=color&type=39155')

    # Плащ, тренч
    get_products.parse_page('Верхняя Одежда',
                            'https://www.ozon.ru/category/plashchi-zhenskie-7532/?type=101121375%2C41422')

    # Бомбер
    get_products.parse_page('Верхняя Одежда',
                            'https://www.ozon.ru/category/kurtki-zhenskie-7530/?opened=type&type=79517')

    # Ветровка, ЧЕРНАЯ
    get_products.parse_page('Верхняя Одежда',
                            'https://www.ozon.ru/category/kurtki-zhenskie-7530/?color=100955526&opened=type&type=39038')

    # Ветровка, НЕ черная
    get_products.parse_page('Верхняя Одежда',
                            'https://www.ozon.ru/category/kurtki-zhenskie-7530/?color=100955540%2C100955527%2C100955530%2C100955528%2C100955546%2C100955534%2C100966307%2C100955532%2C100955547%2C100955535%2C100955537%2C100955529%2C100955536%2C100966310%2C100955542%2C100955544%2C100955541%2C100955545&opened=color%2Ctype&type=39038')

    # Куртка, НЕ черная
    get_products.parse_page('Верхняя Одежда',
                            'https://www.ozon.ru/category/kurtki-zhenskie-7530/?color=100955546%2C100955540%2C100955528%2C100955530%2C100955529%2C100955527%2C100966307%2C100955547%2C100955534%2C100955532%2C100955535%2C100955536%2C100955537%2C100966310%2C100955542%2C100955544%2C100955545%2C100955541%2C101097990&opened=type%2Ccolor&type=37305')

    # Куртка кожаная, НЕ черная
    get_products.parse_page('Верхняя Одежда',
                            'https://www.ozon.ru/category/kurtki-zhenskie-7530/?color=100955546%2C100955540%2C100955528%2C100955530%2C100955529%2C100955527%2C100966307%2C100955547%2C100955534%2C100955532%2C100955535%2C100955536%2C100955537%2C100966310%2C100955542%2C100955544%2C100955545%2C100955541%2C101097990&opened=type%2Ccolor&type=151844')

    # Куртка, ЧЕРНАЯ
    get_products.parse_page('Верхняя Одежда',
                            'https://www.ozon.ru/category/kurtki-zhenskie-7530/?color=100955526&opened=type%2Ccolor&type=37305')

    # Куртка кожаная, ЧЕРНАЯ
    get_products.parse_page('Верхняя Одежда',
                            'https://www.ozon.ru/category/kurtki-zhenskie-7530/?color=100955526&opened=type%2Ccolor&type=151844')

    # Куртка джинсовая
    get_products.parse_page('Верхняя Одежда',
                            'https://www.ozon.ru/category/kurtki-zhenskie-7530/?opened=color%2Ctype&type=151843')


def parse_shorts():
    # Деним
    get_products.parse_page('Шорты',
                            'https://www.ozon.ru/category/shorty-zhenskie-7514/?category_was_predicted=true&deny_category_prediction=true&from_global=true&materialfilterclothes=100960331&text=женские+шорты+джинсовые')
    # Бохо и восточный
    get_products.parse_page('Шорты',
                            'https://www.ozon.ru/category/shorty-zhenskie-7514/?category_was_predicted=true&color=100955528%2C100955530%2C100955527%2C100955547%2C100955534%2C100966307%2C100955535%2C100955532%2C100955546%2C100955529%2C100966310%2C100955537%2C100955536%2C100955544%2C100955542%2C100955545%2C100955540&deny_category_prediction=true&from_global=true&styleapparel=100374527%2C277449&text=женские+шорты')

    # Офис, классический, вечерний
    get_products.parse_page('Шорты',
                            'https://www.ozon.ru/category/shorty-zhenskie-7514/?category_was_predicted=true&color=100955528%2C100955530%2C100955527%2C100955547%2C100955534%2C100966307%2C100955535%2C100955532%2C100955546%2C100955529%2C100966310%2C100955537%2C100955536%2C100955544%2C100955542%2C100955545%2C100955540&deny_category_prediction=true&from_global=true&styleapparel=148380%2C55225%2C57396&text=женские+шорты')

    # Коктейльное, Выпускное, свадебное, праздничное
    get_products.parse_page('Шорты',
                            'https://www.ozon.ru/category/shorty-zhenskie-7514/?category_was_predicted=true&color=100955528%2C100955530%2C100955527%2C100955547%2C100955534%2C100966307%2C100955535%2C100955532%2C100955546%2C100955529%2C100966310%2C100955537%2C100955536%2C100955544%2C100955542%2C100955545%2C100955540&deny_category_prediction=true&from_global=true&styleapparel=106037%2C164217%2C79761%2C101124545&text=женские+шорты')

    # Все категории, ЧЕРНОЕ
    get_products.parse_page('Шорты',
                            'https://www.ozon.ru/category/shorty-zhenskie-7514/?category_was_predicted=true&color=100955526&deny_category_prediction=true&from_global=true&opened=color&text=женские+шорты+джинсовые')

def parse_swimsuit():
    get_products.parse_page('Купальник',
                            'https://www.ozon.ru/category/kupalniki-i-plyazhnaya-odezhda-zhenskie-7540/?category_was_predicted=true&deny_category_prediction=true&from_global=true&text=Купальник+женский')

if __name__ == "__main__":
    parse_trousers()
    # parse_home_clothes()
    parse_jewelry()
    parse_bag()
    parse_tshirts()
    parse_shirts()
    parse_jeans()
    parse_jacket()
    # parse_dress()
    parse_shoes()
    parse_top()
    parse_skirt()
    parse_suit()
    parse_corset()
    parse_accessories()
    # parse_blouse()
    parse_shorts()
    parse_swimsuit()
    parse_kofta()
    parse_outer_wear()
