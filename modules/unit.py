import VS
import debug
import vsrandom


def isLandable (un):
    debug.debug("isLandable")
    if (un):
        me = VS.getPlayer()
        if (not me.isNull()):
            if (un == me):
                return 0
    return un.isDockableUnit()

def isBase (un):
    debug.debug("isBase")
    unit_fgid = un.getFlightgroupName()
    retval = unit_fgid=="Base"
    return retval and not un.isSun()

def findPlayerNum (un):
    debug.debug("findPlayerNum")
    for i in range (VS.getNumPlayers()):
        if (VS.getPlayerX(i)==VS.getPlayer()):
            return i
    return 0

def isAsteroid (un):
    debug.debug("isAsteroid")
    unit_fgid = un.getFlightgroupName()
    retval = unit_fgid=="Asteroid"
    return retval

def getUnitFullName(un):
    debug.debug("getUnitFullName")
    thename = un.getName()
    fg = un.getFlightgroupName()
    if fg == 'Base':
        thename = un.getFullname()+' '+thename.replace('_',' ')
    elif fg != 'Shadow' and fg != '':
        thename = thename+' in the '+fg+' flightgroup'
    return thename

def getSignificant (whichsignificant, landable_only, capship_only):
    debug.debug("getSignificant")
    which=0
    signum=0
    rez = []
    debug.debug("un=VS.getUnit(0)")
    un=VS.getUnit(0)
    #debug.debug("is this null "+str(un.isNull()))
    while (not un.isNull()):
        #debug.debug("is this null "+str(un.isNull()))
        debug.debug("un=VS.getUnit(%d)" % (which))
        un=VS.getUnit(which)
        if (un.isNull()):
            which=0
            if (signum==0):
                signum=whichsignificant+1
        else:
            #debug.debug("checking "+un.getName())
            if ((landable_only) or (capship_only)):
                if(capship_only):
                    if (isBase (un)):
                        signum=signum+1
                        rez.append(un)
                else:
                    if (isLandable (un)):
                        signum=signum+1
                        rez.append(un)
                    else:
                        debug.info("not landable "+un.getName()+" fg "+un.getFlightgroupName())
            else:
                if (un.isSignificant()):
                    signum=signum+1
                    rez.append(un)
            which=which+1
    if (len(rez)==0):
        if (capship_only):
            return getSignificant(whichsignificant,landable_only,0)
        elif(landable_only):
            return getSignificant(whichsignificant,0,0)
        else:
            debug.warning("fatal error, no significants in system "+VS.getSystemFile())
            return VS.getPlayer()
    return rez[vsrandom.randrange(0,len(rez))]

  #this one terminates if fewer than so many planets exist with null

def inSystem(unit):
    debug.debug("inSystem")
    debug.debug("i = VS.getUnitList ()")
    i = VS.getUnitList ()
    while (not i.isDone()):
        #debug.debug("i.next()")
        un = next(i)
        if (not un.isNull() and un == unit):
            return 1
    return 0

def getPlanet (whichsignificant, sig):
    debug.debug("getPlanet(whichsignificant=%d, sig=%d)" % (whichsignificant, sig))
    i = VS.getUnitList()
    unit = VS.Unit()
    if not i.isDone():
        if sig:
            i.advanceNSignificant(whichsignificant)
        else:
            i.advanceNPlanet(whichsignificant)
        unit = i.current()
    debug.debug("return unit=%s" % (str(unit)))
    return unit

def getPlanet_obsolete(whichsignificant, sig):
    debug.debug("getPlanet(whichsignificant=%d, sig=%d)" % (whichsignificant, sig))
    signum = 0
    i = VS.getUnitList()
    #debug.debug("VS.Unit() #1")
    un = VS.Unit()
    #un = None
    while (signum <= whichsignificant):
        debug.debug("(signum=%d <= whichsignificant=%d)?" % (signum, whichsignificant))
        if i.isDone():
            debug.debug("break")
            break
        #debug.debug("i.next() #2")
        un = next(i)
        #if (not un.isNull()):
        if (not un.isNull()):
            debug.debug("if (un=%s) evaluated to True" % (un))
            if(sig):
                if un.isSignificant():
                    debug.debug("un.isSignificant()")
                    signum = signum + 1
            else:
                if un.isPlanet():
                    debug.debug("un.isPlanet()")
                    signum = signum + 1
    debug.debug("un=%s" % (un))
    return un

def getJumpPoint(whichsignificant):
    debug.debug("getJumpPoint")
    #debug.debug("VS.Unit() #2")
    un=VS.Unit()
    which=0
    signum=0
    while (signum<whichsignificant):
        debug.debug("un=VS.getUnit(%d)" % (which))
        un=VS.getUnit(which)
        #if (not un.isNull()):
        if (un):
            debug.debug("if (un=%s) evaulated to True" % (un))
            if (un.isJumppoint()):
                signum=signum+1
            which=which+1
        else:
            which=0
            if (signum==0):
                un.setNull()
                signum=whichsignificant
    return un

def obsolete_getNearestEnemy(my_unit,range):
    ship_nr=0
    min_dist=9999999.0
    #debug.debug("VS.Unit() #3")
    min_enemy=VS.Unit()
    debug.debug("VS.getUnit(%d)" % (ship_nr))
    unit=VS.getUnit(ship_nr)
    while(not unit.isNull()):
        unit_pos=un.getPosition()
        dist=my_unit.getMinDis(unit_pos)
        relation=my_unit.getRelation(unit)
        if(relation<0.0):
            if((my_unit==unit) and (dist<range) and (dist<min_dist)):
                min_dist=dist
                min_enemy=unit
        ship_nr=ship_nr+1
        debug.debug("VS.getUnit(%d)" % (ship_nr))
        unit=VS.getUnit(ship_nr)
    if(min_enemy):
        other_fgid=min_enemy.getFgID()
    return min_enemy


def obsolete_getThreatOrEnemyInRange(un,range):
    threat=un.getThreat()
    if(threat.isNull()):
        threat=obsolete_getNearestEnemy(un,range)
    return threat

def setPreciseTargetShip (which_fgid, target_unit):
    debug.debug("setPreciseTargetShip")
    ship_nr=0
    debug.debug("VS.getUnit(%d)" % (ship_nr))
    un=VS.getUnit(ship_nr)
    if (target_unit):
        while(un.isNull()):
            unit_fgid=un.getFgID()
            if(unit_fgid[:len(which_fgid)]==which_fgid):
                un.SetTarget(target_unit)
            ship_nr=ship_nr+1
            debug.debug("un=VS.getUnit(%d)" % (ship_nr))
            un=VS.getUnit(ship_nr)

def getMinDistFrom(sig1,siglist=None):
    debug.debug("getMinDistFrom(sig1=%s,siglist=%s)" % (sig1, siglist))
    siglist=siglist or getPlanetList(0)
    mindist=100000000000000000000000000000000000000000000.0
    for sig2 in siglist:
        tempdist = sig1.getSignificantDistance(sig2)
        if (tempdist<mindist and tempdist>0.0):
            mindist=tempdist
    return mindist

def obsolete_getMinDistFrom(sig1):
    debug.debug("getMinDistFrom(sig1=%s)" % (sig1))
    debug.debug("sig2=getPlanet(0,0)")
    sig2=getPlanet (0,0)
    debug.debug("sig2=%s" % (sig2))
    mindist=100000000000000000000000000000000000000000000.0
    i=0
    while (sig2):
        debug.debug("while (sig2=%s) evaluated to True" % (str(sig2)))
        tempdist = sig1.getSignificantDistance(sig2)
        if (tempdist<mindist and tempdist>0.0):
            mindist=tempdist
        i+=1
        debug.debug("sig2=getPlanet(i=%d, 0)" % (i))
        sig2 = getPlanet (i,0)
        debug.debug("getPlanet (i,0)")
    return mindist

def minimumSigDistApart():
    debug.debug("minimumSigDistApart")
    debug.debug("calling sig1=getPlanet (0,0)")
    sig1=getPlanet (0,0)
    debug.debug("sig1 = %s" % (str(sig1)))
    i=0
    mindist=100000000000000000000000000000000000000000000.0
    ave=0.0
    while (sig1):
        tempdist = getMinDistFrom (sig1)
        if (ave<0.9):
            mindist = tempdist
        else:
            mindist += tempdist
        ave+=1.0
        i+=1
        sig1 = getPlanet (i,0)
    if (ave!=0.0):
        mindist = mindist/ave
    return mindist

def getUnitByName (name):
    debug.debug("getUnitByName")
    ship_nr=0
    debug.debug("unit = VS.getUnit(0)")
    unit = VS.getUnit(0)
    while (not unit.isNull()):
        if (unit.getName()==name):
            return unit
        ship_nr+=1
        debug.debug("unit = VS.getUnit(%d)" % (ship_nr))
        unit=VS.getUnit(ship_nr)
    return unit

def getUnitByFgIDFromNumber(fgid, ship_nr):
    debug.debug("getUnitByFgIDFromNumber")
    debug.debug("unit=VS.getUnit(%d)" % (ship_nr))
    unit=VS.getUnit(ship_nr)
    #debug.debug("VS.Unit() #4")
    found_unit=VS.Unit()
    while(not unit.isNull() and not found_unit):
        unit_fgid=unit.getFgID()
        if(unit_fgid==fgid):
            found_unit=unit
        ship_nr=ship_nr+1
        debug.debug("unit=VS.getUnit(%d)" % (ship_nr))
        unit=VS.getUnit(ship_nr)
    return found_unit

def getUnitByFgID(fgid):
    debug.debug("getUnitByFgID")
    return getUnitByFgIDFromNumber(fgid,0)

def setTargetShip(which_fgid,target_fgid):
    target_unit=getUnitByFgID(target_fgid)
    setPreciseTargetShip(which_fgid,target_unit)

def removeFg(which_fgid):
    debug.debug("removeFg")
    ship_nr=0
    debug.debug("un=VS.getUnit(%d)" % (ship_nr))
    un=VS.getUnit(ship_nr)
    while(not un.isNull()):
        unit_fgid=un.getFgID()
        if(unit_fgid[:len(which_fgid)]==which_fgid):
            un.Kill()
        else:
            ship_nr=ship_nr+1
        debug.debug("un=VS.getUnit(%d)" % (ship_nr))
        un=VS.getUnit(ship_nr)

# A collection of functions useful for dealing with flightgroup tuples.
# Added as used.
# For more information on the types of variables used,
# see the VS python doc in the manual.

def TfgCloak(state,tup):
    """ Cloaks or uncloaks (1 or 0) a flightgroup tuple (tup). """
    debug.debug("TfgCloak")
    num = len(tup)
    for i in range(num):
        tup[i].Cloak(state)
        num = num + 1

def TfgisNull(tup):
    """ Tells us if a tup is null """
    debug.debug("TfgisNull")
    num = 0
    for i in tup:
        if (i):
            num = num + 1
    if num == 0:
        return 1
    else:
        return 0

def TfgHeadCount(tup):
    """ Returns an integer value of the number of ships in the tup.

        Not sure if it takes notice of null state.
    """
    debug.debug("TfgHeadCount")
    num = 0
    for i in tup:
        if (i):
            num = num + 1
    return num

def setTfgDirective(tup,tgt,dir):
    """ Sets a whole tupled flightgroup on a target. """
    debug.debug("setTfgDirective")
    num = len(tup)
    for i in range(num):
        tup[i].SetTarget(tgt)
        tup[i].setFgDirective(dir)

def TfgJumpTo(tup,system):
    """ Jumps a whole fg tuple using the JumpTo command. """
    debug.debug("TfgJumpTo")
    num = len(tup)
    for i in range(num):
        tup[i].JumpTo(system)
