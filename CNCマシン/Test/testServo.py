import serial
import time

serServo = serial.Serial("/dev/tty.usbserial-14230", 9600)

serServo.write(b"N")
time.sleep(3)
serServo.write(b"G")
time.sleep(3)
serServo.write(b"R")
time.sleep(3)
serServo.write(b"N")
