FyShare (fyshare) Concept document
==================================
Author(s): Gregor Mi

Abstract
--------
This document describes the main concepts of the file exchange client FyShare. The goal of FyShare is to make secure exchange of all kinds of files within a small group of people as easy as possible. This includes automatic encryption and decryption to eliminate hassle when private keys get lost (in the sense of deleted and not stolen).

Secure exchange is achieved by using asymmetric encryption methods. FyShare assists with generating and distributing the keys and identities within the FyShare network.

The assumption are trustworthy family computers but untrustworthy and unencryped transport channels and online file storage. Thus end-to-end encryption is used.

The online file storage is free to choose. In the first version of FyShare could be based on dropbox.

The exchange can be done a) from one person to another b) within a group of people where b) could be implemented by creating a new private key for each combination of group members and distribute it among them via the secure channel of in a).

Related work
------------
### Retroshare
http://retroshare.sourceforge.net/ - decentralized, no central server
“How many people are required for a working RetroShare network?
But it is recommended to tell all your friends to Chat with RetroShare, because then you have enough trusted direct friends and do not rely on friends of friends to keep the network up. Just tell your friends and commit each other to be constant online with RetroShare, then you have always only trusted friends online.
[…]
How fast is the upload and download speed?
Depends on your connection and other traffic, but it is usually limited by the upload capacity of the user uploading. ” (http://retroshare.sourceforge.net/wiki/index.php/Frequently_Asked_Questions, highlighted by author)
Evaluation: FyShare uses central storage to exchange data asynchronously

### Sparkleshare
http://sparkleshare.org/ - gitbased, cannot use central service like dropbox,
TODO: understand the concept and verify that it cannot do what FyShare does.

### Plutus
“Plutus: Scalable Secure File Sharing on Untrusted Storage” (http://dl.acm.org/citation.cfm?id=1090698)
“Plutus is a cryptographic storage system that enables secure file sharing without placing much trust on the file servers. In particular, it makes novel use of cryptographic primitives to protect and share files. Plutus features highly scalable key management while allowing individual users to retain direct control over who gets access to their files. We explain the mechanisms in Plutus to reduce the number of cryptographic keys exchanged between users by using filegroups, distinguish file read and write access, handle user revocation efficiently, and allow an untrusted server to authorize file writes. We have built a prototype of Plutus on OpenAFS. Measurements of this prototype show that Plutus achieves strong security with overhead comparable to systems that encrypt all network traffic.”
see [plutus.pdf](plutus.pdf)

### Further
https://en.wikipedia.org/wiki/WASTE – dead, decentralized, no central server
http://www.syncany.org/ - backup and share with oneself
BeeBEEP (Secure Network Chat) http://sourceforge.net/p/beebeep
http://lifehacker.com/what-s-the-best-way-to-share-large-files-with-friends-1486810038
    http://en.wikipedia.org/wiki/Comparison_of_file_hosting_services
https://www.cloudme.com/en/api/webservices
https://spideroak.com/faq/questions/37/how_do_i_use_the_spideroak_web_api/
http://www.techradar.com/news/internet/cloud-services/send-large-files-10-of-the-best-services-for-sharing-big-files-1181486

Main parts
----------
see [FyShare-Concept.odt](FyShare-Concept.odt)

Online file storage providers
-----------------------------
List of potential free and public file storages. TODO: gibts da noch was besseres?

### dropbox
terms of service: https://www.dropbox.com/terms2014, https://www.dropbox.com/terms#acceptable_use: checked, should be ok
dropbox-cli command line client
what can be automated?

Use https://github.com/lycis/QtDropbox (http://lycis.github.io/QtDropbox/) to implement the following with a root folder named “fyshare”:

* create folder
* upload file
* query folder contents
* download
* delete file

### filedropper
http://www.filedropper.com/

### TODO: evaluate
Die Top 10 der Online-Speicher: http://www.computerwoche.de/a/die-top-10-der-online-speicher,2530609

### Private FTP server
...give your friends access to one specific directory to your simple unencrypted FTP server...

