from qrreader import *
from datenbank_funktionen import *
from ausgabe_text import *
from motorsteuerung1 import forward as forward1
from motorsteuerung2 import forward as forward2
import RPi.GPIO as GPIO
from time import sleep

#Taster konfig
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
TasterPin = 14
GPIO.setup(TasterPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)


#DB Verbindung herstellen
datenbank="/home/pi/Desktop/Belohnungsautomat/V3/qrcheck.db"
datenbank2="/home/pi/Desktop/Belohnungsautomat/V3/automatrestauswurf.db"
db_verbindungqr=db_connection(datenbank)
db_verbindungrest=db_connection(datenbank2)
while True:
    try:
        sleep(1)
        if db_get_anzahlqr(db_verbindungqr)>0 and (db_get_wert(db_verbindungrest,"spirale1")>0 or db_get_wert(db_verbindungrest,"spirale2")>0): #Abfrage ob noch QR-Werte in der DB und noch Belohnung da sind
            zustand=4
            ausgabe_text(zustand)
            if GPIO.input(TasterPin) == False:
                zustand =0 #Bitte QR einlesen
                ausgabe_text(zustand)
                qrwert=qrreader() #QR-Reder scannt
                if qrwert:
                    if db_suche(db_verbindungqr, qrwert):
                        zustand=1
                        ausgabe_text(zustand)
                        if db_get_wert(db_verbindungrest,"spirale1") > 0:
                            forward1(0.005,8*64)
                            db_update_wert(db_verbindungrest,"spirale1",db_get_wert(db_verbindungrest,"spirale1")-1)
                        else:
                            forward2(0.005,8*64)
                            db_update_wert(db_verbindungrest,"spirale2",db_get_wert(db_verbindungrest,"spirale2")-1)
                        db_delete(db_verbindungqr,qrwert)
                    else:
                        zustand=2 #QR-Code schon benutzt
                        ausgabe_text(zustand)
                        sleep(5)
                else:
                    zustand=3 #Timeout
                    ausgabe_text(zustand)
                    sleep(5)
                    
        else:
            zustand=5 #Automat Leer
            ausgabe_text(zustand)
            
    except KeyboardInterrupt:
        break

db_close(db_verbindungqr)
db_close(db_verbindungrest)

