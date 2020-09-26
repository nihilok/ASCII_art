import os
import datetime

import PIL.Image

ASCII_chars = ['@', '#', 'S', '%', '*', '+', ';', ':', ',', '.', '`']


def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width / 1.65
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image


def greyify(image):
    greyscale_image = image.convert('L')
    return greyscale_image


def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = ''.join([ASCII_chars[pixel // 25] for pixel in pixels])
    return characters


def date_stamp():
    return datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
# c:\Users\Michael\Desktop\illum.jpg


def main(path, new_width=100):
    try:
        image = PIL.Image.open(path)
    except:
        return path, ' is not a valid pathname to an image.'

    new_image_data = pixels_to_ascii(greyify(resize_image(image)))
    pixel_count = len(new_image_data)
    ascii_image = '\n'.join(new_image_data[i:(i + new_width)] for i in range(0, pixel_count, new_width))

    return ascii_image