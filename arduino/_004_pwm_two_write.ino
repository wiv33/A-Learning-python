void setup() {
    pinMode(9, OUTPUT);
    pinMode(8, OUTPUT);
    Serial.begin(9600);
}

void loop() {
    int a0, a1, g9, g8;
    a0 = analogRead(0);
    a1 = analogRead(1);
    g9 = toAnalog(a0);
    g8 = toAnalog(a1);
    Serial.print(a0);
    Serial.print(", ");
    Serial.println(a1);
    analogWrite(9, g9);
    analogWrite(8, g8);
}

int toAnalog(int num) {
  return num / 1023.0 * 255.0;
}