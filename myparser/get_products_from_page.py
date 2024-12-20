from bs4 import BeautifulSoup
import itertools

from selenium.webdriver.common.by import By

from myparser.get_product import get_product
import undetected_chromedriver as uc
from myparser import parser_requests
import time
from selenium.webdriver.chrome.options import Options
from selenium_stealth import stealth

telegram_url = "https://api.telegram.org/bot6508472057:AAHdRDqUbaVjn7sstEtnHPMmKAXXAPp6_og"

def get_products_from_page(publication_category, url):
    # Ограничим парсинг первыми n страницами
    print('Start get_products_from_page')
    parser_requests.wait()
    global category
    category = publication_category
    MAX_PAGE = 4
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
    # options1.headless = False
    # options1.add_argument('--headless')
    # options1.add_argument('--headless=new')
    options1.add_argument('--no-sandbox')
    options1.add_argument('--disable-dev-shm-usage')

    options1.add_argument("--disable-extensions")
    options1.add_argument('--disable-application-cache')
    options1.add_argument("--disable-setuid-sandbox")
    options1.add_argument("--disable-gpu")
    options1.add_argument("--remote-allow-origins=*")
    options1.add_argument("--log-path=/home/masha/chromelogs")
    options1.add_argument("--disable-dev-shm-usage")
    options1._session = None

    # options1.binary_location = '/home/masha/ozon_parser/chromedriver/chrome-linux64/chrome'
    options1.binary_location = '/home/masha/ozon_parser/chromedriver/chrome117/chrome-linux64/chrome'
    # options1.binary_location = '/home/masha/ozon_parser/chromedriver/chrome-headless-shell-linux64/chrome-headless-shell'
    print('before Chrome')

    driver = uc.Chrome(
        # driver_executable_path='/home/masha/ozon_parser/chromedriver/chromedriver-linux64/chromedriver',
        patcher_force_close=True, no_sandbox=True, suppress_welcome=True, use_subprocess=False,
        options=options1,
        log_level=10, headless=True, version_main=117)

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

    driver.save_screenshot('10.png')
    driver.refresh()

    #
    # html = driver.page_source
    # print(html)

    # content = driver.find_element(By.ID, 'reload-button')
    # print(content)
    #
    # content.click()

    driver.execute_script("window.scrollTo(5,4000);")
    driver.save_screenshot('11.png')
    time.sleep(10)

    print('after scroll')
    html = driver.page_source
    # print(html)
    # time.sleep(3)

    driver.close()
    driver.quit()
    get_urls(html)


def parse_data(html):
    print('parse_data')
    soup = BeautifulSoup(html, 'html.myparser')
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

    if len(all_links) == 36:
        for link in all_links:
            message_type = False
            get_product(link, category, message_type)
    else:
        text = ('Ошибка! Со страницы определилось ' + str(len(all_links)) +
                ' ссылок. Повторите попытку.')

        parser_requests.error(text)

    message_type = True
    parser_requests.execution_completed(message_type)
    print('End get_products_from_page')