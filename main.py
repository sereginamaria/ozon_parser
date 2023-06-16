import undetected_chromedriver
import time
import json

try:
    driver = undetected_chromedriver.Chrome()
    #driver.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")
    response = driver.get("https://www.ozon.ru/api/entrypoint-api.bx/page/json/v2?url=/product/plate-tvoe-560721955/?asb=V4JBqdAITO1%252FxsJPEHJidk%252BRpUjJEhJUJ82VKaUTFq4%253D&asb2=eaWmaXTL-onw4EOIyuFdpQHq95AELbcEFAJjPe6qnMX4qTOh8G7H0vfeMjVceQ-n&avtc=1&avte=2&avts=1686903024&keywords=%D0%9B%D0%B5%D1%82%D0%BD%D0%B5%D0%B5+%D0%BF%D0%BB%D0%B0%D1%82%D1%8C%D0%B5&layout_container=pdpApparelPage2&layout_page_index=2&sh=chmEfcpKoQ")
    # time.sleep(15)

    print('djsvkn')
    # print(type(driver.page_source))
    # print(driver.page_source.json())

    newjson = json.loads(driver.page_source)
    print(newjson)



except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()