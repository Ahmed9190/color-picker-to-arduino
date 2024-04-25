import cv2
import numpy as np

from colors import nn_model, COLORS


def rgb_to_cmyk(rgb):
    r, g, b = rgb
    if r == g == b == 0:
        return 0, 0, 0, 100
    c = 1 - r / 255
    m = 1 - g / 255
    y = 1 - b / 255
    k = min(c, m, y)
    if k == 1:
        return 0, 0, 0, 100
    c = (c - k) / (1 - k)
    m = (m - k) / (1 - k)
    y = (y - k) / (1 - k)
    return c * 100, m * 100, y * 100, k * 100


def get_color_name(rgb):
    lab_color = cv2.cvtColor(np.uint8([[rgb]]), cv2.COLOR_RGB2LAB)[0][0]
    _, indices = nn_model.kneighbors([lab_color])
    nearest_color_name = list(COLORS.keys())[indices[0][0]]
    return nearest_color_name
