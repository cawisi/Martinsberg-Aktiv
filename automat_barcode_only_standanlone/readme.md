## Du brauchst:
- 1x Raspberry Pi (3,3B,3+...)
- Netzteil für Raspberry
- Raspberry Pi Camera

    Beispiel: LABISTS Offizielle Raspberry Pi V2.0, 8 MP 1080P Kamera-Modul für Raspberry Pi 1,2,3 und 4
    https://www.amazon.de/gp/product/B07VRJKYYB/ref=ppx_yo_dt_b_asin_title_o05_s01?ie=UTF8&psc=1
- Verlängerungskabel für die Kamera

    Beispiel: AZDelivery Ersatz Flexkabel 100 cm für Raspberry Pi Kamera/Display (100 cm)
    https://www.amazon.de/gp/product/B01N5RS4R2/ref=ppx_yo_dt_b_asin_title_o06_s00?ie=UTF8&psc=1
- Schrittmotor

    Beispiel: 5V 28BYJ-48 ULN2003 mit Treiberplatine ULN2003
    https://www.amazon.de/gp/product/B01MEGIHLF/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1
- 5Kanal Relais oder mehr

    Beispiel: AZDelivery 8-Relais Modul 5V mit Optokoppler Low-Level-Trigger kompatibel mit Arduino
    https://www.amazon.de/gp/product/B07CT7SLYQ/ref=ppx_yo_dt_b_asin_image_o00_s00?ie=UTF8&psc=1
    
- 1x Lüfter + Netzteil

    Beispiel: ARCTIC F12 - 120 mm Hochleistungs-Gehäuselüfter mit Standard-Gehäuse
    
        https://www.amazon.de/gp/product/B002KTVFTE/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&psc=1
        
    Universal AC DC Netzteil, Steckernetzteil 12V 2A (2000mA, 5,5/2,5mm) Adapter
    
        https://www.amazon.de/gp/product/B071RP442X/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&psc=1
        
- 4x Led´s

    Beispiel: 5 Stück 8mm 12/24V LED Metall Kontrollleuchte wasserdichte Signallampe Pilot Dash Directional Car Truck Boot mit Draht
    
        https://www.amazon.de/gp/product/B08LDDH912/ref=ppx_yo_dt_b_asin_title_o03_s01?ie=UTF8&psc=1
        
- Kabel und Stecker zum zusammenbauen

    Für Raspberry-Verkabelung:
    
        Beispiel: https://www.amazon.de/gp/product/B07QX51F3B/ref=ppx_yo_dt_b_asin_title_o02_s00?ie=UTF8&psc=1
        
- Gehäuse für alles Marke Eigenbau


## Raspberry einrichten 
https://www.elektronik-kompendium.de/sites/raspberry-pi/index.htm#a1

Ich habe die Einrichtung über SSH gemacht. Hierzu ist "Putty" ein gutes Programm für Windows. ACHTUNG SSH muss im Raspberry erst aktiviert werden.
https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html
Die folgenden Befehle sind für die Eingabe in das Terminal.
### Check auf Updates für den Rasberry eingabe in CMD (sollte man sich für später merken und ab un zu mach ausführen)
```sudo apt-get update```

```sudo apt-get upgrade```

### Installiere folgende Pakete per CMD auf dem Raspberry damit das Skript problemlos läuft
```sudo apt-get install python3-opencv```

```sudo apt-get install libqt4-test python3-sip python3-pyqt5 libqtgui4 libjasper-dev libatlas-base-dev -y```

```pip3 install opencv-contrib-python==4.1.0.25```

```sudo modprobe bcm2835-v4l2```

```sudo apt-get install sqlite3```

#### SQLite Browser installieren (optional) macht es meiner Ansicht nach einfacher später auf der graphischen Oberfläche
```sudo apt-get update```

```sudo apt-get install sqlitebrowser```

### Remote Desktopverbindung (optional) wird aber für den Zugriff der graphischen Oberfläche auf den Raspberry ohne Tastatur und Bildschirm benötigt.
```sudo apt-get install xrdp```

Jetzt kann man sich mit der Remote Desktopverbindung von Windows und der IP-Adresse des Raspberry auf dem Raspberry einloggen.

### Software installation Automat
1. Kopiere den Ordner "Belohnungsautomat" auf den Desktop des Raspberry
2. Progamm in die Autostart-Varianten einfügen damit ich auch immer läuft ;)
- Autostart vor Login

   ```sudo nano /etc/rc.local```
   
   Dort eintragen: ```/home/pi/Desktop/Belohnungsautomat/main.py &``` mit & Zeichen.
   
   Mit STRG + O speichern und mit STRG + X schließen
        
- Auotstar nach Login mit öffenen des DEBUG Fensters

    ```sudo nano /etc/xdg/lxsession/LXDE-pi/autostart```
    
    Hier einfügen:
    ```@lxterminal -e python3 /home/pi/Desktop/Belohnungsautomat/main.py``` 
        
### Software in Betrieb nehmen
1. Die Datenbank für die QR-Werte ist schon gefüllt und enthält 10000 Werte ich hoffe das reicht für den Anfang.
2. Die Datenbank für die Belohnungen (Spiralen) muss noch mit der Anzahl der eingesetzten Belohnungen gefüllt werden.

     ```python3 /home/pi/Desktop/Belohnungsautomat/spiralen_nachfüllen.py``` 





Quellen: https://www.hackster.io/gatoninja236d/scan-qr-codes-in-real-time-with-raspberry-pi-a5268b
