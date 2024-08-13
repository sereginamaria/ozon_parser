import pytesseract
import cv2
import matplotlib.pyplot as plt
from PIL import Image
import io
from urllib.request import urlopen
import requests
from text_recognizer import config
def recognize_text(image_url):
    print(image_url)
    text = ''
    response = requests.get(image_url)
    # add path to tesseract
    path_to_tesseract = config.PATH_TO_TESSERACT
    tessdata_dir_config = config.PATH_TO_TESSDATA
    # print(tessdata_dir_config)

    img = Image.open(io.BytesIO(response.content))
    pytesseract.tesseract_cmd = path_to_tesseract
    #
    # config_options = ['-c', 'psm 6', '-c', 'oem 3', '-c', config.PATH_TO_TESSDATA]
    #
    # # Set configuration options
    # custom_config = r'--psm 0'
    # custom_config += r'--oem 2' # page segmenation mode: assume a single uniform block of vertically aligned text of varying sizes.
    # custom_config += config.PATH_TO_TESSDATA  # language
    # custom_config += r' -l eng'  # language
    # custom_config += r' -l rus'  # language

    text = pytesseract.image_to_string(img, lang='rus+eng', config=tessdata_dir_config)

    # # custom_config1 = r'--psm 0'
    # # custom_config1 += r'--oem 2'  # page segmenation mode: assume a single uniform block of vertically aligned text of varying sizes.
    # # custom_config1 += config.PATH_TO_TESSDATA  # language
    # # custom_config1 += r' -l eng'  # language
    # # custom_config1 += r' -l rus'  # language
    # #
    # text1 = pytesseract.image_to_string(img, lang='rus+eng', config='--oem 2 --psm 3')

    # печатаем
    print(text)
    # print(text1)

    if text == '':
        print('Нет текста')
        return image_url
    else:
        print('Усть текст')

    # if text1 == '':
    #     print('Нет текста111111111111111111111111111111111')
    #     return image_url
    # else:
    #     print('Усть текст1111111111111111111111111111111111111')