import Base
import dynamic_mission
import VS

time_of_day=''
bar=-1
weap=-1
room0=-1
dynamic_mission.CreateMissions()
room = Base.Room ('Landing_Pad')
room0 = room
Base.Texture (room, 'background', 'bases/mining_base/MiningBase_LandingPad'+time_of_day+'.spr', 0, 0)
Base.Texture (room, 'lgt', 'bases/mining_base/MiningBase_LandingPad_lgt'+time_of_day+'.spr', 0.775, 0.375)
Base.Texture (room, 'shp', 'bases/mining_base/MiningBase_LandingPad_shp'+time_of_day+'.spr', 0.2125, 0.6875)
#Base.Ship (room, 'my_ship', (0.044375,-0.319167,3), (0, 0.93, -0.34), (-1, 0, 0))  # original PPU r505 orientation

# (pos_vec), (up_vec), (nose_vec)
# OK basic relative size and position of scale 12 Tarsus
# (180-32.5 degrees yaw anti-clockwise around Y in ./tools/matrix_rotation.py)
#Base.Ship (room, 'my_ship', (0.04, -0.18, 2.6), (0, 1, 0), (-0.5372996083, 0, -0.8433914458)) 
# as above but with +1 degree pitch up (anti-clockwise) around X
Base.Ship (room, 'my_ship', (0.04, -0.18, 2.6), (0.014065, 0.999657, 0.022077), (-0.537115, 0.026177, -0.843102))

room = Base.Room ('Main_Concourse')
room1 = room
Base.Texture (room, 'background', 'bases/mining_base/MiningBase_Concourse'+time_of_day+'.spr', 0, 0)

Base.LaunchPython (room0, 'my_launch_id', 'bases/launch_music.py', -0.3325, -0.58, 0.875, 0.653333, 'Launch')
Base.Link (room0, 'my_link_id', 0.5875, -0.36, 0.2975, 0.573333, 'Main_Concourse', room1)
Base.Link (room1, 'my_link_id', -0.75, -0.11, 0.215, 0.4, 'Landing_Pad', room0)
import commodity_lib
bar = commodity_lib.MakeCommodity (room1,time_of_day)
Base.Link (room1, 'commodity', 0.6975, -0.216667, 0.275, 0.37, 'Commodity_Exchange', bar)
Base.Comp (room1, 'my_comp_id', 0.5425, -0.183333, 0.1075, 0.183333, 'Mission_Computer', 'Missions News Info ')
import mercenary_guild
if (mercenary_guild.Can()):
    merchant = mercenary_guild.MakeMercenaryGuild (room1,time_of_day)
    Base.Link (room1, 'mercenary', 0.2625, 0.196667, 0.225, 0.203333, 'Mercenary_Guild', merchant)
else:
    Base.Texture(room1,'nomercenary','bases/mining_base/nomercenary.spr', 0.425, 0.296875)

import merchant_guild
if (merchant_guild.Can()):
    merchant = merchant_guild.MakeMerchantGuild (room1,time_of_day)
    Base.Link (room1, 'merchant', 0.6775, 0.31, 0.295, 0.263333, 'Merchant_Guild', merchant)
else:
    Base.Texture(room1,'nomerchant','bases/mining_base/nomerchant.spr', 0.85, 0.482421875)

import weapons_lib
if (weapons_lib.CanRepair()):
    weap = weapons_lib.MakeWeapon (room1,time_of_day)
    Base.Link (room1, 'weapon_room', -0.0975, -0.0466667, 0.2225, 0.326667, 'Ship_Dealer/Upgrade', weap)
    Base.Texture (room, 'wk0', 'bases/mining_base/MiningBase_Concourse_wk0'+time_of_day+'.spr', -0.23125, 0.00390625)
else:
    Base.Texture(room1,'noshipdealer','bases/mining_base/noshipdealer.spr', 0.0375, 0.052734375)

Base.Texture (room1, 'car', 'bases/mining_base/MiningBase_Concourse_car'+time_of_day+'.spr', 0.97255, -0.279296875)
import bar_lib
bar = bar_lib.MakeBar (room1,time_of_day,'mining','bases/bar/MiningBase_Bar',True,True,'mining_base',False,[('mb0',-0.8125,-0.19140625),('mb1',-0.46875,-0.20127255),('mb2',-0.1875,-0.025390625)])

Base.Link (room1, 'bar', 0.275, -0.133333, 0.2375, 0.233333, 'Bar', bar)
import campaign_lib
if not campaign_lib.do_not_play_music:
   plist=VS.musicAddList('mining_base.m3u')
   VS.musicPlayList(plist)
