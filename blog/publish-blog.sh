#!/bin/bash -e

# http://superuser.com/questions/409980/sync-two-local-folders-in-bash
SRCDIR=_site
PUBDIR=~/dataDocuments/aux/feinstaub.github.io/blog

# build to destination
# see ../z.Quicksteps-to-blog.md
jekyll build --destination  ~/dataDocuments/aux/feinstaub.github.io/blog

cd $PUBDIR
git add .
git commit -m "update blog"

echo "Push? (ENTER to continue, Ctrl+C to abort)"
read

git push origin master
