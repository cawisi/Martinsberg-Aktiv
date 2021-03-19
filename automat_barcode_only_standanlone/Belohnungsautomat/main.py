from main_funktion import *
from gpiozero import CPUTemperature

#Taster konfig
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(24, GPIO.IN)
GPIO.setup(25, GPIO.OUT)
Scan = 24
Lüfter= 25
GPIO.setup(Scan, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
GPIO.add_event_detect(Scan, GPIO.RISING, callback= scan, bouncetime=1000)

while True:
    try:
        cpu  = CPUTemperature()
        if cpu.temperature < 40 :
            GPIO.output(25, 1)
        else:
            GPIO.output(25, 0)        
        
        sleep(10)
        
    except KeyboardInterrupt:
        break