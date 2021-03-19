def ausgabe_text(wert):
    if wert==0:
        print("Lege deinen QR-Code unter den Scanner, damit du deine Belohnung erhälst")
        
    if wert==1:
        print("Deine Belohnung kommt sofort bitte warte kurz.")
        
    if wert ==2:
        print("Leider wurde der Barcode schon verwendet.\nFalls du noch keine Belohnung erhalten\nkontaktiere uns bitte.")
        
    if wert ==3:
        print("Leider hat es zu länge gedauert.\nProbiere es erneut")
        
    if wert ==4:
        print("Drücke die Scan Taste um den QR-Code für die Belohnung zu Scannen")
        
    if wert ==5:
        print("Leider ist der Automat gerade Leer.\nBitte komme ein anders mal wieder oder\nkontaktiere uns.")
