#define EN        8       
#define X_DIR     5       
#define Y_DIR     6       
#define Z_DIR     7       
#define X_STP     2       
#define Y_STP     3       
#define Z_STP     4       

void step(boolean dir, byte dirPin, byte stepperPin, int steps)
{
  digitalWrite(dirPin, dir);
  delay(50);
  for (int i = 0; i < steps; i++) {
    digitalWrite(stepperPin, HIGH);
    delayMicroseconds(800);  
    digitalWrite(stepperPin, LOW);
    delayMicroseconds(800);  
  }
}

void setup(){
  pinMode(X_DIR, OUTPUT); pinMode(X_STP, OUTPUT);
  pinMode(Y_DIR, OUTPUT); pinMode(Y_STP, OUTPUT);
  pinMode(Z_DIR, OUTPUT); pinMode(Z_STP, OUTPUT);
  pinMode(EN, OUTPUT);
  digitalWrite(EN, LOW);
}

void loop(){
  step(false, X_DIR, X_STP, 200); 
  step(false, Y_DIR, Y_STP, 200); 
  step(false, Z_DIR, Z_STP, 200); 
  delay(1000);
  step(true, X_DIR, X_STP, 200); 
  step(true, Y_DIR, Y_STP, 200); 
  step(true, Z_DIR, Z_STP, 200); 
  delay(1000);

}
