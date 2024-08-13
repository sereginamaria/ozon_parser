import pytesseract
from PIL import Image
import io
import requests
from text_recognizer import config
def recognize_text(image_url):
    response = requests.get(image_url)
    path_to_tesseract = config.PATH_TO_TESSERACT
    tessdata_dir_config = config.PATH_TO_TESSDATA
    img = Image.open(io.BytesIO(response.content))
    pytesseract.tesseract_cmd = path_to_tesseract

    text = pytesseract.image_to_string(img, lang='rus+eng', config=tessdata_dir_config)

    if text == '':
        return image_url
    else:
        print('Есть текст')