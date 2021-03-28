from datenbank_funktionen import *
import sqlite3
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(23, GPIO.OUT) # LEER
GPIO.setup(7, GPIO.OUT) # Button LED



if os.path.exists("/home/pi/Desktop/Belohnungsautomat/automatrestauswurf.db"):
    verbindung = sqlite3.connect("/home/pi/Desktop/Belohnungsautomat/automatrestauswurf.db")
    
    eingabe1 = int(input("Wie viel Belohnungen wurden in Spirale 1 eingelegt?\n"))
    db_update_wert(verbindung, "spirale1", eingabe1)
    
    eingabe2 = int(input("Wie viel Belohnungen wurden in Spirale 2 eingelegt?\n"))
    db_update_wert(verbindung, "spirale2", eingabe2)
    if eingabe1 != 0 or eingabe2 !=0:
        GPIO.output(23, 1) # LEER Automat aus
        GPIO.output(7, 0) # Button LED an
    if eingabe1 == 0 and eingabe2 ==0:
        GPIO.output(23, 0) # LEER Automat aus
        GPIO.output(7, 1) # Button LED an
else:
    print("Datenbank qrcheck.db existiert nicht!")

