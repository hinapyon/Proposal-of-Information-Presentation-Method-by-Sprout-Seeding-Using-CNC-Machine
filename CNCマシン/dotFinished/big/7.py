import serial
import time

serGrbl = serial.Serial("/dev/tty.usbmodem142201", 115200)
serServo = serial.Serial("/dev/tty.usbserial-14230", 9600)

# Grblを目覚めさせる
serGrbl.write("\r\n\r\n".encode())
time.sleep(2)
serGrbl.flushInput()

gcodeFirst = 'G00\nX1.75Y1.75'
gcodeRight ='G91\nX0.5Y0.0'#横線右
gcodeLeft ='G91\nx-0.5y0.0'#横線左
gcodeUp ='G91\nX0.0Y0.5'#縦線上
gcodeDown ='G91\nx0.0Y-0.5'#縦線下
gcodeLeftMove ='G91\nx-2.0y0.0'#横移動
gcodeReset ='G90\nX0.0Y0.0'

# Gcodeを送る
#初期設定
serServo.write(b"N")
serGrbl.write(gcodeFirst.encode() + str.encode('\n'))
time.sleep(3)

#ここから書き始め
#7
for i in range(4):
  serServo.write(b"g")
  time.sleep(0.3)
  serServo.write(b"N")
  serGrbl.write(gcodeRight.encode() + str.encode('\n'))
  time.sleep(1)

for i in range(6):
  serServo.write(b"r")
  time.sleep(0.3)
  serServo.write(b"N")
  serGrbl.write(gcodeUp.encode() + str.encode('\n'))
  time.sleep(1)

for i in range(4):
  serServo.write(b"R")
  time.sleep(0.3)
  serServo.write(b"N")
  serGrbl.write(gcodeLeft.encode() + str.encode('\n'))
  time.sleep(1)

for i in range(3):
  serServo.write(b"R")
  time.sleep(0.3)
  serServo.write(b"N")
  serGrbl.write(gcodeDown.encode() + str.encode('\n'))
  time.sleep(1)

#その他
time.sleep(3)
serGrbl.write(gcodeRight.encode() + str.encode('\n'))
time.sleep(3)

for i in range(3):
  serServo.write(b"G")
  time.sleep(0.3)
  serServo.write(b"N")
  serGrbl.write(gcodeRight.encode() + str.encode('\n'))
  time.sleep(1)

time.sleep(3)
serGrbl.write(gcodeLeftMove.encode() + str.encode('\n'))
time.sleep(3)
serGrbl.write(gcodeDown.encode() + str.encode('\n'))
time.sleep(3)

for i in range(2):
  serServo.write(b"G")
  time.sleep(0.3)
  serServo.write(b"N")
  serGrbl.write(gcodeDown.encode() + str.encode('\n'))
  time.sleep(1)

#初期位置に戻る
time.sleep(3)
serGrbl.write(gcodeReset.encode() + str.encode('\n'))
{}}
