#!/bin/bash


root_dir=.
bin_dir=.
target_bin_html_file=scripts-index.md
SELF=zzz-gen-scripts.sh

echo "  root_dir=$root_dir"
echo "  bin_dir=$bin_dir"
echo "  target_bin_html_file=$target_bin_html_file"

echo "" > $target_bin_html_file
# echo 'HALLO' >> $target_bin_html_file

for script_file in `find $bin_dir` ; do
  if [ $script_file != "." ] && [ $script_file != "./$target_bin_html_file" ] && [ $script_file != "./bash" ] ; then
    echo "   - process $script_file"
    echo "[$script_file]($script_file)" >> $target_bin_html_file
    #cat $bin_dir/$script_file >> $target_bin_html_file
    #echo ")" >> $target_bin_html_file
  fi
done

# echo 'hallo4' >> $target_bin_html_file
