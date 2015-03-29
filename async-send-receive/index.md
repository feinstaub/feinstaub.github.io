asr - async-send-receive
========================

First alpha version: 2015-03-27
Content last updated: 2015-03-29


Introduction
------------
Asr is a tool built around the idea to exchange data between
two computers using a third, potentially completely untrusted, party
(like internet hosting services, corporate network shares etc.)
in an asynchronous way.

Asr currently does not target the ultra-mobile-cloud-user audience
but more the being-offline kind of use cases. Places in the Internet
are classified as untrusted sites and private data should not lie
around needlessly or even unprotected.
So asr tries to provide an electronic way of sending someone a
package via postal service; including privacy of correspondence,
posts and telecommunications.

If you send someone a postal package there is usually no trace of the
package's content between sender and receiver. The only metadata
which is tracked is who sent it and who received it. Asr also
tries to minimize public metadata.

As with regular email, the process of sending and receiving is
asynchronous. The receiver does not have to be online when a package
is sent.

Currently, there is no push notification on new packages
and so the self-collector principle applies (as with regular email).

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


Requirements
------------
Asr is a Python script which currently has the following dependencies:

- tar
- openssl
- python-guidata (has some more python deps)
- gnome-web-photo (optional)
- wget (optional)


Download alpha version
----------------------
* [asr.py](asr.py)
* [asr](asr)
* [asr-demo-config](asr-demo-config)
* [asr-unit-test.py](asr-unit-test.py)


Quickstart: Send someone encrypted files
----------------------------------------
### Scenario
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
