import debug # we use this below so this needs to go first
from difficulty import difficulty
from trading import trading
from random_encounters import random_encounters
debug.debug("imported random_encounters")
import dynamic_universe
import total_jump
#debug.debug("difficulty begin")
#from garbage_collect import garbage_collect
import Director
#debug.debug("directing")
import Briefing
#debug.debug("briefd")


class jump_privateer (Director.Mission):
    loops=()
    def __init__ (self,sigdis, detectiondis, gendis, minships, genships, fighterprob, enemyprob, capprob, credits_to_maximize_difficulty, capdist):#negative garbage collect dist disables that feature
        debug.debug("initing direct")
        Director.Mission.__init__(self)
        debug.debug("done initing direct")
        self.loops=(difficulty (credits_to_maximize_difficulty),
              random_encounters (sigdis, detectiondis, gendis, minships,genships,fighterprob,enemyprob,capprob,capdist),
              trading (),
              dynamic_universe,
              total_jump.total_jump()
    #          garbage_collect (),

              )

    def Execute(self): #this execute function should not need to be changed...
        for i in self.loops:
            i.Execute()

    def initbriefing(self):
        debug.info("init briefing")

    def loopbriefing(self):
        debug.info("loop briefing")
        Briefing.terminate()

    def endbriefing(self):
        debug.info("ending briefing")

#def initstarsystem():
#  random_encounters.initstarsystem() #??? that isn't there
