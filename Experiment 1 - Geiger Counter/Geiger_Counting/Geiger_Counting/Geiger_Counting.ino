const int N = 4;
long index, lastIndex, start, total;
int counter[N] = {0,0,0,0};
int mode = 0;
char buf[32];
int period; /* milliseconds per interval */
int debug = 0;

void click(void) {
  counter[index % N]++;
  total++;
}

void getPeriod(void) {
  int i, rc;
  if (debug) Serial.println("DEBUG: getPeriod()");
  for (i = 0; i < 32; i++) { /* iterate over length of buf */
    while (!Serial.available()); /* wait for data */
    buf[i] = Serial.read();
    if (buf[i] == '\n') {
      buf[i] = 0;
      sscanf(buf,"%d",&period);
      if (debug) {
        Serial.print("DEBUG: buf = ");
        Serial.println(buf);
        Serial.print("DEBUG: rc = ");
        Serial.println(rc);
        Serial.print("DEBUG: period =   ");
        Serial.println(period);
      }
      Serial.println(buf);
      return;
    }
    if (debug) {
      buf[i+1] = 0;
      Serial.print("DEBUG: buf = ");
      Serial.println(buf);
    }
  }  
}

void setup() {
  Serial.begin(115200);
  Serial.println("HELLO"); /* This is a big magic number --- MATLAB waits for this on connect */
}

void loop() {
  if (mode) {
    if (Serial.available()) mode = 0; //reboot();
    index = (millis() - start) / period;
    if (debug & 2) {
      Serial.print("DEBUG: index = ");
      Serial.print(index);
      Serial.print(", ");
      Serial.print("total = ");
      Serial.println(total);
    }
    if (index > lastIndex) {
      Serial.println(counter[lastIndex % N]);
      counter[lastIndex % N] = 0;
      lastIndex = index;
    }
  } else {
    getPeriod();
    lastIndex = 0;
    start = millis();
    attachInterrupt(digitalPinToInterrupt(2),click,RISING);
    mode = 1;
  }
}
