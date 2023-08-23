#!/bin/bash

echo "Enter Filename: ";read a

vim $a

python3 $a

if [[ $? == 0 ]]
then
	bash /home/hdd/gitauto/dsacodingninjas/.git/scripts/gitpush.sh
fi


