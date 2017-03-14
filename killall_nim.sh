#!/bin/bash

nim_dirs=`ls -d /home/nim_*`

for nim_dir in $nim_dirs; do
	echo Killing: $nim_dir
	sudo killall --user `basename $nim_dir`
done


