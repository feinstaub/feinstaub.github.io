Linux advanced notes
====================

Upgrade from Plasma 4 to Plasma 5 and problem solving
-----------------------------------------------------

Got help with konversation in #plasma channel using IceWM.


1. Clean up installed packages

http://unix.stackexchange.com/questions/53474/opensuse-find-all-packages-without-a-repository

`rpm -qa --qf '%-30{DISTRIBUTION} %{NAME}\n'| sort`

Gives a list of packages and their repository source.
Now look for old or unwanted repositories and remove those packages

`zypper ls -u` Lists all repos and their URL

`sudo zypper rr 11 12` Removes two repos from the list

`sudo zypper dup --from repo-oss` Performs a dist upgrade from the given repo (== "switch system packages")

`sudo zypper se --verbose kernel-default` Finds with more information

A note on repos: "KDE:Frameworks5 requires KDE:Qt5. plain 13.2 works with just plain 13.2, and plain TW works with just plain TW" (shumski)


2. Install Plasma

udo zypper install plasma5-desktop


3. Debug X errors

~/.xsession-errors-:0 contains useful information

kwin_x11 --replace

Reason for nasty crashes: Did use nouveau drivers instead of the Nvidia drivers:

Easy installation which also detects correct drivers for installed card: https://en.opensuse.org/SDB:NVIDIA_drivers


4. Switch display manager from KDM to SDDM

`sudo /usr/sbin/yast2`

System -> /etc/sysconfig Editor -> Desktop -> Display manager -> DISPLAYMANGER (change from kdm to sddm)


5. Detected issues






ReplayGain
----------
How to do mass ReplayGain? How to see which files are already gained?

  * Quod Libet
    * Plugins, [see screenshot](img/2014-01-15 replay gain howto todo 1.png)
    * add columns, [see screenshot](img/2014-01-15 replay gain howto todo 2.png)
  * TODO: more

...



Scripts
-------
[bin](../bin/scripts-index.md)


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

