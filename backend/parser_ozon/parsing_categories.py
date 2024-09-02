from parser_ozon import get_products

def parse_trousers():
    # БРЮКИ
    # БРЮКИ, все цвета, кроме черного
    # Бохо и восточный
    get_products.parse_page('Брюки',
                           'https://www.ozon.ru/category/zhenskaya-odezhda-7501/?category_was_predicted=true&color=100955530%2C100955527%2C100955540%2C100955546%2C100955534%2C100955547%2C100955529%2C100966307%2C100955532%2C100955535%2C100955542%2C100955537%2C100955536%2C100966310%2C100955545%2C100955544%2C100955541%2C101097990%2C100955528&deny_category_prediction=true&from_global=true&opened=styleapparel%2Cmodelclothing%2Ccolor&styleapparel=100374527%2C277449&text=Женские+брюки&tf_state=9H8UUG4QKyRe7uTKIAciSe-vUnLHCRFa6VKLVDrsSRcS1Tg%3D')
    
    # Офис, классический, вечерний
    get_products.parse_page('Брюки',
                           'https://www.ozon.ru/category/zhenskaya-odezhda-7501/?category_was_predicted=true&color=100955530%2C100955527%2C100955540%2C100955546%2C100955534%2C100955547%2C100955529%2C100966307%2C100955532%2C100955535%2C100955542%2C100955537%2C100955536%2C100966310%2C100955545%2C100955544%2C100955541%2C101097990%2C100955528&deny_category_prediction=true&from_global=true&opened=styleapparel%2Cmodelclothing%2Ccolor&styleapparel=55225%2C148380%2C57396&text=Женские+брюки&tf_state=9H8UUG4QKyRe7uTKIAciSe-vUnLHCRFa6VKLVDrsSRcS1Tg%3D')
    # Винтаж
    get_products.parse_page('Брюки',
                           'https://www.ozon.ru/category/zhenskaya-odezhda-7501/?category_was_predicted=true&color=100955530%2C100955527%2C100955540%2C100955546%2C100955534%2C100955547%2C100955529%2C100966307%2C100955532%2C100955535%2C100955542%2C100955537%2C100955536%2C100966310%2C100955545%2C100955544%2C100955541%2C101097990%2C100955528&deny_category_prediction=true&from_global=true&opened=color%2Cstyleapparel%2Cmodelclothing&page=4&styleapparel=56425&text=Женские+брюки&tf_state=LRgNOk4dr0qZLzNyXUSCCMtn_bdpR8leFe0UadQ1fR9UNofj')
    
    # Коктейльное, свадебное и праздничное
    get_products.parse_page('Брюки',
                           'https://www.ozon.ru/category/zhenskaya-odezhda-7501/?category_was_predicted=true&color=100955530%2C100955527%2C100955540%2C100955546%2C100955534%2C100955547%2C100955529%2C100966307%2C100955532%2C100955535%2C100955542%2C100955537%2C100955536%2C100966310%2C100955545%2C100955544%2C100955541%2C101097990%2C100955528&deny_category_prediction=true&from_global=true&opened=styleapparel%2Cmodelclothing%2Ccolor&styleapparel=164217%2C79761%2C106037&text=Женские+брюки&tf_state=LRgNOk4dr0qZLzNyXUSCCMtn_bdpR8leFe0UadQ1fR9UNofj')
    
    # ВСЕ категории, ЧЕРНЫЕ
    get_products.parse_page('Брюки',
                           'https://www.ozon.ru/category/zhenskaya-odezhda-7501/?category_was_predicted=true&color=100955526&deny_category_prediction=true&from_global=true&text=Женские+брюки')

def parse_home_clothes():
    # ДОМАШНЯЯ ОДЕЖДА
    # пижамы
    get_products.parse_page('Домашняя Одежда',
                           'https://www.ozon.ru/category/domashnyaya-odezhda-zhenskaya-7541/?category_was_predicted=true&deny_category_prediction=true&from_global=true&text=женская+домашняя+одежда')

    # тапочки
    get_products.parse_page('Домашняя Одежда',
                           'https://www.ozon.ru/category/tapochki-zhenskie-7655/?category_was_predicted=true&deny_category_prediction=true&from_global=true&text=Женская+обувь')

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
        # СУМКА ЧЕРНАЯ
        get_products.parse_page('Сумка',
                               'https://www.ozon.ru/category/sumki-na-plecho-zhenskie-17002/?category_was_predicted=true&color=100955526&deny_category_prediction=true&from_global=true&opened=badfiltermaterial%2Chandletype%2Ctype&text=Сумка+женская')

        # СУМКА НЕ черная
        get_products.parse_page('Сумка',
                               'https://www.ozon.ru/category/sumki-na-plecho-zhenskie-17002/?category_was_predicted=true&color=100955529%2C100955527%2C100955542%2C100955546%2C100955534%2C100955540%2C100955530%2C100955535%2C100966307%2C100955537%2C100955532%2C100955536%2C100955547%2C100966310%2C100955545%2C100955544%2C100955541%2C101097990%2C100955528&deny_category_prediction=true&from_global=true&opened=color%2Chandletype%2Ctype%2Cbadfiltermaterial&text=Сумка+женская')

def parse_tshirts():
    for i in range(4):
        # ФУТБОЛКА
        get_products.parse_page('Футболка',
                               'https://www.ozon.ru/category/futbolki-i-topy-zhenskie-7505/?category_was_predicted=true&deny_category_prediction=true&from_global=true&opened=sleevelength%2Ctypesport%2Cmodelclothing&page=3&text=Женская+футболка&tf_state=FspgpzCmZzTUmLtK2ZGzfLwP_EZYOErq0XKm4xAspaMXFc4j&type=37283')

def parse_shirts():
    for i in range(4):
        # РУБАШКА
        get_products.parse_page('Рубашка',
                               'https://www.ozon.ru/category/bluzy-i-rubashki-zhenskie-7511/?type=37307')


def parse_jeans():
    for i in range(4):
        # ДЖИНСЫ
        get_products.parse_page('Джинсы',
                               'https://www.ozon.ru/category/dzhinsy-zhenskie-7503/?category_was_predicted=true&deny_category_prediction=true&from_global=true&text=Джинсы+женские')

def parse_jacket():
    for i in range(4):
        # ПИДАЖАК
        # ВСЕ кроме черного
        get_products.parse_page('Пиджак',
                                'https://www.ozon.ru/category/zhakety-i-zhilety-zhenskie-7535/?category_was_predicted=true&color=100955530%2C100955527%2C100955534%2C100955528%2C100966307%2C100955546%2C100955535%2C100955529%2C100955537%2C100955532%2C100966310%2C100955536%2C100955547%2C100955542%2C100955545%2C100955544%2C100955541%2C101097990%2C100955540&deny_category_prediction=true&from_global=true&opened=color&text=Женский+пиджак')

    # ПИДАЖАК
    # Черный
    get_products.parse_page('Пиджак',
                            'https://www.ozon.ru/category/zhakety-i-zhilety-zhenskie-7535/?color=100955526&deny_category_prediction=true&from_global=true&opened=color&text=Женский+пиджак')

def parse_dress():
    # ПЛАТЬЕ
    # ПЛАТЬЕ, все цвета, кроме черного
    # Бохо и восточный
    get_products.parse_page('Платье',
                            'https://www.ozon.ru/category/platya-zhenskie-7502/?category_was_predicted=true&color=100955530%2C100955540%2C100955527%2C100955534%2C100955535%2C100955528%2C100955546%2C100955532%2C100955547%2C100955537%2C100955536%2C100955529%2C100966307%2C100966310%2C100955542%2C100955545%2C100955544%2C100955541%2C101097990&deny_category_prediction=true&from_global=true&opened=color%2Cmodelclothing%2Cstyleapparel&styleapparel=100374527%2C277449&text=женское+платье')

    # Офис, классический, вечерний
    get_products.parse_page('Платье',
                            'https://www.ozon.ru/category/platya-zhenskie-7502/?category_was_predicted=true&color=100955530%2C100955540%2C100955527%2C100955534%2C100955535%2C100955528%2C100955546%2C100955532%2C100955547%2C100955537%2C100955536%2C100955529%2C100966307%2C100966310%2C100955542%2C100955545%2C100955544%2C100955541%2C101097990&deny_category_prediction=true&from_global=true&opened=modelclothing%2Cstyleapparel%2Ccolor&styleapparel=55225%2C148380%2C57396&text=женское+платье')

    # Винтаж
    get_products.parse_page('Платье',
                            'https://www.ozon.ru/category/platya-zhenskie-7502/?category_was_predicted=true&color=100955530%2C100955540%2C100955527%2C100955534%2C100955535%2C100955528%2C100955546%2C100955532%2C100955547%2C100955537%2C100955536%2C100955529%2C100966307%2C100966310%2C100955542%2C100955545%2C100955544%2C100955541%2C101097990&deny_category_prediction=true&from_global=true&opened=color%2Cmodelclothing%2Cstyleapparel&styleapparel=56425&text=женское+платье')

    # Коктейльное, Выпускное, свадебное, праздничное
    get_products.parse_page('Платье',
                            'https://www.ozon.ru/category/platya-zhenskie-7502/?category_was_predicted=true&color=100955530%2C100955540%2C100955527%2C100955534%2C100955535%2C100955528%2C100955546%2C100955532%2C100955547%2C100955537%2C100955536%2C100955529%2C100966307%2C100966310%2C100955542%2C100955545%2C100955544%2C100955541%2C101097990&deny_category_prediction=true&from_global=true&opened=styleapparel%2Ccolor%2Cmodelclothing&styleapparel=106037%2C79761%2C101124545%2C164217&text=женское+платье')

    # Все категории, ЧЕРНОЕ
    get_products.parse_page('Платье',
                            'https://www.ozon.ru/category/platya-zhenskie-7502/?category_was_predicted=true&color=100955526&deny_category_prediction=true&from_global=true&text=женское+платье')

def parse_shoes():
    # ОБУВЬ
    # Босоножки и сандалии ЧЕРНЫЕ
    get_products.parse_page('Обувь',
                            'https://www.ozon.ru/category/bosonozhki-zhenskie-7645/?category_was_predicted=true&color=100955526&deny_category_prediction=true&from_global=true&opened=color&text=Женская+обувь')

    # Босоножки и сандалии ВСЕ ЦВЕТА
    get_products.parse_page('Обувь',
                            'https://www.ozon.ru/category/bosonozhki-zhenskie-7645/?category_was_predicted=true&color=100955527%2C100955546%2C100955529%2C100955534%2C100955530%2C100955535%2C100955540%2C100955528%2C100955537%2C100955544%2C100966307%2C100955536%2C100955542%2C100955532%2C100955547%2C100966310%2C100955541%2C101097990%2C100955545&deny_category_prediction=true&from_global=true&opened=color&text=Женская+обувь')

    # Кроссовки
    get_products.parse_page('Обувь',
                            'https://www.ozon.ru/category/obuv-17777/?category_was_predicted=true&deny_category_prediction=true&from_global=true&text=Женская+кроссовки')

    # Кеды
    get_products.parse_page('Обувь',
                            'https://www.ozon.ru/category/zhenskaya-obuv-7640/?category_was_predicted=true&deny_category_prediction=true&from_global=true&text=Женские+кеды')

    # Ботинки
    get_products.parse_page('Обувь',
                            'https://www.ozon.ru/category/botinki-zhenskie-7651/?category_was_predicted=true&deny_category_prediction=true&from_global=true&season=64979&text=Женская+обувь')

    # Сапоги
    get_products.parse_page('Обувь',
                            'https://www.ozon.ru/category/sapogi-i-polusapogi-zhenskie-7652/?category_was_predicted=true&deny_category_prediction=true&from_global=true&text=женская+обувь')

    # Туфли
    get_products.parse_page('Обувь',
                            'https://www.ozon.ru/category/obuv-17777/?category_was_predicted=true&deny_category_prediction=true&from_global=true&text=Женские+туфли')

    # Туфли ЧЕРНЫЕ
    get_products.parse_page('Обувь',
                            'https://www.ozon.ru/category/zhenskaya-obuv-7640/?category_was_predicted=true&color=100955526&deny_category_prediction=true&from_global=true&text=Женские+туфли&type=31864')

    # Туфли НЕ черные
    get_products.parse_page('Обувь',
                            'https://www.ozon.ru/category/zhenskaya-obuv-7640/?category_was_predicted=true&color=100955527%2C100955546%2C100955529%2C100955535%2C100955534%2C100955542%2C100955530%2C100955544%2C100955540%2C100955528%2C100955545%2C100966307%2C100955537%2C100966310%2C100955536%2C100955532%2C100955547%2C100955541%2C101097990&deny_category_prediction=true&from_global=true&opened=color&text=Женские+туфли&type=31864')

    # Лоферы НЕ черные
    get_products.parse_page('Обувь',
                            'https://www.ozon.ru/category/tufli-zhenskie-7644/?category_was_predicted=true&color=100955546%2C100955529%2C100955527%2C100955530%2C100955528%2C100955535%2C100955534%2C100966307%2C100955540%2C100955537%2C100955536%2C100955547%2C100966310%2C100955544%2C100955545%2C100955532%2C100955542%2C100955541%2C101097990&deny_category_prediction=true&from_global=true&opened=color&text=Женские+лоферы')
    # Лоферы ЧЕРНЫЕ
    get_products.parse_page('Обувь',
                            'https://www.ozon.ru/category/tufli-zhenskie-7644/?category_was_predicted=true&color=100955526&deny_category_prediction=true&from_global=true&text=Женские+лоферы')

    # Туфли
    get_products.parse_page('Обувь',
                            'https://www.ozon.ru/category/obuv-17777/?category_was_predicted=true&deny_category_prediction=true&from_global=true&text=Женские+туфли')

    # Туфли
    get_products.parse_page('Обувь',
                            'https://www.ozon.ru/category/obuv-17777/?category_was_predicted=true&deny_category_prediction=true&from_global=true&text=Женские+туфли')

def parse_top():
    # ТОП
    # ТОП, все цвета, кроме черного
    # Бохо и восточный
    get_products.parse_page('Топ',
                            'https://www.ozon.ru/category/mayki-i-topy-zhenskie-7506/?category_was_predicted=true&color=100955527%2C100955534%2C100955528%2C100955546%2C100955530%2C100955540%2C100955535%2C100955529%2C100955532%2C100955537%2C100966307%2C100955536%2C100966310%2C100955542%2C100955544%2C100955545%2C101097990%2C100955541%2C100955547&deny_category_prediction=true&from_global=true&opened=styleapparel%2Ccolor&styleapparel=100374527%2C277449&text=женский+топ')

    # Офис, классический, вечерний
    get_products.parse_page('Топ',
                            'https://www.ozon.ru/category/mayki-i-topy-zhenskie-7506/?category_was_predicted=true&color=100955527%2C100955534%2C100955528%2C100955546%2C100955530%2C100955540%2C100955535%2C100955529%2C100955532%2C100955537%2C100966307%2C100955536%2C100966310%2C100955542%2C100955544%2C100955545%2C101097990%2C100955541%2C100955547&deny_category_prediction=true&from_global=true&opened=styleapparel%2Ccolor&styleapparel=55225%2C148380%2C57396&text=женский+топ')

    # Винтаж
    get_products.parse_page('Топ',
                            'https://www.ozon.ru/category/mayki-i-topy-zhenskie-7506/?category_was_predicted=true&color=100955527%2C100955534%2C100955528%2C100955546%2C100955530%2C100955540%2C100955535%2C100955529%2C100955532%2C100955537%2C100966307%2C100955536%2C100966310%2C100955542%2C100955544%2C100955545%2C101097990%2C100955541%2C100955547&deny_category_prediction=true&from_global=true&opened=styleapparel%2Ccolor&styleapparel=56425&text=женский+топ')

    # Коктейльное, Выпускное, свадебное, праздничное
    get_products.parse_page('Топ',
                            'https://www.ozon.ru/category/mayki-i-topy-zhenskie-7506/?category_was_predicted=true&color=100955527%2C100955534%2C100955528%2C100955546%2C100955530%2C100955540%2C100955535%2C100955529%2C100955532%2C100955537%2C100966307%2C100955536%2C100966310%2C100955542%2C100955544%2C100955545%2C101097990%2C100955541%2C100955547&deny_category_prediction=true&from_global=true&opened=color%2Cstyleapparel&styleapparel=164217%2C79761%2C101124545%2C106037&text=женский+топ')

    # Все категории, ЧЕРНОЕ
    get_products.parse_page('Топ',
                            'https://www.ozon.ru/category/mayki-i-topy-zhenskie-7506/?category_was_predicted=true&color=100955526&deny_category_prediction=true&from_global=true&text=женский+топ')

def parse_skirt():
    # ЮБКА
    # ЮБКА, все цвета, кроме черного
    # Бохо и восточный
    get_products.parse_page('Юбка',
                            'https://www.ozon.ru/category/yubki-zhenskie-7504/?category_was_predicted=true&color=100955530%2C100955527%2C100955528%2C100955540%2C100955546%2C100955529%2C100955534%2C100955535%2C100966307%2C100955547%2C100955532%2C100955536%2C100955542%2C100955537%2C100955544%2C100955545%2C100955541%2C101097990%2C100966310&deny_category_prediction=true&from_global=true&opened=color%2Cstyleapparel&styleapparel=100374527%2C277449&text=женская+юбка')

    # Офис, классический, вечерний
    get_products.parse_page('Юбка',
                            'https://www.ozon.ru/category/yubki-zhenskie-7504/?category_was_predicted=true&color=100955530%2C100955527%2C100955528%2C100955540%2C100955546%2C100955529%2C100955534%2C100955535%2C100966307%2C100955547%2C100955532%2C100955536%2C100955542%2C100955537%2C100955544%2C100955545%2C100955541%2C101097990%2C100966310&deny_category_prediction=true&from_global=true&opened=styleapparel%2Ccolor&styleapparel=57396%2C148380%2C55225&text=женская+юбка')

    # Винтаж
    get_products.parse_page('Юбка',
                            'https://www.ozon.ru/category/yubki-zhenskie-7504/?category_was_predicted=true&color=100955530%2C100955527%2C100955528%2C100955540%2C100955546%2C100955529%2C100955534%2C100955535%2C100966307%2C100955547%2C100955532%2C100955536%2C100955542%2C100955537%2C100955544%2C100955545%2C100955541%2C101097990%2C100966310&deny_category_prediction=true&from_global=true&opened=styleapparel%2Ccolor&styleapparel=56425&text=женская+юбка')

    # Коктейльное, Выпускное, свадебное, праздничное
    get_products.parse_page('Юбка',
                            'https://www.ozon.ru/category/yubki-zhenskie-7504/?category_was_predicted=true&color=100955530%2C100955527%2C100955528%2C100955540%2C100955546%2C100955529%2C100955534%2C100955535%2C100966307%2C100955547%2C100955532%2C100955536%2C100955542%2C100955537%2C100955544%2C100955545%2C100955541%2C101097990%2C100966310&deny_category_prediction=true&from_global=true&opened=styleapparel%2Ccolor&styleapparel=164217%2C79761%2C101124545%2C106037&text=женская+юбка')

    # Все категории, ЧЕРНОЕ
    get_products.parse_page('Юбка',
                            'https://www.ozon.ru/category/yubki-zhenskie-7504/?category_was_predicted=true&color=100955526&deny_category_prediction=true&from_global=true&text=женская+юбка')

    # Твидовая
    get_products.parse_page('Юбка',
                            'https://www.ozon.ru/search/?text=женская+юбка+твидовая&from_global=true')

def parse_suit():
    # КОСТЮМ
    # КОСТЮМ, все цвета, кроме черного
    # Бохо и восточный
    get_products.parse_page('Костюм',
                            'https://www.ozon.ru/category/kostyumy-i-komplekty-odezhdy-zhenskie-7536/?category_was_predicted=true&color=100955527%2C100955530%2C100955540%2C100955534%2C100955546%2C100955535%2C100966307%2C100955547%2C100955537%2C100955529%2C100955532%2C100955536%2C100966310%2C100955542%2C100955544%2C101097990%2C100955545%2C100955541%2C100955528&deny_category_prediction=true&from_global=true&opened=styleapparel%2Ccolor&styleapparel=100374527%2C277449&text=костюм+женский')

    # Офис, классический, вечерний
    get_products.parse_page('Костюм',
                            'https://www.ozon.ru/category/kostyumy-i-komplekty-odezhdy-zhenskie-7536/?category_was_predicted=true&color=100955527%2C100955530%2C100955540%2C100955534%2C100955546%2C100955535%2C100966307%2C100955547%2C100955537%2C100955529%2C100955532%2C100955536%2C100966310%2C100955542%2C100955544%2C101097990%2C100955545%2C100955541%2C100955528&deny_category_prediction=true&from_global=true&opened=styleapparel%2Ccolor&styleapparel=55225%2C148380%2C57396&text=костюм+женский')

    # Винтаж
    get_products.parse_page('Костюм',
                            'https://www.ozon.ru/category/kostyumy-i-komplekty-odezhdy-zhenskie-7536/?category_was_predicted=true&color=100955527%2C100955530%2C100955540%2C100955534%2C100955546%2C100955535%2C100966307%2C100955547%2C100955537%2C100955529%2C100955532%2C100955536%2C100966310%2C100955542%2C100955544%2C101097990%2C100955545%2C100955541%2C100955528&deny_category_prediction=true&from_global=true&opened=styleapparel%2Ccolor&styleapparel=56425&text=костюм+женский')

    # Коктейльное, Выпускное, свадебное, праздничное
    get_products.parse_page('Костюм',
                            'https://www.ozon.ru/category/kostyumy-i-komplekty-odezhdy-zhenskie-7536/?category_was_predicted=true&color=100955527%2C100955530%2C100955540%2C100955534%2C100955546%2C100955535%2C100966307%2C100955547%2C100955537%2C100955529%2C100955532%2C100955536%2C100966310%2C100955542%2C100955544%2C101097990%2C100955545%2C100955541%2C100955528&deny_category_prediction=true&from_global=true&opened=color%2Cstyleapparel&styleapparel=164217%2C79761%2C101124545%2C106037&text=костюм+женский')

    # Все категории, ЧЕРНОЕ
    get_products.parse_page('Костюм',
                            'https://www.ozon.ru/category/kostyumy-i-komplekty-odezhdy-zhenskie-7536/?category_was_predicted=true&color=100955526&deny_category_prediction=true&from_global=true&text=костюм+женский')

    # Твидовый
    get_products.parse_page('Костюм',
                            'https://www.ozon.ru/category/zhenskaya-odezhda-7501/?category_was_predicted=true&deny_category_prediction=true&from_global=true&text=костюм+твидовый+женский')

def parse_corset():
        # КОРСЕТ
        # Бохо и восточный
        get_products.parse_page('Корсет',
                               'https://www.ozon.ru/category/zhenskaya-odezhda-7501/?category_was_predicted=true&color=100955527%2C100955536%2C100955534%2C100955535%2C100955529%2C100955546%2C100955530%2C100955532%2C100955547%2C100966307%2C100955542%2C100955544%2C100955545%2C100955528%2C100955541%2C100955540&deny_category_prediction=true&from_global=true&opened=color%2Cstyleapparel&styleapparel=100374527%2C277449&text=Женский+корсет')

        # Офис, классический, вечерний
        get_products.parse_page('Корсет',
                               'https://www.ozon.ru/category/zhenskaya-odezhda-7501/?category_was_predicted=true&color=100955527%2C100955536%2C100955534%2C100955535%2C100955529%2C100955546%2C100955530%2C100955532%2C100955547%2C100966307%2C100955542%2C100955544%2C100955545%2C100955528%2C100955541%2C100955540&deny_category_prediction=true&from_global=true&opened=styleapparel%2Ccolor&styleapparel=55225%2C148380%2C57396&text=Женский+корсет')

        # Винтаж
        get_products.parse_page('Корсет',
                               'https://www.ozon.ru/category/zhenskaya-odezhda-7501/?category_was_predicted=true&color=100955527%2C100955536%2C100955534%2C100955535%2C100955529%2C100955546%2C100955530%2C100955532%2C100955547%2C100966307%2C100955542%2C100955544%2C100955545%2C100955528%2C100955541%2C100955540&deny_category_prediction=true&from_global=true&opened=color%2Cstyleapparel&styleapparel=56425&text=Женский+корсет')

        # Коктейльное, Выпускное, свадебное, праздничное
        get_products.parse_page('Корсет',
                               'https://www.ozon.ru/category/zhenskaya-odezhda-7501/?category_was_predicted=true&color=100955527%2C100955536%2C100955534%2C100955535%2C100955529%2C100955546%2C100955530%2C100955532%2C100955547%2C100966307%2C100955542%2C100955544%2C100955545%2C100955528%2C100955541%2C100955540&deny_category_prediction=true&from_global=true&opened=styleapparel%2Ccolor&styleapparel=164217%2C79761%2C101124545%2C106037&text=Женский+корсет')

        # Все категории, ЧЕРНОЕ
        get_products.parse_page('Корсет',
                               'https://www.ozon.ru/category/zhenskaya-odezhda-7501/?category_was_predicted=true&color=100955526&deny_category_prediction=true&from_global=true&text=Женский+корсет')

def parse_accessories():
    # АКСЕССУАРЫ
    # ОЧКИ
    get_products.parse_page('Аксессуары',
                            'https://www.ozon.ru/category/ochki-solntsezashchitnye-zhenskie-17019/?category_was_predicted=true&deny_category_prediction=true&from_global=true&text=женские+аксессуары')
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

    # Бандана косынка
    get_products.parse_page('Аксессуары',
                            'https://www.ozon.ru/category/bandany-i-kosynki-zhenskie-17012/?type=40542%2C40550')

    # Кепка
    get_products.parse_page('Аксессуары',
                            'https://www.ozon.ru/category/shapki-zhenskie-36513/?opened=type&type=40548')
    # Берет
    get_products.parse_page('Аксессуары',
                            'https://www.ozon.ru/category/shlyapy-zhenskie-36514/?type=40543')

    # Платки
    get_products.parse_page('Аксессуары',
                            'https://www.ozon.ru/category/platki-i-palantiny-17055/')

    # Шарфы
    get_products.parse_page('Аксессуары',
                            'https://www.ozon.ru/category/sharfy-zhenskie-17057/?type=40556%2C272969')

    # Ремень, пояс
    get_products.parse_page('Аксессуары',
                            'https://www.ozon.ru/category/remni-poyasa-i-portupei-zhenskie-31983/?type=40559%2C40558')

    # Часы
    get_products.parse_page('Аксессуары',
                            'https://www.ozon.ru/category/chasy-zhenskie-17037/?opened=type&type=32931%2C309840%2C38178')

def parse_blouse():
    for i in range(4):
        get_products.parse_page('Блузка',
                                'https://www.ozon.ru/category/bluzy-i-rubashki-zhenskie-7511/?category_was_predicted=true&deny_category_prediction=true&from_global=true&text=%D0%96%D0%B5%D0%BD%D1%81%D0%BA%D0%B0%D1%8F+%D0%B1%D0%BB%D1%83%D0%B7%D0%BA%D0%B0&type=101121374%2C39030')

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

def parse_kofta():
    # Свитер
     get_products.parse_page('Кофта',
                           'https://www.ozon.ru/category/zhenskaya-odezhda-7501/?category_was_predicted=true&deny_category_prediction=true&from_global=true&text=женский+свитер')

    #Лонгслив
     get_products.parse_page('Кофта',
                           'https://www.ozon.ru/category/zhenskaya-odezhda-7501/?category_was_predicted=true&deny_category_prediction=true&from_global=true&text=Лонгслив+женский')

    # Джемпер
     get_products.parse_page('Кофта',
                           'https://www.ozon.ru/category/zhenskaya-odezhda-7501/?text=Женский+джемпер')

    # Кардиган
     get_products.parse_page('Кофта',
                           'https://www.ozon.ru/category/zhenskaya-odezhda-7501/?category_was_predicted=true&deny_category_prediction=true&from_global=true&text=женский+кардиган')

    # Свитшот
     get_products.parse_page('Кофта',
                           'https://www.ozon.ru/category/zhenskaya-odezhda-7501/?category_was_predicted=true&deny_category_prediction=true&from_global=true&text=свитошот+женский')

    # Худи
     get_products.parse_page('Кофта',
                           'https://www.ozon.ru/category/tolstovki-i-olimpiyki-zhenskie-7788/?category_was_predicted=true&deny_category_prediction=true&from_global=true&text=худиженская&type=37308%2C39148')

    # Водолазка
     get_products.parse_page('Кофта',
                           'https://www.ozon.ru/category/svitery-dzhempery-i-kardigany-zhenskie-7537/?category_was_predicted=true&deny_category_prediction=true&from_global=true&text=Водолазка+женская')

    # Боди
     get_products.parse_page('Кофта',
                           'https://www.ozon.ru/category/bodi-i-korsazhi-zhenskie-31309/?category_was_predicted=true&deny_category_prediction=true&from_global=true&text=Боди+женская')


def parse_outer_wear():
    # ВЕРХНЯЯ ОДЕЖДА ВЕСЕННЯЯ
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
    # Бомбер
    get_products.parse_page('Верхняя Одежда',
                            'https://www.ozon.ru/category/zhenskaya-odezhda-7501/?category_was_predicted=true&deny_category_prediction=true&from_global=true&text=Женский+бомбер')

    # Верхняя одежда летняя
    get_products.parse_page('Верхняя Одежда',
                            'https://www.ozon.ru/search/?text=Верхняя+одежда+летняя+женская&from_global=true')


if __name__ == "__main__":
    # parse_trousers()
    # parse_home_clothes()
    # parse_jewelry()
    # parse_bag()
    # parse_tshirts()
    parse_shirts()
    # parse_jeans()
    # parse_jacket()
    # parse_dress()
    # parse_shoes()
    # parse_top()
    # parse_skirt()
    # parse_suit()
    # parse_corset()
    # parse_accessories()
    # parse_blouse()
    # parse_shorts()
    # parse_swimsuit()
    # parse_kofta()
    # parse_outer_wear()
