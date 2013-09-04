import Base
import dynamic_mission
import VS
import pleasure_land

time_of_day=''
bar=-1
weap=-1
room0=-1

dynamic_mission.CreateMissions()

room0 = pleasure_land.MakePleasureAgriculturalLanding(time_of_day)

room = Base.Room ('Casino')
room1 = room
Base.Texture (room, 'background', 'bases/pleasure/Jolson_Concourse'+time_of_day+'.spr', 0, 0)

Base.Texture (room, 'lts', 'bases/pleasure/Jolson_Concourse_lts'+time_of_day+'.spr', 0, 0)

Base.Link (room0, 'my_link_id', 0.66, -0.396667, 0.2425, 0.473333, 'Casino', room1)
import bar_lib
bar = bar_lib.MakeBar (room1,time_of_day,'pleasure','bases/bar/Jolson_Bar',True,True,'pleasure',True,[('pl0',-0.9,-0.083984375),('pl1',-0.1875,-0.23046875),('pl2',-0.18125,-0.025390625),('pl3',0.3625,-0.025390625)])
#Base.Texture(bar,'bartender','bases/pleasure/Jolson_Bar_table.spr',-.75,-.9165)
Base.Link (room1, 'bar', -0.5225, -0.676667, 0.2075, 0.4, 'Pub', bar)
import commodity_lib
commodity = commodity_lib.MakeCommodity (room1,time_of_day)
Base.Link (room1, 'commodity', -0.115, -0.663333, 0.32, 0.51, 'Commodity_Exchange', commodity)
import merchant_guild
if (merchant_guild.Can()):
	merchant = merchant_guild.MakeMerchantGuild (room1,time_of_day)
	Base.Link (room1, 'merchant', 0.2825, -0.666667, 0.045, 0.313333, 'Merchant_Guild', merchant)
else:
	pass #place blocker
import mercenary_guild
if (mercenary_guild.Can()):
	merchant = mercenary_guild.MakeMercenaryGuild (room1,time_of_day)
	Base.Link (room1, 'mercenary', 0.3425, -0.666667, 0.0475, 0.326667, 'Mercenary_Guild', merchant)
else:
	pass #place blocker
Base.Link (room1, 'my_link_id', 0.6125, -0.713333, 0.2, 0.38, 'Landing_Pad', room0)
import weapons_lib
if (weapons_lib.CanRepair()):
	weap = weapons_lib.MakeWeapon (room1,time_of_day)
	Base.Link (room1, 'weapon_room', 0.8475, -1., 0.1225, 2., 'Ship_Dealer', weap)
else:
	pass #place blocker
Base.Comp (room1, 'my_comp_id', 0.415, -0.653333, 0.125, 0.276667, 'Mission_Computer', 'Missions News Info ')
import campaign_lib
if not campaign_lib.do_not_play_music:
   plist=VS.musicAddList('pleasure.m3u')
   VS.musicPlayList(plist)
