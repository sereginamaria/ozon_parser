import pytesseract
from PIL import Image
import io
import requests
from text_recognizer import config, logger
def recognize_text(image_url):
    response = requests.get(image_url)
    path_to_tesseract = config.PATH_TO_TESSERACT
    tessdata_dir_config = config.PATH_TO_TESSDATA

    try:
        img = Image.open(io.BytesIO(response.content))
        pytesseract.tesseract_cmd = path_to_tesseract

        text = pytesseract.image_to_string(img, lang='rus+eng', config=tessdata_dir_config)
        print(text)
        print(len(text))
        if text == '' or len(text) < 10:
            logger.info(f'No text in image {image_url}')
            return image_url
        else:
            logger.info(f'Text in image {image_url}')
    except:
        logger.info(f'Can not find image: {image_url}')

def recognize_text_server(image_url):
    response = requests.get(image_url)
    path_to_tesseract = config.PATH_TO_TESSERACT_SERVER
    tessdata_dir_config = config.PATH_TO_TESSDATA_SERVER

    try:
        img = Image.open(io.BytesIO(response.content))
        pytesseract.tesseract_cmd = path_to_tesseract

        text = pytesseract.image_to_string(img, lang='rus+eng', config=tessdata_dir_config)
        print(text)
        print(len(text))
        print(len(text) < 10)
        if text == '' or len(text) < 10:
            logger.info(f'No text in image {image_url}')
            return image_url
        else:
            logger.info(f'Text in image {image_url}')
    except:
        logger.info(f'Can not find image: {image_url}')