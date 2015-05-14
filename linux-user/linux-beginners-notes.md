Linux beginners notes
=====================

All the things I noticed when switching my home computer from Windows 7 to openSUSE Linux 13.1, 13.2.

See also:

* http://publicstatic.de/gnu/linux/todo-and-solved.html
* http://www.tweakhound.com/2014/11/14/opensuse-13-2-tips-tricks-and-tweaks/


Empfehlenswerte Drucker und Scanner
-----------------------------------
### 2015
Zusammenfassung: **Drucker von HP** sind derzeit für Linux zu empfehlen. Z. B.  HP Officejet 6500 A oder ähnliche Officejets

Preis für das Einsteiger-Kombigerät: zwischen 100 und 200 EUR.

Das wichtigste bei Linux sind die Treiber, ohne die druckt oder scannt die beste Hardware nicht.

Früher konnte man drei Marken empfehlen: HP, Epson, Canon (siehe z. B. http://www.pcwelt.de/ratgeber/Drucker-Vorteil-HP-167717.html)

* Epson produziert meist Billig-Drucker. Linux-Scanner-Treiber werden nicht mehr weiterentwickelt.
* Canon hat früher sehr günstige (kompatible) Patronen gehabt, das gibt es jetzt aber nicht mehr. Früher gab es auch gute Linux-Treiber, aber die Entwicklung wurde weitgehend eingestellt.
* Bleibt nur noch HP übrig. Gute Hardware. Treiber werden OpenSource entwickelt (HpLip) und auf dem aktuellen Stand gehalten.


Format external USB hard drive
------------------------------
1) Create Partition:

* Open gparted
* If drive is completely unformatted then goto Device --> Create Partition Table... --> Choose msdos
  * see gparted help about this topic: "The default partition table type is msdos for disks smaller than 2 Tebibytes in size (assuming a 512 byte sector size) and gpt for disks 2 Tebibytes and larger."
  ```
    The msdos partition table limits partitions as follows:
    Maximum of 4 primary partitions.
    Maximum of 3 primary partitions, and 1 extended partition.
    The extended partition can contain multiple logical partitions. Some GNU/Linux distributions support accessing at most 15 partitions on a disk device.
    Maximum size of a partition is 2 Tebibytes using a sector size of 512 bytes. The partition must also start within the first 2 Tebibytes of the disk device.
  ```
* Insert new partition with ext4 file system
* Set Label to 'backup2014'
* Apply

See here on the advantages of btrfs but recommendation towards ext4 for backup drives:
http://askubuntu.com/questions/331050/which-filesystem-should-i-use-to-format-my-external-backup-hdd-btrfs

2) Mount Partition:
Now mount the partition, e.g. with KDE device notifier.
Because of label the partition gets mounted under /run/media/<username>/backup2014/
The directory can only be written to with root permissions.

3) Set permissions:
We create a folder with correct permissions:
```
cd /run/media/gregor/backup2014/
sudo mkdir backup
sudo chown gregor backup/
sudo chgrp users backup/
```

TODO 1: Kann man auch den **root** der Platte mit gregor/users mounten?
TODO 2: Geht das auch weniger umständlich?

### Related programs

* gnome-disk-utility (todo: try out in detail)
  * Has a benchmark feature
* KDE Partition Manager (todo: try out in detail)
  * https://www.kde.org/applications/system/kdepartitionmanager
  * http://en.wikipedia.org/wiki/KDE_Partition_Manager


### Troubleshooting

Drive can be mounted but not we written.

Disconnect USB.

`$ tail -f /var/log/messages` (see http://askubuntu.com/questions/302480/cant-mount-external-drive-after-reformatting)

Reconnect USB.

```
2014-11-22T10:41:53.548926+01:00 catgroove kernel: [ 4373.543022] usb 2-1.2: USB disconnect, device number 9
2014-11-22T10:41:58.578940+01:00 catgroove kernel: [ 4378.576450] usb 2-1.2: new high-speed USB device number 10 using ehci-pci
2014-11-22T10:42:00.541921+01:00 catgroove kernel: [ 4380.541023] usb 2-1.2: New USB device found, idVendor=174c, idProduct=5106
2014-11-22T10:42:00.541946+01:00 catgroove kernel: [ 4380.541030] usb 2-1.2: New USB device strings: Mfr=2, Product=3, SerialNumber=1
2014-11-22T10:42:00.541949+01:00 catgroove kernel: [ 4380.541033] usb 2-1.2: Product: AS2105
2014-11-22T10:42:00.541951+01:00 catgroove kernel: [ 4380.541036] usb 2-1.2: Manufacturer: ASMedia
2014-11-22T10:42:00.541952+01:00 catgroove kernel: [ 4380.541039] usb 2-1.2: SerialNumber:             W6215S84
2014-11-22T10:42:00.542926+01:00 catgroove kernel: [ 4380.541578] usb-storage 2-1.2:1.0: USB Mass Storage device detected
2014-11-22T10:42:00.542941+01:00 catgroove kernel: [ 4380.541698] usb-storage 2-1.2:1.0: Quirks match for vid 174c pid 5106: 800000
2014-11-22T10:42:00.542944+01:00 catgroove kernel: [ 4380.541738] scsi9 : usb-storage 2-1.2:1.0
2014-11-22T10:42:00.546575+01:00 catgroove mtp-probe: checking bus 2, device 10: "/sys/devices/pci0000:00/0000:00:1d.0/usb2/2-1/2-1.2"
2014-11-22T10:42:00.546996+01:00 catgroove mtp-probe: bus: 2, device: 10 was not an MTP device
2014-11-22T10:42:01.571896+01:00 catgroove kernel: [ 4381.572057] scsi 9:0:0:0: Direct-Access     ST500LM0 21-1KJ152        0001 PQ: 0 ANSI: 5
2014-11-22T10:42:01.572891+01:00 catgroove kernel: [ 4381.572386] sd 9:0:0:0: Attached scsi generic sg2 type 0
2014-11-22T10:42:01.572904+01:00 catgroove kernel: [ 4381.572906] sd 9:0:0:0: [sdb] 976773168 512-byte logical blocks: (500 GB/465 GiB)
2014-11-22T10:42:01.574191+01:00 catgroove kernel: [ 4381.573932] sd 9:0:0:0: [sdb] Write Protect is off
2014-11-22T10:42:01.574207+01:00 catgroove kernel: [ 4381.573943] sd 9:0:0:0: [sdb] Mode Sense: 23 00 00 00
2014-11-22T10:42:01.575900+01:00 catgroove kernel: [ 4381.575786] sd 9:0:0:0: [sdb] No Caching mode page found
2014-11-22T10:42:01.575915+01:00 catgroove kernel: [ 4381.575789] sd 9:0:0:0: [sdb] Assuming drive cache: write through
2014-11-22T10:42:01.629022+01:00 catgroove kernel: [ 4381.628776]  sdb: sdb1
2014-11-22T10:42:01.631909+01:00 catgroove kernel: [ 4381.632009] sd 9:0:0:0: [sdb] Attached SCSI disk
2014-11-22T10:42:01.843946+01:00 catgroove kernel: [ 4381.843516] usb 2-1.2: reset high-speed USB device number 10 using ehci-pci
2014-11-22T10:42:02.469947+01:00 catgroove kernel: [ 4382.469994] usb 2-1.2: reset high-speed USB device number 10 using ehci-pci
2014-11-22T10:42:02.665746+01:00 catgroove udisksd[1822]: Error performing initial housekeeping for drive /org/freedesktop/UDisks2/drives/ST500LM021_1KJ152_W6215S84: Error updating SMART data: sk_disk_smart_status: Input/output error (udisks-error-quark, 0)
```

Creating a file with root user works.

Reason: drive was mounted with wrong permissions. See previous section of how to deal with that.


/etc/fstab with NTFS partitions and bind to move root disk space
--------------------------------------------------------------
```
/dev/disk/by-id/ata-Samsung_SSD_840_Series_S14LNEAD117615F-part5 swap                 swap       defaults              0 0
/dev/disk/by-id/ata-Samsung_SSD_840_Series_S14LNEAD117615F-part6 /                    ext4       acl,user_xattr        1 1
/dev/disk/by-id/ata-Samsung_SSD_840_Series_S14LNEAD117615F-part7 /home                ext4       defaults              1 2
/dev/disk/by-id/ata-Samsung_SSD_840_Series_S14LNEAD117615F-part2 /home/gregor/mnt/windows_c ntfs-3g    users,gid=users,uid=gregor,fmask=133,dmask=022,locale=en_GB.UTF-8,exec    0 0
# deleted (NOTE that if a deleted partition is kept here the system won't boot):
# /dev/disk/by-id/ata-Samsung_SSD_840_Series_S14LNEAD117615F-part4 /home/gregor/mnt/windows_d ntfs-3g    users,uid=gregor,gid=users,fmask=133,dmask=022,locale=en_GB.UTF-8    0 0
/dev/disk/by-id/ata-ST500LM021-1KJ152_W6215S84-part1 /run/media/gregor/backup2014/ ext4       user,noauto,acl,nofail 0 0

# more space for root partition / part 1:
UUID=277f8aa6-978d-45b8-b5a4-0f7f60674b8f /m1                  btrfs      defaults              0 0

# more space for root partition / part 2:
# http://serverfault.com/questions/613179/how-do-i-do-mount-bind-in-etc-fstab
# /media/3tb-vol1/Private/ /srv/Private        none    bind
# remount without reboot: mount -a
/m1/tmp /tmp none bind

# the original /tmp data:
# http://unix.stackexchange.com/questions/37765/mounting-to-non-empty-directory-then-later-deleting-original-files
# Why? Because when mounting /m1/tmp over /tmp then the data in tmp/ will not be deleted which is cool.
#      But we want to be able to delete it later if everything works fine
# /tmp /tmp-orig-see-fstab none bind # this does not work after reboot
# But this
#   (see http://unix.stackexchange.com/questions/37765/mounting-to-non-empty-directory-then-later-deleting-original-files)
#  $ mkdir /mnt/root1
#  $ mount /dev/sda6 /mnt/root1/
# Now delete old contents from /mnt/root1/tmp/

# cp -a /usr/src/* /m1/usr/src/
# 2.2 GB (250.000 files)
/m1/usr/src /usr/src none bind

# cp -a /var/tmp/* /m1/var/tmp/
# 1.1 GB (2.000 files)
/m1/var/tmp /var/tmp none bind

# see http://en.wikipedia.org/wiki/Rsync#Examples
# we do NOT use --safe-link         because there are several absolute and relative ones
#               --prune-empty-dirs  because sometimes the source contains empty dirs
# rsync -avz --delete /usr/share/ /m1/usr/share-TESTTEST-notused/
# currently we got differences when doing a Dolphin-->Properties over all files. Why?
# /usr/share:  5.5 GB (280.000 files)
```

Backup user data
----------------
On Linux doing a backup and restore is quite simple.

Follow these steps:

(TODO)

All the data that needs to be backed up is in the home directory.
But there are some files that don't need to or should not to be restored.
So it is best to ignore them from the beginning.

FreeFileSync

* Download for openSUSE: http://software.opensuse.org/package/FreeFileSync
* Help: https://sourceforge.net/p/freefilesync/discussion/


### Default ignored files list

Not in backup:

* Trash contents
* Mozilla Firefox extension settings
* Cache and lock files

```
*_NOBACKUP_*
*/cache.*
*.lock
*.parentlock
/.adobe/
/.AMD/
/.cache/
/.cache4dev/*
/.cache5/
/.config/akonadi/
/.config/chromium/Default/Extensions/*
/.config/chromium/Default/File System/*
/.config/Clementine/moodbarcache/
/.config/Clementine/networkcache/
/.config/decibel-audio-player/Logs/log
/.config/ibus/
/.config/libreoffice/4-suse/user/psprint/pspfontcache
/.config/libreoffice/4-suse/user/store/.templdir.cache
/.config/pulse/
/.config/smplayer/
/.config/stetic/library-cache/
/.config5/
/.dbus/
/.debug/*
/.gstreamer-0.10/
/.dropbox-dist/*
/.dropbox/*
/.dvdcss/
/.eclipse/*
/.esd_auth
/.fonts/*
/.FreeFileSync/LastSyncs.log
/.giteye/
/.hplip/*
/.icedtea/*
/.kde4/cache-*
/.kde4/share/apps/nepomuk/repository
/.kde4/share/apps/RecentDocuments/
/.kde4/socket-*
/.kde4/tmp-*
/.litecoin/blocks/*
/.litecoin/chainstate/*
/.local/share/gvfs-metadata/
/.local/share/NuGet/Cache/
/.local/share/Trash/
/.local/share/systemd/
/.local5/
/.m2/*
/.macromedia/Flash_Player/
/.mono/
/.mozilla/firefox/Crash Reports/
/.mozilla/firefox/*.default/adblockplus/
/.mozilla/firefox/*.default/extensions/
/.mozilla/firefox/*.default/lock
/.nv/GLCache/*
/.npm/*
/.PyCharm30/system/caches/
/.PyCharm30/system/index/
/.rcc/
/.recently-used
/.sK1/*
/.skel/*
/.speech-dispatcher/
/.thumbnails/
/.thunderbird/*/Cache.*
/.thunderbird/*/lock
/.wine/drive_c/users/Public/Application Data/Package Cache/
/.VirtualBox/VBoxSVC.log*
/.Xauthority
/.xine/
/.xsession-*
/.y2log
/.y2usersettings
```

history of this list: https://github.com/feinstaub/feinstaub.github.io/commits/master/linux-user/linux-beginners-notes.md


openSUSE: upgrade from 13.1 to 13.2
-----------------------------------

Upgrading a distribution: https://en.opensuse.org/SDB:System_upgrade

### Making sure you are up to date

* `sudo zypper repos --uri` list all repos with URIs
* `sudo zypper refresh` refreshes all repos
    * in case of errors: `sudo zypper removerepo http-download.opensuse.org-436383ff`
* `sudo zypper modifyrepo --enable repo-update`
* `sudo zypper modifyrepo --disable 1 2 7`
* Prepare:
    `sudo zypper refresh`
    `sudo zypper update`
* Restart computer
* Defects:
    * VLC does not show images
    * USB sound card makes crazy sounds instead of being normal

This might have something to do with updated packages:
```
vlc-beta-qt-3.0.0-2014102201.3.x86_64         Sat 08 Nov 2014 10:29:18 CET
vlc-beta-gnome-3.0.0-2014102201.3.x86_64      Sat 08 Nov 2014 10:29:18 CET
vlc-beta-aout-pulse-3.0.0-2014102201.3.x86_64 Sat 08 Nov 2014 10:29:18 CET
vlc-beta-3.0.0-2014102201.3.x86_64            Sat 08 Nov 2014 10:29:18 CET
vlc-beta-noX-3.0.0-2014102201.3.x86_64        Sat 08 Nov 2014 10:29:17 CET

gstreamer-0_10-plugins-ffmpeg-0.10.13-2000.4.x86_64 Sat 08 Nov 2014 10:29:07 CET

mpeg2dec-0.5.1-3.1.x86_64                     Sat 08 Nov 2014 10:28:57 CET
gstreamer-0_10-plugins-ugly-orig-addon-0.10.19-14.2.x86_64 Sat 08 Nov 2014 10:28:57 CET

gstreamer-0_10-plugins-fluendo_mpegmux-0.10.4-46.2.x86_64 Sat 08 Nov 2014 10:28:54 CET

mp4v2-2.0.0-1.6.x86_64                        Sat 08 Nov 2014 10:28:51 CET

gstreamer-0_10-plugins-fluendo_mpegdemux-0.10.71-2.6.x86_64 Sat 08 Nov 2014 10:28:38 CET

libvlccore8-3.0.0-2014102201.3.x86_64         Sat 08 Nov 2014 10:27:43 CET
libvlc5-3.0.0-2014102201.3.x86_64             Sat 08 Nov 2014 10:27:43 CET
libmpeg2convert0-0.5.1-8.1.x86_64             Sat 08 Nov 2014 10:27:43 CET
libmp4v2-0-2.0-2.14.x86_64                    Sat 08 Nov 2014 10:27:43 CET
...
```

* Install `vlc` instead of `vlc-beta` fixes video output but sound still is ear-destroying.
* Unplug and replug USB sound card fixes sound.

### Running the upgrade
... see https://en.opensuse.org/SDB:System_upgrade ...
"As already mentioned, any third party or OBS repositories can cause troubles, so it is recommended to disable or remove them before proceeding."
Also disable the CD repo.
Disable all repos with URL http://download.opensuse.org/repositories/*

`sudo cp -Rv /etc/zypp/repos.d /etc/zypp/repos.d.Old`
`sudo sed -i 's/13\.1/13.2/g' /etc/zypp/repos.d/*`
`sudo zypper ref`

"It is strongly recommended that you run this inside GNU screen or tmux to protect the upgrade process in case anything should go wrong with the X session during the upgrade."

`sudo zypper install tmux`
http://tmux.sourceforge.net/
[man page](http://www.openbsd.org/cgi-bin/man.cgi/OpenBSD-current/man1/tmux.1?query=tmux&sec=1)

Quick howto tmux:

* `tmux`
    * Do something inside tmux
    * Press **Ctrl+B D** to detach current client
     `[detached (from session 0)]`
* `tmux attach -t 0` to attach again to session 0 or just `tmux attach` to attach to last session
* `tmux ls` to list all sessions
* reminder: press **Ctrl+Alt+F6** to switch away from X to console and **Ctrl+Alt+F7** to go back to X.

`zypper help dup` - "Perform a distribution upgrade."

`zypper dup --download "in-advance"` - Performs the update

This will ask before continuing.
Check the console output (/home/gregor/sys/upgrade_13.1_13.2/zypper_dup.out.txt) for REMOVED or DOWNGRADED packages to know what will be missing later.

Downloading 5106 packages... done

Installing packages... done

(I leave third-party repos still disabled.)

### Reboot and afterwork

"After upgrade, reboot is recommended to start new kernel and newer versions of everything."

Try to reboot but the system did not boot anymore because kernel was not found. See next section about how to fix boot problems. Now fixed.

After successful reboot: Using KDE Development Platform 4.14.2.

Yast Online Update Installation Summary wants to install ibus. (Note that previously it messed up with Firefox KDE integration)

"In addition, `zypper up` can be run from time to time to ensure you have the latest available packages from the various repositories that you have enabled. YOU (Yast Online Update) only addresses security updates from the official repositories."

Run `sudo zypper dup` again which removes about 150 libraries.

Open "YaST2 - Bootloader" and fix distributor text from "13.1" to "13.2"

Install video codecs (see http://opensuse-guide.org/codecs.php):
```
zypper addrepo -f http://ftp.gwdg.de/pub/linux/packman/suse/openSUSE_13.2/ packman
zypper addrepo -f http://opensuse-guide.org/repo/13.2/ dvd
zypper install libxine2-codecs k3b-codecs ffmpeg lame gstreamer-plugins-bad gstreamer-plugins-ugly gstreamer-plugins-ugly-orig-addon gstreamer-plugins-libav libdvdcss2
http://download.videolan.org/pub/videolan/vlc/SuSE/13.2/
```

`sudo zypper repos --uri` # sort by priority

vlc did not work

1-Click-Install-Codecs. vlc did not work.
Install from http://www.videolan.org/vlc/download-suse.html vlc did not work.

smplayer works by the way.

Read: https://en.opensuse.org/Additional_package_repositories
Read: https://en.opensuse.org/Package_repositories

### Open issues

* fix vlc
* TODO report: KDE Print jobs plasma widget should display on which printer the job is printed; std-printer still defect
    * use case: more than one printer. Sent to wrong printer which is offline. Want to cancel only jobs for the wrong printer.
* TODO report: yast2 Sound: the test sound too loud and too long


openSUSE: Fix grub boot problems
--------------------------------
This is the log about how boot problems after a system upgrade were solved. This steps also helped in similar scenarios.

Concrete case 2014-11-09:
An update from openSUSE 13.1 to 13.2 via `zypper dup` was performed and then reboot was done which lead to a **boot failure**.

![](img/boot-problem-1a.jpg) ![](img/boot-problem-2a.jpg)

Insert **openSUSE 13.1 DVD** and start the **Rescue System**.

The following commands were gathered from the internet some time ago, so the sources are unknown.

(My system is dual-boot and Linux is (currently) not on first partition but on /dev/sda6)

```
Rescue login: root     (no pw required)
$ mount /dev/sda6 /mnt
$ mount -o bind /dev/  /mnt/dev
$ mount -o bind /proc/ /mnt/proc
$ chroot /mnt /bin/bash
```
NOTE: `$ yast2` --> System --> bootloader fails with message:
![](img/boot-problem-3a.jpg)
```
$ grub2-install /dev/sda
```
![](img/boot-problem-4a.jpg)

```
Ctrl+D to log out of chroot environment.
$ reboot
```
FIXED.


VLC does not find some codecs
-----------------------------
Use smplayer (or smplayer2) instead. Very smooth player.


EU-Politik und Freie Software
-----------------------------
"Die 10 Unternehmen, die am meisten Geld für **Lobbyismus in Brüssel** ausgeben, investieren
zusammen 39 Mio EUR/Jahr in ihre Lobbyarbeit. Die Liste wird u. a. angeführt von:
 - Philip Morris (Tabak)
 - ExxonMobil (Öl)
 - **Microsoft** (Software)"
*Quelle: LobbyControl, Dezember 2014, http://lobbyfacts.eu/reports/expenditure/companies, https://www.lobbycontrol.de/*
