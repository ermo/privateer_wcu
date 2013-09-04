import Base
import dynamic_mission
import VS

time_of_day=''
bar=-1
weap=-1
room0=-1
plist=VS.musicAddList('new_constantinople.m3u')
VS.musicPlayList(plist)
dynamic_mission.CreateMissions()
room = Base.Room ('New_Constantinople_Landing_Bay')
room0 = room
Base.Texture (room, 'background', 'bases/new_constantinople/NewCon_LandingBay'+time_of_day+'.spr', 0, 0)
Base.Texture (room, 'lps', 'bases/new_constantinople/NewCon_LandingBay'+time_of_day+'_lps.spr', 0.08125, 0.0234375)
Base.Texture (room, 'lgt', 'bases/new_constantinople/NewCon_LandingBay'+time_of_day+'_lgt.spr', -0.51875, 0.47265625)
Base.Texture (room, 'sh0', 'bases/new_constantinople/NewCon_LandingBay'+time_of_day+'_sh0.spr', -0.34375, 0.375)
Base.Texture (room, 'sh1', 'bases/new_constantinople/NewCon_LandingBay'+time_of_day+'_sh1.spr', -0.2, 0.189453125)
Base.Texture (room, 'sh2', 'bases/new_constantinople/NewCon_LandingBay'+time_of_day+'_sh2.spr', 0.2625, 0.375)
Base.Ship (room, 'my_ship', (0.0,-0.35,5.5), (0, 0.9887, -0.15), ( -0.9662, -0.0, -0.25766265))

room = Base.Room ('Main_Concourse')
room1 = room
Base.Texture (room, 'background', 'bases/new_constantinople/NewCon_Concourse'+time_of_day+'.spr', 0, 0)
Base.Texture (room, 'win', 'bases/new_constantinople/win.spr', 0.8866, 0.085857)
Base.Texture (room, 'stt', 'bases/new_constantinople/NewCon_Concourse'+time_of_day+'_stt.spr', 0.6, 0.6875)
Base.Texture (room, 'stb', 'bases/new_constantinople/NewCon_Concourse'+time_of_day+'_stb.spr', 0.60625, 0.248)
Base.Texture (room, 'sh3', 'bases/new_constantinople/NewCon_Concourse'+time_of_day+'_sh3.spr', 0.6, -0.435546875)
Base.Texture (room, 'sh4', 'bases/new_constantinople/NewCon_Concourse'+time_of_day+'_sh4.spr', 0.6125, 0.6875)
Base.Texture (room, 'car', 'bases/new_constantinople/NewCon_Concourse'+time_of_day+'_car.spr', 0.6, -0.8046875)
Base.Texture (room, 'ldp00000', 'bases/new_constantinople/NewCon_Concourse'+time_of_day+'_ldp00000.spr', 0.94375, 0.375)

Base.LaunchPython (room0, 'my_launch_id', 'bases/launch_music.py', -0.515, -0.93, 1.025, 0.94, 'Launch')
Base.Link (room0, 'my_link_id', -0.9475, -0.576667, 0.305, 0.266667, 'Main_Concourse', room1)
import commodity_lib
commodity = commodity_lib.MakeCommodity (room1,time_of_day)
Base.Link (room1, 'commodity', 0.21, -0.97, 0.755, 0.553333, 'Commodity_Exchange', commodity)
import bar_lib
bar = bar_lib.MakeBar (room1,time_of_day,'default','bases/bar/NewCon_Bar', True, True, 'new_constantinople',False,[('nc0', -0.7456875, -0.0194),('nc1',-0.582,-0.1649),('nc2',-0.1394375, -0.1746),('nc3',-0.0909375, -0.1358),('nc4',0.400125, -0.0679)])
Base.Link (room1, 'bar', 0.2325, -0.17, 0.0925, 0.176667, 'Bar', bar)
import mercenary_guild
merchant = mercenary_guild.MakeMercenaryGuild (room1,time_of_day)
Base.Link (room1, 'mercenary', -0.0875, -0.266667, 0.23, 0.3, 'Mercenary_Guild', merchant)
import merchant_guild
merchant = merchant_guild.MakeMerchantGuild (room1,time_of_day)
Base.Link (room1, 'merchant', -0.895, -0.423333, 0.5275, 0.483333, 'Merchant_Guild', merchant)
Base.Comp (room1, 'my_comp_id', -0.28, -0.306667, 0.14, 0.28, 'Mission_Computer', 'Missions News Info ')
import weapons_lib
weap = weapons_lib.MakeWeapon (room1,time_of_day)
Base.Link (room1, 'weapon_room', 0.515, -0.413333, 0.4575, 0.596667, 'Ship_Dealer/Upgrades', weap)
Base.Python (room1, 'my_link_id', 0.82, 0.226667, 0.16, 0.746667, 'Landing_Pad', '''#
import Base
Base.EraseObj('''+str(room1)+''',"ldp00000")
Base.Texture ('''+str(room1)+''', "ldp", "bases/new_constantinople/NewCon_Concourse_ldp.spr", 0.94375, 0.375) #0.9154375, 0.3492)
Base.Python('''+str(room1)+''', "ldp", -1, -1, 2, 2, "Landing_Pad", "#\\n", True)
Base.RunScript('''+str(room1)+''', "trainleave", """#
import Base
Base.SetCurRoom('''+str(room0)+''')
Base.EraseLink('''+str(room1)+''',"ldp")
Base.EraseObj('''+str(room1)+''',"ldp")
Base.EraseObj('''+str(room1)+''',"trainleave")
Base.Texture ('''+str(room1)+''', "ldp00000", "bases/new_constantinople/NewCon_Concourse"+time_of_day+"_ldp00000.spr", 0.94375, 0.375) #0.9154375, 0.3492)
""", 3.2)
''', False)
