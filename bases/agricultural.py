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

room0 = pleasure_land.MakePleasureAgriculturalLanding(time_of_day)

room = Base.Room ('Main Concourse')
room1 = room
Base.Texture (room, 'background', 'bases/agricultural/Helen_Concourse'+time_of_day+'.spr', 0, 0)
Base.Texture (room, 'wtr', 'bases/agricultural/Helen_Concourse_wtr'+time_of_day+'.spr', 0, 0.75)
Base.Texture (room, 'wk0', 'bases/agricultural/Helen_Concourse_wk0'+time_of_day+'.spr', 0.6875, -0.83)
Base.Texture (room, 'wk1', 'bases/agricultural/Helen_Concourse_wk1'+time_of_day+'.spr', -0.43125, -0.86)
Base.Texture (room, 'wk2', 'bases/agricultural/Helen_Concourse_wk2'+time_of_day+'.spr', 0.275, -0.37)
import commodity_lib
room2 = commodity_lib.MakeCommodity(room1,time_of_day);
Base.Link (room0, 'my_link_id', 0.6025, -0.463333, 0.29, 0.633333, 'Main Concourse', room1)
import bar_lib
bar = bar_lib.MakeBar (room1,time_of_day,'agricultural', "bases/bar/Helen_Bar", True, True, 'agricultural', False, [('ag0', -0.9, -0.123046875),('ag1', -0.58125, -0.15234375),('ag2', -0.11875, -0.103515625),('ag3', 0.41875, -0.03515625)])
#ar = bar_lib.MakeBar (room1,time_of_day,'agricultural', "bases/bar/Helen_Bar", True, True, 'agricultural', False, [('ag0', -0.873, -0.1455),('ag1', -0.5638125, -0.1746),('ag2', -0.1151875, -0.1261),('ag3', 0.4061875, -0.0582)])
Base.Link (room1, 'bar', -0.61, -0.113333, 0.2075, 0.25, 'Bar', bar)

import merchant_guild
if (merchant_guild.Can()):
    merchant = merchant_guild.MakeMerchantGuild (room1,time_of_day)
    Base.Link (room1, 'merchant', 0.03, 0.0933333, 0.22, 0.176667, "Merchant's Guild", merchant)
else:
    Base.Texture (room, 'nomerchant', 'bases/agricultural/nomerchant'+time_of_day+'.spr', 0.15, 0.1796875)

import mercenary_guild
if (mercenary_guild.Can()):
    merchant = mercenary_guild.MakeMercenaryGuild (room1,time_of_day)
    Base.Link (room1, 'mercenary', 0.77, 0.0233333, 0.22, 0.226667, "Mercenary's Guild", merchant)
else:
    Base.Texture (room, 'nomercenary', 'bases/agricultural/nomercenary'+time_of_day+'.spr', 0.8875, 0.130859375)

import weapons_lib
if (weapons_lib.CanRepair()):
    weap = weapons_lib.MakeWeapon (room1,time_of_day)
    Base.Link (room1, 'weapon_room', -0.5725, -0.583333, 0.315, 0.386667, 'Ship_Dealer/Upgrades', weap)
else:
    Base.Texture (room, 'noshipdealer', 'bases/agricultural/noshipdealer'+time_of_day+'.spr', -0.26875, -0.4453125)

Base.Link (room1, 'my_link_id', 0.035, -0.346667, 0.2825, 0.27, 'Landing_Pad', room0)
Base.Link (room1, 'my_link_id', 0.6275, -0.37, 0.3425, 0.17, 'Commodity_Exchange', room2)
Base.Comp (room1, 'my_comp_id', 0.3725, -0.843333, 0.2825, 0.423333, 'Mission_Computer', 'Missions News Info ')
