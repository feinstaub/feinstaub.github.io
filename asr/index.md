asr - async-send-receive
========================

First concept: 2014, First prototype version: 2015-03-27
Web Content last updated: 2015-05-28

asr
---

asr aims to be a free and open, decentralized alternative to proprietary, non-open sync, cloud and file hosting services when it comes to exchange potentially large files over the Internet.

All data and processing logic takes place on the client side. (Almost) everything is encrypted on the way between sender and receiver. Sender and receiver are not required to be online at the same time. Therefore there is always a third party computer involved which serves as (dumb) exchange point. Third party computers are treated untrustworthy by design.

### Target use cases

* Send files from one person's computer to another person's computer.
* Files are potentially larger than they would fit into an email attachment.
* File transfers should be encrypted.
* Minimal setup.
* Encryption should be setup once for a given pair of persons and then reused without having to worry each time.

### Secure

* **Easy-to-understand** security
    * Why is this important? E.g. read [A Plea for Simplicity](https://www.schneier.com/essays/archives/1999/11/a_plea_for_simplicit.html), 1999 by [Bruce Schneier](http://en.wikipedia.org/wiki/Bruce_Schneier)
    * Currently based on passwords (later maybe on public key infrastructure).
* **end-to-end encryption**
    * Based on passwords
    * Since the data is always decrypted after receiving there is no risk to lose data due to a lost password.
* Most **meta-data** is encrypted.
    * Especially **filenames** and **subject line** is encrypted.
    * The following meta-data will **not** be encrypted: sender's id, receiver's id, timestamp.
* **Touch-cloud** solution
    * This means your data in its encrypted form will only touch the cloud. As soon as the receiver gets it, it will vanish. This minimizes the chances of the (encrypted) data from being copied.

### Easy to use

* Client-side files which are sent are encrypted automatically.
* Files being received are decrypted automatically.


### Open

* License GPLv2, free software, use as you please and on your own risk
* Written in Python
* Code hosted on [KDE quickgit](http://quickgit.kde.org/?p=scratch%2Fgregormi%2Fasr.git)
* forum, discussion, issue tracker: currently [hosted at github](https://github.com/feinstaub/asr/issues)
* TODO: protocol specification


### Features

* ...
* Automatic file splitting for big files and limited per file size on exchange point [TODO]
* ...

### Architecture

* All **logic is local**
    * Exchange point servers can be as dumb as possible.
* Having an **exchange point** in the middle is part of the concept
    * But: no dedicated central server is needed. There can be several exchange points.
    * An exchange point can be replaced if it goes out of service.
    * The exchange point can be located on your own hardware.
    * Implication: No special installation required on a central server needed. Make use of COTS FTP account, Networkshare, IMAP account.


### Threat model

* v1.0 (planned)
    * If someone snatches the common login data for the exchange point, a DOS attach can be launched by deleting all files that appear on the exchange point.


Download
--------
Prerequisites for installation:

* Some Linux/UNIX
* python
* git

Additional prerequisites at runtime:

* openssl
* tar
* python-guidata

Step-by-step:

1. Download the [download-and-install.sh](http://quickgit.kde.org/?p=scratch%2Fgregormi%2Fasr.git&a=blob&f=download-and-install.sh) script.
2. Make it executable and run it in a console. Press Enter to continue when asked.
=> The latest asr release will be downloaded into ~/asr/bin/ (which will be erased beforehand during the process)
=> All unit tests will be excecuted to ensure a functional installation.


Quickstart [under codestruction]
--------------------------------

### Scenario: Send someone encrypted files

You would like to send someone familiar some photos. With high probability
you will do that more than once.

### Initial setup for the sender (who setups the exchange point)
* Download asr and put it in your PATH.

* Choose / setup an exchange point: TODO

* Create the directory `~/asr/configfiles` and place the asr-demo-config inside.

* TODO

### Initial setup for the receiver
* Download asr and put it in your PATH.

* TODO


Background
----------
Asr is a tool built around the idea to exchange data between
two computers using a third - potentially completely untrusted - party
(like internet hosting services, corporate network shares etc.)
in an asynchronous way.

Places in the Internet are classified as untrusted sites and private data
should not lie around needlessly and unprotected.
Asr tries to provide the electronic equivalent of sending someone a
package via postal service; including privacy of correspondence,
posts and telecommunications.

If you send someone a postal package there is usually no trace of the
package's content on the way between sender and receiver. The only metadata
which is tracked is who sent the package and who received it.

It is not expected that the sender's and receiver's computer is online
at the sametime. Therefore, the process of sending and receiving is
asynchronous.

Currently, there is no push notification on new packages
and so polling or notification over another channel is required.

### Exchange points

Write something about shareable and throw-away exchange points. ...

* Cheap:
    * On the one hand, an exchange point is like the storage place where your
      postal package is kept until you pick it up.
    * On the other hand, it can be cheap because if someone breaks in
      the package can be stolen but not opened because it is end-to-end encrypted.
    * The exchange point must only contain as much data as the packages which are
      not yet fetched. The data can be deleted as soon as the package is delivered.

* Throw-awayable:
    * If you find out that an exchange point has been compromised just setup another
      (one or change the password.)

* Shareable:
    * Once an internet exchange point is setup you can grant access to
      reliable persons.

* Dumb:
    * list files
    * upload files
    * create directories
    * change to directory
    * download files
    * delete files and directories

* Multiple:
    * You can (in the future) setup asr to fetch multiple exchange points.
    * Possible types of exchange points: filesystem, FTP, email (future), ...


### Required packages [revise later]

asr is a Python script which currently has the following dependencies:

- tar
- openssl
- python-guidata (has some more python deps)
- gnome-web-photo (optional)
- wget (optional)


Support
-------

You would like to support development by donating money? This is currently not possible. Until now, asr is **vegware**. This means if you like it, it would be nice gesture to skip one or more meals which would contain diary products or eggs and consume something mass-exploitation-free instead. Like beer.


Similar Tools
-------------

### SparkleShare

http://sparkleshare.org/, GPLv3

Auto-sync with a git repository in the middle.

[Client Side Encryption](https://github.com/hbons/SparkleShare/wiki/Client-Side-Encryption)

- "To use this feature, simply create an empty Git repository, but make sure it has -crypto in its name."
    - empty means empty, no readme file or something
- "you'll be asked to provide a password"
- "it can can't be changed later"
- "Please note that although file contents can't be retrieved on the server, file names can be."
    - **filenames are not encrypted**
- "simultaneous edits are not merged by git since it has no access to the contents of the files."

Written in C#, based on Mono.

### Syncthing

https://syncthing.net/, BSD-License?

Both parties need to be online?

Written in Go.
