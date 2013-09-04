#!/bin/bash

WORKDIR="./"
VEGADIR="vegastrike/"
EXE="vegastrike"
NB=0

rm *.pyc */*.pyc */*/*.pyc >/dev/null 2>/dev/null
which $EXE >/dev/null 2>&1 #Try to find executable in user PATH.
if [[ $? -eq 0 ]]
then #If found, execute it.
	$EXE
else #If not found seek in parent dirs.
	while [[ ! -f $WORKDIR$VEGADIR$EXE ]]
	do
		(( NB = $NB + 1 ))
		if [[ $NB -ge 4 ]];then exit -1;fi
		WORKDIR=$WORKDIR"../"
	done
	$WORKDIR$VEGADIR$EXE
fi
rm *.pyc */*.pyc */*/*.pyc >/dev/null 2>/dev/null

exit $?
