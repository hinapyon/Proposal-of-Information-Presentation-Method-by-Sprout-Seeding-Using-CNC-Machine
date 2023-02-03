float analog_voltage1 = 0;
float degital_voltage1 = 0;
float analog_voltage2 = 0;
float degital_voltage2 = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  analog_voltage1 = analogRead(0);
  degital_voltage1 = (analog_voltage1 * 5.0) / 1024.0;
  analog_voltage2 = analogRead(2);
  degital_voltage2 = (analog_voltage2 * 5.0) / 1024.0;

  Serial.print("V=");
  Serial.print(degital_voltage1 - degital_voltage2);
  Serial.println("");
  delay(1000);
}
