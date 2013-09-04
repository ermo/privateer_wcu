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

room = Base.Room ('Speke Capital')
room1 = room
Base.Texture (room, 'background', 'bases/guildHQ/Helen_Concourse'+time_of_day+'.spr', 0, 0)
import commodity_lib
room2 = commodity_lib.MakeCommodity(room1,time_of_day);
Base.Link (room0, 'my_link_id', 0.6025, -0.463333, 0.29, 0.633333, 'Speke Capital', room1)
import bar_lib
bar = bar_lib.MakeBar (room1,time_of_day,'agricultural', "bases/bar/Helen_Bar", True, True, 'agricultural', False, [('ag0', -0.9, -0.123),('ag1', -0.58125, -0.15234375),('ag2', -0.11875, -0.103515625),('ag3', 0.41875, -0.03515625)])
Base.Link (room1, 'bar', 0.5, 0.1, 0.2075, 0.25, 'Chez Copernicus', bar)

import merchant_guild
if (merchant_guild.Can()):
    merchant = merchant_guild.MakeMerchantGuild (room1,time_of_day)
    Base.Link (room1, 'merchant', -0.38, -0.3, 0.22, 0.176667, "Merchant's Guild", merchant)
else:
    merchant = merchant_guild.MakeMerchantGuild (room1,time_of_day)
    Base.Link (room1, 'merchant', -0.38, -0.3, 0.22, 0.176667, "Merchant's Guild", merchant)

import mercenary_guild
if (mercenary_guild.Can()):
    merchant = mercenary_guild.MakeMercenaryGuild (room1,time_of_day)
    Base.Link (room1, 'mercenary', -0.38, -0.15, 0.22, 0.226667, "Mercenary's Guild", merchant)
else:
    merchant = mercenary_guild.MakeMercenaryGuild (room1,time_of_day)
    Base.Link (room1, 'mercenary', -0.38, -0.15, 0.22, 0.226667, "Mercenary's Guild", merchant)

import weapons_lib
if (weapons_lib.CanRepair()):
    weap = weapons_lib.MakeWeapon (room1,time_of_day)
    Base.Link (room1, 'weapon_room', -0.9, -0.8, 0.315, 0.386667, 'Ship_Dealer/Upgrades', weap)
else:
    weap = weapons_lib.MakeWeapon (room1,time_of_day)
    Base.Link (room1, 'weapon_room', -0.9, -0.8, 0.315, 0.386667, 'Ship_Dealer/Upgrades', weap)

Base.Link (room1, 'my_link_id', -1, -0.046667, 0.2825, 0.27, 'Landing_Pad', room0)
Base.Link (room1, 'my_link_id', -0.43, -0.5, 0.3425, 0.17, 'Commodity_Exchange', room2)
Base.Comp (room1, 'my_comp_id', 0.66, -0.843333, 0.2825, 0.423333, 'Mission_Computer', 'Missions News Info ')
