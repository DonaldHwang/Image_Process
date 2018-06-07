from PIL import Image
import os

water_mark = Image.open('C:\\Users\\94983\\Desktop\\image_process\\watermark.png')


def get_image():
    image_list = []
    old_images = os.listdir('C:\\Users\\94983\\Desktop\\image_process\\watermarker')
    for image in old_images:
        image_list.append(image)
    return image_list


def put_watermark(images):
    for image in images:
        image_to_be_marked = Image.open("C:\\Users\\94983\\Desktop\\image_process\\watermarker\\" + image)
        new = water_mark.resize(image_to_be_marked.size)
        image_to_be_marked.paste(new, (0, 0))
        image_to_be_marked.save("C:\\Users\\94983\\Desktop\\image_process\\watermarker\\new" + image)


if __name__ == "__main__":
    im = get_image()
    put_watermark(im)
