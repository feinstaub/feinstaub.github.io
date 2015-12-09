#!/bin/bash

# http://superuser.com/questions/409980/sync-two-local-folders-in-bash
SRCDIR=.
PUBDIR=~/dev/src/feinstaub.github.io/arbeitsblatt.net

# http://serverfault.com/questions/225140/rsync-wont-delete-files-on-destination
rsync -av --delete $SRCDIR/ $PUBDIR/

cd $PUBDIR
git add .
git commit -m "update arbeitsblatt"

echo "Push? (ENTER to continue, Ctrl+C to abort)"
read

git push origin
