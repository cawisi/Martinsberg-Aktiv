from main_funktion import *
from gpiozero import CPUTemperature

#Taster config
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21, GPIO.IN)
GPIO.add_event_detect(21, GPIO.RISING, callback= scan, bouncetime=1000) # Wenn Taster gedrückt wird. Wird die Funktion scan in main_funktion.py gestartet
#GPIO.setup(25, GPIO.OUT) #Lüfter groß, Auskommentiert, da es über die Lüftereinstellungen des Raspberry läuft
GPIO.setup(14, GPIO.OUT) # Hier Scannen
GPIO.setup(15, GPIO.OUT) # Belohnungsauswurf
GPIO.setup(18, GPIO.OUT) # Timeout Scan
GPIO.setup(23, GPIO.OUT) # Automat LEER
GPIO.setup(7, GPIO.OUT) # Button LED
GPIO.setup(8, GPIO.OUT) # Relais 7
GPIO.setup(12, GPIO.OUT) # Fehler
aus = 1
an = 0 


#Starteinstellungen
def start():
    #Starteinstellung der Relais beim Start
    GPIO.output(14, aus) # Hier Scannen
    GPIO.output(15, aus) # Belohnungsauswurf
    GPIO.output(18, aus) # # Timeout Scan & Fehler
    GPIO.output(23, aus) # Automat LEER
    GPIO.output(7, an) # Button LED
    GPIO.output(12, aus) # QR-Code schon benutzt 
    GPIO.output(8, aus) # Relais 8
    #Abfrage ob noch Belohnungen vorhanden bei Start oder Neustart des Systems
    #DB Verbindung herstellen
    datenbank="/home/pi/Desktop/Belohnungsautomat/qrcheck.db"
    datenbank2="/home/pi/Desktop/Belohnungsautomat/automatrestauswurf.db"
    db_verbindungqr=db_connection(datenbank)
    db_verbindungrest=db_connection(datenbank2)
    #Abfrage der restlichen Belohnungen
    if db_get_anzahlqr(db_verbindungqr)>0 and (db_get_wert(db_verbindungrest,"spirale1")>0 or db_get_wert(db_verbindungrest,"spirale2")>0): #Abfrage ob noch QR-Werte in der DB und noch Belohnung da sind
        pass #macht nichts :D
    else:
        zustand=5 #Automat Leer
        GPIO.output(7, aus) # Button LED
        GPIO.output(23, an) # Automat LEER
        ausgabe_text(zustand)
    #DB Verbindung schließen
    db_close(db_verbindungqr)
    db_close(db_verbindungrest)
    
#Main!
start()

while True: # Dauerschleife damit das Progamm immer läuft, sonst kann die event_detect Funktion nicht funktionieren
    try:
        #Ist quasi unwichtig, aber irgendetwas kann er ja machen :D
        cpu  = CPUTemperature()
        cputemp = cpu.temperature
        print("CPU-Temperatur: ",cputemp) 
        sleep(20) # sleep >1 CPU schonend daher 20 damit quasi keine Ressourcen dafür benötigt werden
    except KeyboardInterrupt: #Möglichkeit des Abbrechen der Schleife und damit des Skriptes mit STRG + C
        break
GPIO.output(7, aus) #Button LED
