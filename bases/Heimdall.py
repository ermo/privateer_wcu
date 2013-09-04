import Base
import dynamic_mission
import VS
import pleasure_land

time_of_day=''
bar=-1
weap=-1
room0=-1
plist=VS.musicAddList('agricultural.m3u')
VS.musicPlayList(plist)
dynamic_mission.CreateMissions()

room = Base.Room ('Landing_Pad')
room0 = room
Base.Texture (room0, 'background', 'bases/refinery/Edinburgh_LandingBay'+time_of_day+'.spr', 0, 0)
Base.Texture (room0, 'str', 'bases/refinery/Edinburgh_LandingBay_lst'+time_of_day+'.spr', 0.29375, 0.0625)
Base.Texture (room0, 'lit', 'bases/refinery/lit'+time_of_day+'.spr', -0.18866, 0.39393)
Base.Ship (room, 'my_ship', (0.046875,-0.203333,3), (0, 0.93, -0.34), (-1, 0, 0))
Base.LaunchPython (room0, 'my_launch_id', 'bases/launch_music.py', -0.33, -0.573333, 0.8475, 0.6, 'Launch')

room = Base.Room ('Main Deck')
room1 = room

Base.Texture (room, 'background', 'bases/Heimdall/Concourse'+time_of_day+'.spr', 0, 0)
Base.Texture (room, 'str', 'bases/refinery/Anapolis_Concourse_str'+time_of_day+'.spr', 0.6, 0.6875)
Base.Texture (room, 'sh0', 'bases/refinery/Anapolis_Concourse_sh0'+time_of_day+'.spr', 0.6, 0.6582)
Base.Texture (room, 'sh1', 'bases/refinery/Anapolis_Concourse_sh1'+time_of_day+'.spr', 0.6, 0.58)
Base.Texture (room, 'wk0', 'bases/agricultural/Helen_Concourse_wk0'+time_of_day+'.spr', 0.6875, -0.8828)
Base.Texture (room, 'wk1', 'bases/agricultural/Helen_Concourse_wk1'+time_of_day+'.spr', -0.43125, -0.8828)
Base.Texture (room, 'wk2', 'bases/agricultural/Helen_Concourse_wk2'+time_of_day+'.spr', 0.275, -0.423828125)

import commodity_lib
room2 = commodity_lib.MakeCommodity(room1,time_of_day);
Base.Link (room0, 'my_link_id', 0.6025, -0.463333, 0.29, 0.633333, 'Main Deck', room1)

import bar_lib
bar = bar_lib.MakeBar (room1,time_of_day, 'refinery', "bases/bar/Helen_Bar", True, True, 'refinery', False, [("rf0",-.230376,-.1934),("rf1",-.084875,-.0097),("rf3",-.8548125,-.0388),("rf2",-.55775,-.2037)])
Base.Link (room1, 'bar', -0.5975, -0.133333, 0.17, 0.25, 'Bold_Mens_Pub', bar)

import merchant_guild
merchant = merchant_guild.MakeMerchantGuild (room1,time_of_day)
Base.Link (room1, 'merchant', 0.03, 0.0933333, 0.22, 0.176667, "Merchant's Guild", merchant)

import mercenary_guild
merchant = mercenary_guild.MakeMercenaryGuild (room1,time_of_day)
Base.Link (room1, 'mercenary', 0.77, 0.0233333, 0.22, 0.226667, "Mercenary's Guild", merchant)

import weapons_lib
weap = weapons_lib.MakeWeapon (room1,time_of_day)
Base.Link (room1, 'weapon_room', -0.5725, -0.583333, 0.315, 0.386667, 'Ship_Dealer/Upgrades', weap)

import milgui_lib
room = milgui_lib.MakeMilitia(room1, time_of_day='')
room3=room

Base.Link (room1, 'my_link_id', 0.035, -0.346667, 0.2825, 0.27, 'Landing_Pad', room0)

Base.Link (room1, 'my_link_id', 0.6275, -0.37, 0.3425, 0.17, 'Commodity_Exchange', room2)

Base.Link (room1, 'my_room_id', -0.85, -0.9, 0.15, 0.25, 'Militia_Guild_Office', room3)

Base.Comp (room1, 'my_comp_id', 0.3725, -0.843333, 0.2825, 0.423333, 'Mission_Computer', 'Missions News Info ')

