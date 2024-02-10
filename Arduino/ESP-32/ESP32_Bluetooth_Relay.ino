// --------------------------------------------------
//
// Code for control of ESP32 through MIT inventor app (Bluetooth). 
// device used for tests: ESP32-WROOM-32D
// 
// App on phone has three buttons:
// Button 1: 11 for ON and 10 for OFF
// Button 2: 21 for ON and 20 for OFF
// Button 3: 31 for ON and 30 for OFF
//
// Written by mo thunderz (last update: 20.4.2021)
//
// --------------------------------------------------

// this header is needed for Bluetooth Serial -> works ONLY on ESP32
#include "BluetoothSerial.h" 

// init Class:
BluetoothSerial ESP_BT; 


// Parameters for Bluetooth interface
int incoming;

void setup() {
  Serial.begin(19200);
  ESP_BT.begin("I stole your credit card information"); //Name of your Bluetooth interface -> will show up on your phone
  //pinMode (12, OUTPUT);
  pinMode (13, OUTPUT);
  pinMode (25, INPUT);
  pinMode (26, INPUT);
}

void loop() {
  // -------------------- Motor control with IR -------------------------
if (digitalRead(25)==LOW)
  {
    digitalWrite(13,LOW);
    while(digitalRead(26)==HIGH)
    {
  if (ESP_BT.available()) 
  {
    incoming = ESP_BT.read(); //Read what we receive 

    // separate button ID from button value -> button ID is 10, 20, 30, etc, value is 1 or 0
    int button = floor(incoming / 10);
    int value = incoming % 10;
    
    switch (button) {
      case 1:  
        Serial.print("Pause:"); Serial.println(value);
        digitalWrite(13, value);
        break;
      //case 2:  
        //Serial.print("Reset:"); Serial.println(value);
        //digitalWrite(12, value);
        //break;

    }
  }
    }
    digitalWrite(13,HIGH);
  }
  // -------------------- Error Turn on LED -----------------------------
  
  // -------------------- Receive Bluetooth signal ----------------------
  if (ESP_BT.available()) 
  {
    incoming = ESP_BT.read(); //Read what we receive 

    // separate button ID from button value -> button ID is 10, 20, 30, etc, value is 1 or 0
    int button = floor(incoming / 10);
    int value = incoming % 10;
    
    switch (button) {
      case 1:  
        Serial.print("Pause:"); Serial.println(value);
        digitalWrite(13, value);
        break;
      //case 2:  
        //Serial.print("Reset:"); Serial.println(value);
        //digitalWrite(12, value);
        //break;

    }
  }
}
