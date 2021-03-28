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
GPIO.setup(14, GPIO.OUT) # Hier Scannen
GPIO.setup(15, GPIO.OUT) # Belohnungsauswurf
GPIO.setup(18, GPIO.OUT) # Timeout Scan & Fehler
GPIO.setup(23, GPIO.OUT) # Automat LEER
GPIO.setup(7, GPIO.OUT) # Button LED
GPIO.setup(12, GPIO.OUT) # QR-Code schon benutzt 
aus = 1
an = 0

def scan(self):
    #DB Verbindung herstellen
    datenbank="/home/pi/Desktop/Belohnungsautomat/qrcheck.db"
    datenbank2="/home/pi/Desktop/Belohnungsautomat/automatrestauswurf.db"
    db_verbindungqr=db_connection(datenbank)
    db_verbindungrest=db_connection(datenbank2)
    try:
        if db_get_anzahlqr(db_verbindungqr)>0 and (db_get_wert(db_verbindungrest,"spirale1")>0 or db_get_wert(db_verbindungrest,"spirale2")>0): #Abfrage ob noch QR-Werte in der DB und noch Belohnung da sind
            GPIO.output(23, aus) #Automat Leer
            GPIO.output(7, aus) # Button LED
            zustand =0 #Bitte QR einlesen
            ausgabe_text(zustand)
            GPIO.output(14, an) #Hier Scannen
            qrwert=qrreader() #QR-Reder scannt
            GPIO.output(14, aus) #Hier Scannen
            if qrwert:
                if db_suche(db_verbindungqr, qrwert) or qrwert == "CarstensGeheimerAuswurf":
                    zustand=1
                    GPIO.output(15, an) #Belohnungsauswurf
                    ausgabe_text(zustand)
                    if db_get_wert(db_verbindungrest,"spirale1") > 0:
                        forward1(0.005,8*64) #ändern auf backwards1 falls Spirale falschherum läuft
                        db_update_wert(db_verbindungrest,"spirale1",db_get_wert(db_verbindungrest,"spirale1")-1)
                    else :
                        backwards2(0.005,8*64) #ändern auf forward2 falls Spirale falschherum läuft
                        db_update_wert(db_verbindungrest,"spirale2",db_get_wert(db_verbindungrest,"spirale2")-1)
                    if qrwert != "CarstensGeheimerAuswurf":
                        db_delete(db_verbindungqr,qrwert)
                    GPIO.output(15, aus) #Belohnungsauswurf
                else:
                    zustand=2 #QR-Code schon benutzt
                    i=1
                    while i < 5:
                        GPIO.output(12, an) #QR-Code schon benutzt 
                        print ("Timeout: an")
                        sleep(0.5)
                        GPIO.output(12, aus)
                        print ("Timeout: aus") #QR-Code schon benutzt
                        sleep(0.5)
                        i+=1
            else:
                zustand=3 #Timeout
                i=1
                while i < 5:
                    GPIO.output(18, an)
                    print ("Timeout: an") #Timeout Scan & Fehler
                    sleep(0.5)
                    GPIO.output(18, aus)
                    print ("Timeout: aus")#Timeout Scan & Fehler
                    sleep(0.5)
                    i+=1
        else:
            zustand=5 #Automat Leer
            GPIO.output(23, an) #Automat LEER
            ausgabe_text(zustand)
            sleep(5)
    except:
        print("Fehler")
        GPIO.output(15, aus) #Belohnungsauswurf
        GPIO.output(14, aus) #Hier Scannen
        GPIO.output(18, an) #Timeout Scan & Fehler
        ausgabe_text(zustand)
        sleep(5)
        GPIO.output(18, aus) #Timeout Scan & Fehler
        pass
    #Abfrage der restlichen Belohnungen
    if db_get_anzahlqr(db_verbindungqr)>0 and (db_get_wert(db_verbindungrest,"spirale1")>0 or db_get_wert(db_verbindungrest,"spirale2")>0): #Abfrage ob noch QR-Werte in der DB und noch Belohnung da sind
        GPIO.output(7, an) #Button LED
    else:
        zustand=5 #Automat Leer
        GPIO.output(7, aus) # Button LED
        GPIO.output(23, an) # Automat LEER
        ausgabe_text(zustand)
    #DB Verbindung schließen 
    db_close(db_verbindungqr)
    db_close(db_verbindungrest)