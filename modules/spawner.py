from go_to_adjacent_systems import *
from go_somewhere_significant import *
import vsrandom
import launch
import faction_ships
import VS
import Briefing
import universe
import unit
import Vector
import Director
import quest
class spawner (Director.Mission):
    def __init__ (self):
        Director.Mission.__init__(self)
        
        self.fac=[]
        self.facnames=["random","confed","militia","merchant","hunter","pirates","retro","kilrathi","AWACS"]
        self.facnames=self.facnames+self.facnames
        for i in range(len(self.facnames)):
            nam=self.facnames[i]+"_SPAWN"
            if (i>=len(self.facnames)/2): 
               nam+="_CAPSHIP"
            self.fac.append(VS.launchJumppoint(nam,"neutral","75 jump.png %s (ONE ONE)"%nam,"planet","sitting_duck",1,1,Vector.Add((0.,-1000.+i*200.,1000.),VS.getPlayer().Position()),"","Gemini/Troy"))
        self.delay=VS.GetGameTime()
    def Execute (self):
        if (VS.getPlayer()):
            iter=0
            for base in self.fac:                
                if (base.getDistance(VS.getPlayer())<0):
                    if (VS.GetGameTime()-self.delay>4):
                        self.delay=VS.GetGameTime()
                        facname = self.facnames[iter]
                        if (facname=="random"):
                            facname=self.facnames[vsrandom.randrange(0,len(self.facnames))]
                        type=faction_ships.getRandomFighter(facname)
                        if (iter>=len(self.facnames)/2):
                            type=faction_ships.getRandomCapitol(facname)
                        tmp=launch.launch_wave_around_unit("Shadow_"+facname,facname,type,"default",1,200,250,VS.getPlayer(),'',0)
#                        tmp.upgrade("basic_armor",0,0,1,0)
#                        tmp.upgrade("shield_4_Level1",0,0,1,0)
#                        tmp.upgrade("reactor_level_2",0,0,1,0)
#                        tmp.upgrade("add_ablative_hull_coating",0,0,1,0)
#                        tmp.upgrade("add_sublimative_hull_coating",0,0,1,0)
                        VS.getPlayer().upgrade("tungsten",0,0,1,0)
                        VS.getPlayer().upgrade("tungsten_hull",0,0,1,0)
                    else:
                        VS.IOmessage(0,"spawner","all","Going to spawn "+self.facnames[iter]+"starships in %d seconds at."%(10-(VS.GetGameTime()-self.delay)))
                iter+=1
