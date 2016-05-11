#!/bin/bash
#Mostly copied from the nocrash.sh (https://github.com/Charcoal-SE/SmokeDetector/blob/master/nocrash.sh)
#on Smoke Detector made by Charcoal (https://github.com/Charcoal-SE/SmokeDetector)
read -p "Username: " u
export ChatExchangeU=$u
export CEU="h"
stty -echo
read -p "Password: " p
export ChatExchangeP=$p
stty echo
count=0
crashcount=0
stoprunning=0
while [ "$stoprunning" -eq "0" ]
do
   if [ "$count" -eq "0" ]
   then
    python2 main.py first_start
   else
    python2 main.py
   fi

   ecode=$?

   if [ "$ecode" -eq "3" ]
   then
    git checkout master
    git pull
    git submodule update
    count=0
    crashcount=0

   elif [ "$ecode" -eq "4" ]
   then
    count=$((count+1))
    sleep 5
    if [ "$crashcount" -eq "2" ]
    then
     git checkout HEAD~1
     count=0
     crashcount=0
    else
     crashcount=$((crashcount+1))
    fi

    elif [ "$ecode" -eq "5" ]
    then
     count=0
    elif [ "$ecode" -eq "6" ]
    then
     stoprunning=1

    else
     sleep 5
     count=$((count+1))

   fi
done
