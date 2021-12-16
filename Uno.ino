/*
 * Status Bytes
 * 9 - Left Click
 * 10 - Right Click
 */

#include "PS2Mouse.h"
#define MDATA 5
#define MCLK 6
PS2Mouse mouse(MCLK, MDATA);

void setup() {
  pinMode(4, INPUT_PULLUP);
  Serial.begin(230400);
  mouse.initialize();
  mouse.enable_data_reporting();
}

void loop() {
  int16_t data[3];
  mouse.report(data);
  Serial.print(data[0]); // Status Byte
  Serial.print(":");
  Serial.print(data[1]); // X Movement Data
  Serial.print(":");
  Serial.print(data[2]); // Y Movement Data
  Serial.println();
}
