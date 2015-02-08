Linux advanced notes
====================

ReplayGain
----------
How to do mass ReplayGain? How to see which files are already gained?

  * Quod Libet
    * Plugins, [see screenshot](img/2014-01-15 replay gain howto todo 1.png)
    * add columns, [see screenshot](img/2014-01-15 replay gain howto todo 2.png)
  * TODO: more

...


Fix openSUSE Firefox KDE integration
------------------------------------

TODO: This should be enabled by default! Where to file bug reports?

### File chooser

see https://en.opensuse.org/SDB:Mozilla_filechooser

```
Open about:config in Firefox, search for "file_picker" and flip the preference ui.allow_platform_file_picker to false.
```

Now the KDE file dialogs work again.

### Make Firefox for Linux use Dolphin to ‘Open Containing Folder’


see https://fitzcarraldoblog.wordpress.com/2014/09/14/make-firefox-for-linux-use-dolphin-to-open-containing-folder/
see https://forums.opensuse.org/showthread.php/456698-How-use-Dolphin-to-quot-open-containing-folder-quot-from-firefox-downloads?p=2446741#post2446741

My post about the topic: https://forums.opensuse.org/showthread.php/456698-How-use-Dolphin-to-quot-open-containing-folder-quot-from-firefox-downloads?p=2688302#post2688302
(2015-01-10 / wait)

Reply:
```
See those posts for workarounds:
https://forums.opensuse.org/showthre...28#post2687728
https://forums.opensuse.org/showthread.php/504039-Firefox-has-started-a-very-annoying-behaviour!?p=2687953#post2687953

Or uninstall nautilus, the "GTK" (GNOME actually) filemanager you probably mean.
```

=> Workaround if you do not want to deinstall gnome:
```
$ locate org.freedesktop.FileManager1.service
/usr/share/dbus-1/services/org.freedesktop.FileManager1.service
# edit this file as root:
---
[D-BUS Service]
Name=org.freedesktop.FileManager1
Exec=/usr/bin/nautilus --gapplication-service
---
# comment out the last line:
---
[D-BUS Service]
Name=org.freedesktop.FileManager1
# Exec=/usr/bin/nautilus --gapplication-service
---
# Note this has to be done everytime the file gets overwritten.
```
see https://forums.opensuse.org/showthread.php/456698-How-use-Dolphin-to-quot-open-containing-folder-quot-from-firefox-downloads?p=2688494#post2688494


Oracle VirtualBox
-----------------
Resize .vdi drive:
1. `VBoxManage modifyhd MyHardDisk.vdi --resize 42000` resizes to 42.000 KB = about 42 GB
2. In der Datenträgerverwaltung "Volume erweitern"

