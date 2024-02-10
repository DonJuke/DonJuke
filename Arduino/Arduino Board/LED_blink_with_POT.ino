
#define Sound 11
#define A 2
#define B 3
#define C 4
#define D 5
#define E 6
#define F 7
#define G 8
#define H 9
#define I 10

void setup() {
  // put your setup code here, to run once:
  pinMode(A, OUTPUT);
  pinMode(B, OUTPUT);
  pinMode(C, OUTPUT);
  pinMode(D, OUTPUT);
  pinMode(E, OUTPUT);
  pinMode(F, OUTPUT);
  pinMode(G, OUTPUT);
  pinMode(H, OUTPUT);
  pinMode(I, OUTPUT);
  pinMode(A0, INPUT);
  pinMode(Sound, OUTPUT);
  Serial.begin(9600);
}
// Declare the source as an output

void loop() {
  // put your main code here, to run repeatedly:
  int PotValue;
  PotValue = analogRead(A0);
  digitalWrite(A, LOW);
  PotValue = analogRead(A0);
  delay(PotValue);

  PotValue = analogRead(A0);
  digitalWrite(A, HIGH);
  PotValue = analogRead(A0);
  delay(PotValue);

  PotValue = analogRead(A0);
  digitalWrite(B, HIGH);
  PotValue = analogRead(A0);
  delay(PotValue);

  PotValue = analogRead(A0);
  digitalWrite(C, HIGH);
  PotValue = analogRead(A0);
  digitalWrite(A, LOW);
  PotValue = analogRead(A0);
  delay(PotValue);

  PotValue = analogRead(A0);
  digitalWrite(B, LOW);
  PotValue = analogRead(A0);
  digitalWrite(D, HIGH);
  PotValue = analogRead(A0);
  delay(PotValue);

  PotValue = analogRead(A0);
  digitalWrite(C, LOW);
  PotValue = analogRead(A0);
  digitalWrite(E, HIGH);
  digitalWrite(Sound, HIGH);
  PotValue = analogRead(A0);
  delay(PotValue);

  PotValue = analogRead(A0);
  digitalWrite(D, LOW);
  PotValue = analogRead(A0);
  digitalWrite(F, HIGH);
  PotValue = analogRead(A0);
  delay(PotValue);

  PotValue = analogRead(A0);
  digitalWrite(E, LOW);
  digitalWrite(Sound, LOW);
  PotValue = analogRead(A0);
  digitalWrite(G, HIGH);
  PotValue = analogRead(A0);
  delay(PotValue);

  PotValue = analogRead(A0);
  digitalWrite(F, LOW);
  PotValue = analogRead(A0);
  digitalWrite(H, HIGH);
  PotValue = analogRead(A0);
  delay(PotValue);

  PotValue = analogRead(A0);
  digitalWrite(G, LOW);
  PotValue = analogRead(A0);
  digitalWrite(I, HIGH);
  PotValue = analogRead(A0);
  delay(PotValue);

  PotValue = analogRead(A0);
  digitalWrite(H, LOW);
  PotValue = analogRead(A0);
  delay(PotValue);

  PotValue = analogRead(A0);
  digitalWrite(I, LOW);
  PotValue = analogRead(A0);
  delay(PotValue);

  PotValue = analogRead(A0);
  digitalWrite(I, HIGH);
  PotValue = analogRead(A0);
  delay(PotValue);

  PotValue = analogRead(A0);
  digitalWrite(H, HIGH);
  PotValue = analogRead(A0);
  delay(PotValue);

  PotValue = analogRead(A0);
  digitalWrite(I, LOW);
  PotValue = analogRead(A0);
  digitalWrite(G, HIGH);
  PotValue = analogRead(A0);
  delay(PotValue);

  PotValue = analogRead(A0);
  digitalWrite(H, LOW);
  PotValue = analogRead(A0);
  digitalWrite(F, HIGH);
  PotValue = analogRead(A0);
  delay(PotValue);

  PotValue = analogRead(A0);
  digitalWrite(G, LOW);
  PotValue = analogRead(A0);
  digitalWrite(E, HIGH);
  digitalWrite(Sound, HIGH);
  PotValue = analogRead(A0);
  delay(PotValue);

  PotValue = analogRead(A0);
  digitalWrite(F, LOW);
  PotValue = analogRead(A0);
  digitalWrite(D, HIGH);
  PotValue = analogRead(A0);
  delay(PotValue);

  PotValue = analogRead(A0);
  digitalWrite(E, LOW);
  digitalWrite(Sound, LOW);
  PotValue = analogRead(A0);
  digitalWrite(C, HIGH);
  PotValue = analogRead(A0);
  delay(PotValue);

  PotValue = analogRead(A0);
  digitalWrite(D, LOW);
  PotValue = analogRead(A0);
  digitalWrite(B, HIGH);
  PotValue = analogRead(A0);
  delay(PotValue);

  PotValue = analogRead(A0);
  digitalWrite(C, LOW);
  PotValue = analogRead(A0);
  digitalWrite(A, HIGH);
  PotValue = analogRead(A0);
  delay(PotValue);

  PotValue = analogRead(A0);
  digitalWrite(B, LOW);
  PotValue = analogRead(A0);
  delay(PotValue);

  PotValue = analogRead(A0);
  digitalWrite(A, LOW);
  PotValue = analogRead(A0);
  \

}
