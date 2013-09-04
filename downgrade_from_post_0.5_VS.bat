@echo off
uimgmv.bat
IF EXIST textures\backgrounds\white_up.bmp svn\svn switch https://svn.wcjunction.com/priv_pu/trunk --username username --password password --config-dir svn\.subversion\
pause
