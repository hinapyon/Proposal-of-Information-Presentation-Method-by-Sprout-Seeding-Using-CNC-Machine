int MoterPin = 2;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(MoterPin, OUTPUT);  
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(MoterPin,HIGH); // HIGH = 5V
  delay(10000);                // Water supply
  digitalWrite(MoterPin,LOW);  // LOW = 0V

  for(int i=0; i<5; i++)
  {   
    Serial.println(i);
    delay(1000);
  }
}
