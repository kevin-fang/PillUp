const int trigPin = 12;
const int echoPin = 11;
const int pomp = 5;


// defines variables
long duration;
int distance;
void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(pomp, OUTPUT);
  Serial.begin(9600);
}
void loop() {
  // Clears the trigPin

//  digitalWrite(pomp, HIGH);
//  delay(5000);
//  digitalWrite(pomp, LOW);
//  delay(5000);
    
  
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  // Sets the trigPin on HIGH state for 10 micro seconds
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // Reads the echoPin, returns the sound wave travel time in microseconds
  duration = pulseIn(echoPin, HIGH);

  // Calculating the distance
  distance = duration * 0.034 / 2;

  // Prints the distance on the Serial Monitor
  if(distance < 7){
      digitalWrite(pomp, HIGH);
      Serial.println("STOP");

    }
    else{
      digitalWrite(pomp, LOW);
        delay(1000);
      Serial.print("Distance: ");
      Serial.println(distance);
    }
}
