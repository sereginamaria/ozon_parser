import undetected_chromedriver
from selenium.webdriver.common.by import By
import time
import json
from pprint import pprint

try:
    driver = undetected_chromedriver.Chrome()
    response = driver.get("https://www.ozon.ru/api/entrypoint-api.bx/page/json/v2?url=/product/plate-tvoe-923426779/")
    # time.sleep(1)

    content = driver.find_element(By.TAG_NAME, 'pre').text.replace(u'\u2009', ' ')
    parsed_json = json.loads(content)
    parsed_data_json = parsed_json["widgetStates"]

    keys_to_save_list = ['webCharacteristics-545750-default-1', 'webBrand-1033259-default-1', 'webAspects-418189-default-1', 'webModelParams-581523-default-1',
                          'breadCrumbs-1619260-default-1', 'webMarketingMarks-370546-default-1', 'webOzonAccountPrice-2136009-default-1', 'webGallery-1748356-default-1',
                          'webCurrentSeller-735663-default-1', 'webPrice-2136014-default-1', 'webProductHeading-943795-default-1']

    keys_to_save2 = ['breadcrumbs', 'aspects', 'id', 'name', 'link', 'characteristics', 'mainAdvantages', 'images', 'marks', 'textRs', 'priceTextRs', 'originalPrice', 'price', 'title']

    keys_to_save3 = ['text', 'priceTextRs', 'content', 'description', 'name', 'alt', 'src', 'mainAdvantages', 'short', 'variants']

    for key, v in list(parsed_data_json.items()):
        if key not in keys_to_save_list:
            parsed_data_json.pop(key)
        else:
            parsed_data_json[key] = json.loads(parsed_data_json[key])
            for key1, val in list(parsed_data_json[key].items()):
                if key1 not in keys_to_save2:
                    parsed_data_json[key].pop(key1)
                else:
                    if type(parsed_data_json[key][key1]) != int and type(parsed_data_json[key][key1]) != str:
                        for i in range(len(parsed_data_json[key][key1])):
                            for key4, val4 in list(parsed_data_json[key][key1][i].items()):
                                print(parsed_data_json[key][key1][i][key4])
                                if key4 not in keys_to_save3:
                                    print('1')
                                    parsed_data_json[key][key1][i].pop(key4)



    with open('new_file.json', 'w', encoding="utf-8") as outfile:
        json.dump(parsed_data_json, outfile, indent=4, sort_keys=True, ensure_ascii=False,separators=(',', ': '))

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()