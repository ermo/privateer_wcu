import debug # we use this immediately below so it needs to be imported first...

from difficulty import difficulty
debug.debug("imported difficulty")

from random_encounters import random_encounters
debug.debug("imported random_encounters")

from trading import trading

import Briefing
debug.debug("imported Briefing")

import dynamic_universe
debug.debug("imported dynamic_universe")
#from garbage_collect import garbage_collect

import Director
debug.debug("imported Director")


class privateer (Director.Mission):
    loops=()
    def __init__ (self,sigdis, detectiondis, gendis, minships, genships, fighterprob, enemyprob, capprob, credits_to_maximize_difficulty, capdist):#negative garbage collect dist disables that feature
        debug.debug("initing Director.Mission")
        Director.Mission.__init__(self)
        debug.debug("done initing Director.Mission")
        self.loops=(difficulty (credits_to_maximize_difficulty),
              random_encounters (sigdis, detectiondis, gendis, minships,genships,fighterprob,enemyprob,capprob,capdist),
              trading (),
              dynamic_universe
              # garbage_collect (),
              )

    def Execute(self): #this execute function should not need to be changed...
        for i in self.loops:
            #ti = type(i)
            #debug.debug("%s.Execute()" % (ti))
            i.Execute()
    def initbriefing(self):
        debug.info("init briefing")
    def loopbriefing(self):
        debug.info("loop briefing")
        Briefing.terminate();
    def endbriefing(self):
        debug.info("ending briefing")

#def initstarsystem():
#  random_encounters.initstarsystem() #??? that isn't there
