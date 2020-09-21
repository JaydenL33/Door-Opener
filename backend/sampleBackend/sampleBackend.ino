// Pin assignments

# define LED_1 A0

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600); 
  pinMode(A0, OUTPUT);
  digitalWrite(A0, HIGH);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0) {
    // read the incoming byte:
    incomingByte = Serial.read();

    // say what you got:
    Serial.print("I received: ");
    Serial.println(incomingByte, DEC);
  }
}
