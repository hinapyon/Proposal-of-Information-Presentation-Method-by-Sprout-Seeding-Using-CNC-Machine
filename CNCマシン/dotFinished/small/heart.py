import serial
import time

serGrbl = serial.Serial("/dev/tty.usbmodem142201", 115200)
serServo = serial.Serial("/dev/tty.usbserial-14230", 9600)

# Grblを目覚めさせる
serGrbl.write("\r\n\r\n".encode())
time.sleep(2)
serGrbl.flushInput()

gcodeFirst = 'G00\nX2.25Y2.35'

gcode1 ='G91\nX0.4Y0.0' #初期位置に行くために
gcode2 ='G91\nX-0.4Y0.25' #左斜め上
gcode3 ='G91\nX0.4Y0.25' #右斜め上
gcode4 ='G91\nX-0.4Y-0.25' #左斜め
gcode5 ='G91\nX0.4Y-0.25' #右斜め下
gcodeReset ='G90\nX0.0Y0.0'

# Gcodeを送る
#初期設定
serServo.write(b"N")
serGrbl.write(gcodeFirst.encode() + str.encode('\n'))
time.sleep(2)
serGrbl.write(gcode1.encode() + str.encode('\n'))

time.sleep(3)

#ここから書き始め
#左半分
serServo.write(b"R")
time.sleep(0.3)
serServo.write(b"N")
serGrbl.write(gcode2.encode() + str.encode('\n'))
time.sleep(1)
serServo.write(b"R")
time.sleep(0.3)
serServo.write(b"N")
serGrbl.write(gcode2.encode() + str.encode('\n'))
time.sleep(1)
serServo.write(b"R")
time.sleep(0.3)
serServo.write(b"N")
serGrbl.write(gcode3.encode() + str.encode('\n'))
time.sleep(1)
serServo.write(b"R")
time.sleep(0.3)
serServo.write(b"N")
serGrbl.write(gcode5.encode() + str.encode('\n'))
time.sleep(1)
serServo.write(b"R")
time.sleep(0.3)
serServo.write(b"N")
time.sleep(3)
#右半分
serServo.write(b"G")
time.sleep(0.3)
serServo.write(b"N")
serGrbl.write(gcode3.encode() + str.encode('\n'))
time.sleep(1)
serServo.write(b"G")
time.sleep(0.3)
serServo.write(b"N")
serGrbl.write(gcode5.encode() + str.encode('\n'))
time.sleep(1)
serServo.write(b"G")
time.sleep(0.3)
serServo.write(b"N")
serGrbl.write(gcode4.encode() + str.encode('\n'))
time.sleep(1)
serServo.write(b"G")
time.sleep(0.3)
serServo.write(b"N")
serGrbl.write(gcode4.encode() + str.encode('\n'))
time.sleep(1)
serServo.write(b"G")
time.sleep(0.3)
serServo.write(b"N")
time.sleep(3)

#初期位置に戻る
serGrbl.write(gcodeReset.encode() + str.encode('\n'))
