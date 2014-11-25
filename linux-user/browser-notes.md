Firefox
=======

Bookmarks and Tags
------------------
### More results in Awesomebar instead of only 12

about:config:

* `browser.urlbar.maxRichResults` Set to 330 instead of 12
* `places.frecency.bookmarkVisitBonus` set to 300
* `places.frecency.unvisitedBookmarkBonus` set to 300

(see http://lifehacker.com/the-best-about-config-tweaks-that-make-firefox-better-1442137111)


### Search for bookmarks only

Append these to awesomebar search string separated by spaces

```
Add + to search for matches in pages you've tagged.

Add * to search for matches in your bookmarks.

Add ^ to search for matches in your browsing history.
Add % to search for matches in your currently open tabs.
Add ~ to search for matches in pages you've typed.
Add # to search for matches in page titles.
Add @ to search for matches in web addresses (URLs).
```

(see https://support.mozilla.org/en-US/kb/awesome-bar-find-your-bookmarks-history-and-tabs#w_what-can-i-do-to-get-the-best-results)
