import Base
import VS
import GUI
import ShowProgress

import computer_lib
import dj_lib

# No good reason to disable it...
# dj_lib.disable()

def StartNewGame(self,params):
    ShowProgress.activateProgressScreen('loading',3)
    VS.loadGame(VS.getNewGameSaveName())

def QuitGame(self,params):
    Base.ExitGame()

# this uses the original coordinate system of Privateer
GUI.GUIInit(320,200)

time_of_day=''

# Base music
plist_menu=VS.musicAddList('maintitle.m3u')
plist_credits=VS.musicAddList('maincredits.m3u')

def enterMainMenu(self,params):
    global plist_menu
    VS.musicPlayList(plist_menu)

def enterCredits(self,params):
    global plist_credits
    VS.musicPlayList(plist_credits)

# Create menu room
room_menu = Base.Room ('XXXMain_Menu')
guiroom  = GUI.GUIRoom(room_menu)

# Create credits room
credits_guiroom = GUI.GUIRoom(Base.Room('XXXCredits'))
GUI.GUIStaticImage(credits_guiroom, 'background', ( 'interfaces/main_menu/credits.spr', GUI.GUIRect(0, 0, 1024, 768, "pixel", (1024,768)) ))

## Create NET room
#net_room = Base.Room ('XXX_Net')
#GUI.GUIStaticImage(net_room, 'background', ( 'interfaces/main_menu/net.spr', GUI.GUIRect(0, 0, 1024, 768, "pixel", (1024,768)) ))

# Button to go back to the main menu (from the credits)
sprite_loc = GUI.GUIRect(8,697,420,47,"pixel",(1024,768))
sprite = {
    '*':None,
    'down' : ( 'interfaces/main_menu/credits_resume_button_pressed.spr', sprite_loc ) }
GUI.GUIRoomButton (credits_guiroom, guiroom, 'XXXMain Menu','Main_Menu',sprite,sprite_loc,clickHandler=enterMainMenu)


# Create background
GUI.GUIStaticImage(guiroom, 'background', ( 'interfaces/main_menu/menu.spr', GUI.GUIRect(0, 0, 1024, 768, "pixel", (1024,768)) ))

# Create the Quine 4000 screens
rooms_quine = computer_lib.MakePersonalComputer(room_menu, room_menu,
    0, # do not make links
    1, 1, 1, # no missions, finances or manifest
    1, # do enable load
    1, # but disable save
    1) # and return room map, rather than only root room
rooms_quine['computer'].setMode('load')

# Load game 
sprite_loc = GUI.GUIRect(341,906,303,68,"pixel",(1280,1024))
sprite = {
    '*':None,
    'down' : ( 'interfaces/main_menu/load_button_pressed.spr', sprite_loc ) }
GUI.GUIRoomButton(guiroom, rooms_quine['load'], 'XXXLoad Game','Load_Game',sprite,sprite_loc)

# Net game 1
sprite_loc = GUI.GUIRect(643,906,301,68,"pixel",(1280,1024))
sprite = {
    '*':None,
    'down' : ( 'interfaces/main_menu/net_button_pressed.spr', sprite_loc ) }
#GUI.GUIRoomButton(guiroom, net_room, 'XXX_Net','Network_Game',sprite,sprite_loc)
#
## Net game 2
#sprite_loc = GUI.GUIRect(480,412,320,200,"pixel",(1280,1024))
GUI.GUICompButton(guiroom, 'Network', 'XXXNetwork Game','Network_Game',sprite,sprite_loc)

# Link 
sprite_loc = GUI.GUIRect(48,510,1,1,"pixel",(1280,1024))
sprite = {
    '*':None,
    'down' : ( 'interfaces/main_menu/credits_button_pressed.spr', sprite_loc ) }
GUI.GUIRoomButton(guiroom, credits_guiroom, 'XXXShow Credits','Show_Credits',sprite,sprite_loc,clickHandler=enterCredits)

# Link 
sprite_loc = GUI.GUIRect(48,440,1,1,"pixel",(1280,1024))
sprite = {
    '*':None,
    'down' : ( 'interfaces/main_menu/credits_button_pressed.spr', sprite_loc ) }
GUI.GUIRoomButton(guiroom, credits_guiroom, 'XXXShow Introduction','Show_Introduction',sprite,sprite_loc,clickHandler=enterCredits)

# New game
sprite_loc = GUI.GUIRect(30,906,312,68,"pixel",(1280,1024))
sprite = {
    '*':None,
    'down' : ( 'interfaces/main_menu/new_button_pressed.spr', sprite_loc ) }
btn = GUI.GUIButton(guiroom, 'XXXNew Game','New_Game',sprite,sprite_loc,'enabled',StartNewGame)

# Quit game
sprite_loc = GUI.GUIRect(943,906,307,68,"pixel",(1280,1024))
sprite = {
    '*':None,
    'down' : ( 'interfaces/main_menu/quit_button_pressed.spr', sprite_loc ) }
btn = GUI.GUIButton(guiroom, 'XXXQuit Game','Quit_Game',sprite,sprite_loc,'enabled',QuitGame)

# Draw everything
GUI.GUIRootSingleton.broadcastMessage('draw',None)

# Base music
VS.musicPlayList(plist_menu)

