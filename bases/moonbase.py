import Base
import dynamic_mission
import VS

time_of_day=''
bar=-1
weap=-1
room0=-1
plist=VS.musicAddList('mining_base_pirates.m3u')
VS.musicPlayList(plist)
dynamic_mission.CreateMissions()
room = Base.Room ('Landing_Bay')
room0 = room
Base.Texture (room, 'background', 'bases/mining_base/MiningBase_LandingPad'+time_of_day+'.spr', 0, 0)
Base.Ship (room, 'my_ship', (0.044375,-0.319167,3), (0, 0.995, -0.1), (-0.995, 0, 0.1))

room = Base.Room ('Moonbase_Concourse')
room1 = room
Base.Texture (room, 'background', 'bases/mining_base_pirates/PirateBase_Concourse'+time_of_day+'.spr', 0, 0)

Base.LaunchPython (room0, 'my_launch_id', 'bases/launch_music.py', -0.5075, -0.58, 0.8025, 0.76, 'Launch')
Base.Link (room0, 'my_link_id', 0.5875, -0.36, 0.2975, 0.573333, 'Moonbase_Concourse', room1)
import bar_lib
bar = bar_lib.MakeBar (room1,time_of_day,'pirates','bases/bar/MiningBase_Bar',True,True,'mining_base',False,[('mb1',-0.46875,-0.201272552)])
Base.Link (room1, 'bar', 0.2875, -0.29, 0.205, 0.22, 'Bar', bar)
import commodity_lib
commodity = commodity_lib.MakeCommodity (room1,time_of_day)
Base.Link (room1, 'commodity', 0.705, -0.62, 0.255, 0.423333, 'Storage', commodity)
Base.Comp (room1, 'my_comp_id', 0.485, -0.443333, 0.1475, 0.163333, 'Mission_Computer', 'Missions News ShipDealer Info ')
Base.Link (room1, 'my_link_id', -.5, 0.1, .3, 0.33, 'Landing_Bay', room0)
