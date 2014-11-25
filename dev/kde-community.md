KDE building and contributing
=============================

FAQ about dev env
-----------------
When asking questions about KF5, the following information is often requested:
Running Plasma 4 on openSUSE 13.1, KDE version 4.11.5, branch frameworks

Using KDE Development Platform 4.14.2 since 2014-11-09 (openSUSE 13.2)


Build KF5 frameworks hints
--------------------------
see https://community.kde.org/Frameworks/Building

`./kdesrc-build`

Non-critical modules that take very long to compile. Edit the following files and comment things out before running kdesrc-build

`src/extragear/utils/kdesrc-build/kf5-applications-build-include`:

* okteta
* kdepim
* kdevplatform kdevelop/kdevelop
* libkeduvocdocument kanagram khangman analitza kalgebra klettres marble kgeography kiten cantor kig blinken parley kwordquiz
* okular
* konversation

`src/extragear/utils/kdesrc-build/kf5-workspace-build-include`:

* plasma-nm (kf5-network-management)


Fixing things after KF5 run
---------------------------
### Icons in applications have changed
Reason: Icons were set to breeze theme
Solution: The icon theme can be set back to oxygen using the "Icons" KDE Control Module


Plasma5
-------
* https://techbase.kde.org/Development/Tutorials/Plasma5


git repo hints
--------------
* [community: GitKdeOrgManual incl commit hooks](https://community.kde.org/Sysadmin/GitKdeOrgManual)
* [techbase: Commit_Policy incl special keywords](https://techbase.kde.org/Policies/Commit_Policy)
    * keywords: GUI, ...
* https://techbase.kde.org

KDE community contributions [in progress]
-----------------------------------------
### ksnapshot: speed up Send To menu
* will fix [Bug 312495 - Very slow "Send to" menu](https://bugs.kde.org/show_bug.cgi?id=312495) CONFIRMED
* Review Requests
  * https://git.reviewboard.kde.org/r/120920/ (ksnapshot: Fill SendTo menu async to fix "Bug 312495 - Very slow 'Send to' menu")
    * [WAIT for response]

```
On 08/11/14 11:09, Gilles Caulier wrote:> libkipi KF5 branch is created, but code is not yet ported. We plan to
> do it next week end at digiKam Berlin Reunion :
>
> https://techbase.kde.org/Projects/Digikam/CodingSprint2014
```

```
On Sunday, November 2, 2014 18.49:33 Gregor Mi wrote:
> when you built ksnapshot, was KIPI_FOUND defined? I installed
> libkipi-devel but KIPI_FOUND was not set. So is this macro still in use?

Which branch? master should find and use kipi. For the frameworks branch,
however, I am not aware of a Qt5 port of libkipi (master is Qt4 based and
there is no frameworks branch) so the Frameworks 5 version of ksnapshot does
not yet use kipi.
```

```
Hi,

when you built ksnapshot, was KIPI_FOUND defined? I installed
libkipi-devel but KIPI_FOUND was not set. So is this macro still in use?
```

Recomile kipi by deleting kdelibs4support (from cmake req KF5KDELibs4Support) from build/ and usr/

```
./kdesrc-build kdelibs4support libkipi
```

Status for KF5 port of libkipi, see https://techbase.kde.org/Projects/Digikam/CodingSprint2014#KF5.2FQt5_Status


### kate: "crash in kateprojectworker.cpp", 2014-11-02
* Bug report via mailing list
  * kwrite-devel@kde.org
    * "crash in kateprojectworker.cpp", 2014-11-02
* bug created: https://bugs.kde.org/show_bug.cgi?id=340789


### kate: Recently used projects, 2014-11-09
* see my post on http://kate-editor.org/2012/11/02/using-the-projects-plugin-in-kate/#comment-1874
* "Is there a way to open recently used projects similar to recently used files?"


[11:34] <gregormi> It is about the taskbar buttons dimming described in this bug: https://bugs.kde.org/show_bug.cgi?id=311991
[11:37] <gregormi> I advocate to disable the dimming by default because I often hear things from novice users like "Where is the Firefox? Hmm, it's apparently gone. I have to start a new one". In fact, the orange/blue Firefox icon was just dimmed so that it just fell out of view.
[11:41] <gregormi> So is the topic list mentioned above the place where such an issue should be added? When would be next usability meeting (the last one was 2009?)

todo copy from jimdo


Install latest KF5 unstable
---------------------------
### On openSUSE 13.2 VM

* See https://en.opensuse.org/SDB:KDE_repositories#KF5.2C_Plasma_5_and_KF5-based_Applications_Unstable
* Add repo Qt 5.4: http://download.opensuse.org/repositories/KDE:/Qt54/openSUSE_13.2/ with prio 98
* Add repo KDE Unstable Frameworks: http://download.opensuse.org/repositories/KDE:/Unstable:/Frameworks/openSUSE_13.2/ with prio 98
* Install plasma5-session which will deinstall kdebase4-session
* Log out and log in fails because kdeinit5 not found
* Choose IceWM and "switch system packages" for both repos
* Choose Plasma5, login works (with guillotine) but then screen is black. Only mouse is visible. (2014-11-23)
    * Press Host+Backspace twice
* How to debug?
    * <eliasp> gregormi: have a look at ~/.xsession-errors
    * <demm> gregormi: Qt54?
    * <demm> gregormi: in tty can you check ~/.config/kwinrc ?  is it set to XRender?
      * Backend=XRender
    * <demm> gregormi: ok, not the OpenGl issue and Qt5.4 then
    * <eliasp> gregormi: did you try (at least temporarily) whether it works with nouveau instead of the proprietary driver?
    * <eliasp> gregormi: ok, give it a try please to see whether this has any effect… if it has, you might try asking in #kwin as that's most likely where the issue happens then

on #kwin:
```
[19:31] <gregormi> I installed plasma5 with openSUSE 13.2 KF5 unstable distribution in a fresh VM.
[19:31] <gregormi> ~/.config/kwinrc is set to XRender
[19:31] --> ivanich (~ivanich@ivanich.tenet.odessa.ua) has joined this channel.
[19:32] <gregormi> I have nvidia card with nouveau drivers on both host and guest system
[19:32] <gregormi> ~/.xsession-:0 looks like this: http://paste.opensuse.org/79616244, There are some OpenGL related messages
[19:36] <gregormi> e.g. "OpenGL Warning: glFlushVertexArrayRangeNV not found in mesa table". Is it harmful?

[19:49] <fredrikh> i don't know which app prints those errors, but:
[19:50] <fredrikh> libGL error: pci id for fd 10: 80ee:beef, driver (null)
[19:50] <fredrikh> libGL error: core dri or dri2 extension not found
[19:50] <fredrikh> libGL error: failed to load driver: vboxvideo
[19:50] <fredrikh> these clearly show that mesa failed to load a GL driver for you graphics card
```
zypper install mesa-demo-x for glxgears

```
[20:48] <gregormi> fredrikh: thanks for help so far. "libGL error: core dri or dri2 extension not found" might have something to do with VirtualBox
```

Download latest VirtualBox: VirtualBox-4.3-4.3.18_96516_openSUSE123-1.x86_64.rpm
`sudo zypper install VirtualBox-4.3-4.3.18_96516_openSUSE123-1.x86_64.rpm `


NEXT: install VBox Guest additions;
see e.g. here https://www.google.de/search?q=virtual+box+guest+addtions+opensuse&ie=utf-8&oe=utf-8&aq=t&rls=org.mozilla:en-GB:official&client=firefox-a&channel=sb&gfe_rd=cr&ei=Yj5yVPzCNMmg8wep84G4BQ#rls=org.mozilla:en-GB:official&channel=sb&q=virtualbox+guest+additions+opensuse+rpm
see here https://www.virtualbox.org/ticket/12746
TODO: check if maybe already installed


### With Kunbuntu CI / with WMware Player

* Take one of those files http://files.kde.org/snapshots/
  * or see https://community.kde.org/Plasma/InstallingNext

* Download from https://my.vmware.com/web/vmware/free#desktop_end_user_computing/vmware_player/6_0
* VMware-Player-6.0.4-2249910.x86_64.bundle
* +x and run ...
* `$ vmplayer`
* Insert the kubuntu-plasma5-201411201014-i386.iso (create new VM)
  * Enter user and pw for EasyInstall
* vmplayer complains that 3D accel does not work and EasyInstall does not work
  * Wants download & install VMware Tools for Linux. Done.
  * Still same warnings about 3D accel but graphics way faster than with VirtualBox
* `sudo apt-get install mesa-utils`
* `glx-gears` => no error message

* Try to install VMware Tools
  * "VMware Tools installation cannot be started manually while Easy Install is in progress"
  * see http://kb.vmware.com/selfservice/microsites/search.do?language=en_US&cmd=displayKC&externalId=1017687
  * Remove everything (but keep kubutu.iso)
* `tar -xvf file.tar.gz`
* `sudo ./vmware-install.pl`
  * no space left on device
  * TODO...
* But not needed so far.

* Change screen resolution
  * Open start menu
  * Enter display
  * Open the Display Configuration (from KDE)
  * Change resulution
  * Alt+F2, Shutdown
  * Startup, resulution did not change
  * Try in VM settings
    * resulution did not change either
* Staying with 800x600 so far.

* Try to fix 3d message
  * see https://forums.opensuse.org/showthread.php/494522-No-3d-Support-or-graphics-accelleration
    * Add `mks.gl.allowBlacklistedDrivers = "TRUE"` to vmx file
    * Does not remove the message
    * TODO: probably must install nvidia drivers


In VirtualBox (too slow for graphics):
  * kubuntu-plasma5-201411201014-i386.iso works but slow (probably because of openGL issues)


Programs, authors, methods
--------------------------
* [Thomas Lübking](https://git.reviewboard.kde.org/users/luebking/)
  * plasmoid-ihatethecashew
    * http://software.opensuse.org/package/plasmoid-ihatethecashew
    * Plasmoid, packaging
  * quick-usb-formatter
    * http://software.opensuse.org/package/quick-usb-formatter
    * http://download.opensuse.org/repositories/KDE:/Extra/openSUSE_13.2
    * integrate with Device Notifier
    * Formatting drives
  *

* [Eric Vaughan](http://www.tweakhound.com/)
  * http://www.tweakhound.com/2014/11/14/opensuse-13-2-tips-tricks-and-tweaks/
    * quick-usb-formatter, VMware, etc.


Done
----
[kde-community-done](kde-community-done.md)
