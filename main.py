import undetected_chromedriver
import time
import json

from selenium.webdriver.common.by import By

try:
    driver = undetected_chromedriver.Chrome()
    #driver.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")
    response = driver.get("https://www.ozon.ru/api/entrypoint-api.bx/page/json/v2?url=/product/plate-tvoe-560721955/")
    # time.sleep(1)

    # print('djsvkn')
    # print(type(driver.page_source))

    from pprint import pprint
    # pprint(driver.page_source)

    content = driver.page_source.replace(u'\u2009', ',')
    content = driver.find_element(By.TAG_NAME, 'pre').text.replace(u'\u2009', ' ')
    parsed_json = json.loads(content)
    # print(type(parsed_json))
    # print(parsed_json)
    #pre = driver.find_element_by_tag_name("pre").text

    with open('new_file.json', 'w', encoding="utf-8") as outfile:
        json.dump(parsed_json, outfile, indent=4, sort_keys=False, ensure_ascii=False,separators=(',', ': '))
    # print(type(driver.page_source))
    # print(driver.page_source.json())

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()