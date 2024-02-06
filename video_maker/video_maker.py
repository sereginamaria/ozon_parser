# importing libraries
import os
import cv2
import requests
from PIL import Image
# import moviepy.editor as moviepy

# from moviepy.editor import ImageSequenceClip
import imageio.v3 as imageio
telegram_url = "https://api.telegram.org/bot6508472057:AAHdRDqUbaVjn7sstEtnHPMmKAXXAPp6_og"


# Folder which contains all the images
# from which video is to be generated
# os.chdir("/home/masha/ozon_parser")
# path = "/home/masha/ozon_parser"



# num_of_images = len(os.listdir('.'))
#
# for file in os.listdir('.'):
#     im = Image.open(os.path.join(path, file))
#     width, height = im.size
    # im.show()   # uncomment this for displaying the image

def generate_video(text):
    # requests.post(
    #     url=telegram_url + '/sendMessage',
    #     data={'chat_id': 6181726421, 'text': str(text)}
    # ).json()

    requests.post(
        url=telegram_url + '/sendMessage',
        data={'chat_id': 6181726421, 'text': 'Видео создается, ожидайте...'}
    ).json()


    image_folder = '/home/masha/ozon_parser/card_creator/cards/'  # make sure to use your folder
    video_name = '/home/masha/ozon_parser/video_maker/video.mp4'
    # os.chdir("/home/masha/ozon_parser")

    images = []

    print(len(os.listdir(image_folder)))
    # requests.post(
    #     url=telegram_url + '/sendMessage',
    #     data={'chat_id': 6181726421, 'text': str(len(os.listdir(image_folder)))}
    # ).json()

    # for img in os.listdir(image_folder):
    #     if img in text:
    #         images.append(img)

    # images = [img for img in os.listdir(image_folder)
    #           if img.endswith(".jpg") or
    #           img.endswith(".jpeg") or
    #           img.endswith("png")]


    # Array images should only consider
    # the image files ignoring others if any

    for img_num in text:
        t = 'card' + str(img_num) + '.png'
        images.append(t)

    print(images)

    # requests.post(
    #     url=telegram_url + '/sendMessage',
    #     data={'chat_id': 6181726421, 'text': str(images)}
    # ).json()


    # frame = cv2.imread(''.join([image_folder, images[0]]))
    #
    #
    # # setting the frame width, height width
    # # the width, height of first image
    # height, width, layers = frame.shape
    #
    # fourcc = cv2.VideoWriter_fourcc(*'MP4V')
    # video = cv2.VideoWriter(video_name, fourcc, 0.5, (width, height))
    #
    # # Appending the images to the video one by one
    # for image in images:
    #     r = ''.join([image_folder, image])
    #     video.write(cv2.imread(r))
    #
    #
    # cv2.destroyAllWindows()
    # video.release()  # releasing the video generated

    new_m = []
    # for image in images:
    #     new_m.append(''.join([image_folder, image]))

    for image in images:
        k = ''.join([image_folder, image])
        # requests.post(
        #     url=telegram_url + '/sendMessage',
        #     data={'chat_id': 6181726421, 'text': str(k)}
        # ).json()

        i = 0
        while i != 10:
            new_m.append(imageio.imread(k))
            i+=1



    imageio.imwrite("/home/masha/ozon_parser/video_maker/output1.mp4", new_m, fps=5)



    # requests.post(
    #     url=telegram_url + '/sendMessage',
    #     data={'chat_id': 6181726421, 'text': 'Видео должно быьт готово'}
    # ).json()
#
# Calling the generate_video function
# generate_video()



