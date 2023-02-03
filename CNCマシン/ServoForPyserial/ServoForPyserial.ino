// Servoライブラリの読み込み
#include <VarSpeedServo.h>

VarSpeedServo myservo;          // Servoオブジェクトの宣言
const int SV_PIN = 7;   // サーボモーターをデジタルピン7に


void setup()
{
  myservo.attach(SV_PIN, 500, 2400);  // サーボの割当(パルス幅500~2400msに指定)
  Serial.begin(9600);
}

void loop()
{
  int data;

  if(Serial.available()>0){
    data = Serial.read();
    switch(data){
      case 'R':
        myservo.write(15,255);    // サーボモーターを45度の位置まで動かす
        break;
      case 'r':
        myservo.write(25,255);    // サーボモーターを165度の位置まで動かす
        break;
      case 'G':
        myservo.write(165,255);    // サーボモーターを165度の位置まで動かす
        break;
      case 'g':
        myservo.write(155,255);    // サーボモーターを165度の位置まで動かす
        break;
      case 'N':
        myservo.write(90,255);    // サーボモーターを90度の位置まで動かす
        break;
    }
  } else {
  }
}
