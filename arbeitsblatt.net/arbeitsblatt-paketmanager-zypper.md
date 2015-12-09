Software mit der Kommandozeile installieren
===========================================

Cowsay installieren
-------------------

Ziel: cowsay mit Hilfe von zypper installieren

* "Konsole" öffnen (z. B. via K-Menü)
* `cowsay Muh` eingeben
* (Befehl nicht gefunden)
* `cnf cowsay` eingeben
* `sudo zypper install cowsay` eingeben
* (Nach Rückfragen wird cowsay installiert)
* `cowsay Muh` eingeben

```
 _____
< Muh >
 -----
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
```

Befehlsübersicht
----------------
| Befehl        | Beschreibung |
| ------------- |-------------|
| `sudo <befehl>`      | **s**ubstitute **u**ser **do** - wird meistens dazu verwendet, um einen Befehl mit dem Superuser 'root' auszuführen |
| `zypper install <paket_name>` | Paket installieren. Es können auch mehrere Pakete mit Leerzeichen getrennt angegeben werden. |
| `zypper remove <paket_name>` | Paket deinstallieren |
| `zypper search <text>` | Paket suchen |
| `zypper se <text>` | Kurzform für zypper search |
| `zypper info <paket_name>` | Informationen (Version, Beschreibung) über ein Paket anzeigen |
| `cnf`           | **c**ommand **n**ot **f**ound handler - siehe auch `man cnf` |


Tipp
----
Konsolenausgaben genau durchlesen und versuchen zu verstehen.
