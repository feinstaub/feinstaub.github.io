asr - async-send-receive
========================

Intro
-----

asr aims to be a free and open, decentralized alternative to non-free online file sending and sync services - especially when it comes to exchange potentially large files over the Internet.

### Key features

* **Send files** from one person's computer to another person's computer as easy as possible.
* **End-to-end encryption** by default.
* **Asynchronous** in a sense that you can send files while the receiver can be offline.
* **No artificial file size restriction**. Via file splitting (not impl yet) it is possible to send files which are larger than the storage quota of the given exchange point.
* **Decentral** logic. All processing logic is located on the clients. The required exchange point server only serves as a simple temporary file store and is easily replaceable.
* **No long-term dependence** of anonymous service providers because they can easily be replaced.


Download
--------
Currently available for GNU/Linux only but could be ported to other systems.

CURRENT VERSION: 0.4.1


### 1) Install prerequisites

openSUSE 13.2:
`sudo zypper install git python3 python3-virtualenv tar openssl python3-pyside`

Ubuntu:
`apt-get install git-core python3 python3-virtualenv tar openssl python3-pyside` (todo: verify this line)

Details see on [required packages](#Required_packages).


### 2) Download installer file

Download the [download-and-install.sh](http://quickgit.kde.org/?p=scratch%2Fgregormi%2Fasr.git&a=blob&hb=release&o=plain&f=download-and-install.sh) script ([view online](http://quickgit.kde.org/?p=scratch%2Fgregormi%2Fasr.git&a=blob&hb=release&f=download-and-install.sh)) into a **temporary** directory.


### 3) Run installer file

Make installer script executable and run it in a console.
`chmod +x download-and-install.sh`
`./download-and-install.sh`

=> Press Enter to continue when asked.

=> The latest asr release will be downloaded from the code repository and installed into the ~/asr/src/ directory.
NOTE that ~/asr/src/ will be erased beforehand during the process, BUT that the rest of ~/asr/ will stay untouched.

=> Desktop integration files are installed.

=> Some additional Python dependencies are downloaded from Python package site.

=> Unit tests will be excecuted to ensure a functional installation.


### 4) Run
Put the directory ~/asr/src/bin/ in the executable path to make the following two commands available: `asr`, `asrgui`.


Details
-------

### Secure and robust

* **Easy-to-understand** security
    * Why is this important? E.g. read [A Plea for Simplicity](https://www.schneier.com/essays/archives/1999/11/a_plea_for_simplicit.html), 1999 by [Bruce Schneier](http://en.wikipedia.org/wiki/Bruce_Schneier)
    * Security currently based on common passphrases (could later be extended with an asymmetric procedure).
    * No central data storage for long-term data because transfered packages will be deleted as soon as they are received.
    * Third party computers are treated untrustworthy by design.
* **end-to-end encryption**
    * Based on passwords
* **Safe and robust**
    * Since the data is always decrypted after receiving there is **no risk to lose data due to a lost password**, certificate or other stuff that sometimes get lost.
    * **Easy data routing**: Sender --> Exchange point --> Receiver (no complex P2P network).
* **Most meta-data** is encrypted.
    * Especially **filenames** and **subject line** are encrypted.
    * The following meta-data will **not** be encrypted: sender's id, receiver's id, timestamp.
    * Therefore, exchange point providers cannot violate the user's privacy by accident.

### Easy to use

* Minimal setup.
* Client-side files are encrypted automatically before they are being sent over the Internet.
* Received packages are decrypted automatically.
* Encryption must be setup only once for a given pair of persons and then reused without having to worry each time.
* No special P2P network with minimum number of participants or similar required. The sender will initially configure an exchange point, the receiver gets a pickup notice on first receive and then the exchange channel between those two participants is setup.
* todo: Automatic file splitting for big files and limited per file size on exchange point

### Open

* License GPLv3+, free software, use as you please and on your own risk
* Written in Python
* Code hosted on [KDE quickgit](http://quickgit.kde.org/?p=scratch%2Fgregormi%2Fasr.git)
* Forum, discussion, issue tracker: currently [hosted at github](https://github.com/feinstaub/asr/issues)
* todo: protocol specification (until then look at the source code)


### Architecture

* All **logic is local**
    * Exchange point servers can be as dumb as possible.
* Having an **exchange point** in the middle is part of the concept
    * But: no dedicated central server is needed. There can be several exchange points.
    * An exchange point can be replaced if it goes out of service.
    * The exchange point can be located on your own hardware.
    * Implication: No special installation required on a central server needed. Make use of COTS FTP account, Networkshare, IMAP account.
* Console application with minimal GUI

### Threat model

* v1.0 (planned)
    * If someone snatches the common login data for the exchange point, a DOS attach can be launched by deleting all files that appear on the exchange point.


Quickstart
----------

UNDER CODESTRUCTION

Scenario: **Send someone some larger files in an easy secure way**


### Initial setup for the sender
* Download and install asr (see Download section)

* Choose / setup an exchange point: TODO

* TODO: screenshots

### Send files
* Send email with pickup notice to contact... todo

### Receive files
* Download and install asr (see Download section)

* TODO: import pickup notice


More details
------------

### Background
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
at the same time.


### Exchange points

... DRAFT ...

* Cheap:
    * On the one hand, an exchange point is like the storage place where your postal package is kept until you pick it up.
    * On the other hand, it can be cheap because if someone breaks in the package can be stolen but not opened because it is end-to-end encrypted.
    * The exchange point should only contain as much data as the packages which are not yet fetched. The data can be deleted as soon as the package is delivered.

* Throw-awayable:
    * If you find out that an exchange point has been compromised just setup another on (or change the password).

* Shareable:
    * Once an internet exchange point is setup you can grant access to reliable persons.

* Dumb:
    * list files
    * upload files
    * create directories
    * download files
    * delete files and directories

* Extendable:
    * These services are supported at the moment: plain filesystem (for local testing or mounted network shares), FTP, dropbox.com


### Required packages

asr is a [Python3](https://www.python.org/) application which currently has the following dependencies:

- [git](https://git-scm.com/)
- [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/)
- [tar](http://www.gnu.org/software/tar/)
- [openssl](https://www.openssl.org/)
- [PySide](https://en.wikipedia.org/wiki/PySide)


### Protocol
TODO: add some screenshots to visualize the flow of data.


### Support
You would like to support the project by donating money? This is not possible right now.


### Similar Tools

**SparkleShare**

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

**Syncthing**

https://syncthing.net/, BSD-License?

Both parties need to be online?

Written in Go.


**sharedrop.io**

* https://www.sharedrop.io/ (virtually no setup)
* https://thomas-leister.de/internet/aus-der-serie-dateien-mal-schnell-ueber-das-netzwerk-schubsen-sharedrop/
* Both parties have to be online at the same time


### Outlook
* Currently, there is no push notification on new packages and so polling or notification over another channel is required.


### Unsorted
Nothing stored online permanently, so there are no expensive and complex requirements for **datacenters** where exchange points might be located.

**Everything is local**, nothing must be central => You don't have to rely on any central third party which might go away and with it your data. This is possible, because today the client hard-drives are so large that disk-space is (normally) not the problem. Locally there is far more disk space available as with most (cheap or cost-free) online services.

goals: stable usage pattern (i.e. local usage should be stable and exchange points can vary as they must), secure, independent

todo: http://standards.freedesktop.org/secret-service/ch02.html

Pay for exchange point service if needed.

Not everything everywhere but have your stuff at the right places.

Good when you regularly exchange files with the same person.

* todo: idea since 16.02.2015: Private incremental git (asr-sync): Auf dem zentralen Server werden nur git-Bundle-Objekte ausgetauscht (und sofort wieder gelöscht). Ein Nutzer ist gleicher als die anderen und hat master-Branch. Behandlung von merge-Konflikten?
    * Teilen von Notizen, Kalender (ics-Kalender-Datei) etc. (Daten werden bei Austausch jedes Mal erneut verschlüsselt)
    * Lokales Lösen von Konflikten (am besten vermeiden, z. B. jeder hat seinen eigenen Kalender)

* old: [fyshare concept draft](fyshare/index.md)


---

asr: First concept: 2014, First prototype: 2015-03-27 / Web content last updated: 2015-08-20
