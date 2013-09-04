import dynamic_mission
import VS
import vsrandom
import industrial_lib
sunny=vsrandom.uniform(0,1)>=.99

time_of_day=''
plist=VS.musicAddList('new_detroit.m3u')
VS.musicPlayList(plist)
dynamic_mission.CreateMissions()

industrial_lib.MakeIndustrial(sunny,time_of_day,False)
