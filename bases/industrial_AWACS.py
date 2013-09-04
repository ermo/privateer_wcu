import dynamic_mission
import VS
import vsrandom
import industrial_lib
sunny=vsrandom.uniform(0,1)>.9

time_of_day=''
plist=VS.musicAddList('AWACS.m3u')
VS.musicPlayList(plist)
dynamic_mission.CreateMissions()

industrial_lib.MakeIndustrial(sunny,time_of_day,True)
