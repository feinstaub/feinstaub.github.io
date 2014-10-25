kreenshot-editor
================
kreenshot-editor -- **screenshot image editing**

Note! kreenshot-editor is *INCUBATING* and not yet ready for production use. Target schedule for first release: Ende of 2014.

kreenshot-editor is written in QT5 with Linux as target platform.

Target features
---------------

  * Image editing optimized for screenshots. Common editing and annotation tasks that occur when dealing with screenshots:
    * Draw objects and move or resize later
      * rectangle
      * ellipse
      * line
      * arrow
      * text
      * Optional drop shadow for objects
    * Rectangular image operation objects
      * highlight
      * obfuscate
      * Movable and resizeable
    * Crop
    * Undo/Redo
  * Command line interface to integrate it in other screenshot tools that have no own image editor.
    * Example: ```kreenshot-editor --treat-as-new "/tmp/image1.png" --description "Hallo das ist ein Test - aaa \ bbb ///"```
    * Give a secondary image as parameter. This can be used to pass the captured mouse cursor as extra object so the user can move or delete it.
    Thus, the mouse cursor can always be captured and the user decides later.
  * Provide a QWidget component to seemlessly integrate in other screenshot tools
  * Save image to default location with placeholders for date, time etc.

Code
----
(incubating)

  * Source code hosted on [KDE quickgit](http://quickgit.kde.org/?p=scratch%2Fgregormi%2Fkreenshot-editor.git)
  * [README](http://quickgit.kde.org/?p=scratch%2Fgregormi%2Fkreenshot-editor.git&a=blob&f=README.md) with build instructions and current TODOs and open issues.

### Details

  * Widget toolkit: QT 5
  * Primary programming language: C++
  * Build system: cmake

Why?
----

A screenshot tool in general comprises of three parts:

  1. Capture image from screen.
  2. Edit image in some way (optional).
  3. Save image in a standardized user defined way to disk or export it other ways.

kreenshot-editor aims to support the user with task No. 2 and 3.

One goal is to help fixing this [ksnapshot](https://www.kde.org/applications/graphics/ksnapshot/) issue: [Bug 268260 - WISH - Add basic draw functions](https://bugs.kde.org/show_bug.cgi?id=268260)

Inspired by: [Greenshot](http://getgreenshot.org/)

Screenshots
-----------
### dev state 2014-07-05
![Main Window](img/2014-07-05-main-window.png "Main Window")
![Preferences window](img/2014-07-05-prefs.png "Preferences window")
