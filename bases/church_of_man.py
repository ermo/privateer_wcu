import Base
import dynamic_mission
import VS

time_of_day=''
bar=-1
weap=-1
room0=-1
dynamic_mission.CreateMissions()
import pleasure_land
room0 = pleasure_land.MakePleasureAgriculturalLanding(time_of_day)

room = Base.Room ('Temple')
room1 = room
Base.Link (room0, 'my_link_id', 0.6025, -0.463333, 0.29, 0.633333, 'Holy_Temple', room1)
import quest
done_comp=False
if quest.checkSaveValue(VS.getCurrentPlayer(),"jones_dead",1.0):
	Base.Texture (room, 'background', 'bases/church_of_man/GaeaDead.spr', 0, 0)
	Base.Texture (room, 'smk', 'bases/church_of_man/smk.spr', 0.6, -0.25)
	plist=VS.musicAddList('church_of_man_dead.m3u')
	Base.Comp (room1, 'my_comp_id', -0.155, 0.576667, 0.425, 0.243333, 'Save/Load', 'Info ')
	done_comp=True
else:
	Base.Texture (room, 'background', 'bases/church_of_man/Gaea.spr', 0, 0)
	Base.Texture (room, 'fr0', 'bases/church_of_man/fr0.spr', -0.61875, 0.521484375)
	Base.Texture (room, 'fr1', 'bases/church_of_man/fr1.spr', 0.6875, 0.6875)
	Base.Texture (room, 'eye', 'bases/church_of_man/eye.spr', 0, 0.560546875)
	Base.Texture (room, 'lgo', 'bases/church_of_man/lgo.spr', -0.075, -0.357421875)
	Base.Texture (room, 'sn0', 'bases/church_of_man/sn0.spr', -0.6, -0.50390625)
	Base.Texture (room, 'sn1', 'bases/church_of_man/sn1.spr', 0.79375, -0.240234375)
	plist=VS.musicAddList('church_of_man.m3u')
VS.musicPlayList(plist)

Base.Link (room1, 'my_link_id', -0.9725, -0.97, 0.3625, 0.213333, 'Go_To_Landing_Pad', room0)

import campaign_lib

if len(campaign_lib.getActiveCampaignNodes(room1)):
	if not done_comp:
		Base.Comp (room1, 'my_comp_id', -0.155, 0.576667, 0.425, 0.243333, 'Pray_For_Starship', 'Info ShipDealer ')
		done_comp=True

	Base.Python (room1, 'my_link_id', -0.6775, -0.826, 0.47, 0.40, 'Talk_To_Faithful', '#\nprint "AHOY AHOY"\nimport campaign_lib\nimport campaign_lib\ncampaign_lib.clickFixer('+str(room1)+')\n',False)
if not done_comp:
	Base.Comp (room1, 'my_comp_id', -0.155, 0.576667, 0.425, 0.243333, 'Save/Load', 'Info ')
