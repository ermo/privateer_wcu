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
room = Base.Room ('Kilrathi_Weapon_Dump')
room0 = room
Base.Texture (room, 'background', 'bases/generic/airlock_yes.spr', 0, 0)
Base.Comp (room0, 'Inventory', -0.453125, -0.291667, 0.767578, 0.770833, 'Inventory','Upgrade ShipDealer')
Base.LaunchPython (room0, 'launch','bases/launch_music.py', -0.841797, -0.859375, 1.5625, 0.565104, 'Launch Your Ship')
Base.Ship (room0, 'ship', (0,-.6,6),(0,.93,-.34) ,(-1,0,0))
import campaign_lib
cnodelist=campaign_lib.getActiveCampaignNodes(room0)
