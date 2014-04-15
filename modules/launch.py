import VS
import debug
import dj_lib
import ship_upgrades
import sys
import vsrandom
import unit
from difficulty import usingDifficulty


def launch (fgname, faction, type, ai, nr_ships, nr_waves, vec, logo='',useani=1):
    debug.debug("fgname: %s, faction %s" % (fgname, faction))
    debug.debug("type: %s" % (type))
    debug.debug("ai: %s, nr_ships: %d, nr_waves: %d" % (ai, nr_ships, nr_waves))
    debug.debug("vec: %s, logo: %s, useani: %d" % (vec, logo, useani))
    #debug.debug('log'+ str( logo) + ' useani '+ str(useani))
    use_diff = usingDifficulty()
#   if useani:
#       VS.playAnimation ("warp.ani",vec,300.0)
    if isinstance(type, list) or isinstance(type, tuple):
        debug.debug("inside isinstance conditional (type is list or tuple)")
        for t in type:
            if t.endswith(".blank"):
                isblank = True
                break
    else:
        isblank = type.endswith(".blank")
    debug.debug("isblank = %s" % (isblank))
    # originally, this was
    #   if (not diff or not isblank)
    # which effectively always ignored isblank, since diff is almost never false
    if (not isblank):
        debug.info("Launching non-blank ship(s)")
        ret = VS.launch (fgname,type,faction,"unit",ai,nr_ships,nr_waves,VS.SafeEntrancePoint (vec,40),logo)
        dj_lib.PlayMusik(0,dj_lib.HOSTILE_NEWLAUNCH_DISTANCE)
    else:  # only upgrade blank ships (for now)
        debug.info("Launching blank ship(s)")
        rsize=0.0
        diffic = VS.GetDifficulty()
        #debug.debug("VS.Unit #1")
        ret=VS.Unit()
        for i in range(nr_ships):
            mynew=VS.launch(fgname,type,faction,"unit",ai,1,nr_waves,VS.SafeEntrancePoint (vec,40),logo)
            if (i==0):
                ret = mynew
                rsize = mynew.rSize()*1.75
            debug.debug("upgradeUnit '%s' using difficulty %.2f ..." % (mynew.getName(), float(diffic)))
            ship_upgrades.upgradeUnit(mynew,diffic)
            debug.debug("'- Done upgrading unit '%s' using difficulty %.2f ..." % (mynew.getName(), float(diffic)))
            vec=(vec[0]-rsize,
                vec[1],#-rsize
                vec[2]-rsize)
    dj_lib.PlayMusik(0,dj_lib.HOSTILE_NEWLAUNCH_DISTANCE)
    return ret

def launch_waves_around_area(fgname,faction,type,ai,nr_ships,nr_waves,r1,r2,pos,logo='',useani=1):
    pos=((pos[0]+vsrandom.uniform(r1,r2)*vsrandom.randrange(-1,2,2)),
        (pos[1]+vsrandom.uniform(r1,r2)*vsrandom.randrange(-1,2,2)),
        (pos[2]+vsrandom.uniform(r1,r2)*vsrandom.randrange(-1,2,2)))
    return launch(fgname,faction,type,ai,nr_ships,nr_waves,pos,logo,useani)

def launch_wave_around_area(fgname,faction,type,ai,nr_ships,r1,r2,pos,logo='',useani=1):
    #debug.debug('logo:' + str(logo))
    return launch_waves_around_area (fgname,faction,type,ai,nr_ships,1,r1,r2,pos,logo,useani)

def launch_around_station(station_name,fgname,faction,type,ai,nr_ships,nr_waves,logo='',useani=1):
    station_unit=unit.getUnitByFgID(station_name)
    if(station_unit.isNull()):
        sys.stderr.write("launch.py:launch_around_station did not find unit %s\n" % (station_name))
        #debug.debug("VS.Unit() #2")
        return VS.Unit()
    station_pos=station_unit.Position()
    rsize=station_unit.rSize()
    launched =launch_waves_around_area(fgname,faction,type,ai,nr_ships,nr_waves,rsize,rsize*2.0,station_pos,logo,useani)
    return launched

launch_around_unit=launch_around_station

def launch_waves_in_area(fgname,faction,type,ai,nr_ships,nr_waves,radius,pos,logo='',useani=1):
    pos=(pos[0]+vsrandom.uniform((-radius)/2,radius/2.0),
        pos[1]+vsrandom.uniform((-radius)/2,radius/2.0),
        pos[2]+vsrandom.uniform((-radius)/2,radius/2.0))
    un = launch(fgname,faction,type,ai,nr_ships,nr_waves,pos,logo,useani)

def launch_wave_in_area(fgname,faction,type,ai,nr_ships,radius,pos,logo='',useani=1):
    launch_waves_in_area(fgname,faction,type,ai,nr_ships,1,radius,pos,logo,useani)

def launchShipsAtWaypoints(waypoints,faction,type,ainame,nr,logo='',useani=1):
    i=0
    for wp in waypoints:
        outstr="wp%d" % (i)
        launch(outstr,faction,type,ainame,nr,1,wp,logo,useani)
        i+=1

def launch_wave_around_unit (fgname, faction, type, ai, nr_ships, minradius, maxradius, my_unit,logo='',useani=1):
    import faction_ships
    myvec = (0,0,0)
    if (my_unit.isNull()):
        un=launch_wave_around_area (fgname,faction,type,ai,nr_ships,minradius,maxradius,myvec,logo,useani)
        return un
    myvec=my_unit.LocalPosition()
    debug.info("myvec: %s" % (str(myvec)))
    rsiz=my_unit.rSize()
    if (maxradius > faction_ships.max_radius):
        maxradius=faction_ships.max_radius
    if (minradius > faction_ships.max_radius):
        minradius=faction_ships.max_radius
    un=launch_wave_around_area (fgname,faction,type,ai,nr_ships,rsiz+minradius,rsiz+maxradius,myvec,logo,useani)
    return un

def launch_wave_around_significant (fgname,faction,type,ai,nr_ships,minradius, maxradius,significant_number,logo='',useani=1):
    significant_unit=unit.getSignificant(significant_number,0,0)
    if (significant_unit.isNull()):
        significant_unit = VS.getPlayer()
    launched = launch_wave_around_unit(fgname,faction,type,ai,nr_ships,minradius,maxradius,significant_unit,logo,useani)
    return launched


class Launch:
    def __init__ (self):
        self.fg='Shadow'
        self.dynfg=''
        self.type='nova'
        self.num=1
        self.minradius=100.0
        self.maxradius=200.0
        self.useani=1
        self.logo=''
        self.faction='neutral'
        self.ai='default'
        self.numwaves=1
        self._preprocess=0
        self._nr_ships=0
        self.pos=(0,0,0)
        self.fgappend=''
        self.forcetype=False;
        self.capitalp=0

    def Preprocess (self):
        debug.debug("Entering Preprocess()")
        self._preprocess=1
        self._dyn_nr_ships=[]
        self._nr_ships=self.num
        import faction_ships
        if self.dynfg != '':
            import fg_util
            tn=fg_util.ShipsInFG(self.dynfg,self.faction)
            debug.info('Dynamically launching from SaveString flightgroup '+self.dynfg + ' with ships: '+str(tn)+' faction '+ self.faction)
            knum=0
            if (tn!=[] and self.type!=''):
                for i in range (len(tn)):
                    if (tn[i][0]==self.type):
                        knum=tn[i][1]
                        if (knum>self.num):
                            knum=self.num
                        self._dyn_nr_ships=[(self.type,knum)]
                        del tn[i]
                        break
##          if (tn==[]):
##          print 'Dyn-Launch: tn==[]'
##          self.dynfg=''
            elif (tn==[]):
                debug.info("Dyn-Launch: tn=="+str(tn)+", dynfg=='"+str(self.dynfg)+"' getting random fighter")
                self.type=faction_ships.getRandomFighterInt(faction_ships.factionToInt(self.faction))
                self.fg = self.dynfg
                self.dynfg=''
            if self.forcetype and len(self._dyn_nr_ships)==0 and self.type!='':
                self._dyn_nr_ships=[(self.type,1)]
                knum=1
            for i in tn:
                if (knum>=self.num):
                    break
                if (self.capitalp or (not faction_ships.isCapital(i[0])) ):
                    if (i[1]>self.num-knum):
                        i = (i[0],self.num-knum)
                    self._dyn_nr_ships+=[i]
                    knum+=i[1]
            self._nr_ships=self.num-knum

    def launch(self,myunit):
        self.Preprocess()
        if (self.dynfg != ''):
            debug.info('dynamic launch')
            if (self._nr_ships>0):
                if (not myunit):
                    debug.info('launch area')
                    lame= launch_wave_around_area (self.dynfg+self.fgappend, self.faction, self.type, self.ai, self._nr_ships, self.minradius, self.maxradius, self.pos, self.logo, self.useani)
                else:
                    debug.info('launch more ships')
                    lame= launch_wave_around_unit (self.dynfg+self.fgappend, self.faction, self.type, self.ai, self._nr_ships, self.minradius, self.maxradius, myunit, self.logo, self.useani)
            import launch_recycle
            ret= launch_recycle.launch_types_around (self.dynfg, self.faction, self._dyn_nr_ships, self.ai, self.minradius*.5+self.maxradius*.5, myunit, 100000+self.maxradius, self.logo, self.fgappend)
            if (len(self._dyn_nr_ships) or self._nr_ships==0):
                return ret
            else:
                return lame
        else:
            if ((not myunit) and self._nr_ships>0):
                debug.info('launch area')
                return launch_wave_around_area (self.fg+self.fgappend, self.faction, self.type, self.ai, self._nr_ships, self.minradius, self.maxradius, self.pos, self.logo, self.useani)
            elif (self._nr_ships>0):
                debug.info('launch more ships')
                return launch_wave_around_unit (self.fg+self.fgappend, self.faction, self.type, self.ai, self._nr_ships, self.minradius, self.maxradius, myunit, self.logo, self.useani)
            else:
                debug.info('zero or negative number of ships, launching one')
                return launch_wave_around_unit (self.fg+self.fgappend, self.faction, self.type, self.ai, 1, self.minradius, self.maxradius, myunit, self.logo, self.useani)
        return un
