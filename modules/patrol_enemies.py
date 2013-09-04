import patrol
class patrol_enemies(patrol.patrol):
    def __init__(self, numsystemsaway, num_points, distance, creds, jumps, donevar, minships, maxships, encounterprob, capshipprob, faction, forceattack, fgname="", scan_objects=None):
        patrol.patrol.__init__(self, numsystemsaway, num_points, distance, creds, jumps, donevar, scan_objects)
        self.minships=minships
        self.maxships=maxships
        self.encounterprob=encounterprob
        self.capshipprob=capshipprob
        self.faction=faction
        self.forceattack=forceattack
        self.fgname=fgname
    def Track(self,shiptype):
        pass
    def SuccessMission(self):
        patrol.patrol.SuccessMission(self)
    def DeletePatrolPoint(self,num,nam):
        import vsrandom
        if (vsrandom.random()<self.encounterprob):
            import faction_ships
            fac=self.faction
            if (type(fac) is list or type(fac) is tuple):
                fac = fac[vsrandom.randrange(0,len(fac))]
            dynfg=""
            import fg_util
            import VS
            allfg=fg_util.AllFGsInSystem(fac,VS.getSystemFile())
            if (len(allfg)):
                dynfg = allfg[vsrandom.randrange(0,len(allfg))]
            for i in range(vsrandom.randrange(self.minships,self.maxships+1)):
                import launch
                L=launch.Launch()
                if self.fgname=="":
                    fgname="Patrol"
                else:
                    fgname = self.fgname
                L.fg = fgname
                L.dynfg=dynfg
                if (vsrandom.random()<self.capshipprob):
                    L.type=faction_ships.getRandomCapitol(fac)
                else:
                    L.type=faction_ships.getRandomFighter(fac)
                L.ai="default"
                L.faction=fac
                L.num=1
                L.minradius=3000.0
                L.maxradius=4000.0
                if i == 0:
                    L.fgappend=""
                else:
                    L.fgappend="_"+str(i)
                try:
                    L.minradius*=faction_ships.launch_distance_factor
                    L.maxradius*=faction_ships.launch_distance_factor
                except:
                    pass
                if (self.patrolpoints[num]):
                    newun=L.launch(self.patrolpoints[num])
                    if (self.forceattack):
                        lead=newun.getFlightgroupLeader()
                        if (lead):
                            lead.SetTarget(self.you)
                        else:
                            newun.setFlightgroupLeader(newun)
                        newun.SetTarget(self.you)
                        newun.setFgDirective("A.")
                    self.Track(newun)
        patrol.patrol.DeletePatrolPoint(self,num,nam)
