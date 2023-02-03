import serial
import time

serGrbl = serial.Serial("/dev/tty.usbmodem142301", 115200)
serServo = serial.Serial("/dev/tty.usbserial-14220", 9600)

# Grblを目覚めさせる
serGrbl.write("\r\n\r\n".encode())
time.sleep(2)
serGrbl.flushInput()

gcodeFirst = 'G00\nX2.2Y2.5'

gcode1 ='G91\nX0.5Y0.0'
gcode2 ='G91\nX-0.75Y0.5'
gcode3 ='G91\nX0.375Y0.25'
gcode4 ='G91\nX0.375Y-0.25'
gcode5 ='G91\nX0.375Y0.25'
gcode6 ='G91\nX0.375Y-0.25'
gcode7 ='G91\nX-0.75Y-0.5'
gcodeReset ='G90\nX0.0Y0.0'

# Gcodeを送る
#初期設定
serServo.write(b"N")
serGrbl.write(gcodeFirst.encode() + str.encode('\n'))
serGrbl.write(gcode1.encode() + str.encode('\n'))
time.sleep(3)



#ここから書き始め
#左半分
serServo.write(b"R")
time.sleep(1)
serGrbl.write(gcode2.encode() + str.encode('\n'))
time.sleep(1)
serGrbl.write(gcode3.encode() + str.encode('\n'))
time.sleep(1)
serGrbl.write(gcode4.encode() + str.encode('\n'))
time.sleep(0.5)
serServo.write(b"N")
time.sleep(2)

#右半分
serServo.write(b"G")
time.sleep(1)
serGrbl.write(gcode5.encode() + str.encode('\n'))
time.sleep(1)
serGrbl.write(gcode6.encode() + str.encode('\n'))
time.sleep(1)
serGrbl.write(gcode7.encode() + str.encode('\n'))
time.sleep(0.5)
serServo.write(b"N")
time.sleep(2)

#初期位置に戻る
serGrbl.write(gcodeReset.encode() + str.encode('\n'))
