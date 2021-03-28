from motorsteuerung1 import forward as forward1
from motorsteuerung2 import forward as forward2
from motorsteuerung1 import backwards as backwards1
from motorsteuerung2 import backwards as backwards2

motorauswahl = 0
motorauswahl= int(input("Welcher Motor soll bedient werden 1 oder 2?\n"))

if motorauswahl == 1:
    drehung= int(input("Wie viele Umdrehungen soll der Motor 1 machen. Negative Zahl dreht Rückwärts.\n"))
    if drehung > 0 :
       forward1(0.005,drehung*8*64)
       
    if drehung < 0 :
        drehung=drehung*(-1)
        backwards1(0.005,drehung*8*64)
           
if motorauswahl == 2:
    drehung = int(input("Wie viele Umdrehungen soll der Motor 2 machen. Negative Zahl dreht Rückwärts.\n"))
    if drehung >= 0 :
        forward2(0.005,drehung*8*64)
    
    if drehung < 0:
        drehung=drehung*(-1)
        backwards2(0.005,drehung*8*64)
        
print("FERTIG!")
