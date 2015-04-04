from XGUIDebug import *
import Base
import Director
import GUI
import ShowProgress
import VS
import debug
import methodtype
import mission_lib
import os
import universe

pirate_bases = {
    'Gemini/Capella': 'Drake',
    'Gemini/KM-252': 'Smallville',
    'Gemini/Pentonville': 'Oakham',
    'Gemini/Sherwood': "Tuck's",
    'Gemini/Telar': 'Megiddo',
}

quadrants = {
    "Gemini/17-ar": 'Fariss',
    "Gemini/Capella": 'Fariss',
    "Gemini/Castor": 'Fariss',
    "Gemini/Crab-12": 'Fariss',
    "Gemini/Death": 'Fariss',
    "Gemini/Delta_Prime": 'Fariss',
    "Gemini/Eden": 'Fariss',
    "Gemini/Famine": 'Fariss',
    "Gemini/J900": 'Fariss',
    "Gemini/KM-252": 'Fariss',
    "Gemini/New_Caledonia": 'Fariss',
    "Gemini/Nexus": 'Fariss',
    "Gemini/Palan": 'Fariss',
    "Gemini/Pestilence": 'Fariss',
    "Gemini/Regallis": 'Fariss',
    "Gemini/Rygannon": 'Fariss',
    "Gemini/Sherwood": 'Fariss',
    "Gemini/Telar": 'Fariss',
    "Gemini/Valhalla": 'Fariss',
    "Gemini/War": 'Fariss',
    "Gemini/Xyanti": 'Fariss',
    "Gemini/Blockade_Point_Alpha": 'Clarke',
    "Gemini/Blockade_Point_Charlie": 'Clarke',
    "Gemini/Blockade_Point_Tango": 'Clarke',
    "Gemini/CMF-A": 'Clarke',
    "Gemini/Hyades": 'Clarke',
    "Gemini/Lisacc": 'Clarke',
    "Gemini/Mah_Rahn": 'Clarke',
    "Gemini/Midgard": 'Clarke',
    "Gemini/Nitir": 'Clarke',
    "Gemini/Perry": 'Clarke',
    "Gemini/Ragnarok": 'Clarke',
    "Gemini/Rikel": 'Clarke',
    "Gemini/Sumn_Kpta": 'Clarke',
    "Gemini/Surtur": 'Clarke',
    "Gemini/Tingerhoff": 'Clarke',
    "Gemini/Tr_Pakh": 'Clarke',
    "Gemini/41-gs": 'Potter',
    "Gemini/44-p-im": 'Potter',
    "Gemini/Aldebran": 'Potter',
    "Gemini/Auriga": 'Potter',
    "Gemini/DN-N1912": 'Potter',
    "Gemini/Hinds_Variable_N": 'Potter',
    "Gemini/Manchester": 'Potter',
    "Gemini/Metsor": 'Potter',
    "Gemini/ND-57": 'Potter',
    "Gemini/New_Constantinople": 'Potter',
    "Gemini/New_Detroit": 'Potter',
    "Gemini/Newcastle": 'Potter',
    "Gemini/Oxford": 'Potter',
    "Gemini/Raxis": 'Potter',
    "Gemini/Saxtogue": 'Potter',
    "Gemini/Shangri_La": 'Potter',
    "Gemini/XXN-1927": 'Potter',
    "Gemini/119ce": 'Humboldt',
    "Gemini/CM-N1054": 'Humboldt',
    "Gemini/Freyja": 'Humboldt',
    "Gemini/Junction": 'Humboldt',
    "Gemini/Padre": 'Humboldt',
    "Gemini/Penders_Star": 'Humboldt',
    "Gemini/Pentonville": 'Humboldt',
    "Gemini/Pollux": 'Humboldt',
    "Gemini/Prasepe": 'Humboldt',
    "Gemini/Pyrenees": 'Humboldt',
    "Gemini/Troy": 'Humboldt',
    "Gemini/Varnus": 'Humboldt',
}

savefilters = set(["test2_main_menu","New_Game"])

class NewSaveGame: pass

def savelist():
    global savefilters
    from os import listdir
    return [ GUI.GUISimpleListPicker.listitem(path,path)
        for path in listdir(VS.getSaveDir())
        if path[:1] != '.' and path not in savefilters ]

def makeNewSaveName():
    saves = [ i.data for i in savelist() ]
    prefix = "%s_%s_%s_" % (get_system_text()[2] , get_base_text()[1][0] , get_ship_text())
    i = 1
    while ("%s_%02d" % (prefix,i)) in saves:
        i += 1
    return "%s_%02d" % (prefix,i)

def MakePersonalComputer(room_landing_pad, room_concourse, make_links=1, enable_missions=1, enable_finances=1, enable_manifest=1, enable_load=1, enable_save=1, return_room_map=0):

    # create the screen
    room_id = Base.Room ('XXXQuine_4025')

    # create an object to keep the state
    comp = QuineComputer(room_id, room_concourse, enable_missions, enable_finances, enable_manifest, enable_load, enable_save)

    # link this screen with the landing pad and the concourse
    # this will be replaced with a keybinding, eventually
    if make_links:
        Base.Link (room_concourse,   'quine_pc', -1, 0.75, 0.25, 0.25, 'Quine_4025', room_id)
        Base.Link (room_landing_pad, 'quine_pc', -1, 0.75, 0.25, 0.25, 'Quine_4025', room_id)

    if return_room_map:
        # They want a room map, pointing to each section separately (right now... only root,
        # but eventually, something else...) and the computer object, so you can do stuff
        room = GUI.GUIRootSingleton.getRoomById(room_id)
        return { 'root':room, 'load':room, 'save':room, 'computer':comp }
    else:
        return room_id

def change_text_click(self,params):
    GUI.GUIButton.onClick(self,params)
    self.room.owner.change_text(self.index)

def scroll_click(self,params):
    GUI.GUIButton.onClick(self,params)
    self.room.owner.scroll(self.index[4:])

class QuineComputer:
    def __init__(self, room_start, room_exit_to, enable_missions, enable_finances, enable_manifest, enable_load, enable_save):
        # Quine computer is made up of several "rooms" aka screens
        # the room_start show the user's location
        # this is made a lot more complex because of the need to update the cargo manifest
        guiroom = GUI.GUIRoom(room_start)
        self.guiroom = guiroom

        # when a button is clicked, this will allow us to get the QuineComputer instance from the x_click functions
        guiroom.owner = self

        # add background sprite; no need to keep a variable around for this, as it doesn't change
        GUI.GUIStaticImage(guiroom, 'background', ( 'interfaces/quine/main.spr' , GUI.GUIRect(0, 0, 1, 1, "normalized") )).draw()

        # add buttons
        self.buttons = {}
        self.mode = ''
        self.saveGameNameEntryBox = None

        if enable_finances:
            hot_loc = GUI.GUIRect(547, 279, 105, 60, "pixel", (800,600))
            spr_loc = hot_loc
            spr = ("interfaces/quine/fin_pressed.spr",spr_loc)
            spr_disabled = ("interfaces/quine/fin_disabled.spr",spr_loc)
            sprites = { 'enabled':None, 'disabled':spr_disabled, 'down':spr }
            self.add_button( GUI.GUIButton(guiroom,'XXXFinances','btn_finances', sprites, hot_loc), change_text_click )
        if enable_manifest:
            hot_loc = GUI.GUIRect(646, 279, 96, 64, "pixel", (800,600))
            spr_loc = hot_loc
            spr = ("interfaces/quine/man_pressed.spr",spr_loc)
            spr_disabled = ("interfaces/quine/man_disabled.spr",spr_loc)
            sprites = { 'enabled':None, 'disabled':spr_disabled, 'down':spr }
            self.add_button( GUI.GUIButton(guiroom,'XXXManifest','btn_manifest', sprites, hot_loc), change_text_click )
        if enable_load:
            hot_loc = GUI.GUIRect(635, 166, 97, 55, "pixel", (800,600))
            spr_loc = hot_loc
            spr = ("interfaces/quine/load_pressed.spr",spr_loc)
            spr_disabled = ("interfaces/quine/load_disabled.spr",spr_loc)
            sprites = { 'enabled':None, 'disabled':spr_disabled, 'down':spr }
            self.add_button( GUI.GUIButton(guiroom,'XXXLoad'    ,'btn_load'    , sprites, hot_loc), change_text_click )
        if enable_save:
            hot_loc = GUI.GUIRect(541, 166, 97, 55, "pixel", (800,600))
            spr_loc = hot_loc
            spr = ("interfaces/quine/save_pressed.spr",spr_loc)
            spr_disabled = ("interfaces/quine/save_disabled.spr",spr_loc)
            sprites = { 'enabled':None, 'disabled':spr_disabled, 'down':spr }
            self.add_button( GUI.GUIButton(guiroom,'XXXSave'    ,'btn_save'    , sprites, hot_loc), change_text_click )
        if enable_missions:
            hot_loc = GUI.GUIRect(543, 220, 100, 60,"pixel", (800,600))
            spr_loc = hot_loc
            spr = ("interfaces/quine/missions_pressed.spr",spr_loc)
            spr_disabled = ("interfaces/quine/missions_disabled.spr",spr_loc)
            sprites = { 'enabled':None, 'disabled':spr_disabled, 'down':spr }
            self.add_button( GUI.GUIButton(guiroom,'XXXMissions','btn_missions', sprites, hot_loc), change_text_click )

        if enable_load or enable_save:
            hot_loc = [ GUI.GUIRect(631, 346, 51, 69, "pixel", (800,600)), #up-arrow
                        GUI.GUIRect(629, 410, 55, 69, "pixel", (800,600)), #down-
                        GUI.GUIRect(560, 383, 72, 57, "pixel", (800,600)), #left-
                        GUI.GUIRect(684, 383, 72, 57, "pixel", (800,600)) ] #right-
            spr_loc = hot_loc
            spr = [ ("interfaces/quine/up_pressed.spr"   ,spr_loc[0]),
                    ("interfaces/quine/down_pressed.spr" ,spr_loc[1]),
                    ("interfaces/quine/left_pressed.spr" ,spr_loc[2]),
                    ("interfaces/quine/right_pressed.spr",spr_loc[3])
                  ]
            spr_disabled = [ ("interfaces/quine/up_disabled.spr"   ,spr_loc[0]),
                             ("interfaces/quine/down_disabled.spr" ,spr_loc[1]),
                             ("interfaces/quine/left_disabled.spr" ,spr_loc[2]),
                             ("interfaces/quine/right_disabled.spr",spr_loc[3])
                           ]
            sprites = [ { 'enabled':None, 'disabled':spr_disabled[0], 'down':spr[0] },
                        { 'enabled':None, 'disabled':spr_disabled[1], 'down':spr[1] },
                        { 'enabled':None, 'disabled':spr_disabled[2], 'down':spr[2] },
                        { 'enabled':None, 'disabled':spr_disabled[3], 'down':spr[3] }
                      ]
            self.add_button( GUI.GUIButton(guiroom,'XXXUp'   ,'btn_up'   , sprites[0], hot_loc[0]), scroll_click )
            self.add_button( GUI.GUIButton(guiroom,'XXXDown' ,'btn_down' , sprites[1], hot_loc[1]), scroll_click )
            self.add_button( GUI.GUIButton(guiroom,'XXXLeft' ,'btn_left' , sprites[2], hot_loc[2]), scroll_click )
            self.add_button( GUI.GUIButton(guiroom,'XXXRight','btn_right', sprites[3], hot_loc[3]), scroll_click )

        current_base = universe.getDockedBase()
        player = VS.getPlayer()

        # this doesn't change while docked, so only call it once
        self.str_start = get_location_text(current_base)

        screen_loc = GUI.GUIRect(80,90,350,380,"pixel",(800,600))
        screen_color = GUI.GUIColor(20/255.0, 22/255.0 ,10/255.0)
        self.screen_color = screen_color;
        self.screen_loc = screen_loc;

        # first I tried rgb(56 60 24) and rgb(40 44 20); both were too light
        screen_bgcolor = GUI.GUIColor.clear()
        screen_bgcolor_nc = GUI.GUIColor(0.44,0.47,0.17)
        self.screen_bgcolor = screen_bgcolor;

        # text screen
        self.txt_screen = GUI.GUIStaticText(guiroom, 'txt_screen', self.str_start, screen_loc,
            color=screen_color,
            bgcolor=screen_bgcolor)
        self.txt_screen.hide()

        # picker screen
        self.picker_screen = GUI.GUISimpleListPicker(guiroom,'XXXSelect item','picker_screen', screen_loc,
            textcolor    =screen_color     , textbgcolor    =screen_bgcolor,
            selectedcolor=screen_bgcolor_nc, selectedbgcolor=screen_color   )
        self.picker_screen.hide()

        #
        # much of this is temporary, until something better can be worked out:
        #

        # Save/Load screen
        #if enable_save:
        #   x, y, w, h = GUI.GUIRect(217, 56, 40, 18).getHotRect()
        #   Base.Comp (room_start, 'save_comp', x, y, w, h, 'XXXSave/Load/Quit', 'LoadSave')
        #if enable_load:
        #   x, y, w, h = GUI.GUIRect(257, 56, 39, 18).getHotRect()
        #   Base.Comp (room_start, 'load_comp', x, y, w, h, 'XXXSave/Load/Quit', 'LoadSave')

        # Missions
        #if enable_missions:
        #   x, y, w, h = GUI.GUIRect(217, 75, 79, 18).getHotRect()
        #   Base.Comp (room_start, 'missions', x, y, w, h, 'XXXMissions', 'Missions Info Cargo ')

        # Finances
        #if enable_finances:
        #   x, y, w, h = GUI.GUIRect(219, 94, 40, 18).getHotRect()
        #   Base.Comp (room_start, 'missions', x, y, w, h, 'Finances', 'Info ')

        # Manifest
        #if enable_manifest:
        #   x, y, w, h = GUI.GUIRect(260, 94, 40, 18).getHotRect()
        #   Base.Comp (room_start, 'missions', x, y, w, h, 'Manifest', 'Cargo ')

        # Exit button, returns us to concourse
        self.room_id = room_start
        self.exit_room_id = room_exit_to
        self.setExitLinkState(True)

    def setExitLinkState(self,state):
        '''this is here to enable modal behaviour, i.e. hinder exit out of a dialog'''
        if state:
            rect = GUI.GUIRect(224, 167, 35, 14)
            x, y, w, h = rect.getHotRect()
            #       Base.Link (room_start, 'exit', x, y, w, h, 'Exit', room_exit_to)
            Base.LinkPython (self.room_id, 'exit',
                     "#\nimport GUI\nGUI.GUIRootSingleton.getRoomById(%s).owner.reset()\n"
                     % (self.guiroom.getIndex()), x, y, w, h, 'XXXExit', self.exit_room_id)
        else:
            Base.EraseLink (self.room_id, 'exit')


    def reset(self):
        trace(TRACE_DEBUG,"::: QuineComputer.reset()")
        if self.saveGameNameEntryBox is not None:
            self.saveGameNameEntryBox.hide()
            self.saveGameNameEntryBox.focus(False)
            self.saveGameNameEntryBox = None
            for id in list(self.buttons.keys()):
                button = self.buttons[id]
                button.enable()
                button.redraw()
        self.txt_screen.setText( self.str_start )

    def change_text(self, button_index):
        text_screens = {
            'btn_finances' : lambda:get_relations_text(VS.getPlayer()),
            'btn_manifest' : lambda:get_manifest_text(VS.getPlayer()),
            'btn_missions' : lambda:get_missions_text()
            }
        if button_index in text_screens:
            self.txt_screen.setText( text_screens[button_index]() )
            self.txt_screen.show()
            self.picker_screen.hide()
        elif button_index == "btn_load":
            if self.mode != button_index:
                self.picker_screen.items = savelist()
                self.picker_screen.show()
                self.txt_screen.hide()
            elif self.picker_screen.selection is not None:
                ShowProgress.activateProgressScreen('loading',3)
                VS.loadGame(self.picker_screen.items[self.picker_screen.selection].data)
        elif button_index == "btn_save":
            if self.mode != button_index:
                self.picker_screen.items = [
                    GUI.GUISimpleListPicker.listitem("New Game",NewSaveGame)
                    ]+savelist()
                self.picker_screen.show()
                self.txt_screen.hide()
            elif self.picker_screen.visible and self.picker_screen.items[self.picker_screen.selection].data is not NewSaveGame:
                self.picker_screen.hide()
                self.txt_screen.setText(
                    "\n"*7+
                    "Are you sure you want to overwrite the savegame?\n(%s)"%
                        self.picker_screen.items[self.picker_screen.selection]
                    +"\n"*3
                    +"Press SAVE again to do it." )
                self.txt_screen.show()
            elif self.picker_screen.selection is not None:
                savename = ''
                if self.picker_screen.items[self.picker_screen.selection].data is NewSaveGame:
                    savename = makeNewSaveName()
                    self.oldSaveName = None
                else:
                    savename = self.picker_screen.items[self.picker_screen.selection].data
                    self.oldSaveName = savename

                #enter a modal line editor
                boxloc = GUI.GUIRect(120,130,200,20,"pixel",(800,600))
                self.saveGameNameEntryBox = GUI.GUILineEdit(self.saveNameEntryEntered,
                                        self.guiroom,"box_save",
                                        savename, boxloc,
                                        self.screen_color,
                                        bgcolor=self.screen_bgcolor)
                for id in list(self.buttons.keys()):
                    button = self.buttons[id]
                    button.disable()
                    button.redraw()
                self.saveGameNameEntryBox.focus(True)
#               self.setExitLinkState(False)
                self.txt_screen.setText( 'Save Game:' )
                self.txt_screen.show()
                self.saveGameNameEntryBox.show()
                self.picker_screen.hide()
                self.lastEnteredSavegameName = None
                self.guiroom.redraw()

        else:
            self.picker_screen.hide()
            self.txt_screen.hide()
        self.mode = button_index

    #line editor callback
    def saveNameEntryEntered(self,textbox):
        # this is a bit awkward, mostly since we have to emulate modal behaviour through state machines...
        if textbox.getText() is not '' and textbox.canceled is False:
            savename = textbox.getText()
            if savename in savelist() and savename is not self.oldSaveName:
                if savename is not self.lastEnteredSavegameName:
                    self.txt_screen.setText( 'warning: overwriting another game with the same name\n' +
                          'press Enter again to really do it')
                    return
                else:
                    self.lastEnteredSavegameName = savename
            VS.saveGame(savename)
            if self.oldSaveName is not None and savename is not self.oldSaveName:
                try:
                    os.remove(VS.getSaveDir() + os.sep + self.oldSaveName)
                except:
                    trace(TRACE_DEBUG,"could not remove old savegame at "
                          + VS.getSaveDir() + os.sep + self.oldSaveName)
            self.picker_screen.items = [
                GUI.GUISimpleListPicker.listitem("New Game",NewSaveGame)
                ]+savelist()
        self.txt_screen.hide()
        textbox.hide()
        textbox.focus(False)
        for id in list(self.buttons.keys()):
            button = self.buttons[id]
            button.enable()
            button.redraw()
        self.saveGameNameEntryBox = None
        self.picker_screen.show()
#       self.setExitLinkState(True)
        self.guiroom.redraw()

    def scroll(self,direction):
        list_screens = set(['btn_load','btn_save'])
        if self.mode in list_screens:
            if direction == 'up':
                self.picker_screen.pageMove(-1)
            elif direction == 'down':
                self.picker_screen.pageMove(1)
            elif direction == 'left':
                self.picker_screen.viewMove(-1)
            elif direction == 'right':
                self.picker_screen.viewMove(1)

    def add_button(self, guibutton, onclick_handler):
        # add the button to the "buttons" dictionary, draw it, and add onclick handler
        self.buttons[guibutton.index] = guibutton
        guibutton.draw()
        guibutton.onClick = methodtype.methodtype(onclick_handler, guibutton, type(guibutton))

    def setMode(self,mode):
        aliases = dict(load='btn_load',save='btn_save')
        mode = aliases.get(mode,mode)
        if self.mode != mode:
            self.change_text(mode)
        self.guiroom.redrawIfNeeded()

def get_system_text(str_system_file=None, current_base=None):
    if str_system_file is None:
        if current_base is None:
            current_base = universe.getDockedBase()
        # get sector, quadrant, system, and base name
        str_system_file = current_base.getUnitSystemFile()

    n = str_system_file.find('/')
    if (n >= 0):
        str_sector   = str_system_file[:n]
        str_system   = str_system_file[n+1:]
    else:
        str_sector   = 'Unknown'
        str_system   = 'Unknown'

    try:
        str_quadrant = quadrants[str_system_file]
    except KeyError:
        str_quadrant = 'Unknown'

    return (str_quadrant,str_sector,str_system)

def get_base_text(current_base = None, str_system_file = None):
    if current_base is None:
        current_base = universe.getDockedBase()
    if not current_base:
        return ((0,"neutral"),("Unknown","Main Menu"))
    if str_system_file is None:
        # get sector, quadrant, system, and base name
        str_system_file = current_base.getUnitSystemFile()

    # get faction
    int_faction = current_base.getFactionIndex()
    str_faction = current_base.getFactionName()

    # bases and planets aren't consistent in their usage of Name and Fullname values
    if current_base.isPlanet():
        str_base = current_base.getName()
        str_base_type = current_base.getFullname() + " planet"
    else:
        str_base = current_base.getFullname()
        str_base_type = current_base.getName()
        if str_base == '':
            str_base = 'Unknown'
            if str_faction == "pirates":
                try:
                    str_base = pirate_bases[str_system_file]
                except KeyError:
                    str_base = 'Unknown'

    # adjust the base type for certain planets
    if str_base_type == 'new_constantinople':
        str_base_type = "government base"
    elif str_base_type == 'perry':
        str_base_type = "military base"
    elif str_base_type == 'church_of_man planet':
        str_base_type = "agricultural planet"

    return ((int_faction,str_faction),(str_base,str_base_type))

def get_ship_text(unit = None):
    if unit is None:
        player = VS.getPlayer()

    name = player.getName()
    if name.index('.') is None:
        return name.capitalize()
    else:
        return name[:name.index('.')].capitalize()

def get_missions_text():
    missionlist = mission_lib.GetMissionList()

    parth = lambda s:(s and "("+s+")") or s

    full_layout = "\n\nMissions:\n\n%(ENTRIES)s\n\nTotal active missions: %(NUM_MISSIONS)s\n";
    entry_process = lambda e: {
        'MISSION_TYPE'      :e.get('MISSION_TYPE','MISSION').replace('_',' ').capitalize(),
        'SHORT_DESCRIPTION' :e.get('MISSION_SHORTDESC','').split('/',1)[-1],
        'GUILD_NAME'        :parth(e.get('GUILD_NAME',e.get('MISSION_NAME','').split('/',1)[0]).replace('_',' ').title()) }
    entry_layout = "%(MISSION_TYPE)s %(GUILD_NAME)s:\n%(SHORT_DESCRIPTION)s\n\n"

    return full_layout % {
        'NUM_MISSIONS':len(missionlist),
        'ENTRIES':''.join( entry_layout % entry_process(entry) for entry in missionlist ) }

#
#   helper functions
#
def get_location_text(current_base):

    str_quadrant, str_sector, str_system = get_system_text(current_base=current_base)
    (int_faction,str_faction),(str_base,str_base_type) = get_base_text(current_base)

    str_location = """
Location:
   %s
   %s
   %s

System:
   %s

Quadrant:
   %s
   %s Sector


Ready!
""" %(str_base, str_base_type.capitalize(), str_faction, str_system, str_quadrant, str_sector)

    return str_location

def get_manifest_text(player):
    cargo_dict = {}

    # get the hold volume
    int_hold_volume = int( VS.LookupUnitStat( player.getName(), player.getFactionName(), "Hold_Volume" ) )
    if (player.hasCargo("add_cargo_volume")):
        # capacity increases by 50% if they have the cargo expansion
        int_hold_volume = int( int_hold_volume * 1.5 )

    int_total_quantity = 0
    for i in range(player.numCargo()):
        cargo = player.GetCargoIndex(i)

        name     = cargo.GetContent()
        category = cargo.GetCategory()
        quantity = cargo.GetQuantity()

        if name == '': continue
        if category[:8] == 'upgrades': continue
        if category[:9] == 'starships': continue

        if (quantity > 0):
            cargo_dict[name] = quantity
            int_total_quantity += quantity

    int_space_left = int_hold_volume - int_total_quantity
    keys = list(cargo_dict.keys())
    if len(keys) > 0:
        str_manifest = "Space left: %s\n\n" %(int_space_left)
        keys.sort()
        for i in keys:
            count = cargo_dict[i]
            # try to pad the columns so they line up
            str_pad = "   "
            int_pad_len = len(str_pad) - len(str(count))
            if int_pad_len < 1:
                str_pad = ""
            else:
                str_pad = str_pad[:int_pad_len]
            str_manifest += "%s%s  %s\n" %(str_pad, count, i)
    else:
        str_manifest = "Space left: %s\nNo cargo loaded.\n" %(int_space_left)

    return str_manifest


def get_relations_text(player):
    str_relations = "Cash:  %s\n\nKill breakdown:\n" %( int(player.getCredits()) )

    # length of faction_kills = VS.GetNumFactions() + 1
    # could the last entry be the total?  or maybe the number of times the user has died?
    faction_kills = [];
    for i in range(Director.getSaveDataLength( VS.getCurrentPlayer(), 'kills' )):
        faction_kills.append( Director.getSaveData( VS.getCurrentPlayer(), 'kills', i ) )

    displayed_factions = ['confed', 'kilrathi', 'merchant', 'retro', 'pirates', 'hunter', 'militia']

    for i in range(VS.GetNumFactions()):
        # VS.GetFactionIndex(s) expects a string
        # VS.GetFactionIndex(s) expects a name
        faction = VS.GetFactionName(i)
        if faction in displayed_factions:
            # note: the following calls do not always return equal values:
            #   VS.GetRelation(a, b)
            #   VS.GetRelation(b, a)
            relation = int( VS.GetRelation(faction, player.getFactionName()) * 100 )
            if relation > 100:
                relation = 100
            elif relation < -100:
                relation = -100

            # not sure if the AI or Friend/Foe radar agree with these figures, but this ought to work, mostly
            if relation > 20:
                str_relation = "friendly"
            elif relation < -20:
                str_relation = "hostile"
            else:
                str_relation = "neutral"

            try:
                kills = int( faction_kills[i] )
            except:
                kills = 0

            # try to pad the columns
            # (this doesn't work perfectly, since we're using a variable-width font)
            str_pad = "    "
            int_pad_len = len(str_pad) - len(str(kills))
            if int_pad_len < 1:
                str_pad = ""
            else:
                str_pad = str_pad[:int_pad_len]

            # add current faction to the output string
            str_relations = str_relations + "%s%s  %s\t(%s: %s)\n" %(str_pad, kills, faction.capitalize(), str_relation, relation)

    return str_relations
