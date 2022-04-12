void setup() {
  pinMode(9, OUTPUT);
  pinMode(12, INPUT);
}

void loop() {
  if (digitalRead(12) == LOW) {
    digitalWrite(9, LOW);
  } else {
    digitalWrite(9, HIGH);
  }
}