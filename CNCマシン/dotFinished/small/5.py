import serial
import time

serGrbl = serial.Serial("/dev/tty.usbmodem142201", 115200)
serServo = serial.Serial("/dev/tty.usbserial-14230", 9600)

# Grblを目覚めさせる
serGrbl.write("\r\n\r\n".encode())
time.sleep(2)
serGrbl.flushInput()

gcodeFirst = 'G00\nX2.25Y2.5'

gcodeRight ='G91\nX0.5Y0.0'#横線右
gcodeLeft ='G91\nx-0.5y0.0'#横線左
gcodeUp ='G91\nX0.0Y0.1875'#縦線上
gcodeDown ='G91\nx0.0Y-0.1875'#縦線下

gcodeLeft1 ='G91\nx-1.0y0.0'#横線左
gcodeReset ='G90\nX0.0Y0.0'

# Gcodeを送る
#初期設定
serServo.write(b"N")
serGrbl.write(gcodeFirst.encode() + str.encode('\n'))
time.sleep(3)



#ここから書き始め
#5
for i in range(2):
  serServo.write(b"R")
  time.sleep(0.5)
  serServo.write(b"r")
  time.sleep(0.5)
  serGrbl.write(gcodeLeft.encode() + str.encode('\n'))
  time.sleep(0.5)

for i in range(2):
  serServo.write(b"R")
  time.sleep(0.5)
  serServo.write(b"r")
  time.sleep(0.5)
  serGrbl.write(gcodeUp.encode() + str.encode('\n'))
  time.sleep(0.5)


for i in range(5):
  serServo.write(b"R")
  time.sleep(0.5)
  serServo.write(b"r")
  time.sleep(0.5)
  serGrbl.write(gcodeLeft.encode() + str.encode('\n'))
  time.sleep(0.5)

for i in range(2):
  serServo.write(b"R")
  time.sleep(0.5)
  serServo.write(b"r")
  time.sleep(0.5)
  serGrbl.write(gcodeUp.encode() + str.encode('\n'))
  time.sleep(0.5)

for i in range(5):
  serServo.write(b"R")
  time.sleep(0.5)
  serServo.write(b"r")
  time.sleep(0.5)
  serGrbl.write(gcodeRight.encode() + str.encode('\n'))
  time.sleep(0.5)

#その他
for i in range(2):
  serServo.write(b"G")
  time.sleep(0.5)
  serServo.write(b"g")
  time.sleep(0.5)
  serGrbl.write(gcodeDown.encode() + str.encode('\n'))
  time.sleep(0.5)

serServo.write(b"N")
time.sleep(2)
serGrbl.write(gcodeLeft1.encode() + str.encode('\n'))
time.sleep(2)

for i in range(2):
  serServo.write(b"G")
  time.sleep(0.5)
  serServo.write(b"g")
  time.sleep(0.5)
  serGrbl.write(gcodeDown.encode() + str.encode('\n'))
  time.sleep(0.5)
#初期位置に戻る
serServo.write(b"N")
time.sleep(2)
serGrbl.write(gcodeReset.encode() + str.encode('\n'))
