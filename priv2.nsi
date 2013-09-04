 ; GetWindowsVersion
 ;
 ; Based on Yazno's function, http://yazno.tripod.com/powerpimpit/
 ; Updated by Joost Verburg
 ;
 ; Returns on top of stack
 ;
 ; Windows Version (95, 98, ME, NT x.x, 2000, XP, 2003)
 ; or
 ; '' (Unknown Windows Version)
 ;
 ; Usage:
 ;   Call GetWindowsVersion
 ;   Pop $R0
 ;   ; at this point $R0 is "NT 4.0" or whatnot
 
 Function GetWindowsVersion
 
   Push $R0
   Push $R1
 
   ReadRegStr $R0 HKLM \
   "SOFTWARE\Microsoft\Windows NT\CurrentVersion" CurrentVersion

   IfErrors 0 lbl_winnt
   
   ; we are not NT
   ReadRegStr $R0 HKLM \
   "SOFTWARE\Microsoft\Windows\CurrentVersion" VersionNumber
 
   StrCpy $R1 $R0 1
   StrCmp $R1 '4' 0 lbl_error
 
   StrCpy $R1 $R0 3
 
   StrCmp $R1 '4.0' lbl_win32_95
   StrCmp $R1 '4.9' lbl_win32_ME lbl_win32_98
 
   lbl_win32_95:
     StrCpy $R0 '95'
   Goto lbl_done
 
   lbl_win32_98:
     StrCpy $R0 '98'
   Goto lbl_done
 
   lbl_win32_ME:
     StrCpy $R0 'ME'
   Goto lbl_done
 
   lbl_winnt:
 
   StrCpy $R1 $R0 1
 
   StrCmp $R1 '3' lbl_winnt_x
   StrCmp $R1 '4' lbl_winnt_x
 
   StrCpy $R1 $R0 3
 
   StrCmp $R1 '5.0' lbl_winnt_2000
   StrCmp $R1 '5.1' lbl_winnt_XP
   StrCmp $R1 '5.2' lbl_winnt_2003 lbl_error
 
   lbl_winnt_x:
     StrCpy $R0 "NT $R0" 6
   Goto lbl_done
 
   lbl_winnt_2000:
     Strcpy $R0 '2000'
   Goto lbl_done
 
   lbl_winnt_XP:
     Strcpy $R0 'XP'
   Goto lbl_done
 
   lbl_winnt_2003:
     Strcpy $R0 '2003'
   Goto lbl_done
 
   lbl_error:
     Strcpy $R0 ''
   lbl_done:
 
   Pop $R1
   Exch $R0
 
 FunctionEnd
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

  Name "VegaStrike Privateer Remake"        ; caption in titlebar
  OutFile "vs_priv_1.1_win32.exe"	; installer file to create
  Icon "C:\i\privateer\priv\vega.ico"		
  BrandingText " "		; removes default 'nullsoft' branding at
				; bottom of window
  CRCCheck on			; YAY!
  LicenseText "This will install the Vega Strike Privateer Remake onto your PC."
;  LicenseData vega-license.txt

;default install dir, and registry entry
  AutoCloseWindow true
  InstallDir "C:\Program Files\Vegastrike\Privateer"
  InstallDirRegKey HKLM SOFTWARE\Vegastrike\priv\ "Install_Dir"

  ComponentText "This will install the Vega Strike Privateer Remake 1.1 onto your PC."
  DirText "Choose a directory to install in to:"
;  EnabledBitmap "yes.bmp"
;  DisabledBitmap "no.bmp"
  ShowInstDetails show

;first option section - install the program and write uninstall registry
;entries
Section "Privateer Remake Files (Required)"
  SectionIn RO
  SetOutPath $INSTDIR
  File /r "C:\i\privateer\priv\*.*"
  WriteRegStr HKLM SOFTWARE\VegaStrike\priv\ "Install_Dir" "$INSTDIR"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\VegaStrike-Privateer\" "DisplayName" "VegaStrike Privateer"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\VegaStrike-Privateer\" "UninstallString" '"$INSTDIR\uninstall.exe"'
  WriteUninstaller "uninstall.exe"
SectionEnd

;second install option - adds the shortcuts to the start menu. optional.
  Section "Start Menu Shortcuts"
    CreateDirectory "$SMPROGRAMS\Privateer1.1"
    CreateShortCut "$SMPROGRAMS\Privateer1.1\Privateer.lnk" "$INSTDIR\bin\vegastrike.exe" "" "$INSTDIR\bin\vegastrike.exe" 0
    CreateShortCut "$SMPROGRAMS\Privateer1.1\Manual.lnk" "$INSTDIR\Manual.pdf" "" "$INSTDIR\Manual.pdf" 0
    CreateShortCut "$SMPROGRAMS\Privateer1.1\Setup Privateer.lnk" "$INSTDIR\bin\setup.exe" "" "$INSTDIR\bin\setup.exe" 0
    CreateShortCut "$SMPROGRAMS\Privateer1.1\Screenshots.lnk" "explorer.exe" "$INSTDIR\.privateer100\textures\"
    CreateShortCut "$SMPROGRAMS\Privateer1.1\Uninstall Privateer.lnk" "$INSTDIR\uninstall.exe" "" "$INSTDIR\uninstall.exe" 0
  SectionEnd

;uninstaller stuff
UninstallText "This will delete all files in the following directory, aside from files that existed before installing, files you added manually, and your savegame/universe data directory, unlesss you choose to remove it.  Remaining files must be removed manually.  Hit the uninstall button to continue."

!define unicon "C:\i\privateer\priv\uninstall.ico"	
!ifdef unicon
UninstallIcon "${unicon}"
!endif

Section "un.Uninstall Data Files"
  SectionIn RO
  DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\VegaStrike-Privateer"
  DeleteRegKey HKLM "SOFTWARE\VegaStrike\priv"
  Delete "$SMPROGRAMS\Privateer1.1\*.*"
  RMDir /r "$SMPROGRAMS\Privateer1.1\"
; remove vegastrike start menu dir as well if privateer was the only subdir (ie no VS versions installed)
;  RMDir "$SMPROGRAMS\Vega Strike\"
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
  Delete "$INSTDIR\factions.xml"
  Delete "$INSTDIR\master_part_list.csv"
  Delete "$INSTDIR\Manual.pdf"
  Delete "$INSTDIR\setup.config"
  Delete "$INSTDIR\ToDo.txt"
  Delete "$INSTDIR\vegastrike.config"
  Delete "$INSTDIR\vegastrike.config.temp"
  Delete "$INSTDIR\version.txt"
  Delete "$INSTDIR\weapon_list.xml"
  Delete "$INSTDIR\priv.nsi"
  Delete "$INSTDIR\priv2.nsi"
  Delete "$INSTDIR\m3uloki_add.sh"
  Delete "$INSTDIR\m3uloki_remove.sh"
  Delete "$INSTDIR\m3uloki_icon4.ico"
  Delete "$INSTDIR\fixmusic.sh"
  Delete "$INSTDIR\credits.txt"
  Delete "$INSTDIR\makeloki.sh"
  Delete "$INSTDIR\no.bmp"
  Delete "$INSTDIR\yes.bmp"
  Delete "$INSTDIR\play_vs"
  Delete "$INSTDIR\resources.rc"
  Delete "$INSTDIR\setup.base.xml"
  Delete "$INSTDIR\setup.music.xml"
  Delete "$INSTDIR\uninstall.ico"
  Delete "$INSTDIR\vega.ico"
  Delete "$INSTDIR\vegastrike.sh"
  Delete "$INSTDIR\vegastrike.xpm"
  Delete "$INSTDIR\vsinstall.sh"
  Delete "$INSTDIR\vslogo.xpm"
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
Function .onInstSuccess
  Call GetWindowsVersion
  Pop $R0
  StrCmp $R0 '98' lbl_copy
  StrCmp $R0 '95' lbl_copy
  StrCmp $R0 'ME' lbl_copy lbl_avoid_copy
lbl_copy:
  Rename /REBOOTOK $INSTDIR\bin\SDL.dll $INSTDIR\bin\SDL2k.dll
  Rename /REBOOTOK $INSTDIR\bin\SDL98.dll $INSTDIR\bin\SDL.dll
lbl_avoid_copy:
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