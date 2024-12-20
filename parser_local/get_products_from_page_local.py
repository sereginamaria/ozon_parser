from bs4 import BeautifulSoup
import itertools

from selenium.webdriver.common.by import By

from parser_local.get_product_local import get_product
# from myparser.get_product import get_product
import undetected_chromedriver as uc
import time
from selenium.webdriver.chrome.options import Options

telegram_url = "https://api.telegram.org/bot6508472057:AAHdRDqUbaVjn7sstEtnHPMmKAXXAPp6_og"

def get_products_from_page(publication_category, url):
    # Ограничим парсинг первыми n страницами
    print('Start get_products_from_page')
    global category
    category = publication_category
    MAX_PAGE = 2
    i = 2
    while i <= MAX_PAGE:
        if i == 2:
            get_html(url)
        else:
            url_param = url + '?page=' + str(i)
            get_html(url_param)
        i += 1


def get_html(url):
    print('get_html')

    options1 = uc.ChromeOptions()
    options1.headless = False
    # options1.add_argument('--headless')
    # options1.add_argument('--headless=new')
    options1.add_argument('--no-sandbox')
    options1.add_argument('--disable-dev-shm-usage')

    options1.add_argument("--disable-extensions")
    options1.add_argument('--disable-application-cache')
    options1.add_argument("--disable-setuid-sandbox")
    options1.add_argument("--disable-gpu")
    options1.add_argument("--remote-allow-origins=*")
    # options1.add_argument("--log-path=/home/masha/chromelogs")
    options1.add_argument("--disable-dev-shm-usage")
    options1._session = None

    # options1.binary_location = '/home/masha/ozon_parser/chromedriver/chrome-linux64/chrome'
    # options1.binary_location = '/home/masha/ozon_parser/chromedriver/chrome117/chrome-linux64/chrome'
    # options1.binary_location = '/home/masha/ozon_parser/chromedriver/chrome-headless-shell-linux64/chrome-headless-shell'
    print('before Chrome')

    driver = uc.Chrome(
        # driver_executable_path='/home/masha/ozon_parser/chromedriver/chromedriver-linux64/chromedriver',
        patcher_force_close=True, no_sandbox=True, suppress_welcome=True, use_subprocess=False,
        options=options1,
        log_level=10, headless=False)

    # options = Options()
    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-dev-shm-usage')
    # options.headless = False
    # driver = uc.Chrome(options=options)

    print('get')
    driver.get(url)
    print(driver.current_url)
    time.sleep(5)

    print('get ok')

    # driver.save_screenshot('10.png')
    # driver.refresh()

    #
    # html = driver.page_source
    # print(html)

    # content = driver.find_element(By.ID, 'reload-button')
    # print(content)
    #
    # content.click()

    driver.execute_script("window.scrollTo(5,4000);")
    # driver.save_screenshot('11.png')
    time.sleep(10)

    print('after scroll')
    html = driver.page_source
    # print(html)
    # time.sleep(3)

    driver.close()
    driver.quit()
    get_urls(html)


def parse_data(html):
    # print('parse_data')
    soup = BeautifulSoup(html, 'html.parser')
    product_links = set([a.get('href').split('?')[0] for a in list(
        itertools.chain(*[div.find_all('a') for div in soup.find('div').find_all(attrs={'class', 'mj5_23'})]))])
    return product_links


def get_urls(html):
    print('get_urls')
    all_links = []
    links = parse_data(html)
    print('links')
    print(links)
    all_links = all_links + list(links)

    numLines = 0
    # if len(all_links) == 36:
    for link in all_links:
        message_type = False
        get_product(link, category, message_type)
        numLines += 1
        if numLines >= 12:
            break
    # else:
    #     print('Ошибка! Со страницы определилось ' + str(len(all_links)) +
    #             ' ссылок. Повторите попытку.')

    print('End get_products_from_page')


if __name__ == "__main__":

    Trousers = False
    HouseClothes = False
    Tshirs = False
    Bag = False
    Dress = False
    Shoes = False
    Top = False
    Skirt = False
    OuterWear = False
    Kofta = False
    Corset = True
    Jewelry = False
    Accessories = True
    Jacket = False
    Shirt = False
    Jeans = False
    Suit = False
    Blouse = False
    Shorts = False
    Swimsuit = False

    if OuterWear == True:
        #ВЕРХНЯЯ ОДЕЖДА ВЕСЕННЯЯ
        # #Куртка весенняя
        # get_products_from_page('Верхняя Одежда',
        #                            'https://www.ozon.ru/category/zhenskaya-odezhda-7501/?category_was_predicted=true&deny_category_prediction=true&from_global=true&text=Женская+весенняя+куртка')
        #
        # #Плащ
        # get_products_from_page('Верхняя Одежда',
        #                        'https://www.ozon.ru/category/zhenskaya-odezhda-7501/?category_was_predicted=true&deny_category_prediction=true&from_global=true&text=Женский+весенний+плащ')
        #
        # #Пальто
        # get_products_from_page('Верхняя Одежда',
        #                        'https://www.ozon.ru/category/zhenskaya-odezhda-7501/?category_was_predicted=true&deny_category_prediction=true&text=женское+весеннее+пальто')
        #
        # # Дубленка
        # get_products_from_page('Верхняя Одежда',
        #                        'https://www.ozon.ru/category/zhenskaya-odezhda-7501/?text=Женская+весенняя+дубленка')
        #

        # # Верхняя одежда летняя
        # #Бомбер
        # get_products_from_page('Верхняя Одежда',
        #                        'https://www.ozon.ru/category/zhenskaya-odezhda-7501/?category_was_predicted=true&deny_category_prediction=true&from_global=true&text=Женский+бомбер')
        #
        # #Верхняя одежда летняя
        # get_products_from_page('Верхняя Одежда',
        #                        'https://www.ozon.ru/search/?text=Верхняя+одежда+летняя+женская&from_global=true')

        #ВЕРХНЯЯ ОДЕЖДА ОСЕННЯЯ
        #Дубленки
        get_products_from_page('Верхняя Одежда',
                               'https://www.ozon.ru/category/dublenki-i-shuby-zhenskie-7534/')

        #Жилеты
        get_products_from_page('Верхняя Одежда',
                               'https://www.ozon.ru/category/zhilety-zhenskie-7529/')

        #Куртки и пуховики
        get_products_from_page('Верхняя Одежда',
                               'https://www.ozon.ru/category/kurtki-zhenskie-7530/')

        #Пальто
        get_products_from_page('Верхняя Одежда',
                               'https://www.ozon.ru/category/palto-zhenskie-7531/')

        #Плащи
        get_products_from_page('Верхняя Одежда',
                               'https://www.ozon.ru/category/plashchi-zhenskie-7532/')

        # Джинсовая куртка
        get_products_from_page('Верхняя Одежда',
                               'https://www.ozon.ru/category/zhenskaya-odezhda-7501/?category_was_predicted=true&deny_category_prediction=true&from_global=true&text=джинсовая+куртка+женская')


    if Kofta  == True:
        # # Свитер
        # get_products_from_page('Кофта',
        #                        'https://www.ozon.ru/category/zhenskaya-odezhda-7501/?category_was_predicted=true&deny_category_prediction=true&from_global=true&text=женский+свитер')
        #
        # #Лонгслив
        # get_products_from_page('Кофта',
        #                        'https://www.ozon.ru/category/zhenskaya-odezhda-7501/?category_was_predicted=true&deny_category_prediction=true&from_global=true&text=Лонгслив+женский')

        #Джемпер
        get_products_from_page('Кофта',
                               'https://www.ozon.ru/category/zhenskaya-odezhda-7501/?text=Женский+джемпер')

        #Кардиган
        get_products_from_page('Кофта',
                               'https://www.ozon.ru/category/zhenskaya-odezhda-7501/?category_was_predicted=true&deny_category_prediction=true&from_global=true&text=женский+кардиган')

        #Свитшот
        get_products_from_page('Кофта',
                               'https://www.ozon.ru/category/zhenskaya-odezhda-7501/?category_was_predicted=true&deny_category_prediction=true&from_global=true&text=свитошот+женский')

        #Худи
        get_products_from_page('Кофта',
                               'https://www.ozon.ru/category/tolstovki-i-olimpiyki-zhenskie-7788/?category_was_predicted=true&deny_category_prediction=true&from_global=true&text=худиженская&type=37308%2C39148')

        #Водолазка
        get_products_from_page('Кофта',
                               'https://www.ozon.ru/category/svitery-dzhempery-i-kardigany-zhenskie-7537/?category_was_predicted=true&deny_category_prediction=true&from_global=true&text=Водолазка+женская')

        #Боди
        get_products_from_page('Кофта',
                               'https://www.ozon.ru/category/bodi-i-korsazhi-zhenskie-31309/?category_was_predicted=true&deny_category_prediction=true&from_global=true&text=Боди+женская')

    if Trousers == True:
    #БРЮКИ
        #БРЮКИ, все цвета, кроме черного
        #Бохо и восточный
        get_products_from_page('Брюки',
                             'https://www.ozon.ru/category/zhenskaya-odezhda-7501/?category_was_predicted=true&color=100955530%2C100955527%2C100955540%2C100955546%2C100955534%2C100955547%2C100955529%2C100966307%2C100955532%2C100955535%2C100955542%2C100955537%2C100955536%2C100966310%2C100955545%2C100955544%2C100955541%2C101097990%2C100955528&deny_category_prediction=true&from_global=true&opened=styleapparel%2Cmodelclothing%2Ccolor&styleapparel=100374527%2C277449&text=Женские+брюки&tf_state=9H8UUG4QKyRe7uTKIAciSe-vUnLHCRFa6VKLVDrsSRcS1Tg%3D')

        #Офис, классический, вечерний
        get_products_from_page('Брюки',
                               'https://www.ozon.ru/category/zhenskaya-odezhda-7501/?category_was_predicted=true&color=100955530%2C100955527%2C100955540%2C100955546%2C100955534%2C100955547%2C100955529%2C100966307%2C100955532%2C100955535%2C100955542%2C100955537%2C100955536%2C100966310%2C100955545%2C100955544%2C100955541%2C101097990%2C100955528&deny_category_prediction=true&from_global=true&opened=styleapparel%2Cmodelclothing%2Ccolor&styleapparel=55225%2C148380%2C57396&text=Женские+брюки&tf_state=9H8UUG4QKyRe7uTKIAciSe-vUnLHCRFa6VKLVDrsSRcS1Tg%3D')
        #Винтаж
        get_products_from_page('Брюки',
                               'https://www.ozon.ru/category/zhenskaya-odezhda-7501/?category_was_predicted=true&color=100955530%2C100955527%2C100955540%2C100955546%2C100955534%2C100955547%2C100955529%2C100966307%2C100955532%2C100955535%2C100955542%2C100955537%2C100955536%2C100966310%2C100955545%2C100955544%2C100955541%2C101097990%2C100955528&deny_category_prediction=true&from_global=true&opened=color%2Cstyleapparel%2Cmodelclothing&page=4&styleapparel=56425&text=Женские+брюки&tf_state=LRgNOk4dr0qZLzNyXUSCCMtn_bdpR8leFe0UadQ1fR9UNofj')

        #Коктейльное, свадебное и праздничное
        get_products_from_page('Брюки',
                               'https://www.ozon.ru/category/zhenskaya-odezhda-7501/?category_was_predicted=true&color=100955530%2C100955527%2C100955540%2C100955546%2C100955534%2C100955547%2C100955529%2C100966307%2C100955532%2C100955535%2C100955542%2C100955537%2C100955536%2C100966310%2C100955545%2C100955544%2C100955541%2C101097990%2C100955528&deny_category_prediction=true&from_global=true&opened=styleapparel%2Cmodelclothing%2Ccolor&styleapparel=164217%2C79761%2C106037&text=Женские+брюки&tf_state=LRgNOk4dr0qZLzNyXUSCCMtn_bdpR8leFe0UadQ1fR9UNofj')

        #ВСЕ категории, ЧЕРНЫЕ
        get_products_from_page('Брюки',
                               'https://www.ozon.ru/category/zhenskaya-odezhda-7501/?category_was_predicted=true&color=100955526&deny_category_prediction=true&from_global=true&text=Женские+брюки')

    if HouseClothes == True:
    #ДОМАШНЯЯ ОДЕЖДА
        #пижамы
        get_products_from_page('Домашняя Одежда',
                               'https://www.ozon.ru/category/domashnyaya-odezhda-zhenskaya-7541/?category_was_predicted=true&deny_category_prediction=true&from_global=true&text=женская+домашняя+одежда')

        #тапочки
        get_products_from_page('Домашняя Одежда',
                               'https://www.ozon.ru/category/tapochki-zhenskie-7655/?category_was_predicted=true&deny_category_prediction=true&from_global=true&text=Женская+обувь')

    if Jewelry == True:
        # УКРАШЕНИЯ
        #Браслеты
        get_products_from_page('Украшения',
                               'https://www.ozon.ru/category/braslety-bizhuternye-zhenskie-17031/?from_global=true&text=erhfitybz')

        # #Брелки
        # get_products_from_page('Украшения',
        #                        'https://www.ozon.ru/category/breloki-zhenskie-17033/?from_global=true&text=erhfitybz')

        #Броши и значки
        get_products_from_page('Украшения',
                               'https://www.ozon.ru/category/broshi-bizhuternye-zhenskie-17034/?from_global=true&text=erhfitybz')

        #Колье и бусы
        get_products_from_page('Украшения',
                               'https://www.ozon.ru/category/kole-i-ozherelya-bizhuternye-zhenskie-17027/?from_global=true&text=erhfitybz')

        #Кольца
        get_products_from_page('Украшения',
                               'https://www.ozon.ru/category/koltsa-bizhuternye-zhenskie-17023/?from_global=true&text=erhfitybz')

        #Комплекты
        get_products_from_page('Украшения',
                               'https://www.ozon.ru/category/komplekty-bizhuternyh-ukrasheniy-zhenskie-17032/?from_global=true&text=erhfitybz')

        #Подвески и кулоны
        get_products_from_page('Украшения',
                               'https://www.ozon.ru/category/podveski-i-kulony-bizhuternye-zhenskie-17029/?from_global=true&text=erhfitybz')

        #Серьги
        get_products_from_page('Украшения',
                               'https://www.ozon.ru/category/sergi-bizhuternye-17024/?from_global=true&text=erhfitybz')

        #Цепочки
        get_products_from_page('Украшения',
                               'https://www.ozon.ru/category/tsepochki-bizhuternye-zhenskie-17030/?from_global=true&text=erhfitybz')


    for i in range(4):
        if Tshirs == True:
        #ФУТБОЛКА
            get_products_from_page('Футболка',
                                   'https://www.ozon.ru/category/futbolki-i-topy-zhenskie-7505/?category_was_predicted=true&deny_category_prediction=true&from_global=true&opened=sleevelength%2Ctypesport%2Cmodelclothing&page=3&text=Женская+футболка&tf_state=FspgpzCmZzTUmLtK2ZGzfLwP_EZYOErq0XKm4xAspaMXFc4j&type=37283')

        if Shirt == True:
            #УКРАШЕНИЯ
            get_products_from_page('Рубашка',
                                   'https://www.ozon.ru/category/zhenskaya-odezhda-7501/?category_was_predicted=true&deny_category_prediction=true&from_global=true&text=Рубашка+женская')

        if Jeans == True:
            #ДЖИНСЫ
            get_products_from_page('Джинсы',
                                   'https://www.ozon.ru/category/dzhinsy-zhenskie-7503/?category_was_predicted=true&deny_category_prediction=true&from_global=true&text=Джинсы+женские')

        if Bag == True:
        #СУМКА
           #СУМКА ЧЕРНАЯ
            get_products_from_page('Сумка',
                                   'https://www.ozon.ru/category/sumki-na-plecho-zhenskie-17002/?category_was_predicted=true&color=100955526&deny_category_prediction=true&from_global=true&opened=badfiltermaterial%2Chandletype%2Ctype&text=Сумка+женская')

           #СУМКА НЕ черная
            get_products_from_page('Сумка',
                                   'https://www.ozon.ru/category/sumki-na-plecho-zhenskie-17002/?category_was_predicted=true&color=100955529%2C100955527%2C100955542%2C100955546%2C100955534%2C100955540%2C100955530%2C100955535%2C100966307%2C100955537%2C100955532%2C100955536%2C100955547%2C100966310%2C100955545%2C100955544%2C100955541%2C101097990%2C100955528&deny_category_prediction=true&from_global=true&opened=color%2Chandletype%2Ctype%2Cbadfiltermaterial&text=Сумка+женская')

        if Jacket == True:
            # ПИДАЖАК
            # ВСЕ кроме черного
            get_products_from_page('Пиджак',
                                   'https://www.ozon.ru/category/zhakety-i-zhilety-zhenskie-7535/?category_was_predicted=true&color=100955530%2C100955527%2C100955534%2C100955528%2C100966307%2C100955546%2C100955535%2C100955529%2C100955537%2C100955532%2C100966310%2C100955536%2C100955547%2C100955542%2C100955545%2C100955544%2C100955541%2C101097990%2C100955540&deny_category_prediction=true&from_global=true&opened=color&text=Женский+пиджак')


    if Jacket == True:
    #ПИДАЖАК
        #Черный
        get_products_from_page('Пиджак',
                               'https://www.ozon.ru/category/zhakety-i-zhilety-zhenskie-7535/?color=100955526&deny_category_prediction=true&from_global=true&opened=color&text=Женский+пиджак')


    if Dress == True:
    #ПЛАТЬЕ
        #ПЛАТЬЕ, все цвета, кроме черного
        #Бохо и восточный
        get_products_from_page('Платье',
                               'https://www.ozon.ru/category/platya-zhenskie-7502/?category_was_predicted=true&color=100955530%2C100955540%2C100955527%2C100955534%2C100955535%2C100955528%2C100955546%2C100955532%2C100955547%2C100955537%2C100955536%2C100955529%2C100966307%2C100966310%2C100955542%2C100955545%2C100955544%2C100955541%2C101097990&deny_category_prediction=true&from_global=true&opened=color%2Cmodelclothing%2Cstyleapparel&styleapparel=100374527%2C277449&text=женское+платье')

        #Офис, классический, вечерний
        get_products_from_page('Платье',
                               'https://www.ozon.ru/category/platya-zhenskie-7502/?category_was_predicted=true&color=100955530%2C100955540%2C100955527%2C100955534%2C100955535%2C100955528%2C100955546%2C100955532%2C100955547%2C100955537%2C100955536%2C100955529%2C100966307%2C100966310%2C100955542%2C100955545%2C100955544%2C100955541%2C101097990&deny_category_prediction=true&from_global=true&opened=modelclothing%2Cstyleapparel%2Ccolor&styleapparel=55225%2C148380%2C57396&text=женское+платье')

        #Винтаж
        get_products_from_page('Платье',
                               'https://www.ozon.ru/category/platya-zhenskie-7502/?category_was_predicted=true&color=100955530%2C100955540%2C100955527%2C100955534%2C100955535%2C100955528%2C100955546%2C100955532%2C100955547%2C100955537%2C100955536%2C100955529%2C100966307%2C100966310%2C100955542%2C100955545%2C100955544%2C100955541%2C101097990&deny_category_prediction=true&from_global=true&opened=color%2Cmodelclothing%2Cstyleapparel&styleapparel=56425&text=женское+платье')

        #Коктейльное, Выпускное, свадебное, праздничное
        get_products_from_page('Платье',
                               'https://www.ozon.ru/category/platya-zhenskie-7502/?category_was_predicted=true&color=100955530%2C100955540%2C100955527%2C100955534%2C100955535%2C100955528%2C100955546%2C100955532%2C100955547%2C100955537%2C100955536%2C100955529%2C100966307%2C100966310%2C100955542%2C100955545%2C100955544%2C100955541%2C101097990&deny_category_prediction=true&from_global=true&opened=styleapparel%2Ccolor%2Cmodelclothing&styleapparel=106037%2C79761%2C101124545%2C164217&text=женское+платье')

        #Все категории, ЧЕРНОЕ
        get_products_from_page('Платье',
                               'https://www.ozon.ru/category/platya-zhenskie-7502/?category_was_predicted=true&color=100955526&deny_category_prediction=true&from_global=true&text=женское+платье')

    if Shoes == True:
    #ОБУВЬ
        # #Босоножки и сандалии ЧЕРНЫЕ
        # get_products_from_page('Обувь',
        #                        'https://www.ozon.ru/category/bosonozhki-zhenskie-7645/?category_was_predicted=true&color=100955526&deny_category_prediction=true&from_global=true&opened=color&text=Женская+обувь')
        #
        # #Босоножки и сандалии ВСЕ ЦВЕТА
        # get_products_from_page('Обувь',
        #                        'https://www.ozon.ru/category/bosonozhki-zhenskie-7645/?category_was_predicted=true&color=100955527%2C100955546%2C100955529%2C100955534%2C100955530%2C100955535%2C100955540%2C100955528%2C100955537%2C100955544%2C100966307%2C100955536%2C100955542%2C100955532%2C100955547%2C100966310%2C100955541%2C101097990%2C100955545&deny_category_prediction=true&from_global=true&opened=color&text=Женская+обувь')

        #Кроссовки
        get_products_from_page('Обувь',
                                   'https://www.ozon.ru/category/obuv-17777/?category_was_predicted=true&deny_category_prediction=true&from_global=true&text=Женская+кроссовки')

        #Кеды
        get_products_from_page('Обувь',
                               'https://www.ozon.ru/category/zhenskaya-obuv-7640/?category_was_predicted=true&deny_category_prediction=true&from_global=true&text=Женские+кеды')

        #Ботинки
        get_products_from_page('Обувь',
                               'https://www.ozon.ru/category/botinki-zhenskie-7651/?category_was_predicted=true&deny_category_prediction=true&from_global=true&season=64979&text=Женская+обувь')

        #Сапоги
        get_products_from_page('Обувь',
                               'https://www.ozon.ru/category/sapogi-i-polusapogi-zhenskie-7652/?category_was_predicted=true&deny_category_prediction=true&from_global=true&text=женская+обувь')

        #Туфли
        get_products_from_page('Обувь',
                               'https://www.ozon.ru/category/obuv-17777/?category_was_predicted=true&deny_category_prediction=true&from_global=true&text=Женские+туфли')

        #Туфли ЧЕРНЫЕ
        get_products_from_page('Обувь',
                               'https://www.ozon.ru/category/zhenskaya-obuv-7640/?category_was_predicted=true&color=100955526&deny_category_prediction=true&from_global=true&text=Женские+туфли&type=31864')

        #Туфли НЕ черные
        get_products_from_page('Обувь',
                               'https://www.ozon.ru/category/zhenskaya-obuv-7640/?category_was_predicted=true&color=100955527%2C100955546%2C100955529%2C100955535%2C100955534%2C100955542%2C100955530%2C100955544%2C100955540%2C100955528%2C100955545%2C100966307%2C100955537%2C100966310%2C100955536%2C100955532%2C100955547%2C100955541%2C101097990&deny_category_prediction=true&from_global=true&opened=color&text=Женские+туфли&type=31864')

        #Лоферы НЕ черные
        get_products_from_page('Обувь',
                               'https://www.ozon.ru/category/tufli-zhenskie-7644/?category_was_predicted=true&color=100955546%2C100955529%2C100955527%2C100955530%2C100955528%2C100955535%2C100955534%2C100966307%2C100955540%2C100955537%2C100955536%2C100955547%2C100966310%2C100955544%2C100955545%2C100955532%2C100955542%2C100955541%2C101097990&deny_category_prediction=true&from_global=true&opened=color&text=Женские+лоферы')
        #Лоферы ЧЕРНЫЕ
        get_products_from_page('Обувь',
                               'https://www.ozon.ru/category/tufli-zhenskie-7644/?category_was_predicted=true&color=100955526&deny_category_prediction=true&from_global=true&text=Женские+лоферы')

        # Туфли
        get_products_from_page('Обувь',
                               'https://www.ozon.ru/category/obuv-17777/?category_was_predicted=true&deny_category_prediction=true&from_global=true&text=Женские+туфли')

        # Туфли
        get_products_from_page('Обувь',
                               'https://www.ozon.ru/category/obuv-17777/?category_was_predicted=true&deny_category_prediction=true&from_global=true&text=Женские+туфли')

    if Top == True:
    #ТОП
        #ТОП, все цвета, кроме черного
        #Бохо и восточный
        get_products_from_page('Топ',
                               'https://www.ozon.ru/category/mayki-i-topy-zhenskie-7506/?category_was_predicted=true&color=100955527%2C100955534%2C100955528%2C100955546%2C100955530%2C100955540%2C100955535%2C100955529%2C100955532%2C100955537%2C100966307%2C100955536%2C100966310%2C100955542%2C100955544%2C100955545%2C101097990%2C100955541%2C100955547&deny_category_prediction=true&from_global=true&opened=styleapparel%2Ccolor&styleapparel=100374527%2C277449&text=женский+топ')

        #Офис, классический, вечерний
        get_products_from_page('Топ',
                               'https://www.ozon.ru/category/mayki-i-topy-zhenskie-7506/?category_was_predicted=true&color=100955527%2C100955534%2C100955528%2C100955546%2C100955530%2C100955540%2C100955535%2C100955529%2C100955532%2C100955537%2C100966307%2C100955536%2C100966310%2C100955542%2C100955544%2C100955545%2C101097990%2C100955541%2C100955547&deny_category_prediction=true&from_global=true&opened=styleapparel%2Ccolor&styleapparel=55225%2C148380%2C57396&text=женский+топ')

        #Винтаж
        get_products_from_page('Топ',
                               'https://www.ozon.ru/category/mayki-i-topy-zhenskie-7506/?category_was_predicted=true&color=100955527%2C100955534%2C100955528%2C100955546%2C100955530%2C100955540%2C100955535%2C100955529%2C100955532%2C100955537%2C100966307%2C100955536%2C100966310%2C100955542%2C100955544%2C100955545%2C101097990%2C100955541%2C100955547&deny_category_prediction=true&from_global=true&opened=styleapparel%2Ccolor&styleapparel=56425&text=женский+топ')

        #Коктейльное, Выпускное, свадебное, праздничное
        get_products_from_page('Топ',
                               'https://www.ozon.ru/category/mayki-i-topy-zhenskie-7506/?category_was_predicted=true&color=100955527%2C100955534%2C100955528%2C100955546%2C100955530%2C100955540%2C100955535%2C100955529%2C100955532%2C100955537%2C100966307%2C100955536%2C100966310%2C100955542%2C100955544%2C100955545%2C101097990%2C100955541%2C100955547&deny_category_prediction=true&from_global=true&opened=color%2Cstyleapparel&styleapparel=164217%2C79761%2C101124545%2C106037&text=женский+топ')

        #Все категории, ЧЕРНОЕ
        get_products_from_page('Топ',
                               'https://www.ozon.ru/category/mayki-i-topy-zhenskie-7506/?category_was_predicted=true&color=100955526&deny_category_prediction=true&from_global=true&text=женский+топ')

    if Skirt == True:
    #ЮБКА
        #ЮБКА, все цвета, кроме черного
        #Бохо и восточный
        get_products_from_page('Юбка',
                               'https://www.ozon.ru/category/yubki-zhenskie-7504/?category_was_predicted=true&color=100955530%2C100955527%2C100955528%2C100955540%2C100955546%2C100955529%2C100955534%2C100955535%2C100966307%2C100955547%2C100955532%2C100955536%2C100955542%2C100955537%2C100955544%2C100955545%2C100955541%2C101097990%2C100966310&deny_category_prediction=true&from_global=true&opened=color%2Cstyleapparel&styleapparel=100374527%2C277449&text=женская+юбка')

        #Офис, классический, вечерний
        get_products_from_page('Юбка',
                               'https://www.ozon.ru/category/yubki-zhenskie-7504/?category_was_predicted=true&color=100955530%2C100955527%2C100955528%2C100955540%2C100955546%2C100955529%2C100955534%2C100955535%2C100966307%2C100955547%2C100955532%2C100955536%2C100955542%2C100955537%2C100955544%2C100955545%2C100955541%2C101097990%2C100966310&deny_category_prediction=true&from_global=true&opened=styleapparel%2Ccolor&styleapparel=57396%2C148380%2C55225&text=женская+юбка')

        #Винтаж
        get_products_from_page('Юбка',
                               'https://www.ozon.ru/category/yubki-zhenskie-7504/?category_was_predicted=true&color=100955530%2C100955527%2C100955528%2C100955540%2C100955546%2C100955529%2C100955534%2C100955535%2C100966307%2C100955547%2C100955532%2C100955536%2C100955542%2C100955537%2C100955544%2C100955545%2C100955541%2C101097990%2C100966310&deny_category_prediction=true&from_global=true&opened=styleapparel%2Ccolor&styleapparel=56425&text=женская+юбка')

        #Коктейльное, Выпускное, свадебное, праздничное
        get_products_from_page('Юбка',
                               'https://www.ozon.ru/category/yubki-zhenskie-7504/?category_was_predicted=true&color=100955530%2C100955527%2C100955528%2C100955540%2C100955546%2C100955529%2C100955534%2C100955535%2C100966307%2C100955547%2C100955532%2C100955536%2C100955542%2C100955537%2C100955544%2C100955545%2C100955541%2C101097990%2C100966310&deny_category_prediction=true&from_global=true&opened=styleapparel%2Ccolor&styleapparel=164217%2C79761%2C101124545%2C106037&text=женская+юбка')

        #Все категории, ЧЕРНОЕ
        get_products_from_page('Юбка',
                               'https://www.ozon.ru/category/yubki-zhenskie-7504/?category_was_predicted=true&color=100955526&deny_category_prediction=true&from_global=true&text=женская+юбка')

        #Твидовая
        get_products_from_page('Юбка',
                               'https://www.ozon.ru/search/?text=женская+юбка+твидовая&from_global=true')

    if Suit == True:
        # ЮБКА
        # ЮБКА, все цвета, кроме черного
        # Бохо и восточный
        get_products_from_page('Костюм',
                               'https://www.ozon.ru/category/kostyumy-i-komplekty-odezhdy-zhenskie-7536/?category_was_predicted=true&color=100955527%2C100955530%2C100955540%2C100955534%2C100955546%2C100955535%2C100966307%2C100955547%2C100955537%2C100955529%2C100955532%2C100955536%2C100966310%2C100955542%2C100955544%2C101097990%2C100955545%2C100955541%2C100955528&deny_category_prediction=true&from_global=true&opened=styleapparel%2Ccolor&styleapparel=100374527%2C277449&text=костюм+женский')

        # Офис, классический, вечерний
        get_products_from_page('Костюм',
                               'https://www.ozon.ru/category/kostyumy-i-komplekty-odezhdy-zhenskie-7536/?category_was_predicted=true&color=100955527%2C100955530%2C100955540%2C100955534%2C100955546%2C100955535%2C100966307%2C100955547%2C100955537%2C100955529%2C100955532%2C100955536%2C100966310%2C100955542%2C100955544%2C101097990%2C100955545%2C100955541%2C100955528&deny_category_prediction=true&from_global=true&opened=styleapparel%2Ccolor&styleapparel=55225%2C148380%2C57396&text=костюм+женский')

        # Винтаж
        get_products_from_page('Костюм',
                               'https://www.ozon.ru/category/kostyumy-i-komplekty-odezhdy-zhenskie-7536/?category_was_predicted=true&color=100955527%2C100955530%2C100955540%2C100955534%2C100955546%2C100955535%2C100966307%2C100955547%2C100955537%2C100955529%2C100955532%2C100955536%2C100966310%2C100955542%2C100955544%2C101097990%2C100955545%2C100955541%2C100955528&deny_category_prediction=true&from_global=true&opened=styleapparel%2Ccolor&styleapparel=56425&text=костюм+женский')

        # Коктейльное, Выпускное, свадебное, праздничное
        get_products_from_page('Костюм',
                               'https://www.ozon.ru/category/kostyumy-i-komplekty-odezhdy-zhenskie-7536/?category_was_predicted=true&color=100955527%2C100955530%2C100955540%2C100955534%2C100955546%2C100955535%2C100966307%2C100955547%2C100955537%2C100955529%2C100955532%2C100955536%2C100966310%2C100955542%2C100955544%2C101097990%2C100955545%2C100955541%2C100955528&deny_category_prediction=true&from_global=true&opened=color%2Cstyleapparel&styleapparel=164217%2C79761%2C101124545%2C106037&text=костюм+женский')

        # Все категории, ЧЕРНОЕ
        get_products_from_page('Костюм',
                               'https://www.ozon.ru/category/kostyumy-i-komplekty-odezhdy-zhenskie-7536/?category_was_predicted=true&color=100955526&deny_category_prediction=true&from_global=true&text=костюм+женский')

        # Твидовый
        get_products_from_page('Костюм',
                               'https://www.ozon.ru/category/zhenskaya-odezhda-7501/?category_was_predicted=true&deny_category_prediction=true&from_global=true&text=костюм+твидовый+женский')

    if Corset == True:
        #КОРСЕТ
       # Бохо и восточный
        get_products_from_page('Корсет',
                               'https://www.ozon.ru/category/zhenskaya-odezhda-7501/?category_was_predicted=true&color=100955527%2C100955536%2C100955534%2C100955535%2C100955529%2C100955546%2C100955530%2C100955532%2C100955547%2C100966307%2C100955542%2C100955544%2C100955545%2C100955528%2C100955541%2C100955540&deny_category_prediction=true&from_global=true&opened=color%2Cstyleapparel&styleapparel=100374527%2C277449&text=Женский+корсет')

        # Офис, классический, вечерний
        get_products_from_page('Корсет',
                               'https://www.ozon.ru/category/zhenskaya-odezhda-7501/?category_was_predicted=true&color=100955527%2C100955536%2C100955534%2C100955535%2C100955529%2C100955546%2C100955530%2C100955532%2C100955547%2C100966307%2C100955542%2C100955544%2C100955545%2C100955528%2C100955541%2C100955540&deny_category_prediction=true&from_global=true&opened=styleapparel%2Ccolor&styleapparel=55225%2C148380%2C57396&text=Женский+корсет')

        # Винтаж
        get_products_from_page('Корсет',
                               'https://www.ozon.ru/category/zhenskaya-odezhda-7501/?category_was_predicted=true&color=100955527%2C100955536%2C100955534%2C100955535%2C100955529%2C100955546%2C100955530%2C100955532%2C100955547%2C100966307%2C100955542%2C100955544%2C100955545%2C100955528%2C100955541%2C100955540&deny_category_prediction=true&from_global=true&opened=color%2Cstyleapparel&styleapparel=56425&text=Женский+корсет')

        # Коктейльное, Выпускное, свадебное, праздничное
        get_products_from_page('Корсет',
                               'https://www.ozon.ru/category/zhenskaya-odezhda-7501/?category_was_predicted=true&color=100955527%2C100955536%2C100955534%2C100955535%2C100955529%2C100955546%2C100955530%2C100955532%2C100955547%2C100966307%2C100955542%2C100955544%2C100955545%2C100955528%2C100955541%2C100955540&deny_category_prediction=true&from_global=true&opened=styleapparel%2Ccolor&styleapparel=164217%2C79761%2C101124545%2C106037&text=Женский+корсет')

        # Все категории, ЧЕРНОЕ
        get_products_from_page('Корсет',
                               'https://www.ozon.ru/category/zhenskaya-odezhda-7501/?category_was_predicted=true&color=100955526&deny_category_prediction=true&from_global=true&text=Женский+корсет')


    if Accessories == True:
    #АКСЕССУАРЫ
        #ОЧКИ
        get_products_from_page('Аксессуары',
                               'https://www.ozon.ru/category/ochki-solntsezashchitnye-zhenskie-17019/?category_was_predicted=true&deny_category_prediction=true&from_global=true&text=женские+аксессуары')
        #ДЛЯ ВОЛОС
        get_products_from_page('Аксессуары',
                               'https://www.ozon.ru/category/aksessuary-dlya-volos-zhenskie-17047/?category_was_predicted=true&deny_category_prediction=true&from_global=true&text=женские+аксессуары')

    if Blouse == True:
        get_products_from_page('Блузка',
                                 'https://www.ozon.ru/category/bluzy-i-rubashki-zhenskie-7511/?category_was_predicted=true&deny_category_prediction=true&from_global=true&text=Блузка+женская')


    if Shorts == True:
        #Деним
        get_products_from_page('Шорты',
                                 'https://www.ozon.ru/category/shorty-zhenskie-7514/?category_was_predicted=true&deny_category_prediction=true&from_global=true&materialfilterclothes=100960331&text=женские+шорты+джинсовые')
        # Бохо и восточный
        get_products_from_page('Шорты',
                               'https://www.ozon.ru/category/shorty-zhenskie-7514/?category_was_predicted=true&color=100955528%2C100955530%2C100955527%2C100955547%2C100955534%2C100966307%2C100955535%2C100955532%2C100955546%2C100955529%2C100966310%2C100955537%2C100955536%2C100955544%2C100955542%2C100955545%2C100955540&deny_category_prediction=true&from_global=true&styleapparel=100374527%2C277449&text=женские+шорты')

        # Офис, классический, вечерний
        get_products_from_page('Шорты',
                               'https://www.ozon.ru/category/shorty-zhenskie-7514/?category_was_predicted=true&color=100955528%2C100955530%2C100955527%2C100955547%2C100955534%2C100966307%2C100955535%2C100955532%2C100955546%2C100955529%2C100966310%2C100955537%2C100955536%2C100955544%2C100955542%2C100955545%2C100955540&deny_category_prediction=true&from_global=true&styleapparel=148380%2C55225%2C57396&text=женские+шорты')

        # Коктейльное, Выпускное, свадебное, праздничное
        get_products_from_page('Шорты',
                               'https://www.ozon.ru/category/shorty-zhenskie-7514/?category_was_predicted=true&color=100955528%2C100955530%2C100955527%2C100955547%2C100955534%2C100966307%2C100955535%2C100955532%2C100955546%2C100955529%2C100966310%2C100955537%2C100955536%2C100955544%2C100955542%2C100955545%2C100955540&deny_category_prediction=true&from_global=true&styleapparel=106037%2C164217%2C79761%2C101124545&text=женские+шорты')

        # Все категории, ЧЕРНОЕ
        get_products_from_page('Шорты',
                               'https://www.ozon.ru/category/shorty-zhenskie-7514/?category_was_predicted=true&color=100955526&deny_category_prediction=true&from_global=true&opened=color&text=женские+шорты+джинсовые')

    if Swimsuit == True:
        get_products_from_page('Купальник',
                                 'https://www.ozon.ru/category/kupalniki-i-plyazhnaya-odezhda-zhenskie-7540/?category_was_predicted=true&deny_category_prediction=true&from_global=true&text=Купальник+женский')
#
# get_products_from_page('Рубашка',
#                        'https://www.ozon.ru/category/bluzy-i-rubashki-zhenskie-7511/?category_was_predicted=true&color=100955526%2C100955530%2C100955534%2C100955546%2C100955528%2C100955547%2C100955535%2C100955537%2C100955532%2C100966307%2C100955536%2C100955529%2C100955542%2C100966310%2C100955545%2C100955544%2C100955541%2C101097990%2C100955540&deny_category_prediction=true&from_global=true&opened=color&text=Женские+рубашки')

# get_products_from_page('Украшения',
#                        'https://www.ozon.ru/category/bizhuternye-ukrasheniya-zhenskie-17022/?from_global=true&text=%3Atycrbt+erhfitybz+%2Cb%3Benthbz')
