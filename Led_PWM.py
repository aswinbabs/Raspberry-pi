import RPi.GPIO as GPIO
led_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin,GPIO.OUT)
PWM_led = GPIO.PWM(led_pin,50)  #500Hz
PWM_led.start(0)
while True:
    duty_s = input("Enter Brightness (0 to 100)")
    duty = int(duty_s)
    PWM_led.ChangeDutyCycle(duty)
    