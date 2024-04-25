#include<assert.h>

#define C_PIN 2
#define M_PIN 3
#define Y_PIN 4
#define K_PIN 5

int percentToMsTime(int percent);
void setupColorPinModes(int c, int m, int y, int k);
void disableAllPumps(int c, int m, int y, int k);

void setup() {
  Serial.begin(9600);
  setupColorPinModes(C_PIN, M_PIN, Y_PIN, K_PIN);
  disableAllPumps(C_PIN, M_PIN, Y_PIN, K_PIN);
}

void setupColorPinModes(int c, int m, int y, int k){
  pinMode(c, OUTPUT);
  pinMode(m, OUTPUT);
  pinMode(y, OUTPUT);
  pinMode(k, OUTPUT);
}

void disableAllPumps(int c, int m, int y, int k){
  digitalWrite(c, HIGH);
  digitalWrite(m, HIGH);
  digitalWrite(y, HIGH);
  digitalWrite(k, HIGH);
}

void pumpColor(int pin, int percent){
  if(percent == 0) return;

  int pumpTime = percentToMsTime(percent);

  digitalWrite(pin, LOW);
  delay(pumpTime);
  digitalWrite(pin, HIGH);
}

int SCALE = 10;
int percentToMsTime(int percent){
  assert(percent >= 0 && percent <= 100);

  return SCALE * percent;
}

void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');
    int c_percent, m_percent, y_percent, k_percent;
    sscanf(data.c_str(), "%d,%d,%d,%d", &c_percent, &m_percent, &y_percent, &k_percent);

    pumpColor(C_PIN, c_percent);
    pumpColor(M_PIN, m_percent);
    pumpColor(Y_PIN, y_percent);
    pumpColor(K_PIN, k_percent);
  }
}