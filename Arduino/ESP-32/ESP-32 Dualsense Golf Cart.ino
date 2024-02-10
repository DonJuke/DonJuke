#include "BTS7960.h"
#include <PS4Controller.h>
#include "esp_bt_main.h"
#include "esp_bt_device.h"
#include "esp_gap_bt_api.h"
#include "esp_err.h"
const uint8_t EN = 0;
const uint8_t L_PWM = 2;
const uint8_t R_PWM = 15;
unsigned long lastTimeStamp = 0;
BTS7960 motorController(EN, L_PWM, R_PWM);
int PUL1 = 25; //define Pulse pin
int DIR1 = 26; //define Direction pin
int ENA1 = 27; //define Enable Pin
int PUL2 = 13; //define Pulse pin
int DIR2 = 12; //define Direction pin
int ENA2 = 14; //define Enable Pin


#define EVENTS 1




void setup() {
  pinMode (PUL1, OUTPUT);
  pinMode (DIR1, OUTPUT);
  pinMode (ENA1, OUTPUT);
  pinMode (PUL2, OUTPUT);
  pinMode (DIR2, OUTPUT);
  pinMode (ENA2, OUTPUT);
  Serial.begin(115200);
  PS4.attach(notify);
  PS4.attachOnConnect(onConnect);
  PS4.begin("5C:93:A2:1D:BE:E4");
  removePairedDevices(); // This helps to solve connection issues
  Serial.print("This device MAC is: ");
  printDeviceAddress();
  Serial.println("");
  motorController.Enable(); 
   
}

void loop() {
 //delay(100);

}

void removePairedDevices() {
  uint8_t pairedDeviceBtAddr[20][6];
  int count = esp_bt_gap_get_bond_device_num();
  esp_bt_gap_get_bond_device_list(&count, pairedDeviceBtAddr);
  for (int i = 0; i < count; i++) {
    esp_bt_gap_remove_bond_device(pairedDeviceBtAddr[i]);
  }
}

void printDeviceAddress() {
  const uint8_t* point = esp_bt_dev_get_address();
  for (int i = 0; i < 6; i++) {
    char str[3];
    sprintf(str, "%02x", (int)point[i]);
    Serial.print(str);
    if (i < 5) {
      Serial.print(":");
    }
  }
}

void onConnect() {
  Serial.println("Connected!");
}

void notify() {
#if EVENTS
  boolean sqd = PS4.event.button_down.square,
          squ = PS4.event.button_up.square,
          trd = PS4.event.button_down.triangle,
          tru = PS4.event.button_up.triangle,
          r2d = PS4.event.button_down.r2,
          r2u = PS4.event.button_up.r2,
          l2d = PS4.event.button_down.l2,
          l2u = PS4.event.button_up.l2,
          r1d = PS4.event.button_down.r1,
          r1u = PS4.event.button_up.r1,
          l1d = PS4.event.button_down.l1,
          l1u = PS4.event.button_up.l1;
  int lx = PS4.LStickX();
    //ly = PS4.LStickY(),
    //rx = PS4.RStickX(),
    //ry = PS4.RStickY();
    int log = 0;

  if (r2d==1){
     digitalWrite(DIR1, LOW);
  for (int i = 0; i < 200; i++) {
    digitalWrite(PUL1, HIGH);
    delayMicroseconds(700);
    digitalWrite(PUL1, LOW);
    delayMicroseconds(700);
}
  }
 if (l2d){
       digitalWrite(DIR1, HIGH);
  for (int i = 0; i < 200; i++) {
    digitalWrite(PUL1, HIGH);
    delayMicroseconds(700);
    digitalWrite(PUL1, LOW);
    delayMicroseconds(700);
}
}
  
  

  if (l1d){
     digitalWrite(DIR2, LOW);
  for (int i = 0; i < 200; i++) {
    digitalWrite(PUL2, HIGH);
    delayMicroseconds(700);
    digitalWrite(PUL2, LOW);
    delayMicroseconds(700);
}   
  }
  if (r1d){
     digitalWrite(DIR2, HIGH);
  for (int i = 0; i < 200; i++) {
    digitalWrite(PUL2, HIGH);
    delayMicroseconds(700);
    digitalWrite(PUL2, LOW);
    delayMicroseconds(700);
}    
  }
  if (squ|tru){
  //   motorController.Stop();
  }
if (lx > 20) {  
    motorController.TurnRight(lx*2);
} 

if (lx < -20) {
    motorController.TurnLeft(abs(lx*2));
}      
if (lx >-20 && lx < 20) {
    motorController.Stop();
} 

#endif
}