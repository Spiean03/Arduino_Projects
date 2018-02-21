unsigned long long prev_micros = 0;
unsigned long buffer[256]; // much overkill ... I hope
volatile unsigned char head = 0, tail = 0;
volatile int count = 0;
int ready = 0;

/*
 * This is the interrupt handler
 * =============================
 */
void click(void) {
  PORTD |= B00010000;
  unsigned long long current_micros = micros();
  buffer[head++] = current_micros - prev_micros;
  prev_micros = current_micros;
  count++;
  analogWrite(5,count);
  PORTD &= B11101111;
}

void setup() {
  Serial.begin(115200);
  Serial.println("Geiger 2018");
  attachInterrupt(digitalPinToInterrupt(2),click,RISING);
  pinMode(4,OUTPUT);
  digitalWrite(4,0);
  pinMode(2, INPUT);           // set pin to input
}

void loop() {
  if (tail != head) {
    if (!ready) { // ignore the first click
      ready = 1;
      tail++;
      cli();
      count--;
      sei();
      return;
    }
    if (count > 254) {
      Serial.println("Overrun");
      Serial.flush();
      cli();
      head = tail = 0;
      count = 0;
      sei();
      return;
    }
    cli();
    count--;
    sei();
    long value = buffer[tail++];
    Serial.println(value);
    Serial.flush();
  }
}
