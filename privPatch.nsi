; MamiyaOtaru's Privateer Remake install script, adapted from
; Kinnear's NSIS SuperPiMP VS Install Script
; requires recent version of NSIS (2.1 is good)

Page components
Page directory
Page instfiles
UninstPage uninstConfirm
UninstPage components
UninstPage instfiles

SetDatablockOptimize off ;fark.. 50 minutes to compile down to 2

  Name "VegaStrike Privateer Remake 1.1 Patch (beta)"        ; caption in titlebar
  OutFile "vs_priv_1.1_patch_win32.exe"	; installer file to create
  Icon "D:\privateer\priv\vega.ico"		
  BrandingText " "		; removes default 'nullsoft' branding at
				; bottom of window
  CRCCheck on			; YAY!
  LicenseText "This will install the Vega Strike Privateer Remake 1.1 Patch (beta) onto your PC."
;  LicenseData vega-license.txt

;default install dir, and registry entry
  AutoCloseWindow true
  InstallDir "C:\Program Files\Vegastrike\Privateer"
  InstallDirRegKey HKLM SOFTWARE\Vegastrike\priv\ "Install_Dir"

  ComponentText "This will update the Vega Strike Privateer Remake to version 1.1 (beta)."
  DirText "Select the directory where the Remake is installed"
;  EnabledBitmap "yes.bmp"
;  DisabledBitmap "no.bmp"
  ShowInstDetails show

;first option section - install the program and write uninstall registry (no uninstall for patch)
;entries
Section "Privateer Remake 1.1 Patch Files (Required)"
  SectionIn RO
  SetOutPath $INSTDIR
  File /r "D:\privateer\privateer\*.*"
  WriteUninstaller "uninstall.exe"
  Rename "$SMPROGRAMS\Privateer1.0" "$SMPROGRAMS\Privateer1.1"
SectionEnd

;uninstaller stuff
UninstallText "This will delete all files in the following directory, aside from files that existed before installing, files you added manually, and your savegame/universe data directory, unlesss you choose to remove it.  Remaining files must be removed manually.  Hit the uninstall button to continue."

!define unicon "D:\privateer\priv\uninstall.ico"	
!ifdef unicon
UninstallIcon "${unicon}"
!endif

Section "un.Uninstall Data Files"
  SectionIn RO
  DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\VegaStrike-Privateer"
  DeleteRegKey HKLM "SOFTWARE\VegaStrike\priv"
  Delete "$SMPROGRAMS\Privateer1.1\*.*"
  RMDir /r "$SMPROGRAMS\Privateer1.1\"
  RMDir /r "$INSTDIR\ai"
  RMDir /r "$INSTDIR\animations"
  RMDir /r "$INSTDIR\bases"
  RMDir /r "$INSTDIR\bin"
  RMDir /r "$INSTDIR\cockpits"
  RMDir /r "$INSTDIR\communications"
  RMDir /r "$INSTDIR\meshes"
  RMDir /r "$INSTDIR\mission"
  RMDir /r "$INSTDIR\modules"
  RMDir /r "$INSTDIR\music"
  RMDir /r "$INSTDIR\sectors"
  RMDir /r "$INSTDIR\sounds"
  RMDir /r "$INSTDIR\sprites"
  RMDir /r "$INSTDIR\textures"
  RMDir /r "$INSTDIR\units"
  RMDir /r "$INSTDIR\universe"
  Delete "$INSTDIR\credits.txt"
  Delete "$INSTDIR\factions.xml"
  Delete "$INSTDIR\Manual.pdf"
  Delete "$INSTDIR\master_part_list.csv"
  Delete "$INSTDIR\setup.config"
  Delete "$INSTDIR\ToDo.txt"
  Delete "$INSTDIR\vegastrike.config"
  Delete "$INSTDIR\vegastrike.config.temp"
  Delete "$INSTDIR\version.txt"
  Delete "$INSTDIR\weapon_list.xml"
  ; MUST REMOVE UNINSTALLER, too
  Delete $INSTDIR\uninstall.exe
  RMDir "$INSTDIR"
  ;RMDir /r "$INSTDIR"
SectionEnd

Section "un.Remove Savegame/Universe Data directory (optional)" 
  RMDir /r "$INSTDIR\.privateer100"
  RMDir "$INSTDIR"
SectionEnd

;Other Functions - this one is what to do once install or uninstall is completed

; confirm that a previous version of privateer exists in that directory
Function .onVerifyInstDir
  IfFileExists $INSTDIR\vegastrike.config Good
    Abort
  Good:
FunctionEnd

Function .onInstSuccess
  ExecWait $INSTDIR/bin/SETUP.EXE 
  MessageBox MB_YESNO "Installation Successful. View readme?" IDNO NoReadme
     ExecShell "open" $INSTDIR/Manual.pdf
     NoReadme:
FunctionEnd

Function .onInstFailed
        MessageBox MB_OK "Installation Cancelled or Data corrupt."  
FunctionEnd

Function un.onUninstSuccess
  IfFileExists $INSTDIR Leftovers
  MessageBox MB_OK "You have successfully uninstalled the Privateer Remake"
  goto end
  
  Leftovers:
    MessageBox MB_OK "You have successfully uninstalled the Privateer Remake.  Certain files were not deleted.  These include either files that existed before installation or new files (either manually added by yourself, or savegames if you chose not to uninstall them).  Such files can only be removed manually."
    goto end
      
  End:
FunctionEnd

; eof