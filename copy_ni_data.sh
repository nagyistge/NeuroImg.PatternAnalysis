#!/bin/bash

nim_dirs=`ls -d /home/nipa_*`
echo Copying $1 to $nim_dirs

for nim_dir in $nim_dirs; do
	echo Copying to: $nim_dir
	sudo cp -R $1 $nim_dir
	sudo chown -R `basename $nim_dir`:`basename $nim_dir` $nim_dir/$1
done
