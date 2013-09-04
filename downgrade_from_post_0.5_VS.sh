#!/bin/bash

[[ -f uimgmv.sh ]] && chmod u+rx uimgmv.sh && ./uimgmv.sh && [[ -f textures/backgrounds/white_up.bmp ]]
if [[ $? -eq 0 ]]
then
svn switch https://svn.wcjunction.com/priv_pu/trunk --username username --password password --config-dir svn/.subversion/
fi

exit $?
