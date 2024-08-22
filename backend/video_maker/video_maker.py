import os
import io
import imageio.v3 as imageio

def generate_video(cards_list):
    new_m = []
    for card in cards_list:
        i = 0
        while i != 10:
            new_m.append(imageio.imread(io.BytesIO(card)))
            i += 1

    # imageio.imwrite("./video_maker/output1.mp4", new_m, fps=5)
    path = imageio.imwrite("/home/masha/ozon_parser_new/backend/video_maker/output1.mp4", new_m, fps=5)
    image_b = open('./video_maker/output1.mp4', 'rb').read()
    os.remove('./video_maker/output1.mp4')

    return image_b


