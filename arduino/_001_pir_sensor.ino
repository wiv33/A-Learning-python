int state = 0;

void setup() {
  pinMode(2, INPUT); // 2번 핀에서 입력을 받음
  pinMode(3, OUTPUT); // 3번 핀으로 상태 표시
  Serial.begin(9600);
}

void loop() {
  state = digitalRead(2);
  if (state == HIGH) {
    digitalWrite(3, HIGH);
    delay(3000);
  } else {
    digitalWrite(3, LOW);
  }

  Serial.println(state);
}