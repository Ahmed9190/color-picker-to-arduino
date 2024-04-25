import serial
import time

ser = serial.Serial("COM3", 9600)


def send_to_arduino(cmyk):
    c, m, y, k = cmyk
    ser.write(f"{c},{m},{y},{k}\n".encode())
    time.sleep(2)

    line = ser.readline().decode("utf-8").strip()
    print(f"Received from Arduino: {line}")


# Test each color individually
send_to_arduino((100, 0, 0, 0))  # Cyan
time.sleep(2)
send_to_arduino((0, 100, 0, 0))  # Magenta
time.sleep(2)
send_to_arduino((0, 0, 100, 0))  # Yellow
time.sleep(2)
send_to_arduino((0, 0, 0, 100))  # Black
time.sleep(2)

ser.close()
