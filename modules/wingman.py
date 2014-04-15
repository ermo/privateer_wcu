from go_to_adjacent_systems import *
from go_somewhere_significant import *
import Briefing
import Director
import VS
import debug
import faction_ships
import launch
import unit
import universe
import vsrandom


class wingman (Director.Mission):
    def __init__ (self,price,factionname,numships,difficulty):
        Director.Mission.__init__(self)
        self.price=price/3
        self.faction=factionname
        self.you = VS.getPlayer()
        self.numships=numships
        self.diff=difficulty
        self.adjsys=go_somewhere_significant (self.you,0,5000,0)
        self.wingship = faction_ships.getRandomFighter(factionname)
        nam = "[%s]" % self.wingship
        self.adjsys.Print("Hello I'm waiting for your arrival at %s" ,self.wingship)
        VS.IOmessage(1,self.wingship,"all","Once you meet me")
        VS.IOmessage(2,self.wingship,"all","I will obey your commands until our contracts expire.")

    def GenerateWingmen(self):
        if (self.you):
            if (self.you.getCredits()>=self.price):
                self.you.addCredits(-self.price)
                lead=launch.launch_wave_around_unit(self.you.getFlightgroupName(),
                                                    self.you.getFactionName(),
                                                    self.wingship,
                                                    "default",
                                                    self.numships,
                                                    500,
                                                    1000,
                                                    self.you)
                VS.IOmessage (0,lead.getName(),"all","I am at your service commander. Let us succeed!")
            else:
                lead=launch.launch_wave_around_unit("ForHire",
                                                    self.faction,
                                                    self.wingship,
                                                    "default",
                                                    self.numships,
                                                    500,
                                                    1000,
                                                    self.you)
                if (self.diff>0):
                    lead.SetTarget(self.you)
                    VS.IOmessage (0,lead.getName(),"all","You don't have the agreed money... prepare to DIE!")
                else:
                    VS.IOmessage (0,lead.getName(),"all","You don't have the money. A fool like you won't last long!")

    def Execute (self):
        if (self.adjsys.Execute()):
            self.GenerateWingmen()
            VS.terminateMission(1)

    def initbriefing(self):
        debug.info("init briefing")

    def loopbriefing(self):
        debug.info("loop briefing")
        Briefing.terminate()

    def endbriefing(self):
        debug.info("ending briefing")

