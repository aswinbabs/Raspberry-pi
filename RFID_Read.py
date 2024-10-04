import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
    print("Place your card near the reader")
    id, text = reader.read()
    print(f"ID: {id}\nText: {text}")
finally:
    GPIO.cleanup()