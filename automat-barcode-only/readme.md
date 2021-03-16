## Du brauchst:
- 1x Raspberry Pi (3,3B,3+...)
- Netzteil für Raspberry
- Raspberry Pi Camera
- Schrittmotor
    Beispiel: 5V 28BYJ-48 ULN2003 mit Treiberplatine ULN2003
    (https://www.amazon.de/gp/product/B01MEGIHLF/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1)


## Raspberry einrichten



## Check auf Updates für den Rasberry eingabe in CMD (sollte man sich für später merken und ab un zu mach ausführen)
sudo apt-get update

## Installiere folgende Pakete per CMD auf dem Raspberry damit das Skript problemlos läuft
sudo apt-get install python3-opencv

sudo apt-get install libqt4-test python3-sip python3-pyqt5 libqtgui4 libjasper-dev libatlas-base-dev -y

pip3 install opencv-contrib-python==4.1.0.25

sudo modprobe bcm2835-v4l2




Quelle: https://www.hackster.io/gatoninja236d/scan-qr-codes-in-real-time-with-raspberry-pi-a5268b
