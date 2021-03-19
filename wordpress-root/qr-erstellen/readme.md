## Wichtig!
Seite welche den QR Code ausgibt bzw. das Snippet benutzt darf keine Unterseite sein.

## Diesen QR-Code-Ergzeuger noch hier einfügen
- QR-Code-Erzeugung: http://sourceforge.net/apps/mediawiki/phpqrcode/index.php?title=Main_Page

## In dem Verzeichnis noch einen Ordenr "qrbild" erstellen
Hier werden die QR-Code gespeichert.

## Benötigt das folgende Snippet zur Abfrage ob alle Schilder erledigt sind und dann erst QR-Code ausgibt.
QR-Ausgabe-Erledigte-Schilder
```SQL
<?php
session_start();
$servername = "db5001541733.hosting-data.io";
    $username = "dbu1595093";
    $password = "......";
    $dbname = "dbs1288901";
// Create connection
    $conn = new mysqli($servername, $username, $password, $dbname);
    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    } 
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
    if ($AnzahlBesuchterSchilder >= 8) { 
        echo "<h2>Super! Du warst an allen Schildern. Hohl Dir jetzt Deine Belohnung an der Turnhalle ab.</h2>";
       if (!isset($_SESSION['qr'])) {
		 	$sql = "SELECT `wert` FROM `qrcheck` ORDER BY `wert` ASC LIMIT 1";
			$result = $conn->query($sql);
     		$row = $result->fetch_assoc() ;
      		$_id = $_SESSION['qr'] = $row["wert"];	
    		$result->free();
			$sql = "DELETE FROM `qrcheck` WHERE `wert`= '{$_id}'";
			$conn->query($sql);
			$conn->close();
        }
       $codeContents = $_SESSION['qr'];
 
       $path = $_SERVER['DOCUMENT_ROOT'];
       $path .= "/qr-erstellen/qrgenerator.php";
       include  $path;

      $tempbild = "../qr-erstellen/qrbild/";
      echo '<img src="'.$tempbild.$codeContents.'_erstellt.png"/>';
      echo '<p><a href="'.$tempbild.$codeContents.'_erstellt.png">Download</a></p>';
    } else {
      if ($AnzahlBesuchterSchilder == 7) {
        echo "<h2>Dir fehlt noch das folgende Schild: $FehlendeSchilderStr\n</h2>";
    } else {
        echo "<h2>Dir fehlen noch folgende ".(8-$AnzahlBesuchterSchilder)." Schilder für eine Belohnung: $FehlendeSchilderStr \n</h2>";
    }
	}
?>
```
