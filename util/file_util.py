import os, random


def list_files(path):
    files = os.listdir(path)

    images = [i for i in files if is_image(path)]

    return images


def is_image(path):
    return path.endswith('.png') or path.endswith('.PGN') or path.endswith('.jpg') or path.endswith('.JPG')


def get_random_file(path):
    files = list_files(path)
    i = random.randint(0, len(files) - 1)

    return files[i]
