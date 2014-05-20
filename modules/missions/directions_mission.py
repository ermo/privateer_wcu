from go_somewhere_significant import *
from go_to_adjacent_systems import *
import Briefing
import Director
import VS
import faction_ships
import launch
import quest
import unit
import universe
import vsrandom


class go_none:
    def Execute(self):
        return 1
    def HaveArrived(self):
        return 1
    def SignificantUnit(self):
        debug.debug("return VS.getUnit(0)")
        return VS.getUnit(0);
    def __init__(self):
        pass

isambushrunning={}

class directions_mission (Director.Mission):
    def dir_privateSetupPlayer(self,cp):
        debug.info("setting up mission")
        debug.info("jumps:"+self.jumps)
        self.arrived=0
        self.wasnull=0
        self.you=VS.getPlayerX(cp)
        self.adjsys=go_to_adjacent_systems(self.you,0,self.jumps)
        self.adjsys.Print("You should start in the system named %s","Then jump to %s","Lastly, jump to %s, your final destination","cargo mission",1)

    def setupPlayer(self,cp):
        self.dir_privateSetupPlayer(cp)

    def __init__ (self,savevar,jumps=(),destination=''):
        Director.Mission.__init__(self);
        debug.info("Directions: Starting")
        global isambushrunning
        self.var=savevar
        self.savedCargo=self.getCargo(VS.getPlayer())
        debug.debug("self.savedCargo:"+self.savedCargo)
        if (self.var,self.savedCargo) in isambushrunning:
            #VS.terminateMission(0)
            debug.info("Directions: Stopping: directions already running! (before mission restore)")
        isambushrunning[(self.var,self.savedCargo)]=True
        self.jumps=jumps
        self.cp=VS.getCurrentPlayer()
        self.you=VS.Unit()
        self.base=VS.Unit()
        self.arrived=0
        self.destination=destination
        self.mplay="all"
        self.dir_privateSetupPlayer(self.cp)
        self.mplay=universe.getMessagePlayer(self.you)
        self.obj=0
        name = self.you.getName ()

    def takeCargoAndTerminate (self,you, remove=1):
        global isambushrunning
        if ((self.var,self.savedCargo) in isambushrunning):
            del isambushrunning[(self.var,self.savedCargo)]
        if self.var!='':
            quest.removeQuest(self.you.isPlayerStarship(),self.var,1)
        VS.terminateMission(1)
        return
        
    def findUnit(self, name):
        debug.debug("testun=VS.getUnit(0)")
        testun=VS.getUnit(0)
        itt=1
        while(not testun.isNull()):
            if testun.getName().lower()==name.lower() or testun.getFullname().lower()==name.lower():
                return testun
            debug.debug("testun=VS.getUnit(%d)" % (itt))
            testun=VS.getUnit(itt)
            itt+=1
        debug.debug("testun=VS.getUnit(0)")
        testun=VS.getUnit(0)
        while(not testun.isNull()):
            if testun.isDockableUnit():
                return testun
            debug.debug("testun=VS.getUnit(%d)" % (itt))
            testun=VS.getUnit(itt)
            itt+=1
        debug.debug("return VS.getUnit(0)")
        return VS.getUnit(0)

    def getCargo(self,un):
        lis=[]
        for i in range(un.numCargo()):
            if (un.GetCargoIndex(i).GetMissionFlag()):
                lis.append(un.GetCargoIndex(i).GetContent())
        return tuple(lis)

    def checkCargo(self,un):
        return not (quest.checkSaveValue(self.cp,self.var,0) or quest.checkSaveValue(self.cp,self.var,1) or quest.checkSaveValue(self.cp,self.var,-1) or self.getCargo(un)!=self.savedCargo)

    def Execute (self):
        if (VS.getPlayerX(self.cp).isNull()):
            self.wasnull=1
            return
        if (self.arrived and self.base.isNull()):
            return
        if (self.wasnull):
            debug.info("INEQUALITY")
            if (not self.checkCargo(VS.getPlayerX(self.cp))):
                self.takeCargoAndTerminate(self.you,1)
                return
            else:
                self.setupPlayer(self.cp)
        if (not self.you):
            return
        if (not self.adjsys.Execute()):
            return
        if (self.destination=='' and len(self.jumps)==0):
            return #obviously wrapper for ambush
        if (self.arrived):
            dis=self.you.getSignificantDistance(self.base)
            if (dis<200):
                VS.setCompleteness(self.obj,1)
            if (dis<50 or self.base.isDocked(self.you) or self.you.isDocked(self.base)):
                self.takeCargoAndTerminate(self.you,1)
                return
        else:
            self.arrived=1
            self.adjsys=go_none()
            self.base=self.findUnit(self.destination)
            self.obj=VS.addObjective("Deliver cargo to %s." % self.destination);
            VS.setOwner(self.obj,self.you)
            VS.setCompleteness(self.obj,0)






