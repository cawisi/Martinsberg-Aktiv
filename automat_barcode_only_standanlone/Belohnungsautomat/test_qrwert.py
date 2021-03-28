from datenbank_funktionen import *

if os.path.exists("/home/pi/Desktop/Belohnungsautomat/qrcheck.db"):
    verbindung = sqlite3.connect("/home/pi/Desktop/Belohnungsautomat/qrcheck.db")
    
    eingabe1 = input("Welchen Wert hat der Test QR-Code?\n")
    db_eingabe(verbindung, "daten", eingabe1)
    print("Wert in Datenbank eingefügt")
    
    
else:
    print("Datenbank qrcheck.db existiert nicht!")