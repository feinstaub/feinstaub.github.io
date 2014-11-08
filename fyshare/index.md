fyshare
=======

...INCUBATING... [Concept](concept.md)

Assumption
----------
It is assumed that within the group of people who want to exchange things with fyshare there is at least one person who has interest and technical insight to setup the central storage server that will hold the sent data in encrypted form. This person has to know how to setup an FTP server and doing basic administering tasks as creating a user and password.

Now the trust in families comes into play because the user and password will be shared among them. When data is sent to a specific person, only this person can decrypt the data locally because of the public key cryptography. But with the shared password it is possible to disturb the operation by deleting files from the central server. But this person will probably be out-cast soon.

Glossary
--------
| Term               | Explanation   |
| ------------------ | ------------- |
| encrypt with public key of receiver          | only the receiver can decrypt the data |
| sign with private key of sender              | receiver can be sure that the data is sent by the sender and not anybody else (by using the public key of the sender) |

Behind fyshare
--------------
The fy in fyshare stands for "family". The program is designed to allow easy and secure sharing of information among family members.
Family can be used in any sense you like. In narrow or extended ways.
When exchanging information there is often the need of sending files bigger than fit in a regular email. For example
the video of the last holiday (with sensible imagary which should not leak out to anyone but the specific family member you send it to).
It should also be suited for smaller files like legal documents. Medium file sizes would be images of the holiday or family event.
