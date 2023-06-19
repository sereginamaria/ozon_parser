import copy

import undetected_chromedriver
from selenium.webdriver.common.by import By
import time
import json
from pprint import pprint

# try:
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

new_dict = copy.deepcopy(parsed_data_json)
from pprint import pprint
# for key, v in parsed_data_json.items():
#     if key not in keys_to_save_list:
#         new_dict.pop(key)
#         # pass
#     else:
#         str_data = json.loads(parsed_data_json[key])
#         new_dict[key] = str_data
#         for key1, val in str_data.items():
#             if key1 not in keys_to_save2:
#                 # pass
#                 new_dict[key].pop(key1)
#             else:
#                 str_data2 = str_data[key1]
#                 if type(str_data2) == list:
#                     for object in str_data2:
#                         for key4, val4 in object.items():
#                             print(object[key4])
#                             if key4 not in keys_to_save3:
#                                 print('1')
#                                 # object.pop(key4)
#
d1 = {k:json.loads(v) for k, v in parsed_data_json.items() if k in keys_to_save_list}
# pprint(d1)
d2 = {}

for k1, v1 in d1.items():
    d2[k1] = {}
    for k2, v2 in v1.items():
        if k2 not in keys_to_save2:
            continue
        if type(v2) == list:
            d2[k1][k2] = []
            for object in v2:
                if type(object) == dict:
                    for k3, v3 in object.items():
                        if k3 in keys_to_save3:
                            d2[k1][k2].append({k3: v3})

        else:
            d2[k1][k2] = v2
pprint(d2)






with open('new_file.json', 'w', encoding="utf-8") as outfile:
    outfile.write(json.dumps(d2, indent=4, sort_keys=True, ensure_ascii=False,separators=(',', ': ')))
    # outfile.write(json.dumps(parsed_data_json, indent=4, sort_keys=True, ensure_ascii=False,separators=(',', ': ')))

# except Exception as ex:
#     print(ex)
# finally:
#     driver.close()
#     driver.quit()