import Base
import dynamic_mission
import VS

time_of_day=''
bar=-1
weap=-1
room0=-1
plist=VS.musicAddList('refinery.m3u')
VS.musicPlayList(plist)
dynamic_mission.CreateMissions()
room = Base.Room ('Landing_Pad')
room0 = room
Base.Texture (room, 'background', 'bases/refinery/Edinburgh_LandingBay'+time_of_day+'.spr', 0, 0)
Base.Texture (room, 'str', 'bases/refinery/Edinburgh_LandingBay_lst'+time_of_day+'.spr', 0.29375, 0.0625)
Base.Texture (room, 'lit', 'bases/refinery/lit'+time_of_day+'.spr', -0.18866, 0.39393)

Base.Ship (room, 'my_ship', (-0.05,-0.203333,3), (0, 0.93, -0.34), (-1, 0, 0))
room = Base.Room ('Concourse')
room1 = room
Base.Texture (room, 'background', 'bases/refinery/Anapolis_Concourse'+time_of_day+'.spr', 0, 0)
Base.Texture (room, 'str', 'bases/refinery/Anapolis_Concourse_str'+time_of_day+'.spr', 0.6, 0.6875)
Base.Texture (room, 'sh0', 'bases/refinery/Anapolis_Concourse_sh0'+time_of_day+'.spr', 0.6, 0.6582)
Base.Texture (room, 'sh1', 'bases/refinery/Anapolis_Concourse_sh1'+time_of_day+'.spr', 0.6, 0.58)
Base.Texture (room, 'wk0', 'bases/agricultural/Helen_Concourse_wk0'+time_of_day+'.spr', 0.6875, -0.83)
Base.Texture (room, 'wk1', 'bases/agricultural/Helen_Concourse_wk1'+time_of_day+'.spr', -0.43125, -0.86)
Base.Texture (room, 'wk2', 'bases/agricultural/Helen_Concourse_wk2'+time_of_day+'.spr', 0.275, -0.37)

Base.LaunchPython (room0, 'my_launch_id', 'bases/launch_music.py', -0.33, -0.573333, 0.8475, 0.6, 'Launch')
Base.Link (room0, 'my_link_id', 0.6225, -0.416667, 0.2425, 0.5, 'Concourse', room1)
import bar_lib
bar = bar_lib.MakeBar (room1,time_of_day, 'refinery', "bases/bar/Helen_Bar", True, True, 'refinery', False, [("rf0",-0.2375,-0.17127),("rf1",-0.0875,0.013671875),("rf3",-0.88125,-0.015625),("rf2",-.575,-0.18164)])
Base.Link (room1, 'bar', -0.5975, -0.133333, 0.17, 0.25, 'Bar', bar)

import merchant_guild
if (merchant_guild.Can()):
	merchant = merchant_guild.MakeMerchantGuild (room1,time_of_day)
	Base.Link (room1, 'merchant', 0.03, 0.0933333, 0.22, 0.176667, "Merchant's Guild", merchant)
else:
	Base.Texture (room, 'nomerchant', 'bases/agricultural/nomerchant'+time_of_day+'.spr', 0.15, 0.1796875)

import mercenary_guild
if (mercenary_guild.Can()):
	merchant = mercenary_guild.MakeMercenaryGuild (room1,time_of_day)
	Base.Link (room1, 'mercenary', 0.73, 0.0466667, 0.235, 0.14, 'Mercenary_Guild', merchant)
else:
	Base.Texture (room, 'nomercenary', 'bases/agricultural/nomercenary'+time_of_day+'.spr', 0.8875, 0.13086)

Base.Link (room1, 'my_link_id', 0.035, -0.34, 0.28, 0.266667, 'Landing_Pad', room0)

import weapons_lib
if (weapons_lib.CanRepair()):
	weap = weapons_lib.MakeWeapon (room1,time_of_day)
	Base.Link (room1, 'weapon_room', -0.545, -0.563333, 0.255, 0.36, 'Ship_Dealer/Upgrade', weap)
else:
	Base.Texture (room, 'noshipdealer', 'bases/agricultural/noshipdealer'+time_of_day+'.spr', -0.26875, -0.4453125)

import commodity_lib
commodity = commodity_lib.MakeCommodity (room1,time_of_day)
Base.Link (room1, 'commodity', 0.6475, -0.366667, 0.32, 0.156667, 'Commodity_Exchange', commodity)
Base.Comp (room1, 'my_comp_id', 0.4075, -0.85, 0.15, 0.276667, 'Mission_Computer', 'Missions News Info ')
