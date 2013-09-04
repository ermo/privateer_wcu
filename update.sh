#!/bin/bash

svn update svn/update.sh --username username --password password --config-dir svn/.subversion/
cd svn
chmod u+rx update.sh
./update.sh

exit $?
