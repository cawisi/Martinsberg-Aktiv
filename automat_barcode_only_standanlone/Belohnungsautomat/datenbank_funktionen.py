import sqlite3
import os, sys

def db_connection(db):
    if os.path.exists(db):
        connection = sqlite3.connect(db)
        print("Connected to ",db)
        return connection
    else:
        print("ERROR Connection: ",db )
        sys.exit(0)
   
def db_close(verbindung):
    verbindung.close()
    print("The Datenbank connection is closed")
    

def db_erstellen(verbindung):
    zeiger = verbindung.cursor()
    
    sql_anweisung = """
    CREATE TABLE IF NOT EXISTS werte (
    daten REAL
    );"""

    zeiger.execute(sql_anweisung)

    verbindung.commit()

def db_eingabe(verbindung,spalte,eingabe):
    zeiger = verbindung.cursor()
    
    zeiger.execute("INSERT INTO (" + spalte + ") VALUES (?)", (eingabe,))

    verbindung.commit()
    
def db_delete(verbindung,eingabe):
    zeiger = verbindung.cursor()
    
    zeiger.execute("DELETE FROM werte WHERE daten = (?)", (eingabe,))

    verbindung.commit()

def db_suche(verbindung,eingabe):
    zeiger = verbindung.cursor()
    try:
        zeiger.execute("SELECT daten FROM werte WHERE daten = (?)",(eingabe,))
        rueckgabe = zeiger.fetchone()
        if rueckgabe:
            zurueck, = rueckgabe
        
        else :
            zurueck = None
        
        zeiger.close()
        return zurueck

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)

def db_get_anzahlqr(verbindung):
    zeiger = verbindung.cursor()
    zeiger.execute("SELECT daten FROM werte")
    anzahl= len(zeiger.fetchall())
    zeiger.close()
    return anzahl

def db_get_wert(verbindung, spalte):
    zeiger = verbindung.cursor()
    try:
        zeiger.execute("SELECT (" + spalte + ") FROM restauswurf ")
        rueckgabe = zeiger.fetchone()
        if rueckgabe:
            zurueck, = rueckgabe
        
        else :
            zurueck = None
        
        zeiger.close()
        return zurueck

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
        
def db_update_wert(verbindung,spalte,eingabe):
    zeiger = verbindung.cursor()
    try:
        zeiger.execute("Update restauswurf SET (" + spalte + ") = (?) WHERE 1=rowid ",(eingabe,))
        verbindung.commit()
        zeiger.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    


