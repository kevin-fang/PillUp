#include <Servo.h>

const int trigPin = 5;
const int echoPin = 4;
const int pomp = 10;
int n;
bool state = false;
// defines variables
long duration;
int distance;
int counterOff = 0;
int counterOn = 0;
int calculate_distance() {

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
  pinMode(pomp, OUTPUT);
  Serial.begin(9600);

}
void loop() {

  calculate_distance();
  Serial.println(distance);

  if (distance < 4 && state ) {
      counterOn++;
      if(counterOn > 7)
      {
        delay(1000*1.5);
        digitalWrite(pomp, HIGH);
        delay(100);
        state = false;
        counterOn = 0;
        Serial.println("Pump is on");
    }
  }
  else{
    if(!state && distance > 8 )
    {
      counterOff++;
  //    printf("Counter off value is %d", counterOff, "\n");
      if (counterOff > 10){
      state = true; 
      counterOff = 0;
      }
  }
    }
    digitalWrite(pomp, LOW);

}