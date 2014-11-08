KDE building and contributing
=============================

FAQ about dev env
-----------------
When asking questions about KF5, the following information is often requested:
Running Plasma 4 on openSUSE 13.1, KDE version 4.11.5, branch frameworks


Build KF5 frameworks hints
--------------------------
see https://community.kde.org/Frameworks/Building

./kdesrc-build, non-critical modules that take very long to compile:

* okteta
* kdepim

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

-- Aaron J. Seigo
```

```
Hi,

when you built ksnapshot, was KIPI_FOUND defined? I installed
libkipi-devel but KIPI_FOUND was not set. So is this macro still in use?

Regards

Gregor
_______________________________________________
Kde-graphics-devel mailing list
Kde-graphics-devel@kde.org
https://mail.kde.org/mailman/listinfo/kde-graphics-devel
```

### kate: "crash in kateprojectworker.cpp", 2014-11-02
* Bug reports via mailing list
  * kwrite-devel@kde.org
    * "crash in kateprojectworker.cpp", 2014-11-02


KDE community contributions [done]
----------------------------------
* Wiki
 * https://community.kde.org/Frameworks/Building
 * https://community.kde.org/User:Gregormi

