import Base
import dynamic_mission
import VS
import vsrandom
#import industrial_lib

def MakeIndustrial(sunny,time_of_day='',AWACS=False):
    room = Base.Room ('Landing_Pad')
    room0 = room
    if sunny:
        Base.Texture (room, 'background', 'bases/new_detroit/NewDet_LandingPad_Sunny.spr', 0, 0)
    else:
        Base.Texture (room, 'background', 'bases/new_detroit/NewDet_LandingPad'+time_of_day+'.spr', 0, 0)
    if (AWACS):
        Base.Texture (room, 'background', 'bases/new_detroit/NewDet_LandingPad_AWACS.spr', 0, 0)
    Base.Ship (room, 'my_ship', (-0.25375,0.1175,4.5), (0, .725, -.6887), (-.8, -.4, -.4472))
    Base.Texture (room, 'sh0', 'bases/new_detroit/NewDet_LandingPad_sh0'+time_of_day+'.spr', -0.2, 0.6875)
    Base.Texture (room, 'sh1', 'bases/new_detroit/NewDet_LandingPad_sh1'+time_of_day+'.spr', 0.825, 0.6875)
    Base.Texture (room, 'sh2', 'bases/new_detroit/NewDet_LandingPad_sh2'+time_of_day+'.spr', 0.3875, -0.943359375)
    Base.Texture (room, 'sh3', 'bases/new_detroit/NewDet_LandingPad_sh3'+time_of_day+'.spr', -0.2, -0.46484375)
    if not sunny:
        Base.Texture (room, 'rlp', 'bases/new_detroit/NewDet_LandingPad_rlp'+time_of_day+'.spr', 0.6, -0.25)
    
    room = Base.Room ('Main_Street')
    room1 = room
    
    if sunny:
        Base.Texture (room, 'background', 'bases/new_detroit/NewDet_Concourse_Sunny.spr', 0, 0)
    else:
        Base.Texture (room, 'background', 'bases/new_detroit/NewDet_Concourse'+time_of_day+'.spr', 0, 0)
    if (AWACS):
        Base.Texture (room, 'background', 'bases/new_detroit/NewDet_Concourse_AWACS.spr', 0, 0)
    if not sunny:
        Base.Texture (room, 'rsc', 'bases/new_detroit/NewDet_Concourse_rsc'+time_of_day+'.spr', 0.9125, -0.708984375)
        Base.Texture (room, 'wk0', 'bases/new_detroit/NewDet_Concourse_wk0'+time_of_day+'.spr', -0.11875, -0.38671875)
        Base.Texture (room, 'hvc', 'bases/new_detroit/NewDet_Concourse_hvc'+time_of_day+'.spr', 0.08125, -0.25)
        Base.Texture (room, 'rnc', 'bases/new_detroit/NewDet_Concourse_rnc'+time_of_day+'.spr', 0.6, -0.25)
    Base.Texture (room, 'wk1', 'bases/new_detroit/NewDet_Concourse_wk1'+time_of_day+'.spr', 0.7125, -0.630859375)
    Base.Texture (room, 'wk2', 'bases/new_detroit/NewDet_Concourse_wk2'+time_of_day+'.spr', -0.30625, -0.396484375)
    Base.Texture (room, 'ber', 'bases/new_detroit/NewDet_Concourse_ber'+time_of_day+'.spr', -0.76875, 0.375)
    
    Base.LaunchPython (room0, 'my_launch_id', 'bases/launch_music.py', -0.625, -0.193333, 0.595, 0.693333, 'Launch')
    Base.Link (room0, 'my_link_id', 0.115, 0.01, 0.585, 0.67, 'Main_Street', room1)
    import bar_lib
    bar = bar_lib.MakeBar (room1,time_of_day,'industrial','bases/bar/NewDet_Bar', True, True, 'new_detroit', False, [('nd0', -0.7125, 0.04296875), ('nd1', -0.31875, 0.0625), ('nd2', -0.08125, 0.072265625), ('nd3', 0.3375, 0.1015625)])
    Base.Link (room1, 'bar', -0.8525, -0.84, 0.2475, 1, 'Bar', bar)
    import commodity_lib
    commodity = commodity_lib.MakeCommodity (room1,time_of_day)
    Base.Link (room1, 'commodity', -0.36, -0.413333, 0.19, 0.176667, 'Commodity_Exchange', commodity)
    Base.Comp (room1, 'my_comp_id', 0.785, -0.666667, 0.125, 0.34, 'Mission_Computer', 'Missions News Info ')
    Base.Link (room1, 'my_link_id', -0.52, -0.46, 0.08, 0.273333, 'To_Landing_Pad', room0)
    import weapons_lib
    weap = weapons_lib.MakeWeapon (room1,time_of_day)
    Base.Link (room1, 'weapon_room', 0.3325, 0.0866667, 0.625, 0.873333, 'Ship_Dealer/Upgrade', weap)
    import merchant_guild
    merchant = merchant_guild.MakeMerchantGuild (room1,time_of_day)
    Base.Link (room1, 'merchant', -0.035, -0.0266667, 0.13, 0.236667, 'Merchant_Guild', merchant)
    import mercenary_guild
    merchant = mercenary_guild.MakeMercenaryGuild (room1,time_of_day)
    Base.Link (room1, 'mercenary', -0.04, 0.306667, 0.2325, 0.36, 'Mercenary_Guild', merchant)
