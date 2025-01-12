#define echoPin 2 
#define trigPin 3 

long duration; 
int distance; 

void setup() {
  pinMode(trigPin, OUTPUT); 
  pinMode(echoPin, INPUT); 
  Serial.begin(9600); 
}

void loop() {
  
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  
  duration = pulseIn(echoPin, HIGH);
  
  distance = duration * 0.034 / 2; 

  
  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");

  
  if (distance < 10) {
    Serial.println("Mode Switch");
  } else if (distance >= 10 && distance <= 30) {
    Serial.println("Action 1");  
  } else if (distance > 30 && distance <= 45) {
    Serial.println("Action 2");  
  }

  delay(500); 
}
