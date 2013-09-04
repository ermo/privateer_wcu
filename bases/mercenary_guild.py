import Base
import VS
import guilds
def Can():
    return guilds.CanMercenaryGuild()

def MakeMercenaryGuild(concourse,timeofdayignored="_day"):
    room = Base.Room ('Mercenary_Guild')
    room0 = room
    Base.Texture (room, 'background', 'bases/merchant_guild/mercernaryguild.spr', 0, 0)
    Base.Texture (room, 'myg', 'bases/merchant_guild/myg.spr', 0.125, 0.04)
    Base.Texture (room, 'psm', 'bases/merchant_guild/psm.spr', -0.73, 0.112)
    
    Base.Python (room0, 'talk_mercenary', -0.065, -0.17, 0.23, 0.506667, 'Talk_To_Receptionist', 'bases/mercenary_talk.py',0)
    Base.Link (room0, 'exit_mercenary', -0.7275, -0.976667, 1.48, 0.146667, 'Exit_Mercenary_Guild',concourse)
    room = Base.Room ('Mercenary_Guild_Computer')
    Base.Texture (room, 'background1', 'bases/merchant_guild/mercernaryguildcomp.spr', 0, 0)
    Base.Texture (room, 'psc', 'bases/merchant_guild/psc.spr', -0.8, -0.267)
    room1 = room
    Base.Link(room0,'to_merc_comp',-0.415, -0.226667, 0.335, 0.293333,'Examine_Mercenary_Guild_Computer',room1)
    Base.Link(room1,'to_merc_comp',-0.7275, -0.976667, 1.48, 0.146667,'To_Mercenary_Guild',room0)
    guildroom=guilds.GuildRoom(guilds.guilds['Mercenary'],room1)
    guildroom.AddMissionButton(guilds.MissionButton(("bases/merchant_guild/mercernarycd1.spr",0.61875,-0.67887), 0.1825, -0.653333, 0.2575, 0.52, guildroom, 3))
    guildroom.AddMissionButton(guilds.MissionButton(("bases/merchant_guild/mercernarycd2.spr",0.61875,-0.67887), 0.35, -0.713333, 0.2975, 0.593333, guildroom, 2))
    guildroom.AddMissionButton(guilds.MissionButton(("bases/merchant_guild/mercernarycd3.spr",0.61875,-0.67887), 0.44, -0.683333, 0.345, 0.556667, guildroom, 1))
    guildroom.AddMissionButton(guilds.MissionButton(("bases/merchant_guild/mercernarycd4.spr",0.61875,-0.67887), 0.66, -0.6, 0.3375, 0.496667, guildroom, 0))
    guildroom.AddAcceptButton(guilds.AcceptButton(None, -0.7325, -0.526667, 1.0175, 1.08667, guildroom))
    Base.TextBox(room1, 'mercenarybox', '', -0.6325, 0.4067, (.27, -.55, 1), (0,0,0), 0, (1,1,1))
    guildroom.AddTextBox('mercenarybox');
    guilds.CreateGuild(guildroom)
    return room0
