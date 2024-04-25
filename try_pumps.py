import serial
import time

from arduino_communication import send_to_arduino

serial = serial.Serial("COM3", 9600)


# Test each color individually
# send_to_arduino((0, 0, 0, 0), serial)  # Cyan
time.sleep(2)
send_to_arduino((100, 0, 0, 0), serial)  # Cyan
time.sleep(2)
send_to_arduino((0, 100, 0, 0), serial)  # Magenta
time.sleep(2)
send_to_arduino((0, 0, 100, 0), serial)  # Yellow
time.sleep(2)
send_to_arduino((0, 0, 0, 100), serial)  # Black
time.sleep(2)

serial.close()
