import Base
import dynamic_mission
import VS
import quest

time_of_day=''
bar=-1
weap=-1
room0=-1
plist=VS.musicAddList('church_of_man.m3u')
VS.musicPlayList(plist)
room = Base.Room ('Airlock Tunnel')
room0 = room
Base.Texture (room, 'background', 'bases/generic/airlock.spr', 0, 0)
Base.LaunchPython (room0, 'launch','bases/launch_music.py', -0.453125, -0.291667, 0.767578, 0.770833, 'Access_Denied')
Base.LaunchPython (room0, 'launch','bases/launch_music.py', -0.841797, -0.859375, 1.5625, 0.565104, 'Undock')
Base.Ship (room0, 'ship', (0,-.6,4),(0,.93,-.34) ,(-1,0,0))
import campaign_lib
cnodelist=campaign_lib.getActiveCampaignNodes(room0)
