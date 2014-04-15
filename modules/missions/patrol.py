from go_to_adjacent_systems import *
import Briefing
import Director
import VS
import debug
import faction_ships
import launch
import quest
import unit
import universe
import vsrandom


class patrol (Director.Mission):
    def __init__ (self, numsystemsaway, num_significants_to_patrol, scan_object_distance, creds, jumps=(), donevar='', scan_objects=None):
        Director.Mission.__init__(self)
        if scan_objects is None or type(scan_objects) != dict or len(scan_objects) == 0:
            scan_objects = None
        else:
            scan_objects.setdefault("exceptall", [])
            scan_objects.setdefault("except", [])
            scan_objects.setdefault("addall", [])
            scan_objects.setdefault("add", [])
        self.scan_objects = scan_objects #If not None, do not randomly select significants, instead select them from this dictionary.
        self.donevar=donevar
        self.jnum=0
        self.cred=creds
        self.patrolpoints = []
        self.objectives = []
        self.distance = scan_object_distance
        self.you = VS.getPlayer()
        self.quantity=num_significants_to_patrol
        name = self.you.getName ()
        self.mplay=universe.getMessagePlayer(self.you)
        VS.IOmessage (0,"patrol",self.mplay,"Greetings, %s. You must patrol a system for us :" % name)
        self.adjsys = go_to_adjacent_systems(self.you,numsystemsaway,jumps)
        self.adjsys.Print("From the %s system,","Carefully go to %s.","You should shortly arrive in the %s: patrol it.","patrol",1)

    def SuccessMission (self):
        self.you.addCredits (self.cred)
        if self.donevar!='':
            quest.removeQuest(self.you.isPlayerStarship(),self.donevar,1)
        VS.IOmessage (0,"computer",self.mplay,"[Computer] Transmitting Data..")
        VS.IOmessage (0,"patrol",self.mplay,"Thank you! Patrol Complete.")
        VS.IOmessage (0,"patrol",self.mplay,"We have credited your account.")
        VS.terminateMission(1)
    def FailMission (self):
        self.you.addCredits (self.cred)
        if self.donevar!='':
            quest.removeQuest(self.you.isPlayerStarship(),self.donevar,-1)
        VS.IOmessage (0,"patrol",self.mplay,"Mission a failure!")
        VS.terminateMission(0)

    def GeneratePatrolList (self):
        VS.IOmessage (0,"patrol",self.mplay,"You must get within %f klicks of:" % self.distance)
        scan_objects = self.scan_objects
        if True: # Bypass, because second option doesn't work yet :(
#       if scan_objects is None: # Randomly selects targets to scan
            count=self.quantity*2
            str=""
            while (self.quantity>0 and count > 0):
                count -= 1
                sig = unit.getSignificant (vsrandom.randrange (0,128),0,0)
                if (not sig.isNull()):
                    if (not (sig in self.patrolpoints)):
                        self.patrolpoints += [sig]
                        self.quantity = self.quantity-1
                        fac = sig.getFactionName()
                        nam = sig.getFullname ()
                        fg = sig.getFlightgroupName()
                        if (fac!="neutral"):
                            if (fg=="Base"):
                                obj=VS.addObjective("Scan %s %s"% (nam,sig.getName()))
                            else:
                                obj=VS.addObjective("Scan %s %s"% (nam,fg))
                            VS.IOmessage (0,"patrol",self.mplay,"%s owned %s " % (fac,nam))
                        else:
                            if (sig.isPlanet()):
                                nam =sig.getName ()
                                if (sig.isJumppoint()):
                                    obj=VS.addObjective("Scan Jumppoint %s" % nam)
                                else:
                                    obj=VS.addObjective("Scan %s" % nam)
                            else:
                                obj=VS.addObjective("Scan Natural Phenomenon: %s" % nam)
                            VS.IOmessage(0,"patrol",self.mplay,"The object %s " % nam)
                        VS.setOwner(int(obj),self.you)
                        VS.setCompleteness(int(obj),-1.0)
                        self.objectives+=[int(obj)]
    
            self.quantity=0
        elif self.quantity != 0: # Only pick some in-system targets as specified in scan_objects
            excepted = False
            toadd = False
            units_in_sys = VS.getUnitList()
            while (not units_in_sys.isDone()):
                un = units_in_sys.current()
                if un.isNull():
                    units_in_sys.advance()
                    continue
                uname = un.getFullname()
                ufac = un.getFactionName()
                ufg = un.getFlightgroupName()
                debug.info("Unit name:'" + uname + "' flightgroup:'" + ufg + "' faction:'" + ufac + "'")
                if uname in scan_objects["except"]: # Exclude those
                    excepted = True
                for obj in scan_objects["exceptall"]: # Exclude all of those
                    if excepted:
                        break
                    obj = obj.capitalize().replace("unit", "Unit").replace("ship", "Ship")
                    try: # Valid fonctions: isSignificant isAsteroid isJumppoint isPlanet isDockableUnit isStarShip isCapitalShip isSun
                        if eval("un.is" + obj + "()"):
                            excepted = True
                    except Exception, inst:
                        if obj == "Base" and ufg == "Base":
                            excepted = True
                        elif obj == "Nav" and uname.find("Nav") == 0:
                            excepted = True
                if excepted:
                    excepted = False
                    units_in_sys.advance()
                    continue
                if uname in scan_objects["add"]: # Add those
                    toadd = True
                for obj in scan_objects["addall"]: # Add all things of a certain kind
                    if toadd:
                        break
                    obj = obj.capitalize().replace("unit", "Unit").replace("ship", "Ship")
                    try: # Valid fonctions: isSignificant isAsteroid isJumppoint isPlanet isDockableUnit isStarShip isCapitalShip isSun
                        if eval("un.is" + obj + "()"):
                            toadd = True
                    except Exception, inst:
                        if obj == "Base" and ufg == "Base":
                            toadd = True
                        elif obj == "Nav" and uname.capitalize().find("Nav") == 0:
                            toadd = True
                if toadd:
                    toadd = False
                    self.patrolpoints += [un]
                    obj=VS.addObjective("Scan %s" % nam)
                    VS.IOmessage(0,"patrol",self.mplay,"The object %s " % nam)
                    VS.setOwner(int(obj),self.you)
                    VS.setCompleteness(int(obj),-1.0)
                    self.objectives+=[int(obj)]
                units_in_sys.advance()
            self.quantity=0
                    

    def DeletePatrolPoint (self,num,nam):
        VS.IOmessage (0,"patrol",self.mplay,"[Computer] %s scanned, data saved..."%nam)
        VS.setCompleteness(self.objectives[self.jnum],1.0)
        self.you.commAnimation("scan_complete.ani")
        del self.objectives[self.jnum]
        del self.patrolpoints[self.jnum]

    def FinishedPatrol (self):
        if (self.jnum<len(self.patrolpoints)):
            jpoint =self.patrolpoints[self.jnum]
            if (jpoint.isNull()):
                self.DeletePatrolPoint(self.jnum,"Debris")
            else:
                if (self.you.getSignificantDistance (jpoint)<self.distance):
                    self.DeletePatrolPoint(self.jnum,jpoint.getName())
                else:
                    self.jnum+=1
        else:
            self.jnum=0
        return (len(self.patrolpoints)==0)

    def Execute (self):
        if (self.you.isNull()):
            VS.terminateMission(0)
            return
        if (self.adjsys.Execute()):
            if (self.quantity>0):
                self.GeneratePatrolList ()
            else:
                if (self.FinishedPatrol()):
                    self.SuccessMission()

    def initbriefing(self):
        debug.info("init briefing")

    def loopbriefing(self):
        debug.info("loop briefing")
        Briefing.terminate();

    def endbriefing(self):
        debug.info("ending briefing")

def initrandom (minsysaway,maxsysaway,minsigtopatrol,maxsigtopatrol,mincred,maxcred):
    nsys = vsrandom.randrange (minsysaway, maxsysaway)
    nsig = vsrandom.randrange (minsigtopatrol, maxsigtopatrol)
    return patrol (nsys, nsig,vsrandom.randrange(100.0,300.0),(1+nsys*0.5)*nsig*vsrandom.randrange (mincred,maxcred))
