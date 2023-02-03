import serial
import time

serGrbl = serial.Serial("/dev/tty.usbmodem142301", 115200)
serServo = serial.Serial("/dev/tty.usbserial-14220", 9600)

# Grblを目覚めさせる
serGrbl.write("\r\n\r\n".encode())
time.sleep(2)
serGrbl.flushInput()

gcodeFirst = 'G00\nX2Y2'


gcode1 ='G00\nX0.4Y0.0'
gcode2 ='G00\nX0.4Y0.4'
gcode3 ='G00\nX0.0Y0.4'
gcode4 ='G00\nX0.0Y0.0'

# Gcodeを送る
serServo.write(b"N")
time.sleep(2)
serGrbl.write(gcodeFirst.encode() + str.encode('\n'))
time.sleep(1)
serServo.write(b"G")
time.sleep(1)
serGrbl.write(gcode1.encode() + str.encode('\n'))
time.sleep(1)
serServo.write(b"R")
time.sleep(1)
serGrbl.write(gcode2.encode() + str.encode('\n'))
time.sleep(1)
serServo.write(b"G")
time.sleep(1)
serGrbl.write(gcode3.encode() + str.encode('\n'))
time.sleep(1)
serServo.write(b"R")
time.sleep(1)
serGrbl.write(gcode4.encode() + str.encode('\n'))
time.sleep(1)
serServo.write(b"N")
time.sleep(1)
