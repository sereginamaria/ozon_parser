import undetected_chromedriver
from selenium.webdriver.common.by import By
import time
import json


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
            time.sleep(5)
            html = driver.page_source
            with open('pages/' + self.filename, 'w', encoding='utf-8') as f:
                f.write(html)
        except Exception as ex:
            print(ex)
        finally:
            driver.close()
            driver.quit()


try:

    # time.sleep(1)
    url = "https://www.ozon.ru/category/platya-zhenskie-7502/"
    # Ограничим парсинг первыми 10 страницами
    MAX_PAGE = 2
    i = 1
    while i <= MAX_PAGE:
        filename = f'page_' + str(i) + '.html'
        if i == 1:
            UseSelenium(url, filename).save_page()
        else:
            url_param = url + '?page=' + str(i)
            UseSelenium(url_param, filename).save_page()

        i += 1


    # driver.execute_script("window.scrollTo(5,4000);")
    # time.sleep(5)
    # html = driver.page_source
    #
    # print(html)
    # with open('pages/' + self.filename, 'w', encoding='utf-8') as f:
    #     f.write(html)
    #
    # content = driver.find_element(By.TAG_NAME, 'pre').text.replace(u'\u2009', ' ')
    # parsed_json = json.loads(content)
    #
    # with open('new_file_category.json', 'w', encoding="utf-8") as outfile:
    #     json.dump(parsed_json, outfile, indent=4, sort_keys=True, ensure_ascii=False,separators=(',', ': '))

except Exception as ex:
    print(ex)
finally:
    print('final')