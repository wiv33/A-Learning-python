#include <Servo.h>
int angle = 90;
Servo myServo;

void setup() {
  Serial.begin(9600);
  myServo.attach(9);
}

void loop() {
  if (digitalRead(2) == HIGH) angle -= 10;
  if (digitalRead(3) == HIGH) angle += 10;
  angle = constrain(angle, 0, 180);

  Serial.println(angle);

  myServo.write(angle);
  delay(200);
}