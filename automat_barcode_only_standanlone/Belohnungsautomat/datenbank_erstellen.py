import sqlite3
import os


def db_erstellen_complett():
    if os.path.exists("/home/pi/Desktop/Belohnungsautomat/qrcheck.db"):
        print("Datenbank qrcheck existiert bereits!")
    else:
        verbindung = sqlite3.connect("/home/pi/Desktop/Belohnungsautomat/qrcheck.db")
        zeiger = verbindung.cursor()

        sql_anweisung = sql_anweisung = """
            CREATE TABLE IF NOT EXISTS werte (
            daten TEXT
            );"""

        zeiger.execute(sql_anweisung)
        verbindung.commit()
        
        verbindung.close()
        print("Datenbank qrcheck erstellt!")

    if os.path.exists("automatrestauswurf.db"):
        print("Datenbank automatrestauswurf existiert bereits!")
    else:
        verbindung = sqlite3.connect("automatrestauswurf.db")
        zeiger = verbindung.cursor()

        sql_anweisung = sql_anweisung = """
            CREATE TABLE IF NOT EXISTS werte (
            spalte1 REAL,
            spalte2 REAL
            );"""

        zeiger.execute(sql_anweisung)

        verbindung.commit()
        verbindung.close()
        print("Datenbank automatrestauswurf erstellt!")

db_erstellen_complett()

