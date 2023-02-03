float analog_voltage = 0;
float degital_voltage = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  analog_voltage = analogRead(A0);
  degital_voltage= (analog_voltage * 5.0) / 1024.0;

  Serial.print("ACD=");
  Serial.print(analog_voltage);
  Serial.println("");
  
  Serial.print("V=");
  Serial.print(degital_voltage);
  Serial.println("");
  Serial.println("");
  Serial.println("");
  delay(1000);
}
