## Beschreibung:
qrcheck.db ist die Datenbank mit den QR-Werten. Diese muss gleich sein der Werte in der Datenbank zum erstellen der QR-Codes auf der Webseite hier würde man auch neue QR-Werte einlesen falls diese all sind. Standartmäßig ist diese Datenbank schon mit 10000 Werten gefüllt.

qrwerte.csv sind 10000 Werte per Zufall generiert.

automatrestauswurf.db ist die Datenbank welche verwaltet wie viele Belohnungen noch vorhanden sind in den zwei Spiralen

spirale_nachfüllen.py ist die Datei zum Nachfüllen der Belohnungen hier wird die automatrestauswurf.db geändert nach den Benutzerabfragen. Fall man nur eine Spirale hat lässt man die zweite einfach auf 0.

main_funktion.py ist die Hauptfunktion. Hier muss ggf. die Richtung des Motor gedreht werden in der Abfrage. Bedeutet man muss aus forward1 in backwards1 ändern falls der Motor falsch herum läuft. Selbiges für den zweiten Motor nur mit 2 statt 1. Ist im Code aber auch an der passenden Stelle kommentiert.
