#include <Servo.h>

int pos = 0;    // variable to store the servo position
const int trigPin = 12;
const int echoPin = 11;
//const int pomp = 5;


// defines variables
long duration;
int distance;
Servo myservo;

int calculate_distance(){
  
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

  return distance;
  
  
  }

void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
//  pinMode(pomp, OUTPUT);
  myservo.attach(5);  // attaches the servo on pin 9 to the servo object
  Serial.begin(9600);
  
}
void loop() {
  
    calculate_distance();

  if(distance < 7){
    
//      digitalWrite(pomp, HIGH);
      myservo.write(45);
      delay(1000);                      
      myservo.write(-45);
      delay(1000); 
      
      Serial.println("STOP");

    }
    else{
//      digitalWrite(pomp, LOW);
        delay(1000);
      Serial.print("Distance: ");
      Serial.println(distance);
    }
}
