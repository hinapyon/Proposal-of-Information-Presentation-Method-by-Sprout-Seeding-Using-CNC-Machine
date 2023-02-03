import serial
import time

serServo = serial.Serial("/dev/tty.usbserial-14230", 9600)

for i in range(4):
  serServo.write(b"r")
  time.sleep(0.3)
  serServo.write(b"N")
  time.sleep(1)
  serServo.write(b"g")
  time.sleep(0.3)
  serServo.write(b"N")
  time.sleep(1)

for i in range(2):
  serServo.write(b"R")
  time.sleep(0.3)
  serServo.write(b"N")
  time.sleep(1)
  serServo.write(b"G")
  time.sleep(0.3)
  serServo.write(b"N")
  time.sleep(1)
