Install openSUSE Leap 42.1
==========================

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

* 70 GB root
* 12 GB swap
* extended (/dev/sda3)
    * 25 GB ext4 (replaces btrfs and swap)
    * 30 GB ext4 (keep old root and use as data space)
    * 330 GB ext4 (keep /home)


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

Reboot with stick plugged in.
