#!/bin/bash
UPGRADE_FILE_NAME="upgrade_to_post_0.5_VS"
SVNDATA="svn/upgrade_files/"
SVNDIR=`svn info|grep URL|awk '{print $2}'|sed -re 's/.*\/([^\/]+)/\1/'`
UPSVN=$SVNDATA$SVNDIR
EUPSVN=`echo $UPSVN | sed -re 's/\//\\\\\//g'`
UPDIR=`ls -CF $SVNDATA"upgrade_to."*|sed -re 's/.*\.([^\.]+)/\1/'`
UPTO=$SVNDATA$UPDIR
[[ $UPTO"x" == "x" ]] && UPTO=$UPSVN
EUPTO=`echo $UPTO | sed -re 's/\//\\\\\//g'`

REV=`svn info |grep Revision|awk '{print $2}'`
PRE="svn/"
OUT="imgmv"
UPFILEBASE=$OUT"_"$SVNDIR"-r"$REV
DOWNFILEBASE="u"$OUT"_"$SVNDIR"-r"$REV
UPFILE=$PRE$UPFILEBASE
DOWNFILE=$PRE$DOWNFILEBASE
mkdir -p $UPSVN

function doit() {
IFS=":"
#Files
LINES=`find $DIR -type f -name "*."$EXT`
FIRSTFILE=`echo $LINES | head -n 1`
FIRSTFILEW=`echo $FIRSTFILE | sed -re 's/\//\\\/g'`
#.svn data
SVNDIRS=`find $DIR -type d -name ".svn"`
#Remove subdirs we do elsewhere.
for EX in $EXCEPT
do
LINES=`echo $LINES | awk '! /'$EX'/'`
SVNDIRS=`echo $LINES | awk '! /'$EX'/'`
done
#Linux
echo $LINES | sed -re 's/(.*)(\.'$EXT')$/mv \1\2 \1.'$EXTOUT'/' >>$UPFILE.sh.$$
echo $LINES | sed -re 's/(.*)(\.'$EXT')$/mv \1.'$EXTOUT' \1\2/' >>$DOWNFILE.sh.$$
echo $LINES | sed -re 's/(.*\/)([^\/]+)(\.'$EXT')$/mv \1.svn\/prop-base\/\2\3.svn-base \1.svn\/prop-base\/\2.'$EXTOUT'.svn-base/' >>$UPFILE.sh.$$
echo $LINES | sed -re 's/(.*\/)([^\/]+)(\.'$EXT')$/mv \1.svn\/prop-base\/\2.'$EXTOUT'.svn-base \1.svn\/prop-base\/\2\3.svn-base/' >>$DOWNFILE.sh.$$
echo $LINES | sed -re 's/(.*\/)([^\/]+)(\.'$EXT')$/mv \1.svn\/text-base\/\2\3.svn-base \1.svn\/text-base\/\2.'$EXTOUT'.svn-base/' >>$UPFILE.sh.$$
echo $LINES | sed -re 's/(.*\/)([^\/]+)(\.'$EXT')$/mv \1.svn\/text-base\/\2.'$EXTOUT'.svn-base \1.svn\/text-base\/\2\3.svn-base/' >>$DOWNFILE.sh.$$
#Windows
BLINES=`echo $LINES | sed -re 's/\//\\\/g'`
echo $BLINES | sed -re 's/(.*)(\.'$EXT')$/rename \1\2 \1.'$EXTOUT'/' >>$UPFILE.bat.$$
echo $BLINES | sed -re 's/(.*)(\.'$EXT')$/rename \1.'$EXTOUT' \1\2/' >>$DOWNFILE.bat.$$
echo $BLINES | sed -re 's/(.*\\)([^\\]+)(\.'$EXT')$/rename \1.svn\\prop-base\\\2\3.svn-base \1.svn\\prop-base\\\2.'$EXTOUT'.svn-base/' >>$UPFILE.bat.$$
echo $BLINES | sed -re 's/(.*\\)([^\\]+)(\.'$EXT')$/rename \1.svn\\prop-base\\\2.'$EXTOUT'.svn-base \1.svn\\prop-base\\\2\3.svn-base/' >>$DOWNFILE.bat.$$
echo $BLINES | sed -re 's/(.*\\)([^\\]+)(\.'$EXT')$/rename \1.svn\\text-base\\\2\3.svn-base \1.svn\\text-base\\\2.'$EXTOUT'.svn-base/' >>$UPFILE.bat.$$
echo $BLINES | sed -re 's/(.*\\)([^\\]+)(\.'$EXT')$/rename \1.svn\\text-base\\\2.'$EXTOUT'.svn-base \1.svn\\text-base\\\2\3.svn-base/' >>$DOWNFILE.bat.$$
#Copies svn special files
IFS=$' \t\n'
svn rm $SVNDATA$SVNDIR --force
`echo $SVNDIRS | sed -re 's/^(.*\/)\.(svn)$/mkdir -p '$EUPSVN'\/\1\2/'`
`echo $SVNDIRS | sed -re 's/^(.*\/)\.(svn)$/cp -f \1\.\2\/all-wcprops \1\.\2\/entries '$EUPSVN'\/\1\2\//'`
svn add $SVNDATA$SVNDIR
#If we have an upgrade dir, execute this script there and grab the svn data.
if [[ $UPDIR"x" != "x" ]];then
cp -a $0 ../$UPDIR/$0
cd ../$UPDIR
$0
cd -
svn rm $SVNDATA$UPDIR --force
rsync "-rlpti" "--delete-during" "--exclude=*/.svn/*" "../"$UPDIR"/"$SVNDATA$UPDIR $SVNDATA
svn add $SVNDATA$UPDIR --force
svn rm "../"$UPDIR"/"$SVNDATA$SVNDIR --force
rsync "-rlpti" "--delete-during" "--exclude=*/.svn/*" $SVNDATA$SVNDIR "../"$UPDIR"/"$SVNDATA
svn add "../"$UPDIR"/"$SVNDATA$SVNDIR --force
fi
IFS=":"
#Linux
echo $SVNDIRS | sed -re 's/^(.*\/)\.(svn)$/cp -f '$EUPTO'\/\1\2\/all-wcprops '$EUPTO'\/\1\2\/entries \1\.\2\//' >>$UPFILE.sh.$$
echo $SVNDIRS | sed -re 's/^(.*\/)\.(svn)$/cp -f '$EUPSVN'\/\1\2\/all-wcprops '$EUPSVN'\/\1\2\/entries \1\.\2\//' >>$DOWNFILE.sh.$$
#Windows
echo $SVNDIRS | sed -re 's/^(.*\/)\.(svn)$/copy -f '$EUPTO'\/\1\2\/all-wcprops '$EUPTO'\/\1\2\/entries \1\.\2\//' | sed -re 's/\//\\/g' >>$UPFILE.bat.$$
echo $SVNDIRS | sed -re 's/^(.*\/)\.(svn)$/copy -f '$EUPSVN'\/\1\2\/all-wcprops '$EUPSVN'\/\1\2\/entries \1\.\2\//' | sed -re 's/\//\\/g' >>$DOWNFILE.bat.$$
IFS=$' \t\n'
}

# Script to find extensions (including multiple extensions) for all files.
#find . -type f |sed -re 's/.*.svn.*//g'|sed -re 's/^.\/(.*)/\1/'|sed -re 's/.*\/([^\/]+)$/\1/'|sed -re 's/[^.]*(\..*)$/\1/'|grep "\." >ext
#sort -u ext >ext.sort

#Directories to migrate with renaming information.
EXTOUT="image"
DIR=".";EXT="bmp";EXCEPT=""
#doit
DIR=".";EXT="gif";EXCEPT=""
#doit
DIR=".";EXT="png";EXCEPT=""
#doit
DIR=".";EXT="PNG";EXCEPT=""
#doit
DIR=".";EXT="png.jpg";EXCEPT=""
#doit
DIR=".";EXT="jpg";EXCEPT=".png.jpg$"
#doit

EXTOUT="texture";EXCEPT="^textures\/backgrounds\/:^textures\/upgrades\/:^textures\/cargo\/:^textures\/cockpit\/"
DIR="textures/";EXT="png"
#doit
DIR="textures/";EXT="jpg"
#doit
DIR="textures/";EXT="bmp"
#doit

EXTOUT="image";EXCEPT=""
DIR="textures/backgrounds/";EXT="bmp"
doit
DIR="textures/upgrades/";EXT="png"
#doit
DIR="textures/cargo/";EXT="png"
#doit
DIR="textures/cargo/";EXT="jpg"
#doit
DIR="textures/cockpit/";EXT="png"
#doit
DIR="cockpits/";EXT="png"
#doit
DIR="cockpits/";EXT="bmp"
#doit
DIR="animations/";EXT="jpg"
#doit
DIR="animations/";EXT="png"
#doit
DIR="units/";EXT="png"
#doit
DIR="sprites/";EXT="png"
#doit
DIR="sprites/";EXT="png.jpg"
#doit
EXCEPT=".png.jpg$"
DIR="sprites/";EXT="jpg"
#doit

EXTOUT="sprite";EXCEPT=""
DIR="cockpits/";EXT="spr"
#doit
DIR="sprites/";EXT="spr"
#doit

#Linux
echo "#!/bin/bash
cd .." >$UPFILE.sh
sort $UPFILE.sh.$$ | awk '! /^$/' >>$UPFILE.sh
rm $UPFILE.sh.$$
echo "exit 0" >>$UPFILE.sh

echo "#!/bin/bash
cd .." >$DOWNFILE.sh
sort $DOWNFILE.sh.$$ | awk '! /^$/' >>$DOWNFILE.sh
rm $DOWNFILE.sh.$$
echo "exit 0" >>$DOWNFILE.sh

#Windows
echo "cd .." >$UPFILE.bat
sort $UPFILE.bat.$$ | awk '! /^$/' >>$UPFILE.bat
rm $UPFILE.bat.$$
echo "pause" >>$UPFILE.bat
unix2dos $UPFILE.bat

echo "cd .." >$DOWNFILE.bat
sort $DOWNFILE.bat.$$ | awk '! /^$/' >>$DOWNFILE.bat
rm $DOWNFILE.bat.$$
echo "pause" >>$DOWNFILE.bat
unix2dos $DOWNFILE.bat

#If we want to be able to un-upgrade we need the script after the upgrade.
if [[ $UPDIR"x" != "x" ]];then
cp -f $DOWNFILE.sh ../$UPDIR/$DOWNFILE.sh
cp -f $DOWNFILE.bat ../$UPDIR/$DOWNFILE.bat
fi

#Create upgrade scripts
echo "#!/bin/bash
cd svn
svn up svn
./upgrades.sh
exit $?" > $UPGRADE_FILE_NAME.sh
svn revert svn/upgrades.sh
echo "#!/bin/bash
svn up $UPFILEBASE.sh
[[ -f $UPFILEBASE.sh ]] && chmod u+rx $UPFILEBASE.sh && ./$UPFILEBASE.sh && [[ ! -f ../$FIRSTFILE ]]
if [[ $? -eq 0 ]]
then
svn switch https://svn.wcjunction.com/priv_pu/priv_pu .. --username username --password password --config-dir .subversion/
svn co https://svn.wcjunction.com/priv_pu/win32bin ../../win32bin/ --username username --password password --config-dir .subversion/
fi
exit $?" >> svn/upgrades.sh

echo "cd svn
svn up svn
upgrades.bat" > $UPGRADE_FILE_NAME.bat
unix2dos $UPGRADE_FILE_NAME.bat
svn revert svn/upgrades.bat
echo "svn up $UPFILEBASE.bat
IF EXIST ..\\$FIRSTFILEW $UPFILEBASE.bat
#If successful do the following:
IF NOT EXIST ..\\$FIRSTFILEW svn switch https://svn.wcjunction.com/priv_pu/priv_pu .. --username username --password password --config-dir .subversion\\
IF NOT EXIST ..\\$FIRSTFILEW svn co https://svn.wcjunction.com/priv_pu/win32bin ..\\..\\win32bin\\ --username username --password password --config-dir .subversion\\" >> svn/upgrades.bat
unix2dos svn/upgrades.bat

TARGETS="$UPFILE.sh $DOWNFILE.sh $UPFILE.bat $DOWNFILE.bat $UPGRADE_FILE_NAME.sh $UPGRADE_FILE_NAME.bat svn/upgrades.sh svn/upgrades.bat ../$UPDIR/$DOWNFILE.sh ../$UPDIR/$DOWNFILE.bat"
svn add $TARGETS
svn propset svn:executable $TARGETS


exit $?
