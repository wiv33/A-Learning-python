const float NOTE_C = 261.6;
const float NOTE_D = 294.1;
const float NOTE_E = 329.6;
const float NOTE_F = 349.2;

void setup() {
  pinMode(9, OUTPUT);
}

void loop() {
  if (digitalRead(2) == HIGH) toneWrapper(NOTE_C);
  else if (digitalRead(3) == HIGH) toneWrapper(NOTE_D);
  else if (digitalRead(4) == HIGH) toneWrapper(NOTE_E);
  else if (digitalRead(5) == HIGH) toneWrapper(NOTE_F);
  else noTone(9);
}

void toneWrapper(int note) {
  tone(9, note);
}
