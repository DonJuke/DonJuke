#include <LiquidCrystal.h> 
#include <DHT11.h>
const int rs = 23, en = 22, d4 = 5, d5 = 4, d6 = 2, d7 = 15;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);
DHT11 dht11(18);

void setup() {
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

void loop(){
  int centigrade, fahrenheight, humidity, result;
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
  }