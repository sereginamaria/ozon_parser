from PIL import Image, ImageDraw, ImageFont, ImageChops
import requests

def made_png(product_images):
    #Создание картинки
    new_img = Image.new('RGB', (1024, 1280), 'white')

    new_product_images = product_images.split(',')

    img_url0 = new_product_images[0]
    img_url1 = new_product_images[1]
    img_url2 = new_product_images[2]
    img_url10 = new_product_images[10]

    #Добавление картинки по url
    resp0 = requests.get(img_url0, stream=True).raw
    img0 = Image.open(resp0)
    resp1 = requests.get(img_url1, stream=True).raw
    img1 = Image.open(resp1)
    resp2 = requests.get(img_url2, stream=True).raw
    img2 = Image.open(resp2)
    resp10 = requests.get(img_url10, stream=True).raw
    img10 = Image.open(resp10)

    result0 = ImageChops.difference(img0, img0)
    result = ImageChops.difference(img0, img1)
    result1 = ImageChops.difference(img0, img10)
    # result.show()
    if len(set(ImageChops.difference(img0, img1).getdata())) > 100:
        print(len(set(ImageChops.difference(img0, img0).getdata())))
        print(len(set(ImageChops.difference(img0, img1).getdata())))
        print(len(set(ImageChops.difference(img0, img10).getdata())))
    print(result.getdata())
    print(result1.getdata())
    # #Изменение размера
    # width, height = img0.size
    # new_width = 380  # ширина
    # new_height = int(new_width * height / width)
    #
    # img0 = img0.resize((new_width, new_height))
    #
    # #Обрезка картинки
    # img0 = img0.crop((0, 80, 200, 400))
    #
    # # Добавление фотки на фон
    # new_img.paste(img0, (500, 0))
    # new_img.paste(img1, (550, 500))
    # new_img.paste(img2, (0, 999))
    #
    # #Добавление текста
    # font = ImageFont.load_default()
    # pencil = ImageDraw.Draw(new_img)
    # pencil.text((100, 100), 'Hello World', font=font, fill='blue', size=36)
    #
    # new_img.show()
