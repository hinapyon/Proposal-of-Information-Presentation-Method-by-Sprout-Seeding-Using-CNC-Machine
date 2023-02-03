void setup()
{
  pinMode(7,OUTPUT);
  Serial.begin(9600);
}

void loop()
{
  int input;

  if(Serial.available()>0){
    input = Serial.read();
    switch(input){
      case 's':
        digitalWrite(13,HIGH);
        break;
      case 'd':
        digitalWrite(13,LOW);
        break;
    }
  } else {
  }
}
