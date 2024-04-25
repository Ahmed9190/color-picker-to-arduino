from serial import Serial
import time

ser = Serial("COM3", 9600)


def send_to_arduino(cmyk, serial=ser):
    c, m, y, k = cmyk
    serial.write(f"{c},{m},{y},{k}\n".encode())
    time.sleep(0.1)
