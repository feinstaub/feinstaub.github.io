Linux advanced notes
====================

Upgrade from Plasma 4 to Plasma 5.4.2 and solved problems
---------------------------------------------------------

Got help with konversation in #plasma channel using IceWM.


### Clean up installed packages

http://unix.stackexchange.com/questions/53474/opensuse-find-all-packages-without-a-repository

`rpm -qa --qf '%-30{DISTRIBUTION} %{NAME}\n'| sort`

Gives a list of packages and their repository source.
Now look for old or unwanted repositories and remove those packages

`zypper ls -u` Lists all repos and their URL

`sudo zypper rr 11 12` Removes two repos from the list

`sudo zypper dup --from repo-oss` Performs a dist upgrade from the given repo (== "switch system packages")

`sudo zypper se --verbose kernel-default` Finds with more information

A note on repos: "KDE:Frameworks5 requires KDE:Qt5. plain 13.2 works with just plain 13.2, and plain TW works with just plain TW" (shumski)


### Install Plasma

`sudo zypper install plasma5-desktop`

`plasmashell --version` --> 5.4.2


### Debug X errors / graphic card drivers

~/.xsession-errors-:0 contains useful information

`kwin_x11 --replace` starts kwin5 if crashed

Reason for nasty crashes: Did use nouveau drivers instead of the Nvidia drivers:

Easy installation which also detects correct drivers for installed card: https://en.opensuse.org/SDB:NVIDIA_drivers


### Switch display manager from KDM to SDDM

`sudo /usr/sbin/yast2`

System -> /etc/sysconfig Editor -> Desktop -> Display manager -> DISPLAYMANGER (change from kdm to sddm)


### Detected issues in 5.4.2

* OPEN: How to get Plasma's version other than plasmashell --version?
    * e.g. Plasma menu > About...
    * https://forum.kde.org/viewtopic.php?f=285&t=128873


* OPEN: kinfocenter is not installed by default
    * part of this discussion: https://forum.kde.org/viewtopic.php?f=285&t=128873
    * sudo zypper install kinfocenter5
    * NOTE that kinfocenter5 is part of openSUSE 42.1


* OPEN/WAIT: Glitch: Delete an item with DEL key has a delay and shows no confirmation
    * Response to delete by keyboard shortcut very slow: https://bugs.kde.org/show_bug.cgi?id=354100
    * TODO: report "In dolphin this behaviour is configurable in the Confirmations tab of the General category of the Preferences dialog. (On a side note, with dolphin 15.07.90, this seems to be broken: I got no confirmation regardless of the setting)" as separate issue
    * still with 5.4.3


* OPEN/WAIT: F2 key on selected item has no effect - expect rename item  / F2 on desktop items does not work
    * my duplicate: https://bugs.kde.org/show_bug.cgi?id=354101
    * https://bugs.kde.org/show_bug.cgi?id=344969 - "Shortcut configuration for Folder View actions not handled by standard keys" -
    * still with 5.4.3


* OPEN/WAIT: Glitch: Show Desktop, put item in rename mode, hit ESC unshows desktop
    * https://bugs.kde.org/show_bug.cgi?id=352988
    * see also Add "Minimize all" to the "Show Desktop" widget's context menu  - https://bugs.kde.org/show_bug.cgi?id=354257 -


* OPEN/WAIT: Plasma desktop new file is created top right instead of where the mouse is
    * Right click to create a file creates the item next to the top-right item instead of where the mouse was clicked
    * https://bugs.kde.org/show_bug.cgi?id=354104


* OPEN/WAIT: No Trash/Wastebin on desktop or panel by default?
    * https://forum.kde.org/viewtopic.php?f=285&t=128894
    * see also https://forum.kde.org/viewtopic.php?f=285&t=127490
    * wait for more user feedback


* OPEN/WAIT: Glitch: Choose Leave -> Switch user -> "New session" -> "ok"
    -> Standby mode (happens only the first time after reboot)
    * reported here: https://bugs.kde.org/show_bug.cgi?id=354250


* OPEN/WAIT: Leave logout shows buttons (Cancel, Shutdown) in unexpected order
    * https://bugs.kde.org/show_bug.cgi?id=354244


* OPEN/WAIT: Device Notifier does not react on inserted DVD
    * https://bugs.kde.org/show_bug.cgi?id=354245


* NOTE: Panel menu -> "More settings..." contains "Lock widgets" menu item reachable with left clicks.


* OPEN/WAIT: Add "Minimize all" to the "Show Desktop" widget's context menu
    * Left-click on the "Show Desktop" widget switches to a certain show desktop mode.
        This is good because this way it is possible to restore all the windows as they were before the switch.
        There are situations where one would like to minimize all windows, e.g. to have a fresh start or working with the desktop itself.
        In this case it would be helpful if there was a "Minimize all" option in the context menu of "Show Desktop" widget.
    * https://bugs.kde.org/show_bug.cgi?id=354257


* OPEN/WAIT: Dolphin 15.07.90: Confirmation setting for "Deleting files or folders" is ignored
    * https://bugs.kde.org/show_bug.cgi?id=354261


* OPEN: Display configuration allows overlapping of screens. Intended?
    * https://bugs.kde.org/show_bug.cgi?id=354662


* OPEN: Bug 354663 - "Display configuration" does not remember settings
    * https://bugs.kde.org/show_bug.cgi?id=354663


* OPEN: Access to "Display Configuration" to context menu
    * https://forum.kde.org/viewtopic.php?f=285&t=129088


### issues not reported yet (5.4.2)

* OPEN: !!!, see https://forum.kde.org/viewtopic.php?f=285&t=128894#p344183
    On my openSUSE 13.2, Plasma 5.4.2, an empty user gets indeed the Home and Trash desktop items put into ~/Desktop. But when I right-click the desktop to open the Settings there is "Desktop" chosen as layout and not "Folder View", so the desktop was empty. I switched to "Folder View" manually.
    TODO: report bug and post to forum


* OPEN/WAIT 5.5: QuickLaunch widget is missing, which makes the following scripts disappear:
    - Lupe on/off (big icons)
    - zypper update
    - create KF5 documenation
    - ???
    - TODO..... report


* WAIT?/STRANGE: plasma font and some images (like login image) stretched...?


* OPEN: Make Tweak --> "Press and hold" on by default. This is really awesome!
    TODO: check on empty user if it is maybe already default


* OPEN: Panel, menu, Lock widget is probably most often used but hidden under "More settings..."
    * "Lock widgets with left mouse button"


* SOLVED/TODO: Sometimes switching between desktop layouts is grayed out
    --> Widgets were locked.
    = Unintuitive => REPORT


* OPEN: Make "Folder View" the default Desktop layout
    1) ...instead of "Desktop", upstream
    Main argument: "Desktop" is a feature subset of "Folder View", so why not present the user a more feature-rich desktop by default?

    see also my topic https://forum.kde.org/viewtopic.php?f=285&t=128894 (last replies)
    see also https://forum.kde.org/viewtopic.php?f=285&t=123394&hilit=press+%26amp%3B+hold

    2) Changing a default setting is often a delicate matter, so in the following I tried to anticipate some objects and respond to them

        - With "Desktop" the desktop is cleaner
            Yes, but also less functional, e.g. the contents of the ~/Desktop folder is not shown.

        - People should keep their Desktop clean
            Maybe, but let the user decide for himself.

        - Some people like the empty desktop
            They could switch back to "Desktop" layout

        - It has more features and therefore is harder to maintain
            As long as it can be chosen by the user as option it should be as good as possible.

        - Folder View is similar to the Windows 7 Desktop and therefore a bad default choice
            Only because a concept was or is used by Windows or Mac does not make the concept bad.
            (Plus: Moving people to free software is hard enough. As a matter of fact most people use Windows nowadays.
            So they know some concepts. I don't see point in making these people suffer more than necessary.
            There is enough other stuff to teach people in the free software world.
            Also, everyone is free to change the setting back to desktop.)

        - Plasma should not be Windows clone
            Copying or mimicking a feature does not make Plasma be like Windows. Inner values count also, like being free software.

        - Plasma should be unique and therefore should not copy Windows or Mac features
            1) The desktop is a kind of infrastructure. The more familiar it is to users the better they can concentrate on their own tasks.
            2) Copying one or the other feature of those OSes can benefit Plasma because those OS companies also employ designers with good ideas.

        - Distros
            ...can their current ideas if they want. It's only the upstream default that should be changed.

        - People should learn that there are widgets they can use
            Place a simple widget - like analog clock - on the desktop by default.


* ? / KF5 File Dialog -- accept DND event like drop a file for moving or linking or copying


### Detected issues in 5.4.3

`sudo zypper update --details`

`sudo zypper update`

=> Leaves Plasma5 broken because 5.4.2 is installed from system packages.

`zypper ls -u` Lists all repos and their URL

`sudo zypper dup --from KDE_Frameworks5` Performs a dist upgrade from the given repo (== "switch system packages")

Did not work at once because repo was broken, see https://build.opensuse.org/package/show/KDE:Frameworks5/plasma5-openSUSE_13.2 and wait for the trucks.


* WAIT/MINOR: Application menu design issues:
    see http://wstaw.org/m/2015/10/29/shot1.png
    see https://bugs.kde.org/show_bug.cgi?id=355680 - Favorite icons could be mixed up as item icons
    Kmenu/k-menu

    wait: I thought about why I find the current Kicker(=Application Menu) appearance strange: it is because the favorite icons have no text at all. On other UIs there often is some text next to or below the icon.

    "Yes, the ones with the five tabs at the bottom." is Plasma default

    TODO: ask in openSUSE forum


### issues not reported yet (5.4.3)

NOT REP: Markdown icon is a bit confusing when in a tree view (e.g. kate), because of down arrow
    * suggestion: use "MD" or "md" because this often also is the file extension for such files


ReplayGain
----------
How to do mass ReplayGain? How to see which files are already gained?

  * Quod Libet
    * Plugins, [see screenshot](img/2014-01-15 replay gain howto todo 1.png)
    * add columns, [see screenshot](img/2014-01-15 replay gain howto todo 2.png)
  * TODO: more

...



Useful shell scripts
--------------------
[codestruct-util.git](https://quickgit.kde.org/?p=scratch%2Fgregormi%2Fcodestruct-util.git&a=tree)


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


System Logs
-----------
old: /var/log/messages
new: `journalctl -xn`
(https://forums.opensuse.org/showthread.php/502318-Wo-sind-die-Logs-in-opensuse-13-2)
