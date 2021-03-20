# Hier habe ich das fertige Image für den Automaten. 
Dies kann einfach Installiert werden und euer Raspberry läuft.
Benutzername ist Standardmäßig "pi" mit dem Standardpasswort "raspberry" ändert dieses Passwort am besten!

### Gebraucht wird ein Raspberry Pi 3B mit 8 GB MicroSD Card

## Installation mit PI Imager

1. Hier herunterladen: https://www.raspberrypi.org/software/
2. Installieren
3. Programm starten
4. Button "OS Wählen drücken"
5. In dem geöffneten Fenster ganz runterscollen und "Eigenes Image" auswählen
6. Imagedatei "Raspberry_Pi_3B_Belohnungsautomat.img" auswählen
7. Auf den Button "SD-Karte wählen" drücken und die richtigte SD-Karte aufwählen
8. Auf den Button "Schreiben" drücke und warten.

### Was ist drauf?
- Dateien für den Belohnungsautomaten mit allen Installationen aus der Anleitung
- Belohnungsautomat in den Autostart optionen
- 10000 QR-Werte sind hinterlegt. Gleiche wie in "eue-turnt/wordpress-root/qr-erstellen/qrwerte.csv"
- unter http://"IpDesRasberry":8888/ kann man den "RPi-Monitor" aufrufen und sich System Werte anzeigen lassen.
- Remote Desktopverbindung für Windows ist Aktiviert
- SSH ist aktiviert
- Sprache und Layout ist auf Deutsch
-  ```python3 /home/pi/Desktop/Belohnungsautomat/test_qrwert.py```

  fügt einen Testwert in die QR-Datenbank ein um das System leichter zu testen mit einem QR-Code, welcher nicht so lang und kompliziert ist wie aus der "qrwert.csv". Ich benutze meistens den Wert 1
## Was muss noch gemacht werden?
- Wenn Spirale mit Belohnungen gefüllt ist muss diese auf in der Datenbank gefüllt werden.

  ```python3 /home/pi/Desktop/Belohnungsautomat/spiralen_nachfüllen.py```
  
  einfach Anzahl der Belohnungen je Spirale eingeben.
  
## Backup erstellen:
```sudo dd if=/dev/mmcblk0 of=/media/pi/EUER_USB_DEVICE/abbild.img status=progress```

Erstellt auf dem USB-Stick "EUER_USB_DEVICE" eine Datei mit dem Namen "abbild.img" dies ist das Backup des kompletten Systems.
Wichtig ist der USB-Stick muss größer sein als die Verwendete SD-Karte im Raspberry Pi, da er ein komplettes Backup erstellt. Bedeutet SD-Karten-Größe = Größe des Backups

### Backup verkleinern
```cd /media/EUER_USB_DEVICE```

```sudo pishrink.sh abbild.img```

jetzt ist das Backup nur noch so groß wie die Daten auf dem System auch sind.

Quelle: https://techgeeks.de/raspberry-pi-image-installieren-backup-und-verkleinern/#pishrink



