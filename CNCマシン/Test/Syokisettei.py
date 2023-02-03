import serial
import time

serGrbl = serial.Serial("/dev/tty.usbmodem142301", 115200)
serServo = serial.Serial("/dev/tty.usbserial-14220", 9600)

# Grblを目覚めさせる
serGrbl.write("\r\n\r\n".encode())
time.sleep(2)
serGrbl.flushInput()

gcodeFirst = 'G00\nX2Y2.25'

serServo.write(b"N")
serGrbl.write(gcodeFirst.encode() + str.encode('\n'))
time.sleep(3)
