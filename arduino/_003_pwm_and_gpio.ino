void setup() {
    pinMode(9, OUTPUT);
    Serial.begin(9600);
}

void loop() {
    int a0, g9;
    a0 = analogRead(0);
    Serial.println(a0);
    // 0번째 단자는 0 ~ 1023 값이므로, 0~255 사이의 값으로 변환 작업
    g9 = a0 / 1023.0 * 255.0;

    analogWrite(9, g9);
}