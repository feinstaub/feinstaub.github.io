Install openSUSE Leap 42.1
==========================

(date: 2016-01)

Preliminary considerations
--------------------------

* [Historical problems and solutions](linux-beginners-notes.md) with openSUSE 13.2 and solving boot problems

* [How to check the health of a hard drive](http://superuser.com/questions/171195/how-to-check-the-health-of-a-hard-drive)
    * SMART
    * gnome-disks --> Menü --> SMART-Werte und Selbsttest

* openSUSE Leap
    * http://www.cio.com/article/3003168/linux/7-things-you-should-know-about-opensuse-leap.html
        * ...
        * Conservative packages => "I discourage installing the latest packages through extra repositories", "However, if you are looking for the latest, just baked packages, then you should try Tumbleweed instead of using unstable repos on Leap"
        * ...

Swap space
----------

* Should it be swap | root or root | swap ?
    * Tuxedo
        * swap, root
    * http://www.slackbook.org/html/installation-partitioning.html
        * swap, root
    * http://www.howtogeek.com/howto/35676/how-to-choose-a-partition-scheme-for-your-linux-pc/
        * root, home, swap
    * http://www.tldp.org/HOWTO/Partition/requirements.html
        * http://www.tldp.org/HOWTO/Partition/requirements.html#SwapPlacement
        * "The short answer is anywhere is fine."
    * OPEN ISSUE: will the system still boot when I increase or decrease the swap partition size and therefore move the root partitions start cylinder?
        * => **root, swap, home** seems the way to go for me.

* What size should the swap partition have?
    * search "linux swap size"
    * https://help.ubuntu.com/community/SwapFaq
        * the table says **8 GB RAM => 11 GB swap when using Hibernation**
    * http://askubuntu.com/questions/49109/i-have-16gb-ram-do-i-need-32gb-swap
        * the table says **8GB to 64GB of RAM => 1.5 times the amount of RAM when using Hibernation**
        * **8 GB => 12 GB**

* Swap partition or swap file?
    * http://www.linux.com/news/software/applications/8208-all-about-linux-swap-space
    * web search => swap **partition** seems to be the normal case.


Partition layout
----------------
500 GB SSD drive

OLD:

* DELETE: /dev/sda1   nfts    100 MB
* DELETE: /dev/sda2   nfts     73 GB
* extended (/dev/sda3)
    * DELETE: /dev/sd8   btrfs     25 GB
    * DELETE: /dev/sd5    swap      2 GB
    * KEEP:   /dev/sda6  30 GB ext4 (keep old root & use as data space)
    * KEEP:   /dev/sda7 330 GB ext4 (/home)


NEW:

* /dev/sda1 71 GB root (62000 MB)
* /dev/sda2 12 GB swap
* extended (/dev/sda3)
    * /dev/sdaX    25 GB ext4 (replaces btrfs and swap)
    * /dev/sda5    30 GB ext4 (keep old root and use as data space)
    * /dev/sda6   330 GB ext4 (keep /home)


NOTE, Try to delete a partition left of the /home partition with gparted (after sucessful Leap installation) shows this error message:

```
Unable to delete /dev/sda5!

Please unmount any logical partitions having a number higher than 5
```

So I deleted the contents manually (rm -R *) and resized to fit the empty space on the left.

* /dev/sda1 71 GB root (62000 MB)
* /dev/sda2 12 GB swap
* /dev/sda3 extended
    * /dev/sda5    55 GB ext4 (/mnt/extraspace)
    * /dev/sda6   330 GB ext4 (/home)


Prepare installation media
--------------------------
* Download from http://software.opensuse.org/421/en
    * **openSUSE-Leap-42.1-NET-x86_64.iso** - 85 MB
    * (OPTIONAL today: openSUSE-Leap-42.1-DVD-x86_64.iso - 4.3 GB)

* [How do I verify the checksum of a file](http://kb.mit.edu/confluence/pages/viewpage.action?pageId=153815809)

```
$ shasum -c openSUSE-Leap-42.1-NET-x86_64.iso.sha256
openSUSE-Leap-42.1-NET-x86_64.iso: OK
shasum: WARNING: 15 lines are improperly formatted
```

"After having successfully downloaded the ISO image(s), create a bootable USB stick or burn the image(s) to a DVD (or a CD if the chosen image fits)."

This time I try the network install way using a live-fat-stick: https://en.opensuse.org/SDB:Live_USB_stick

**live-fat-stick**: "If you'd rather not reformat the USB device and keep the ability of putting files on it and accessible by other operating systems."

Install tools:

```
sudo zypper install live-fat-stick live-usb-gui
```

1. Run **live-usb-gui**
2. Select **openSUSE-Leap-42.1-NET-x86_64.iso**
3. Select USB-Stick (e.g. **/dev/sdb1**)
4. Select distribution **suse**
5. Confirm
    - if wrong USB-Sick-device was chosen (e.g. /dev/sdb without number) there is still a success message :(
    - if correct USB-Stick was chosen there will be command line window showing some dd_rescue output
6. Original data on stick is still present


Installation
------------
* Use gparted live CD to change the partions.

* Reboot with the openSUSE 42.1 stick plugged in.

openSUSE Leap 42.1 installer:

- Installation optionss (none)

- Expert Partionioner needed because of historical partitition table

- Time zone

- Create New User (I used the same user name as before; user id could not be entered, but it worked)

- Software Settings (keep default, KDE5 etc.) => shows 1.4 download from repos

- Downloading and Installing. Not more than 60 minutes. Reboots automatically if there is no user intervention.

- System works. Login with default user possible. All other users from previous installation are gone.


After installation notes
------------------------
- comes with Plasma 5.4.3

- First: many system updates via "Software Updates" applet

- After reboot 4 application updates shown by "Software Updates" applet which is a bit broken when showing package description (because package system is used by yast at that time?
    - so use YaST: takes long time and CPU downloading quite many application packages

- Cannot play movie files (smplayer or vlc not installed, Dragon Player does not work)

- baloo_file_extractor uses 25 % CPU (one full core for more than 1 hour)
    => disable baloo via system settings (uncheck "Enable File Search")
    - try reboot to stop the baloo_file_extractor process
    -> OK / gone after reboot


### The following packages were not installed:


```
xinput thunderbird yakuake gparted kate virtualbox smplayer krusader clementine kdf filelight git-core

```

Notes:

- xinput is used for mouse fix
- kinfocenter WAS already installed (version 5.4.3)
- filelight and kdf was NOT installed (-> kmoretools)
- virtualbox auto-recommends virtualbox-qt
- TODO: after smplayer installation still cannot play video files
    - reboot does not help
- Some package required kate4-parts (REMIND: could cause problems?)


### The following packages need extra repos:

- http://software.opensuse.org/package/FreeFileSync
    - adds the "network" repo

- software.opensuse.org/package/extreme-tuxracer
    - adds the "games" repo and the following: "languages/haskell", "languages/pascal", "games/tools"

- http://software.opensuse.org/package/git-cola
    - adds the "devel/tools/scm" repo

- Multimedia codecs, see http://opensuse-guide.org/codecs.php, no OneClick-Install available

```
zypper addrepo -f http://packman.inode.at/suse/openSUSE_Leap_42.1/ packman
zypper addrepo -f http://opensuse-guide.org/repo/openSUSE_Leap_42.1/ dvd
# my change: do not install `k3b-codecs`
zypper install ffmpeg lame phonon-backend-vlc phonon4qt5-backend-vlc vlc-codecs libdvdcss2
zypper remove phonon-backend-gstreamer phonon4qt5-backend-gstreamer
```
video with smplayer still does not work

install vlc

playback works with vlc!

TODO: reboot


### Manual Settings:

- Mount point for extraspace

- Make USB sound card primary
    - Use KDE "Audio and Video" settings to move USB soundcard to top
    - Distorted test sound
    - relogin / reboot
    - OK / Sound good

- Try to use nvidia graphics driver (fails)
    although the nouveau drivers seem to use I choose the nvidia graphics drivers
    - YaST Configure Software Repos -> Add -> Community repos -> nVidia Graphics Drivers
    - Then choose package x11-video-nvidiaG04.
    - REMIND: installs some additional kernel packages (e.g. kernel-macros) and gcc48. Could cause problems?
    - reboot
    - black screen
    - goto console
    - install x11-video-nvidiaG04 => black screen
    - install x11-video-nvidiaG03 => compile errors
    - remove nvidia* / reboot
    - video ok again
    - remove the nvidia repo

- Plasma Taskbar
    - Add QuickShare widget
    - (Add Search widget == krunner)
    - (Add Printer widget)

- TODO: Configure Printer and scanner


### Non-reported bugs:

* LibreOffice: cannot open file because path contains a 'ß' character

```
/home/aaa/bbb_ß_ccc/ddd.odt does not exist.
```
TODO: report


### Reported bugs:

* [Kate Sessions plasma addon fails silently if kate is not installed](https://bugs.kde.org/show_bug.cgi?id=357850)


Later:


- TODO: thunderbird font is very narrow and does not look at all integrated into desktop theme
