// ==================== PYTHON CODE ====================
// Libraries: pip install pyserial psutil
// Run: python filename.py

import serial
import psutil
import time

arduino = serial.Serial('COM3', 9600)  
time.sleep(2)

while True:
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    net = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv

    data = f"CPU: {cpu}%, MEM: {memory}%, DISK: {disk}%, NET: {net//1024} KB"
    print("Sending:", data)
    arduino.write((data + '\n').encode())
    time.sleep(2)

// ==================== ARDUINO CODE ====================
// Arduino IDE -> Upload

void setup() {
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
    String data = Serial.readStringUntil('\n');
    Serial.println("Received from PC: " + data);
  }
}