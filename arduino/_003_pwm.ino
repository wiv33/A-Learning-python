void setup() {
    pinMode(9, OUTPUT);
}

void loop() {
    on();
    off();
}

void on() {
    for(int i = 0; i <= 255; i++) {
        analogWrite(9, i);
        delay(5);
    }
}

void off() {
    for(int i = 255; i >= 0; i--) {
        analogWrite(9, i);
        delay(5);
    }
}