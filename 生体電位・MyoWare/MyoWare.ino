// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
}
  float v_m1 = 0;
  unsigned long previousMillis = 0;



void loop() {

  unsigned long currentMillis = millis();

  if(currentMillis - previousMillis <= 60000) {
    v_m1 += analogRead(A0);
  }else{
    Serial.println((v_m1 * 5.0) / 1024);
    previousMillis = currentMillis;
    v_m1 = 0;
  }
  delay(100);       // 0.1秒ごとに
}
