; Kinnear's NSIS SuperPiMP VS Install Script

  Name "Privateer 0.6.0"        ; caption in titlebar
  OutFile "\temp\priv_006.exe"	; installer file to create
  Icon "icon4.ico"		
  BrandingText " "		; removes default 'nullsoft' branding at
				; bottom of window
  CRCCheck on			; YAY!
;  LicenseText "This will install Privateer 0.6.0 onto your PC."
;  LicenseData vega-license.txt

;default install dir, and registry entry
  AutoCloseWindow true
  InstallDir "C:\Program Files\Privateer"
  InstallDirRegKey HKLM SOFTWARE\Privateer\0.6.0\ "Install_Dir"

  ComponentText "This will install Privateer 0.6.0 onto your PC."
  DirText "Choose a directory to install in to:"
  ;EnabledBitmap "yes.bmp"
  ;DisabledBitmap "no.bmp"
  ShowInstDetails show

;first option section - install the program and write uninstall registry
;entries
  Section "Privateer Files (Required)"
  SetOutPath $INSTDIR\Privateer-0.6.0
  File /r "c:\docume~1\danielrh\Desktop\scratch\priv\*.*"
  WriteRegStr HKLM SOFTWARE\Privateer\0.6.0\ "Install_Dir" "$INSTDIR"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Privateer-0.6.0\" "DisplayName" "Privateer 0.6.0"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Privateer-0.6.0\" "UninstallString" '"$INSTDIR\Privateer-0.6.0\uninstall.exe"'
  WriteUninstaller "Privateer-0.6.0\uninstall.exe"
  Rename "$INSTDIR\Vegastrike.exe" "$INSTDIR\Vegastrike.exe.oldrelease"
  Rename "$INSTDIR\Launcher.exe" "$INSTDIR\Launcher.exe.oldrelease"
  Rename "$INSTDIR\Setup.exe" "$INSTDIR\Setup.exe.oldrelease"
  SectionEnd

;second install option - adds the shortcuts to the start menu. optional.
;  Section "Privateer Music (Recommended)"
;  SetOutPath $INSTDIR\Privateer-0.6.0\music
;  File /r "F:\programming\vegastrike\anonymous\priv\music\*.*"
;  WriteRegStr HKLM SOFTWARE\Privateer\0.6.0\ "Install_Dir" "$INSTDIR"
;  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Privateer-0.6.0\" "DisplayName" "Privateer 0.6.0"
;  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Privateer-0.6.0\" "UninstallString" '"$INSTDIR\Privateer-0.6.0\uninstall.exe"'
;  WriteUninstaller "Privateer-0.6.0\uninstall.exe"
;  SectionEnd

;third install option - adds the shortcuts to the start menu. optional.
  Section "Start Menu Shortcuts"
    CreateDirectory "$SMPROGRAMS\Privateer\0.6.0"
    CreateShortCut "$SMPROGRAMS\Privateer\0.6.0\Privateer Story.lnk" "$INSTDIR\Privateer-0.6.0\documentation\CelesteStory.txt" "" "$INSTDIR\Privateer-0.6.0\documentation\CelesteStory.txt" 0
    CreateShortCut "$SMPROGRAMS\Privateer\0.6.0\Privateer Manual.lnk" "$INSTDIR\Privateer-0.6.0\documentation\readme.url" "" "$INSTDIR\Privateer-0.6.0\documentation\readme.url" 0
    CreateShortCut "$SMPROGRAMS\Privateer\0.6.0\Privateer Readme.lnk" "$INSTDIR\Privateer-0.6.0\documentation\readme.txt" "" "$INSTDIR\Privateer-0.6.0\documentation\readme.txt" 0
    CreateShortCut "$SMPROGRAMS\Privateer\0.6.0\Privateer Launcher.lnk" "$INSTDIR\Privateer-0.6.0\bin\Launcher.exe" "" "$INSTDIR\Privateer-0.6.0\bin\Launcher.exe" 0
    CreateShortCut "$SMPROGRAMS\Privateer\0.6.0\Privateer Setup.lnk" "$INSTDIR\Privateer-0.6.0\bin\setup.exe" "" "$INSTDIR\Privateer-0.6.0\bin\setup.exe" 0
    CreateShortCut "$SMPROGRAMS\Privateer\0.6.0\Privateer Uninstall.lnk" "$INSTDIR\Privateer-0.6.0\uninstall.exe" "" "$INSTDIR\Privateer-0.6.0\uninstall.exe" 0
;    CreateShortCut "$SMPROGRAMS\Privateer\0.6.0\Privateer Updater.lnk" "$INSTDIR\Privateer-0.6.0\bin\AutoUpdate.bat" "" "$INSTDIR\Privateer-0.6.0\bin\AutoUpdate.bat" 0
  SectionEnd

;Other Functions - this one is what to do once install is completed
Function .onInstSuccess
;        ExecWait $INSTDIR/Privateer-0.6.0/bin/OpenALwEAX.exe
      ExecWait $INSTDIR/Privateer-0.6.0/bin/SETUP.EXE 
      MessageBox MB_YESNO "Installation Successful. View readme?" IDNO NoReadme
         ExecShell "open" $INSTDIR\Privateer-0.6.0\documentation\readme.txt
         NoReadme:
      MessageBox MB_YESNO "Would you like to veiw the story behind Privateer?" IDNO NoStory
         ExecShell "open" "$INSTDIR\Privateer-0.6.0\history\a brief history in time and space.pdf"
         NoStory:
  FunctionEnd

 Function .onInstFailed
        MessageBox MB_OK "Installation Cancelled or Data corrupt."  
 FunctionEnd

;uninstaller stuff
UninstallText "This will delete the following directory and remove ALL of its contents, including your saved games. Hit the uninstall button to continue."

Section "Uninstall"
  DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Privateer-0.6.0\"
  DeleteRegKey HKLM SOFTWARE\Privateer\0.6.0\
  Delete "$SMPROGRAMS\Privateer\0.6.0\*.*"
  RMDir /r "$SMPROGRAMS\Privateer\0.6.0\"
  RMDir /r "$INSTDIR"
SectionEnd

; note - i haven't made the uninstaller remove Privateer folder. This is
; because we don't want it to delete EVERY copy of VS.. just the one
; they're uninstalling. :)

; eof
