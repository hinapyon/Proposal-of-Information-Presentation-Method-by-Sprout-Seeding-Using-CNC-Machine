import serial
import time

#CNC部のArduino端末と接続しているシリアルポートを設定
serGrbl = serial.Serial("/dev/tty.usbmodem142201", 115200)
#播種部のArduino端末と接続しているシリアルポートを設定
serHasyu = serial.Serial("/dev/tty.usbserial-14230", 9600)

#CNC部のArduino端末を目覚めさせる
serGrbl.write("\r\n\r\n".encode())
time.sleep(2)
serGrbl.flushInput()

#CNCマシンの移動距離を設定
gcodeFirst = 'G00\nX1.75Y1.75'#書き始めの始点位置への移動
gcodeRight ='G91\nX0.5Y0.0'#横線右
gcodeLeft ='G91\nx-0.5y0.0'#横線左
gcodeUp ='G91\nX0.0Y0.5'#縦線上
gcodeDown ='G91\nx0.0Y-0.5'#縦線下
gcodeReset ='G90\nX0.0Y0.0'#初期位置へ戻る

#Gcodeを送る
#初期設定，始点への移動
serHasyu.write(b"N")
serGrbl.write(gcodeFirst.encode() + str.encode('\n'))
time.sleep(3)

#0を書き始める
#LEDの点灯している部分を書く
for i in range(6):
  serHasyu.write(b"R")
  time.sleep(0.3)
  serHasyu.write(b"N")
  serGrbl.write(gcodeUp.encode() + str.encode('\n'))
  time.sleep(1)

for i in range(4):
  serHasyu.write(b"R")
  time.sleep(0.3)
  serHasyu.write(b"N")
  serGrbl.write(gcodeRight.encode() + str.encode('\n'))
  time.sleep(1)

for i in range(6):
  serHasyu.write(b"R")
  time.sleep(0.3)
  serHasyu.write(b"N")
  serGrbl.write(gcodeDown.encode() + str.encode('\n'))
  time.sleep(1)

for i in range(4):
  serHasyu.write(b"R")
  time.sleep(0.3)
  serHasyu.write(b"N")
  serGrbl.write(gcodeLeft.encode() + str.encode('\n'))
  time.sleep(1)

#LEDが点灯していない部分を書くために移動
for i in range(3):
  serGrbl.write(gcodeUp.encode() + str.encode('\n'))
  time.sleep(1)

#LEDが点灯していない部分を書く
for i in range(4):
  serHasyu.write(b"G")
  time.sleep(0.3)
  serHasyu.write(b"N")
  serGrbl.write(gcodeRight.encode() + str.encode('\n'))
  time.sleep(1)

#初期位置に戻る
time.sleep(3)
serGrbl.write(gcodeReset.encode() + str.encode('\n'))
