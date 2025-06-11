// Library: MPU6050 by Electronic Cats (Library Manager)
// Arduino IDE -> Upload
#include <Wire.h>
#include <MPU6050.h>

MPU6050 mpu;

void setup() {
  Serial.begin(9600);
  Wire.begin();
  mpu.initialize();
}

void loop() {
  int16_t ax, ay, az;
  mpu.getAcceleration(&ax, &ay, &az);

  float x = ax / 16384.0;
  float y = ay / 16384.0;
  float z = az / 16384.0;

  float pitch = atan2(x, sqrt(y * y + z * z)) * 180 / 3.14;
  float roll  = atan2(y, sqrt(x * x + z * z)) * 180 / 3.14;

  Serial.print("Pitch: ");
  Serial.print(pitch);
  Serial.print(" Roll: ");
  Serial.println(roll);

  delay(500);
}