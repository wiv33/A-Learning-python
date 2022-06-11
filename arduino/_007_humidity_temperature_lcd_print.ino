#include <LiquidCrystal.h>

#include "DHT.h"
#define DHTPIN 7     // DHT11이 연결된 핀
#define DHTTYPE DHT11   // DHT 11, DHT시리즈중 11을 선택합니다.

DHT dht(DHTPIN, DHTTYPE);
LiquidCrystal lcd(12,11,5,4,3,2);

void setup() {

  Serial.begin(9600);

  lcd.begin(16, 2);
  dht.begin();
}

void loop() {
  delay(2000);

  float h = dht.readHumidity();// 습도
  float t = dht.readTemperature();// 온도
  float f = dht.readTemperature(true);// 화씨 온도

  // 값 읽기에 오류가 있으면 오류를 출력합니다.
  if (isnan(h) || isnan(t) || isnan(f)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

  displayLcd(h, t);

  sendSerial(h, t, f);
}

void displayLcd(float h, float t) {
  lcd.setCursor(0, 0);
  lcd.print("Humi: ");
  lcd.print(h);
  lcd.print(" %");

  lcd.setCursor(0, 1);
  lcd.print("Temp: ");
  lcd.print(t);
  lcd.print(" C");
}

void sendSerial(float h, float t, float f) {
  // 보정된 화씨 값을 가져옵니다.
  float hif = dht.computeHeatIndex(f, h);
  // 보정된 섭씨 값을 가져옵니다.
  float hic = dht.computeHeatIndex(t, h, false);

  Serial.print("Humidity: ");
  Serial.print(h);
  Serial.print(" %\t");
  Serial.print("Temperature: ");
  Serial.print(t);
  Serial.print(" *C ");
  Serial.print(f);
  Serial.print(" *F\t");
  Serial.print("Heat index: ");
  Serial.print(hic);
  Serial.print(" *C ");
  Serial.print(hif);
  Serial.println(" *F");

}
