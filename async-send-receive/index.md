asr - async-send-receive
========================

First alpha version: 2015-03-27
Content last updated: 2015-03-28


Introduction
------------
Asr is a tool built around the idea to exchange data between
two computers using a third, potentially completely untrusted, party
(like internet hosting services, corporate network shares etc.)
in an asynchronous way.

Asr currently does not target the ultra-mobile-cloud-user audience
but more the being-offline kind of use cases. Places in the Internet
are classified as untrusted sites and private data should lie
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


Quickstart
----------
* Download asr and put it in your PATH.

* Create the directory `~/asr/configfiles` and place the asr-demo-config inside.

* TODO

