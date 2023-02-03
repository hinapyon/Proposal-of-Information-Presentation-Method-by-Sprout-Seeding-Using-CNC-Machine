import serial
import time

serGrbl = serial.Serial("/dev/tty.usbmodem142201", 115200)

# Grblを目覚めさせる
serGrbl.write("\r\n\r\n".encode())
time.sleep(2)
serGrbl.flushInput()

gcodeFirst = 'G00\nX2.25Y2.5'

gcode1 ='G91\nX0.5Y0.0' #初期位置に行くために
gcode2 ='G91\nX-0.25Y0.25' #左斜め上
gcode3 ='G91\nX0.25Y0.25' #右斜め上
gcode4 ='G91\nX-0.25Y-0.25' #左斜め下
gcode5 ='G91\nX0.25Y-0.25' #右斜め下
gcodeReset ='G90\nX0.0Y0.0'

# Gcodeを送る
#初期設定
serGrbl.write(gcodeFirst.encode() + str.encode('\n'))
time.sleep(3)
serGrbl.write(gcode1.encode() + str.encode('\n'))
time.sleep(3)


#ここから書き始め
#左半分
serGrbl.write(gcode2.encode() + str.encode('\n'))
time.sleep(1)
serGrbl.write(gcode2.encode() + str.encode('\n'))
time.sleep(1)
serGrbl.write(gcode3.encode() + str.encode('\n'))
time.sleep(1)
serGrbl.write(gcode5.encode() + str.encode('\n'))
time.sleep(1)

#右半分
serGrbl.write(gcode3.encode() + str.encode('\n'))
time.sleep(1)
serGrbl.write(gcode5.encode() + str.encode('\n'))
time.sleep(1)
serGrbl.write(gcode4.encode() + str.encode('\n'))
time.sleep(1)
serGrbl.write(gcode4.encode() + str.encode('\n'))
time.sleep(1)

#初期位置に戻る
serGrbl.write(gcodeReset.encode() + str.encode('\n'))
