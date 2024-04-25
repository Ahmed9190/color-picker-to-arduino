import serial
import time

from arduino_communication import send_to_arduino

ser = serial.Serial("COM3", 9600)


# Test each color individually
send_to_arduino((100, 0, 0, 0), ser)  # Cyan
time.sleep(2)
send_to_arduino((0, 100, 0, 0), ser)  # Magenta
time.sleep(2)
send_to_arduino((0, 0, 100, 0), ser)  # Yellow
time.sleep(2)
send_to_arduino((0, 0, 0, 100), ser)  # Black
time.sleep(2)

ser.close()
