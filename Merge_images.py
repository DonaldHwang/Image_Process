from PIL import Image
import os

# Create a new 1000 * 1000 image
image = Image.new('RGB', (1000, 1000), 'white')
image.save('C:\\Users\\94983\\Desktop\\image_process\\white_image.jpg')


def change_resolution():
    i = 0
    old_images = os.listdir('C:\\Users\\94983\\Desktop\\image_process\\oldImage')
    for images in old_images:
        temp_image = Image.open('C:\\Users\\94983\\Desktop\\image_process\\oldImage\\' + images)
        temp = temp_image.resize((250, 250))  # 修改分辨率
        temp.save('C:\\Users\\94983\\Desktop\\image_process\\newImage\\' + str(i) + '.jpg')
        i += 1

    image_list = []
    i = 0
    new_images = os.listdir('C:\\Users\\94983\\Desktop\\image_process\\newImage')
    for image_file in new_images:
        temp_file = Image.open('C:\\Users\\94983\\Desktop\\image_process\\newImage\\' + image_file)
        image_list.append(temp_file)
        i += 1
    return image_list


def add_image(new_image):
    big_image = Image.open('C:\\Users\\94983\\Desktop\\image_process\\white_image.jpg')
    a = 0
    # 修改图像个数循环
    for m in range(0, 4, 1):
        for n in range(0, 4, 1):
            big_image.paste(new_image[a], (m * 250, n * 250))  # 修改图像滑动距离
            a += 1
    big_image.save('C:\\Users\\94983\\Desktop\\new_image.jpg')


if __name__ == "__main__":
    add_image(change_resolution())
