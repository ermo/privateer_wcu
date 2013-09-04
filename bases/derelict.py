import Base
import dynamic_mission
import VS
import quest

time_of_day=''
bar=-1
weap=-1
room0=-1
plist=VS.musicAddList('derelict.m3u')
VS.musicPlayList(plist)
dynamic_mission.CreateMissions()
room = Base.Room ('')
room0 = room
Base.Texture (room, 'background', 'bases/derelict/derelict'+time_of_day+'.spr', 0, 0)
Base.Ship (room, 'my_ship', (-0.525,-0.341667,6), (0, 1, 0), (0,-.2,-.93))
Base.Comp (room0, 'my_comp_id', -0.9725, -0.986667, 0.285, 0.553333, 'Save', 'Info ')

room = Base.Room ('')
room1 = room
Base.Texture (room, 'background', 'bases/derelict/derelictship_noweapon'+time_of_day+'.spr', 0, 0)
if not quest.checkSaveValue(VS.getCurrentPlayer(),'have_the_gun'):
    Base.Texture (room1, 'weapon', 'bases/derelict/derelictship_weapon'+time_of_day+'.spr', 0, 0)
    Base.Python (room1, 'weapon', -0.605, -0.78, 0.2975, 0.423333, 'Mount Weapon On Your Ship', '''#
import Base
import VS
plr=VS.getPlayer()
if plr:
    if not quest.checkSaveValue(VS.getCurrentPlayer(),'have_the_gun'):
        percentage = plr.upgrade('steltek_gun',0,0,True,True)
        if percentage != 1.0:
            quest.removeQuest(VS.getCurrentPlayer(),'have_the_gun',1)
            Base.EraseObj('''+str(room1)+''', 'weapon')
            Base.EraseLink('''+str(room1)+''', 'weapon')
        else:
            Base.Message("Can't install the weapon on this ship!")
    else:
        Base.EraseObj('''+str(room1)+''', 'weapon')
        Base.EraseLink('''+str(room1)+''', 'weapon')
''', False)

Base.Link (room0, 'my_link_id', -0.8225, -0.27, 0.225, 0.2, 'Inspect Alien Ship', room1)
Base.LaunchPython (room0, 'my_launch_id', 'bases/launch_music.py', -0.53, -0.423333, 0.35, 0.276667, 'Launch')
Base.Link (room1, 'my_link_id', -0.9725, -0.98, 1.945, 0.0766667, 'Return To Docking Bay', room0)
