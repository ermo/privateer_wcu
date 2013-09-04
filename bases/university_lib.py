import Base
import dynamic_mission
import VS
import quest
import campaign_lib

def MakeUniversity (time_of_day='_day'):
    bar=-1
    weap=-1
    room0=-1

    campaign_lib.masterson_extraspeech=""
    plist=VS.musicAddList('oxford.m3u')
    VS.musicPlayList(plist)
    dynamic_mission.CreateMissions()
    room = Base.Room ('Landing_Pad')
    room0 = room
    Base.Texture (room, 'background', 'bases/university/Landing_Pad.spr', 0.0, 0.0)
    Base.Texture (room, 'tnl00000', 'bases/university/Landing_Pad_tnl00000.spr', 0.6, 0.375)
    Base.Ship (room, 'my_ship', (0.2,-0.375,5.75), (0.05, 0.988746, 0.141), (-0.7, 0.141, -0.7))
    
    room = Base.Room ('Landing_Pad')
    room0train = room
    Base.Texture (room, 'background', 'bases/university/Landing_Pad.spr', 0.0, 0.0)
    Base.Ship (room, 'my_ship', (0.2,-0.375,5.75), (0.05, 0.988746, 0.141), (-0.7, 0.141, -0.7))
    
    room = Base.Room ('Campus_Quad')
    room1 = room
    Base.Texture (room, 'background', 'bases/university/Main_Quad.spr', 0.0, 0.0)
    Base.Texture (room, 'tnc', 'bases/university/Main_Quad_tnc.spr', -0.8, -0.943359375)
    Base.Texture (room, 'wk0', 'bases/university/Main_Quad_wk0.spr', 0.3125, -0.015625)
    Base.Texture (room, 'brd', 'bases/university/Main_Quad_brd.spr', 0.13125, -0.38671875)
    room2 = -1
    room = Base.Room ('Library_Stacks')
    room2 = room
    denied=False
    if quest.checkSaveValue(VS.getPlayer().isPlayerStarship(),"access_to_library",2):
        denied=True
    the_campaigns=campaign_lib.getActiveCampaignNodes(room2)
    if quest.checkSaveValue(VS.getPlayer().isPlayerStarship(),"access_to_library",2):
        denied=True
    if quest.checkSaveValue(VS.getPlayer().isPlayerStarship(),"access_to_library",1): # access granted
        Base.Texture (room, 'background', 'bases/university/Library_Main.spr', 0, 0)
        room = Base.Room ('Computer_Console')
        room3 = room
        Base.Texture (room, 'background', 'bases/university/ComputerMain.spr', 0, 0)
        
        room = Base.Room ('Library_Terminal')
        room4 = room
        Base.Texture (room, 'background', 'bases/university/ComputerAnalysing.spr', 0, 0)
        room = Base.Room ('Library_Terminal')
        room5 = room
        Base.Texture (room, 'background', 'bases/university/Monkhouse.spr', 0, 0)
        Base.Link (room2, 'my_link_id', -0.9875, -0.743333, 0.11, 1.71, 'Campus_Quad', room1)
        Base.Link (room2, 'my_link_id', -0.155, -0.913333, 0.405, 0.286667, 'Library_Console', room3)
        Base.Link (room3, 'my_link_id', 0.105, -0.756667, 0.77, 0.8, 'Computer_Analysis', room4)
        Base.Link (room3, 'my_link_id', -0.9725, -0.97, 0.5325, 1.95, 'Library_Stacks', room2)
        Base.Link (room4, 'my_link_id', 0.1025, -0.75, 0.77, 0.783333, 'Read_Computer_Screen', room5)
        Base.Link (room4, 'my_link_id', -0.9775, -0.96, 0.3, 1.95333, 'Library_Stacks', room2)
        Base.Link (room5, 'my_link_id', -1, -1, 2, 2, 'Turn_Off_Computer', room3)
        if denied:
            Base.Texture(room2,'masterson_access', 'bases/university/masterson.spr', 0, 0)
            ##campaign_lib.clickFixer(room2)
            Base.Python(room2,'masterson_access', -1, -1, 2, 2, 'Enter_Library',
                "#\nimport Base\nBase.EraseLink("+str(room2)+", 'masterson_access')\nBase.EraseObj("+str(room2)+", 'masterson_access')\n", False)
            campaign_lib.masterson_extraspeech="barspeech/campaign/mastersonfinal.wav"
    else:
        Base.Texture (room, 'background', 'bases/university/masterson.spr', 0, 0)
        ##campaign_lib.clickFixer(room2)
        if len(the_campaigns) and denied: # mission in progress.
            Base.LinkPython(room2, 'masterson_return', '#\nimport campaign_lib\n##campaign_lib.clickFixer('+str(room2)+')\n', -1, -1, 2, 2, 'Exit_Library', room1)
        else: # Access denied. Come back after Lynch missions
            campaign_lib.displayText(room2, [("Masterson","Excuse me, where do you think you're going?"),
                ("Burrows","I have some personal research I need to conduct."),
                ("Masterson","I'm sorry, sir, but access to the Oxford library files is restricted to students."),
                ("Burrows","Look, couldn't I just buy a library card?"),
                ("Masterson","I'm afraid not. Good day to you, sir.")])
            campaign_lib.masterson_extraspeech="campaign/onlyforstudents-priv.ogg"
            Base.LinkPython(room2, 'masterson_return','#\nimport VS\nVS.StopAllSounds()\n', -1, -1, 2, 2, 'Exit_Library', room1)
    
    Base.LaunchPython (room0, 'my_launch_id', 'bases/launch_music.py', -0.0075, -0.59, 0.4725, 0.31, 'Launch')
    Base.LinkPython (room0, 'my_link_id', '''#
import Base
Base.Texture ('''+str(room0train)+''', "tnl", "bases/university/Landing_Pad_tnl.spr", 0.6, 0.375) #0.582, 0.3492)
Base.RunScript('''+str(room0train)+''', "trainleave", """#
import Base
Base.SetCurRoom('''+str(room1)+''')
Base.EraseObj('''+str(room0train)+''',"tnl")
Base.EraseObj('''+str(room0train)+''',"trainleave")
""", 3.2)
''', 0.4225, -0.103333, 0.5425, 0.466667, 'Train_To_University_Campus', room0train)
    Base.Link (room1, 'my_link_id', -0.9675, -0.97, 0.595, 0.923333, 'Train_To_Landing_Pad', room0)
    Base.Comp (room1, 'my_comp_id', -0.5925, 0.293333, 0.09, 0.213333, 'Mission_Computer', 'Missions News Info ')
    import weapons_lib
    weap = weapons_lib.MakeWeapon (room1,time_of_day,"bases/university/Oxford_Shipdealer")
    Base.Link (room1, 'weapon_room', 0.695, -0.88, 0.2875, 0.913333, 'Ship_Dealer', weap)
    import commodity_lib
    commodity = commodity_lib.MakeCommodity (room1,time_of_day)
    Base.Link (room1, 'commodity', 0.09, -0.973333, 0.5275, 0.34, 'Commodity_Exchange', commodity)
    import bar_lib
    bar = bar_lib.MakeBar (room1,time_of_day,"oxford","bases/university/Bar",False,False,None,False,[],"oxford")
    Base.Link (room1, 'bar', -0.9725, 0.0966667, 0.2325, 0.666667, 'Campus_Bar', bar)
    import mercenary_guild
    merchant = mercenary_guild.MakeMercenaryGuild (room1,time_of_day)
    Base.Link (room1, 'mercenary', -0.53, 0.516667, 0.2, 0.456667, 'Mercenary_Guild', merchant)
    import merchant_guild
    merchant = merchant_guild.MakeMerchantGuild (room1,time_of_day)
    Base.Link (room1, 'merchant', -0.2625, 0.593333, 0.1375, 0.39, 'Merchant_Guild', merchant)
    Base.LinkPython (room1, 'my_link_id','#\nimport campaign_lib\ncampaign_lib.clickFixer('+str(room2)+')\nif campaign_lib.masterson_extraspeech!="":\n\timport VS\n\tVS.playSound(campaign_lib.masterson_extraspeech,(0.,0.,0.),(0.,0.,0.,))\n\tcampaign_lib.masterson_extraspeech=""\n', 0.34, 0.45, 0.6375, 0.513333, 'Library', room2)
    #Base.Link (room1, 'my_link_id', 0.36, 0.696667, 0.0625, 0.0966667, 'Talk_To_Masterson', room5)
    return room1
