Fortune auf Deutsch
-------------------

Fortune kann nicht nur englische Sprüche anzeigen. Es gibt auch andere Sprachen. Bei openSUSE sind die anderen Sprachen (darunter Deutsch) leider nicht paketiert, so dass man sich
anderweitig behelfen muss.

* Erzeuge ein temporäres Arbeitsverzeichnis und wechsle hinein.

`cd ~/tmp/fortune`

* Debian ist die Linux-Distribution mit den meisten Paketen. Dort gibt es für Fortune die deutschen Sprachdateien

    1) Seite https://packages.debian.org/de/jessie/fortunes-de mit einem Browser besuchen.

    2) Ganz rechts in der Liste die Datei `fortunes-de_0.31.orig.tar.gz` runterladen.

* Mit einem Archivprogramm öffnen (z. B. "ark" durch Klick auf die Datei)

* Den Ordner "data" ins Verzeichnis aus dem ersten Schritt entpacken.

* `cd ~/tmp/fortunes`

* `ls data` sollte nun einige Dateien auflisten.

* `cd data`

* `strfile sprichworte`

* `cd ..`

* `fortune data`


Quelle
------
* https://forums.opensuse.org/showthread.php/486875-Fortune-program-in-other-languages
