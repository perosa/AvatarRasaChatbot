import os, random
import logging


def list_files(path):
    files = os.listdir(path)

    images = [i for i in files if is_image(i)]

    logging.debug(f'images {images}')

    return images


def is_image(path):
    return path.endswith('.png') or path.endswith('.PGN') or path.endswith('.jpg') or path.endswith('.JPG')


def get_random_file(path):

    files = list_files(path)

    lower = 0
    upper = len(files) - 1
    if upper == -1:
        upper = 0

    i = random.randint(lower, upper)

    file = path + '/' + files[i]
    logging.info(f"Found {file}")

    return file
