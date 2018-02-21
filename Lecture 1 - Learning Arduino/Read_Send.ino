//String readString;
String Message = "";

void setup() {
  Serial.begin(115200);
  Serial.println("Arduino2018");
}
void loop() {
  if(Serial.available() > 0) {
    Message = Serial.readStringUntil('\n');
    if (Message == "Hello."){
      Serial.print("Hello Sir!");
    }
    else if(Message == "How old are you?"){
      Serial.print("I'm old enough.");
    }
    else if(Message == "What is your name?"){
      Serial.print("Why do you want to know this. Is it important?");
    }
    else {
      Serial.print(Message);
    }
  }
}

