Linux advanced notes
====================

ReplayGain
----------
How to do mass ReplayGain? How to see which files are already gained?

  * Quod Libet
    * Plugins, [see screenshot](img/2014-01-15 replay gain howto todo 1.png)
    * add columns, [see screenshot](img/2014-01-15 replay gain howto todo 2.png)
  * TODO: more

...


Fix openSUSE Firefox KDE integration
------------------------------------

TODO: This should be enabled by default! Where to file bug reports?

### File chooser

see https://en.opensuse.org/SDB:Mozilla_filechooser

```
Open about:config in Firefox, search for "file_picker" and flip the preference ui.allow_platform_file_picker to false.
```

Now the KDE file dialogs work again.

### Make Firefox for Linux use Dolphin to ‘Open Containing Folder’


see https://fitzcarraldoblog.wordpress.com/2014/09/14/make-firefox-for-linux-use-dolphin-to-open-containing-folder/
see https://forums.opensuse.org/showthread.php/456698-How-use-Dolphin-to-quot-open-containing-folder-quot-from-firefox-downloads?p=2446741#post2446741

```
create a file named ~/.local/share/applications/defaults.list containing the following:
[Default Applications]
x-directory/normal=kde4-dolphin.desktop;kde4-kfmclient_dir.desktop;
```

DOES not work.

My post about the topic: https://forums.opensuse.org/showthread.php/456698-How-use-Dolphin-to-quot-open-containing-folder-quot-from-firefox-downloads?p=2688302#post2688302
(2015-01-10 / wait)

