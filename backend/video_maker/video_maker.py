import os
import io
import imageio.v3 as imageio
from video_maker import logger

def generate_video(cards_list):
    logger.info('Start generate_video')
    new_cards_list = []
    for card in cards_list:
        i = 0
        while i != 10:
            new_cards_list.append(imageio.imread(io.BytesIO(card)))
            i += 1

    # imageio.imwrite("./video_maker/output1.mp4", new_cards_list, fps=5)
    path = imageio.imwrite("/home/masha/ozon_parser_new/backend/video_maker/output1.mp4", new_cards_list, fps=5)
    image_b = open('./video_maker/output1.mp4', 'rb').read()
    os.remove('./video_maker/output1.mp4')

    logger.info('End generate_video')
    return image_b


