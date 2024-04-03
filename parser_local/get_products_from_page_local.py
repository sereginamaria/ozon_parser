from bs4 import BeautifulSoup
import itertools

from selenium.webdriver.common.by import By

from parser_local.get_product_local import get_product
# from parser.get_product import get_product
import undetected_chromedriver as uc
import time
from selenium.webdriver.chrome.options import Options
from selenium_stealth import stealth

telegram_url = "https://api.telegram.org/bot6508472057:AAHdRDqUbaVjn7sstEtnHPMmKAXXAPp6_og"

def get_products_from_page(publication_category, url):
    # Ограничим парсинг первыми n страницами
    print('Start get_products_from_page')
    global category
    category = publication_category
    MAX_PAGE = 1
    i = 1
    while i <= MAX_PAGE:
        if i == 1:
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
        itertools.chain(*[div.find_all('a') for div in soup.find('div').find_all(attrs={'class', 'wi3'})]))])
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
    # for i in range(5):
    #     i += 1
    #
    #     #Просто верхняя одежда
    #     get_products_from_page('Верхняя Одежда',
    #                                'https://www.ozon.ru/category/verhnyaya-odezhda-zhenskaya-7528/?category_was_predicted=true&deny_category_prediction=true&from_global=true&season=64979&text=верхняя+одежда+женская')
    #
    #     #Куртка весенняя
    #     get_products_from_page('Верхняя Одежда',
    #                                'https://www.ozon.ru/category/zhenskaya-odezhda-7501/?category_was_predicted=true&deny_category_prediction=true&from_global=true&text=Женская+весенняя+куртка')
    #
    #     #Плащ
    #     get_products_from_page('Верхняя Одежда',
    #                            'https://www.ozon.ru/category/zhenskaya-odezhda-7501/?category_was_predicted=true&deny_category_prediction=true&from_global=true&text=Женский+весенний+плащ')
    #
    #     #Пальто
    #     get_products_from_page('Верхняя Одежда',
    #                            'https://www.ozon.ru/category/zhenskaya-odezhda-7501/?category_was_predicted=true&deny_category_prediction=true&text=женское+весеннее+пальто')
    #
        # #Бомбер
        # get_products_from_page('Верхняя Одежда',
        #                        'https://www.ozon.ru/category/zhenskaya-odezhda-7501/?category_was_predicted=true&deny_category_prediction=true&from_global=true&text=Женский+бомбер')
    #
    #     #Дубленка
    #     get_products_from_page('Верхняя Одежда',
    #                            'https://www.ozon.ru/category/zhenskaya-odezhda-7501/?text=Женская+весенняя+дубленка')

    # for i in range(5):
    #     i += 1
    #     #Лонгслив
    #     get_products_from_page('Кофта',
    #                            'https://www.ozon.ru/category/zhenskaya-odezhda-7501/?category_was_predicted=true&deny_category_prediction=true&from_global=true&text=Лонгслив+женский')

    # #Джемпер
    # get_products_from_page('Кофта',
    #                        'https://www.ozon.ru/category/zhenskaya-odezhda-7501/?text=Женский+джемпер')

        # Лонгслив
        # get_products_from_page('Кофта',
        #                        'https://www.ozon.ru/category/zhenskaya-odezhda-7501/?category_was_predicted=true&deny_category_prediction=true&from_global=true&text=Лонгслив+женский')

        # Лонгслив
        # get_products_from_page('Кофта',
        #                        'https://www.ozon.ru/category/zhenskaya-odezhda-7501/?category_was_predicted=true&deny_category_prediction=true&from_global=true&text=Лонгслив+женский')


    #
    # get_products_from_page('Рубашка',
    #                        'https://www.ozon.ru/category/bluzy-i-rubashki-zhenskie-7511/?category_was_predicted=true&color=100955526%2C100955530%2C100955534%2C100955546%2C100955528%2C100955547%2C100955535%2C100955537%2C100955532%2C100966307%2C100955536%2C100955529%2C100955542%2C100966310%2C100955545%2C100955544%2C100955541%2C101097990%2C100955540&deny_category_prediction=true&from_global=true&opened=color&text=Женские+рубашки')

    # get_products_from_page('Топ',
    #                        'https://www.ozon.ru/category/mayki-i-topy-zhenskie-7506/?category_was_predicted=true&deny_category_prediction=true&from_global=true&opened=styleapparel&styleapparel=57396%2C56425%2C164217&text=топ+женский')
    #
    # get_products_from_page('Платье',
    #                        'https://www.ozon.ru/category/platya-zhenskie-7502/?category_was_predicted=true&color=100955530%2C100955540%2C100955527%2C100955534%2C100955535%2C100955528%2C100955546%2C100955532%2C100955547%2C100955537%2C100955529%2C100966307%2C100966310%2C100955545%2C100955544%2C100955541%2C101097990%2C100955542&deny_category_prediction=true&from_global=true&opened=color&season=64979%2C31829&text=платье+женское')

    # get_products_from_page('Сумка',
    #                        'https://www.ozon.ru/category/sumki-na-plecho-zhenskie-17002/?category_was_predicted=true&color=100955529%2C100955527%2C100955542%2C100955546%2C100955534%2C100955540%2C100955530%2C100955535%2C100966307%2C100955537%2C100955532%2C100955547%2C100955536%2C100966310%2C100955545%2C100955544%2C100955541%2C101097990%2C100955528&deny_category_prediction=true&from_global=true&opened=color&text=Сумка+женская')
    #
    # get_products_from_page('Украшения',
    #                        'https://www.ozon.ru/category/bizhuternye-ukrasheniya-zhenskie-17022/?from_global=true&text=%3Atycrbt+erhfitybz+%2Cb%3Benthbz')
    #
    # get_products_from_page('Костюм',
    #                      'https://www.ozon.ru/category/kostyumy-i-komplekty-odezhdy-zhenskie-7536/?category_was_predicted=true&deny_category_prediction=true&from_global=true&opened=styleapparel&styleapparel=55228%2C55225%2C148380%2C57396%2C56425%2C164217%2C100374527%2C101124545%2C106037&text=Костюм+женский')
    #
    # get_products_from_page('Юбка',
    #                        'https://www.ozon.ru/category/yubki-zhenskie-7504/?category_was_predicted=true&deny_category_prediction=true&from_global=true&text=Юбка+женская')

    # get_products_from_page('Обувь',
    #                        'https://www.ozon.ru/category/zhenskaya-obuv-7640/?category_was_predicted=true&deny_category_prediction=true&from_global=true&text=женская+обувь+на+весну')
    #
    # #Обувь, тип кроссовки, кеды
    # get_products_from_page('Обувь',
    #                        'https://www.ozon.ru/category/zhenskaya-obuv-7640/?category_was_predicted=true&deny_category_prediction=true&from_global=true&opened=type&text=Обувь+женская+весенняя&type=31863%2C31953%2C100214566%2C57295')
    #
