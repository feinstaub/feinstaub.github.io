Bugs, wishes and annoyances / KDE UI
====================================
This page collects issues I stumbled on when using Linux with KDE.

ksnapshot [several]
----------------
### Make "Send to..." configurable

Current situation: the menu is crowed with over 20 entries and takes up to a few seconds to load.

SUGGESTION: Add item "Configure this menu".
All kipi plugin entries should be present by default and the Configure dialog should
allow to exclude undesired items. In addition, it should be possible to define user
defined commands to edit images.

### Add option for 100% zoom

Current situation: the preview image zoomed to fit which makes it cumbersome to view it 100% for pixel perfectness.

SUGGESTION: add option to zoom to 100%.
If image is too large, scrollbars should be shown. Or at least the image should not be zoom more than 100%.

### Reversed check boxes

see [Reversed check boxes in ksnapshot](http://agateau.com/2010/common-user-interface-mistakes-in-kde-applications-part-2-dialog-layouts/)


Dolphin [wish]: Symlink --> Show original file
----------------------------------------------
v4.11.5, 2014, not reported yet, WAIT for KF5

There is currently no quick way to navigate to the original file or folder behind a symlink.

see also [ Bug 336194 - "Show Original Directory" in context menu on symlinked folder on desktop does not work](https://bugs.kde.org/show_bug.cgi?id=336194)


Dolphin [wish]: Drag and Drop to compress
-----------------------------------------
v4.11.5, 2014, not reported yet, WAIT for KF5

TODO: make it public to community (first: check latest plasma)

When dropping selected files and or folders to some folder the user gets a menu with the following options:

### CURRENT

  * Move here
  * Copy here
  * Link here

When dropping an archive file (zip, rar, tgz etc.) there is already an “Extract here” menu item.

### SUGGESTED
Add a new item with submenu items taken from the standard Compress context menu.

  * Compress here >
    * Here
    * As ZIP Archive
    * As RAR Archive
    * …
    * Compress To…

### Use cases where current methods are inconvenient
  * Goal is to compress a local folder on an external drive (e.g. to archive the folder away).
  With suggested method it is easy to minimize the data will be transferred from one drive to the other.


Font Installer [usability]: wrong kind of message box
-----------------------------------------------------
2014-10, WAIT for KF5

This should be an information box and not error box:

![](img/Font Installer - should be information and not error.png)


Thunderbird [bug]: Drag and Drop attachment
-------------------------------------------
2014-06, not solved since 2007

Drag and Drop of attachment files from Mozilla Thunderbird to the KDE Desktop is not working. The appearing menu shows “Link here” and “Cancel” instead of “Copy here”.

Bug exists since 2007 in TB: [Bug 377621 - Drag and Drop attachments to desktop or folders doesn't work ](https://bugzilla.mozilla.org/show_bug.cgi?id=377621)


Plasma [usability]: flash modal
-------------------------------
2014-10-26, WAIT for KF5

A modal dialog should flash or similar when the gray dolphin window is clicked.

Currently it does nothing.
![](img/plasma-flash-modal.png "Modal dialog should flash or similar when the gray dolphin window is clicked")


See also
--------
  * Aurélien Gâteau's article series about [Common user interface mistakes in KDE applications](http://agateau.com/article-series/common-ui-mistakes-in-kde-applications/) (TODO: read)
