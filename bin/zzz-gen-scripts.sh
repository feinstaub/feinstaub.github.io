#!/bin/bash

bin_dir=.
target_bin_html_file=scripts-index.md
SELF=zzz-gen-scripts.sh
GEN_DIR=web-gen

echo "  bin_dir=$bin_dir"
echo "  target_bin_html_file=$target_bin_html_file"

mkdir -p $GEN_DIR

echo "" > $target_bin_html_file
# echo 'HALLO' >> $target_bin_html_file

for SUB_DIR in $bin_dir $bin_dir/bash ; do

    # http://unix.stackexchange.com/questions/48492/list-only-regular-files-but-not-directories-in-current-directory
    for script_file in `ls $SUB_DIR -p | grep -v /` ; do
    if [ $script_file != "$target_bin_html_file" ] ; then
        echo "   - process $SUB_DIR/$script_file"
        cp $SUB_DIR/$script_file $GEN_DIR/${script_file}.txt
        echo "[$SUB_DIR/$script_file]($GEN_DIR/${script_file}.txt)" >> $target_bin_html_file
        # cat $bin_dir/$script_file >> $target_bin_html_file
        #echo ")" >> $target_bin_html_file
    fi
    done

done

# echo 'hallo4' >> $target_bin_html_file