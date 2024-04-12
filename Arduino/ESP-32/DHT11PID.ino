#include <DHT11.h>
#include <LiquidCrystal.h> 
#include <PID_v1.h>

#define RelayPin 21
pinMode(RelayPin, OUTPUT);

int centigrade, fahrenheight, humidity, result, hu, tp, sp, mpd, op, rs = 23, en = 22, d4 = 5, d5 = 4, d6 = 2, d7 = 15;
double aggKp = 4, aggKi = 10, aggKd = 2, consKp = 2, consKi = 5, consKd = 1, setpoint, input, output, gap;

DHT11 dht11(18);
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);
PID myPID(&Input, &Output, &Setpoint, consKp, consKi, consKd, DIRECT);
myPID.SetOutputLimits(0, 1);
myPID.SetMode(AUTOMATIC);

setpoint = 23;

void setup()
{
  Serial.begin(115200);
  lcd.begin(16,2);  
  lcd.setCursor(0,0);
  lcd.print("A Pissboy");
  lcd.setCursor(0,1);
  lcd.print("Product ");
  lcd.print((char) 175);
  delay(2000);
  lcd.clear();
}

void loop()
{

  result = dht11.readTemperatureHumidity(centigrade, humidity);
  fahrenheight = (centigrade * 9/5) + 32;
  String TEMP = "Temp: " + String(fahrenheight) + (char) 223 + "F " + String(centigrade) + (char) 223 + "C ";
  String HUM = "Humidity: " + String(humidity) + "% ";
  Serial.println("Temp: " + String(fahrenheight) +  "°F " + String(centigrade) + "°C ");
  Serial.println(HUM);
  //Remove comment lines to use serial plotter
  //Serial.print("Humidity:");
  //Serial.println(humidity);
  //Serial.print("Fahrenheight:");
  //Serial.println(fahrenheight);
  lcd.setCursor(0,1);
  lcd.print(HUM);
  if (humidity>50){
    lcd.print((char) 239);
   }
  else{ 
    lcd.print("  ");
   }
  lcd.setCursor(0,0); 
  lcd.print(TEMP);
  Serial.println(result);

  sp = (setpoint * 100) / 100;
  hu = (humidity * 10) / 10;
  tp = (centigrade * 10) / 10; 
  Input = tp;
  gap = abs(setpoint - input); 
  if (gap < 10)
  { 
    myPID.SetTunings(consKp, consKi, consKd);
  }
  else
  {
    myPID.SetTunings(aggKp, aggKi, aggKd);
  }
  myPID.Compute();
  if (Output >= 1) {
   digitalWrite(RelayPin,0);
  }
 if (Output < 1) {
   digitalWrite(RelayPin,1);
 }
  delay(10);
}