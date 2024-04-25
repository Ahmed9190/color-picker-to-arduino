from serial import Serial
from constants import ENTER_ASCII_CODE
import cv2
from arduino_communication import send_to_arduino
from color_conversion import rgb_to_cmyk, get_color_name
from drawing import draw_color_square, draw_center_point

url = "http://192.168.1.18:4747/video"
cap = cv2.VideoCapture(url)
serial = Serial("COM3", 9600)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Couldn't capture frame")
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    h, w, _ = rgb_frame.shape
    center_pixel_color = rgb_frame[h // 2, w // 2]
    cmyk_color_double = rgb_to_cmyk(center_pixel_color)
    cmyk_color_int = tuple(map(int, cmyk_color_double))
    draw_color_square(frame, tuple(center_pixel_color))
    draw_center_point(frame)

    color_name = get_color_name(tuple(center_pixel_color))
    cv2.putText(
        frame,
        color_name,
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 255, 255),
        2,
        cv2.LINE_AA,
    )

    cv2.imshow("IP Camera", frame)

    key = cv2.waitKey(1)
    if key == ENTER_ASCII_CODE:

        send_to_arduino(cmyk_color_int, serial)
        print(f"CMYK Color Sent to Arduino: {cmyk_color_int}")

    elif key & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
serial.close()
