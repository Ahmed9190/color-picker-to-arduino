import cv2


def draw_color_square(frame, color):
    square_size = 100
    top_right_corner = (frame.shape[1] - square_size, 0)
    bottom_left_corner = (frame.shape[1], square_size)

    b, g, r = map(int, color[::-1])

    cv2.rectangle(frame, top_right_corner, bottom_left_corner, (b, g, r), -1)


def draw_center_point(frame):
    center = (frame.shape[1] // 2, frame.shape[0] // 2)
    cv2.circle(frame, center, 3, (255, 255, 255), -1)
