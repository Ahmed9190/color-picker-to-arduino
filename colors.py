import cv2
import numpy as np
from sklearn.neighbors import NearestNeighbors

COLORS = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "yellow": (255, 255, 0),
    "cyan": (0, 255, 255),
    "magenta": (255, 0, 255),
    "black": (0, 0, 0),
    "white": (255, 255, 255),
    "orange": (255, 165, 0),
    "purple": (128, 0, 128),
    "pink": (255, 192, 203),
    "brown": (165, 42, 42),
    "olive": (128, 128, 0),
    "teal": (0, 128, 128),
    "navy": (0, 0, 128),
    "maroon": (128, 0, 0),
    "gray": (128, 128, 128),
    "lime": (0, 255, 0),
    "silver": (192, 192, 192),
    "gold": (255, 215, 0),
    "skyblue": (135, 206, 235),
    "lavender": (230, 230, 250),
    "indigo": (75, 0, 130),
    "turquoise": (64, 224, 208),
    "coral": (255, 127, 80),
}

LAB_COLORS = {
    name: cv2.cvtColor(np.uint8([[rgb]]), cv2.COLOR_RGB2LAB)[0][0]
    for name, rgb in COLORS.items()
}

nn_model = NearestNeighbors(n_neighbors=1, algorithm="ball_tree").fit(
    list(LAB_COLORS.values())
)
