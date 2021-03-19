from qrreader import *
from datenbank_funktionen import *
from ausgabe_text import *
from motorsteuerung1 import forward as forward1
from motorsteuerung2 import forward as forward2
from motorsteuerung1 import backwards as backwards1
from motorsteuerung2 import backwards as backwards2
from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)             
GPIO.setup(14, GPIO.OUT) # jetzt Scannen
GPIO.setup(15, GPIO.OUT) # Belohnung
GPIO.setup(18, GPIO.OUT) # Fehler nochmal
GPIO.setup(23, GPIO.OUT) # LEER

def scan(self):
    #DB Verbindung herstellen
    datenbank="/home/pi/Desktop/Belohnungsautomat/qrcheck.db"
    datenbank2="/home/pi/Desktop/Belohnungsautomat/automatrestauswurf.db"
    db_verbindungqr=db_connection(datenbank)
    db_verbindungrest=db_connection(datenbank2)
    try:
        if db_get_anzahlqr(db_verbindungqr)>0 and (db_get_wert(db_verbindungrest,"spirale1")>0 or db_get_wert(db_verbindungrest,"spirale2")>0): #Abfrage ob noch QR-Werte in der DB und noch Belohnung da sind
            GPIO.output(23, 0)
            zustand =0 #Bitte QR einlesen
            ausgabe_text(zustand)
            GPIO.output(14, 1)
            qrwert=qrreader() #QR-Reder scannt
            GPIO.output(14, 0)
            if qrwert:
                if db_suche(db_verbindungqr, qrwert):
                    zustand=1
                    GPIO.output(15, 1)
                    ausgabe_text(zustand)
                    if db_get_wert(db_verbindungrest,"spirale1") > 0:
                        forward1(0.005,8*64) #ändern auf backward1 falls Spirale falschherum läuft, sowie die Schritte des Motor für eine Umdrehung nach dem Komma ist der Wert für die Schritte.
                        db_update_wert(db_verbindungrest,"spirale1",db_get_wert(db_verbindungrest,"spirale1")-1)
                    else:
                        forward2(0.005,8*64) #ändern auf backward2 falls Spirale falschherum läuft, sowie die Schritte des Motor für eine Umdrehung nach dem Komma ist der Wert für die Schritte.
                        db_update_wert(db_verbindungrest,"spirale2",db_get_wert(db_verbindungrest,"spirale2")-1)
                    db_delete(db_verbindungqr,qrwert)
                    GPIO.output(15, 0)
                else:
                    zustand=2 #QR-Code schon benutzt
                    GPIO.output(18, 1)
                    ausgabe_text(zustand)
                    sleep(5)
                    GPIO.output(18, 0)
            else:
                zustand=3 #Timeout
                GPIO.output(18, 1)
                ausgabe_text(zustand)
                sleep(5)
                GPIO.output(18, 0)
        else:
            zustand=5 #Automat Leer
            GPIO.output(23, 1)
            ausgabe_text(zustand)
            sleep(5)
    except:
        print("Fehler")
        pass
    
    db_close(db_verbindungqr)
    db_close(db_verbindungrest)
