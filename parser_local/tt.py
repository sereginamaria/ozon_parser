import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By


def print_hi():
    # driver = uc.Chrome()
    #
    # driver.get("https://www.ozon.ru/api/entrypoint-api.bx/page/json/v2?url=/product/kurtka-be-stars-1249221472/")
    # time.sleep(10)
    # content = driver.find_element(By.TAG_NAME, 'pre').text.replace(u'\u2009', ' ')
    # print(content)
    # driver.close()
    # driver.quit()


    options1 = uc.ChromeOptions()
    options1.add_argument("--headless")
    options1.add_argument('--headless=new')
    options1.add_argument('--no-sandbox')
    options1.add_argument('--disable-dev-shm-usage')

    driver1 = uc.Chrome()

    driver1.get("https://www.ozon.ru/search/?text=23+февраля+подарок+прикольный&from_global=true")
    time.sleep(5)

    # content = driver1.find_element(By.TAG_NAME, 'pre').text.replace(u'\u2009', ' ')
    # print(content)

    driver1.close()
    driver1.quit()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

