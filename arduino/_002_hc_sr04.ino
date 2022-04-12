/*
초음파로 소리 인식 후 장애물의 거리 계산하기
*/
int i = 0;
int trig = 2;
int echo = 3;

void setup() {
  Serial.begin(9600);
  pinMode(echo, INPUT);
  pinMode(trig, OUTPUT);
}

void loop() {
  digitalWrite(trig, HIGH);
  delayMicroseconds(10);
  digitalWrite(trig, LOW);


  int distance = toCm(pulseIn(echo, HIGH) * 340 / 2);

  Serial.print(distance);
  Serial.println("cm");
  delay(100);
}

/**
 초음파 속도는 초당 340m, 10000으로 나눈 이유는 거리를 cm 단위로 변환
*/
int toCm(int num) {
    return num / 10000;
}