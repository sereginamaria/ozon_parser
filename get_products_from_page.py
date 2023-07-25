import undetected_chromedriver
import time
from get_urls import get_urls

def get_products_from_page(url):

    # Ограничим парсинг первыми n страницами
    MAX_PAGE = 1
    i = 1
    while i <= MAX_PAGE:
        filename = f'page_' + str(i) + '.html'
        if i == 1:
            UseSelenium(url, filename).save_page()
        else:
            url_param = url + '?page=' + str(i)
            UseSelenium(url_param, filename).save_page()

        i += 1


class UseSelenium:
    def __init__(self, url: str, filename: str):
        self.url = url
        self.filename = filename

    def save_page(self):
        try:
            driver = undetected_chromedriver.Chrome()

            driver.get(self.url)
            time.sleep(3)
            driver.execute_script("window.scrollTo(5,4000);")
            #time.sleep(5)
            html = driver.page_source
            with open('pages/' + self.filename, 'w', encoding='utf-8') as f:
                f.write(html)

            get_urls()
        except Exception as ex:
            print(ex)
        finally:
            driver.close()
            driver.quit()
