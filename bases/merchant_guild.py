import Base
import VS
import guilds
def Can():
    return guilds.CanMerchantGuild()
def MakeMerchantGuild(concourse,timeofdayignored="_day"):
    room = Base.Room ('Merchant_Guild')
    room0 = room
    Base.Texture (room, 'background', 'bases/merchant_guild/merchantguild.spr', 0, 0)
    Base.Texture (room, 'mtg', 'bases/merchant_guild/mtg.spr', -0.03125, 0.01367) # -0.0303125, -0.0097)
    
    Base.Python (room0, 'talk_merchant', -0.0975, -0.133333, 0.1975, 0.416667, 'Talk_To_Merchant', 'bases/merchant_talk.py',0)
    Base.Link (room0, 'exit_merchant', -0.985, -0.993333, 1.725, 0.21, 'Exit_Merchant_Guild',concourse)
    room = Base.Room ('Merchant_Guild_Computer')
    Base.Texture (room, 'background1', 'bases/merchant_guild/merchantguildcomp.spr', 0, 0)
    room1=room
    Base.Link(room0,'to_merc_comp',-0.3175, -0.103333, 0.195, 0.223333,'Examine_Merchant_Guild_Computer',room1)
    Base.Link(room1,'to_merc_comp',-0.7275, -0.976667, 1.48, 0.146667,'To_Merchant_Guild',room0)
    guildroom=guilds.GuildRoom(guilds.guilds['Merchant'],room1)
#   guildroom.AddMissionButton(guilds.MissionButton(("bases/merchant_guild/merchantcd1.spr",0.5759375,-0.7469), 0.2825, -0.793333, 0.205, 0.466667, guildroom, 3))
#   guildroom.AddMissionButton(guilds.MissionButton(("bases/merchant_guild/merchantcd2.spr",0.5759375,-0.7469), 0.4075, -0.766667, 0.1325, 0.463333, guildroom, 2))
#   guildroom.AddMissionButton(guilds.MissionButton(("bases/merchant_guild/merchantcd3.spr",0.5759375,-0.7469), 0.5375, -0.7, 0.1175, 0.42, guildroom, 1))
#   guildroom.AddMissionButton(guilds.MissionButton(("bases/merchant_guild/merchantcd4.spr",0.5759375,-0.7469), 0.59, -0.676667, 0.13, 0.423333, guildroom, 0))
    guildroom.AddMissionButton(guilds.MissionButton(("bases/merchant_guild/merchantcd1.spr",0.59375,-0.7285), 0.2825, -0.793333, 0.205, 0.466667, guildroom, 3))
    guildroom.AddMissionButton(guilds.MissionButton(("bases/merchant_guild/merchantcd2.spr",0.59375,-0.7285), 0.4075, -0.766667, 0.1325, 0.463333, guildroom, 2))
    guildroom.AddMissionButton(guilds.MissionButton(("bases/merchant_guild/merchantcd3.spr",0.59375,-0.7285), 0.5375, -0.7, 0.1175, 0.42, guildroom, 1))
    guildroom.AddMissionButton(guilds.MissionButton(("bases/merchant_guild/merchantcd4.spr",0.59375,-0.7285), 0.59, -0.676667, 0.13, 0.423333, guildroom, 0))
    guildroom.AddAcceptButton(guilds.AcceptButton(("bases/merchant_guild/merchantguildcompon.spr",0.4061875,0.1358),-0.3625, -0.0966667, 0.8875, 0.876667,guildroom))
    Base.TextBox(room1, 'merchantbox', '', -0.3395, 0.7275, (0.5, -0.7954, 1), (0,0,0), 0, (1,1,1))
    guildroom.AddTextBox('merchantbox');
    guilds.CreateGuild(guildroom)
    return room0
