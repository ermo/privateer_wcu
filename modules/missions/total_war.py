import Briefing
import Director
import VS
import debug
import faction_ships
import launch
import universe
import unit
import vsrandom

class total_war (Director.Mission):
    def __init__(self):
        debug.info("init total_war")
        VS.SetDifficulty(.9)
        Director.Mission.__init__(self)
        self.lasttime=-1000
        self.waittime=10.0

    def launch_new_wave(self):
        un = VS.getPlayer()
        if (vsrandom.randrange(0,4)==0):
            if (un):
                currentsystem = VS.getSystemFile()
                numadj=VS.GetNumAdjacentSystems(currentsystem)
                if (numadj):
                    cursys=VS.GetAdjacentSystem(currentsystem,vsrandom.randrange(0,numadj))
                else:
                    cursys = 'enigma_sector/heavens_gate'
                debug.info("TJ: jumping to "+cursys)
                un.JumpTo(cursys)
            else:
                debug.info("TJ: jumping to [ERROR: you are null]")
        side = vsrandom.randrange(0,2)
        faction="confed"
        ai = vsrandom.randrange(0,6)
        if (0 and ai==0):
            ai = "printhello.py"
        else:
            ai = "default"
        if (side==0):
            faction=faction_ships.get_enemy_of("confed")
        else:
            faction=faction_ships.get_friend_of("confed")
        launched = launch.launch_wave_around_unit ("Shadow",faction,faction_ships.getRandomFighter(faction),ai,vsrandom.randrange(1,10),100.0,2000.0,VS.getPlayer(),'')
        if (vsrandom.randrange(0,10)==0):
            launch.launch_wave_around_unit ("ShadowCap",faction,faction_ships.getRandomCapitol(faction),ai,1,2000.0,4000.0,VS.getPlayer(),'')

    def Execute (self):
        un=VS.getUnit(0);
        i=0
        while (un):
            i+=1
            un=  VS.getUnit(i)
        time = VS.GetGameTime()
        if (time-self.lasttime>self.waittime):
            self.launch_new_wave()
            self.waittime=vsrandom.randrange(4.0,20.0)
            self.lasttime=time

    def initbriefing(self):
        debug.info("init briefing")
    def loopbriefing(self):
        debug.info("loop briefing")
        Briefing.terminate();
    def endbriefing(self):
        debug.info("ending briefing")
