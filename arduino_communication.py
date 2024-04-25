import time


def send_to_arduino(cmyk, serial):
    c, m, y, k = cmyk
    serial.write(f"{{{c},{m},{y},{k}}}\n".encode())
    time.sleep(0.1)
