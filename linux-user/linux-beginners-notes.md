Linux beginners notes
=====================

All the things I noticed when switching my home computer from Windows 7 to openSUSE Linux 13.1.

TODO: move from here: http://publicstatic.de/gnu/linux/todo-and-solved.html

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

`zypper help dup` - Perform a distribution upgrade.
This will ask before continuing.
Check /home/gregor/sys/upgrade_13.1_13.2/zypper_dup.out.txt for REMOVED packages to know what will be missing later.

... to be continued ...
