# Libraries: RPi.GPIO, smtplib, email (built-in)
# Run: python3 filename.py
import RPi.GPIO as GPIO
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SENSOR_PIN = 17

EMAIL_SENDER = 'your_email@gmail.com'
EMAIL_PASSWORD = 'your_app_password'
EMAIL_RECEIVER = 'receiver_email@example.com'

GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)

def send_email():
    subject = "Water Detected!"
    body = "Alert: Water has been detected by the sensor on your Raspberry Pi."
    
    msg = MIMEMultipart()
    msg['From'] = EMAIL_SENDER
    msg['To'] = EMAIL_RECEIVER
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
        server.quit()
        print("Email sent successfully.")
    except Exception as e:
        print("Failed to send email:", e)

try:
    print("Monitoring water sensor...")
    while True:
        if GPIO.input(SENSOR_PIN) == 0:
            print("Water Detected!")
            send_email()
            time.sleep(60)
        time.sleep(1)
except KeyboardInterrupt:
    print("Exiting...")
finally:
    GPIO.cleanup()