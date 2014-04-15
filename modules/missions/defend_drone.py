from go_to_adjacent_systems import go_to_adjacent_systems
from go_somewhere_significant import go_somewhere_significant
import Director
import Briefing
import Vector
import VS
import faction_ships
import launch
import quest
import quest_drone
import universe
import unit
import vsrandom


class defend_drone (Director.Mission):
    def SetVar (self,val):
        if (self.var_to_set!=''):
            quest.removeQuest (self.you.isPlayerStarship(),self.var_to_set,val)

    def __init__ (self,helpship,helpfac,helpsystem,attackship,attackfac,numgood,goodfac,jumps,var_to_set='',helptext=[]):
        Director.Mission.__init__ (self)
        self.firsttime=VS.GetGameTime()
        self.lastjump="Gemini/Blockade_Point_Tango"
        if (jumps):
            if (len(jumps)):
                self.lastjump=jumps[-1]
        self.jumpingtime=VS.GetGameTime()
        self.newshiphelp=helpship
        self.newshipattack=attackship
        self.newshipgood=''
        self.mplay="all"
        self.var_to_set = var_to_set
        self.istarget=0
        self.obj=0
        self.curiter=0
        self.arrived=0
        self.helpfaction = helpfac
        self.helpsystem = helpsystem
        self.goodfaction = goodfac
        self.attackfaction = attackfac
        self.numgood=numgood
        self.runaway=False
        self.greetingText=helptext
        self.cred=0
        mysys=VS.getSystemFile()
        sysfile = VS.getSystemFile()
        self.you=VS.getPlayer()
        self.enemy=VS.Unit()
        self.helperpos=(0,0,0)
        self.helper=VS.Unit()
        self.adjsys=go_to_adjacent_systems (self.you,0,jumps)
        self.mplay=universe.getMessagePlayer(self.you)
        self.displayLocation=True
        if (self.you):
            VS.IOmessage (0,"defend mission",self.mplay,"[Computer] Defend Mission Objective: (%.2f Credits)" % self.cred)
            self.adjsys.Print("From %s system","Procede to %s","Search for target at %s, your final destination","defend mission",1)
            VS.IOmessage (1,"defend mission",self.mplay,"Target is a %s unit." % (self.attackfaction))
        else:
            debug.info("aborting defend_drone constructor...")
            VS.terminateMission (0)

    def AdjLocation(self):
        debug.info("ADJUSTING LOC")
        quest_drone.drone.SetPosition(Vector.Add(quest_drone.drone.LocalPosition(),Vector.Scale(quest_drone.drone.GetVelocity(),-40)))     #eta 20 sec

    def Win (self,un,terminate):
        self.SetVar(1)
        quest.removeQuest(self.you.isPlayerStarship(),"quest_drone")
        VS.IOmessage (0,"defend mission",self.mplay,"[Computer] #00ff00Defend Mission Accomplished!")
        un.addCredits(self.cred)
        if (terminate):
            debug.info("you win defend mission!")
            VS.terminateMission(1)

    def Lose (self,terminate):
        VS.IOmessage(0,"defend mission",self.mplay,"[Computer] #ff0000Defend Mission Failed.")
        self.SetVar(-1)
        if (terminate):
            debug.info("lose defend mission")
            VS.terminateMission(0)

    def Execute (self):
        isSig=0
        if (self.you.isNull()):
            self.Lose (1)
            return
        if (self.arrived==3):
            if (not self.runaway):
                if (not self.istarget):
                    quest_drone.drone.SetTarget(self.you)
            if quest_drone.drone:
                pos=quest_drone.drone.LocalPosition()
                yourpos=self.you.LocalPosition()
                if pos[0]<yourpos[0]-10000 or pos[0]>yourpos[0]+10000 or pos[1]<yourpos[1]-10000 or pos[1]>yourpos[1]+10000 or pos[2]<yourpos[2]-10000 or pos[2]>yourpos[2]+10000:
                    quest_drone.drone.SetPosition((yourpos[0]-1000,yourpos[1]-4000,yourpos[2]+1000))
            else:
                self.Win(self.you,1)
                return
        elif (self.arrived==2):
            #significant=self.adjsys.SignificantUnit()
            #if (significant.isNull ()):
            #    debug.debug("sig null")
            #    VS.terminateMission(0)
            #    return
            if (1):
                if (1):
                    newshipgood="broadsword"#faction_ships.getRandomFighter(self.goodfaction)
                    #quest_drone.drone=launch.launch_wave_around_unit("Shadow",self.faction,self.newship,"default",4,3000.0,4000.0,significant)
                    L = launch.Launch()
                    L.fg="AlphaPrime"
                    L.dynfg=''
                    L.type = newshipgood
                    L.faction = self.goodfaction
                    L.ai = "default"
                    L.num=4
                    L.minradius=5000.0
                    L.maxradius = 6000.0
                    try:
                        L.minradius*=faction_ships.launch_distance_factor
                        L.maxradius*=faction_ships.launch_distance_factor
                    except:
                        pass
                    goodguysC=L.launch(self.you)
                    L.num=1
                    L.type=faction_ships.getRandomCapitol(self.goodfaction);
                    goodguysA=L.launch(self.you)
                    if not quest_drone.drone:
                            L = launch.Launch()
                            L.fg="Shadow"
                            L.dynfg=''
                            L.type = self.newshipattack
                            L.faction = self.attackfaction
                            L.ai = "default"
                            L.num=1
                            L.minradius=15000.0
                            L.maxradius = 15000.0
                            try:
                                L.minradius*=faction_ships.launch_distance_factor
                                L.maxradius*=faction_ships.launch_distance_factor
                            except:
                                pass
                            quest_drone.drone=L.launch(self.you)
                    if quest_drone.drone.getUnitSystemFile()!=VS.getSystemFile():
                        quest_drone.drone.JumpTo(VS.getSystemFile())
                    goodguysC.SetTarget(quest_drone.drone)
                    goodguysA.SetTarget(quest_drone.drone)
                    self.you.SetTarget(quest_drone.drone)
                    self.obj=VS.addObjective("Destroy the %s ship." % (quest_drone.drone.getName ()))
                    if (quest_drone.drone):
                        self.arrived=3
                    else:
                        debug.info("enemy null")
                        VS.terminateMission(0)
                        return
                    #quest_drone.drone.SetHull(40.0)
        elif self.arrived==1:
            if VS.getSystemFile()==self.helpsystem:
                if (VS.GetGameTime()-self.jumpingtime>78):
                    self.you.JumpTo(self.lastjump)
                    self.jumpingtime=VS.GetGameTime()+10000000.
                elif self.helper:
                    self.helper.DeactivateJumpDrive()
                    self.helper.SetTarget(VS.Unit())
                    #self.helper.SetVelocity( (0,0,0) )
                    #self.helper.SetPosition( self.helperpos )
            if (self.adjsys.Execute()):
                self.arrived=2
                if (self.newshipattack==""):
                    self.newshipattack=faction_ships.getRandomFighter(self.attackfaction)
                #self.adjsys=go_somewhere_significant(self.you,0,10000.0,0,'','',self.displayLocation)
                #localdestination=self.adjsys.SignificantUnit().getName()
                tmpfg="shadow"
                #VS.IOmessage (3,"defend mission",self.mplay,"Hunt the %s unit in the %s flightgroup in this system." % (self.newshipattack,tmpfg))
                #if (self.runaway):        #ADD OTHER JUMPING IF STATEMENT CODE HERE
                #    VS.IOmessage (4,"defend mission",self.mplay,"Target is fleeing to the jump point!")
                #    VS.IOmessage (5,"defend mission",self.mplay,"Target Destination appears to be %s" % (localdestination))
                VS.IOmessage (1,"Admiral Reismann",self.mplay,"You're just in time for the massacre!")
                VS.IOmessage (5,"Admiral Reismann",self.mplay,"Cut the chatter and listen: This is Admiral Reismann. We'll hit the thing as soon as it arrives. Hold your position until it does. And, uh, feel free to join in. Reismann out.")
                VS.playSound("campaign/Reismann.wav",(0.,0.,0.),(0.,0.,0.))
        else:
            if VS.getSystemFile()==self.helpsystem:
                    debug.info("Launching helper ship!")
                    if (self.newshiphelp==""):
                        self.newshiphelp=faction_ships.getRandomFighter(self.helpfaction)
                    L = launch.Launch()
                    L.fg="Unknown"
                    L.dynfg=''
                    L.type = self.newshiphelp
                    L.faction = self.helpfaction
                    L.ai = "default"
                    L.num=1
                    L.minradius=1500.0
                    L.maxradius = 1600.0
                    try:
                        L.minradius*=faction_ships.launch_distance_factor
                        L.maxradius*=faction_ships.launch_distance_factor
                    except:
                        pass
                    self.helper=L.launch(self.you)
                    self.helperpos=self.helper.Position()
                    self.you.SetTarget(self.helper)
                    universe.greet(self.greetingText,self.helper,self.you)
                    whichmount=self.you.removeWeapon("Steltek",0,True)
                    if (whichmount!=-1):
                        self.you.upgrade('steltek_gun_boosted',whichmount,whichmount,True,True)
                    self.jumpingtime=VS.GetGameTime()                
                    self.arrived=1

    def initbriefing(self):
        debug.info("init briefing")

    def loopbriefing(self):
        debug.info("loop briefing")
        Briefing.terminate();

    def endbriefing(self):
        debug.info("ending briefing")
