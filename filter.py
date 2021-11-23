from PIL import Image
import numpy as np


def do_mosaic(img, size, num_grey):
    """
    Самый главный метод. Принимает старую картинку и возвращает новую.

    :param img
    :param size: int
    :param num_grey: int
    """
    for x in range(0, len(img), size):
        for y in range(0, len(img[0]), size):
            img[x:x + size, y:y + size] = find_average(
                img[x:x + size, y:y + size], size, num_grey)
    return img


def find_average(img_part, size, num_grey):
    """
    Метод вызывается для нахождения среднего цвета, которым в дальнейшем будет заполнена новая ячейка мозаики

    :param img_part
    :param size: int
    :param num_grey: int

    >>> find_average([[238, 222, 199], [238, 222, 199], [238, 222, 199],  [238, 222, 199], [238, 222, 199],
    [238, 222, 199], [238, 222, 199], [238, 222, 199], [238, 222, 199]], 10, 5)
    215

    >>> find_average([[215, 208, 200], [215, 208, 200], [216, 209, 203], [216, 209, 203], [216, 209, 203],
    [216, 209, 203], [216, 209, 203], [216, 209, 203], [216, 209, 203]], 10, 5)
    205

    >>> find_average([[173, 172, 186], [173, 172, 186], [173, 172, 186], [173, 172, 186], [172, 171, 185],
    [172, 171, 185], [172, 171, 185], [172, 171, 185], [171, 170, 184]], 10, 5)
    175
    """
    average_color = (img_part[:size, :size].sum() / 3) // size ** 2
    return int(average_color // num_grey) * num_grey


np.seterr(over='ignore')
source_img = Image.open(input("Введите имя файла, которое хотите конвертировать: "))
mosaic_size = int(input("Введите размер мозаики: "))
grey = int(input("Введите количество градаций серого: "))

img_code = np.array(source_img)
grey_size = 255 // grey

res = Image.fromarray(do_mosaic(img_code, mosaic_size, grey_size))
res.save(input("Введите имя файла, в которой хотите сохранить результат: "))
