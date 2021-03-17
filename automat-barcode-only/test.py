import RPi.GPIO as GPIO

actionpin1 = 14

def action1(self):
    print ("button pressed 1")
    
GPIO.setmode(GPIO.BCM)


GPIO.setup(actionpin1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(actionpin1, GPIO.RISING, callback=action1, bouncetime=100)