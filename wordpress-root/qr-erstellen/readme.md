## Diesen QR-Code-Ergzeuger noch hier einfügen
- QR-Code-Erzeugung: http://sourceforge.net/apps/mediawiki/phpqrcode/index.php?title=Main_Page

##Benötigt das Snippet zur Abfrage ob alle Schilder erledigt sind und dann erst QR-Code ausgibt.
```<?php
session_start();
$sessionIDStr = session_id();

$AnzahlBesuchterSchilder = 0;
for ($i=1; $i<=8; $i++) {
    if (isset($_SESSION['besuchtesSchild'][$i])) {
        $AnzahlBesuchterSchilder++;
    }
}

$FehlendeSchilderStr = "";
$konsekutiveSchilder = 0;
for ($i=1; $i<=8; $i++) {
    if (!isset($_SESSION['besuchtesSchild'][$i])) {
      if ($konsekutiveSchilder == 0)  { 
        if (strlen($FehlendeSchilderStr) > 0) $FehlendeSchilderStr .= ", ";
        $FehlendeSchilderStr .= "$i";
      }
      $konsekutiveSchilder++;
    }
   else {
      if ($konsekutiveSchilder>2) {
        $FehlendeSchilderStr .= "-".($i-1);
      } else {
        if ($konsekutiveSchilder>1) {
          $FehlendeSchilderStr .= ", ".($i-1);
        }
      }
      $konsekutiveSchilder = 0;
    }
}
//Letztes Schild nochmal separat überprüfen
    if (!isset($_SESSION['besuchtesSchild'][8])) {
        if ($konsekutiveSchilder>2) {
          $FehlendeSchilderStr .= "-8";
        } else {
          if ($konsekutiveSchilder>1) {
            $FehlendeSchilderStr .= ", 8";
          }
        }
}


// "Test, ob schon Belohnung erhalten?\n";
if (isset($_SESSION['BelohnungErhalten']) and ($_SESSION['BelohnungErhalten'] == true) ) {
    echo "Du hast bereits Deine Belohnung erhalten. Bei Fehlern wende Dich bitte an uns.\n";
} else {
    if ($AnzahlBesuchterSchilder >= 8) {
        echo "<h2>Super! Du warst an allen Schildern. Hohl Dir jetzt Deine Belohnung an der Turnhalle ab.</h2>";
       $codeContents = 123456; // TODO: Datenbank Abfrage
 
       $path = $_SERVER['DOCUMENT_ROOT'];
       $path .= "/qr-erstellen/qrgenerator.php";
       include  $path;

      $tempbild = "../qr-erstellen/qrbild/";
      echo '<img src="'.$tempbild.$codeContents.'_erstellt.png"/>';
    } else {
      if ($AnzahlBesuchterSchilder == 7) {
        echo "Dir fehlt noch das folgende Schild: $FehlendeSchilderStr\n";
    } else {
        echo "Dir fehlen noch folgende ".(8-$AnzahlBesuchterSchilder)." Schilder: $FehlendeSchilderStr\n";
    }
    }
} //Test auf Belohnung
```
