#include <dummy.h>


#define dirPin 0
#define stepPin 1
#define dirPin 2
#define stepPin 3
#define dirPin 4
#define stepPin 5
#define dirPin 6
#define stepPin 7
#define dirPin 8
#define stepPin 9
#define dirPin 10
#define stepPin 11
#define stepsPerRevolution 200

void setup() {
  // Declare pins as output:
    pinMode(stepPin0, OUTPUT);
    pinMode(dirPin0, OUTPUT);
    pinMode(stepPin1, OUTPUT);
    pinMode(dirPin1, OUTPUT);
    pinMode(stepPin2, OUTPUT);
    pinMode(dirPin2, OUTPUT);
    pinMode(stepPin3, OUTPUT);
    pinMode(dirPin3, OUTPUT);
    pinMode(stepPin4, OUTPUT);
    pinMode(dirPin4, OUTPUT);
    pinMode(stepPin5, OUTPUT);
    pinMode(dirPin5, OUTPUT);
    pinMode(A0, INPUT);
    pinMode(A1, INPUT);
    pinMode(A2, INPUT);
    pinMode(A3, INPUT);
    pinMode(A4, INPUT);
    pinMode(A5, INPUT);
    Serial.begin(9600);
}

void loop() {
    int PotValue0,
        PotValue1,
        PotValue2,
        PotValue3,
        PotValue4,
        PotValue5;
    PotValue0 = analogRead(A0);
    PotValue1 = analogRead(A1);
    PotValue2 = analogRead(A2);
    PotValue3 = analogRead(A3);
    PotValue4 = analogRead(A4);
    PotValue5 = analogRead(A5);
  // Set the spinning direction clockwise:



  // Set the spinning direction counterclockwise:

  // Spin the stepper motor 1 revolution quickly:
  for (int i = 0; i < stepsPerRevolution; i++) {
    // These four lines result in 1 step:
    digitalWrite(stepPin, HIGH);
    delayMicroseconds(200);
    digitalWrite(stepPin, LOW);
    delayMicroseconds(200);
  }


  // Set the spinning direction clockwise:

}