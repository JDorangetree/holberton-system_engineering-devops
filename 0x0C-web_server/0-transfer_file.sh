#!/usr/bin/env bash
#transfers a file from our client to a server
if [ "$#" -le 2 ]
then
    echo "Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY"
elif [ "$#" -eq 3 ]
then
    scp -o Stricthostkeychecking=no "$1" "$3@$2":~/
elif [ "$#" -eq 4 ]
then
    scp -o Stricthostkeychecking=no Stricthostkeychecking=no "$1" "$3@$2":~/ -i "$4"
fi
