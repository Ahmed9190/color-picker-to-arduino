import serial
import time

ser = serial.Serial("COM3", 9600)


def send_to_arduino(cmyk):
    c, m, y, k = cmyk
    ser.write(f"{c},{m},{y},{k}\n".encode())
    time.sleep(2)

    line = ser.readline().decode("utf-8").strip()
    print(f"Received from Arduino: {line}")


send_to_arduino((100, 0, 0, 0))  # Cyan
send_to_arduino((0, 100, 0, 0))  # Magenta
send_to_arduino((0, 0, 100, 0))  # Yellow
send_to_arduino((0, 0, 0, 100))  # Black

ser.close()
