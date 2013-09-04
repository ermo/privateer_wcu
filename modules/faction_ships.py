from faction_ships_lists import *
import vsrandom
import VS

def Precache():
    pass
#Caching only seems to pointlessly make the main_menu freeze for a few seconds after it becomes visible, so disable it.
#   import VS
#   tmp=VS.vsConfig("graphics","precache","false")
#   if tmp=="true" or tmp=="True" or tmp=="TRUE" or tmp=="1":
#       i = 0
#       for s in fighters:
#           fac = factions[i]
#           VS.precacheUnit(s[0],fac) #Just cache the first ship of every faction
#           i+=1
#Caching all ships is too slow.
#       ships = set()
#       i = 0
#       for fs in allships:
#           ships.clear()
#           ships.update(fs) #Put the list in a set to remove duplicates
#           fac = factions[i]
#           for s in ships:
#               VS.precacheUnit(s,fac)
#           i+=1

def blankify(tup):
    ret=[]
    for i in tup:
        ret.append(i*.75)
    return tuple(ret)

for i in tuple(stattable.keys()):
    stattable[i+".blank"]=blankify(stattable[i])

def GetStats( name):
    try:
        return stattable[name]
    except:
        print 'cannot find '+name
        return(.5,.5,1,1,1)

capitols=capitals
capitaldict={}
for i in capitols:
    for j in i:
        capitaldict[j]=1
for i in capitols:
    for j in i:
        capitaldict[j+'.blank']=1

def isCapital(type):
    return type in capitaldict

basedict={}
for i in bases:
    for j in i:
        basedict[j]=1

def appendName(faction):
    from difficulty import usingDifficulty
    if(useBlank[faction]>vsrandom.random() and usingDifficulty()):
        return ".blank"
    else:
        return ""

def factionToInt(faction):
    try:
        return factiondict[faction]
    except:
        return 0
    return 0

def intToFaction(faction):
    return factions[faction]

def getMaxFactions():
    return len(factions)

def blankify(tup):
    ret=[]
    for i in tup:
        ret.append(i*.75)
    return tuple(ret)
for i in tuple(stattable.keys()):
        stattable[i+".blank"]=blankify(stattable[i])

# At least work out a system that returns stuff based on ship characteristics... seriously...
#SHIPNAME:(CHANCE_TO_HIT,CHANCE_TO_DODGE,DAMAGE,SHIELDS,ORDINANCE_DAMAGE),

def GetStats(name):
    try:
        return stattable[name]
    except:
        import VS
        shipclass = VS.LookupUnitStat(name,"default","Combat_Role")
        print 'cannot find '+name+' in stattable, using defaults for class ' + shipclass +' - fix faction_ships_lists.py'
        if((shipclass == "INTERCEPTOR") or (shipclass == "FIGHTER") or (shipclass == "SCAVENGER")):
             return(0.62,0.66,18,52.5,48)
        if(shipclass == "TROOP"):
             return(.5,.5,1,1,1)
        if(shipclass == "BOMBER"):
             return(0.44,0.48,95.8,80,148)
        if(shipclass == "MERCHANTMAN"):
             return(0.1,0.2,32.8,80,38)
        if(shipclass == "CAP_NOPHASE"):
             return(0.26,0.2,68.3,220,66)
        if(shipclass == "CAP_PHASE"):
             return(0.2,0.2,77.22,260,66)
        if(shipclass == "CARRIER"):
             return(0.26,0.2,68.3,320,66)
        if(shipclass == "BASE"):
             return(.5,0,600,6000,2)
        else:
             return(.5,.5,1,1,1)

capitols=capitals
capitaldict={}
for i in capitols:
    for j in i:
        capitaldict[j]=1
for i in capitols:
    for j in i:
        capitaldict[j+'.blank']=1

def isCapital(type):
    return type in capitaldict

basedict={}
for i in bases:
    for j in i:
        basedict[j]=1

# allows for deciding when to use blanks, e.g. for semimilitary factions, confed would have 0 and, say, militia may have 0.33

def appendName(faction):
    import vsrandom
    from difficulty import usingDifficulty
    if((useBlank[faction] >= vsrandom.random()) and usingDifficulty()):
        return ".blank"
    else:
        return ""

def factionToInt(faction):
    try:
        return factiondict[faction]
    except:
        return 0
    return 0

def intToFaction(faction):
    return factions[faction]

def getMaxFactions():
    return len(factions)

def get_X_of(mylist, index):
    x_list = mylist[index]
    import vsrandom
    newindex = vsrandom.randrange(0,len(x_list))
    return intToFaction(x_list[newindex])

def get_enemy_of(faction_name):
    return get_X_of(enemies, factionToInt(faction_name))

def get_insys_enemy_of(faction_name):
    return get_X_of(insysenemies, factionToInt(faction_name))

def get_friend_of(faction_name):
    return get_X_of(friendlies, factionToInt(faction_name))

def get_rabble_of(faction_name):
    return get_X_of(rabble, factionToInt(faction_name))

def get_guest_of(faction_name):
    try:
        shiptype = get_X_of(guests, factionToInt(faction_name))
    except:
        shiptype = get_X_of(friendlies, factionToInt(faction_name))
    return shiptype

def get_militaryally_of(faction_name):
    try:
        shiptype = get_X_of(militaryallies, factionToInt(faction_name))
    except:
        shiptype = get_X_of(friendlies, factionToInt(faction_name))
    return shiptype

def get_parentfaction_of(faction_name):
    try:
        factype = get_X_of(parentfaction, factionToInt(faction_name))
    except:
        factype = faction_name
    return factype

def get_militaryenemy_of(faction_name):
    try:
        shiptype = get_X_of(militaryenemies, factionToInt(faction_name))
    except:
        shiptype = get_X_of(enemies, factionToInt(faction_name))
    return shiptype

# Simple way to make sure that a ship is only spawned if it exists in units.csv
def getRandomShipType(ship_list):
    import vsrandom
    #print "fishingship"
    ffvalidate = ""
    while(ffvalidate == ""):
        index=vsrandom.randrange(0,len(ship_list))
        fishedship = ship_list[index]
        ffvalidate = str(VS.LookupUnitStat(fishedship,"default","Default_Speed_Governor"))
        if(ffvalidate == ""):
            print "Warning: Ship type "+str(fishedship)+" does not have a flight model!"
    #print "shipdata: "+str(fishedship) +" is "+str(ffvalidate)
    return fishedship
    
def getFigher(faction_name, fighter):
    fighterlist = fighters[faction_name]
    fighterlist = fighterlist[fighter]
    return fighterlist+appendName(faction_name)

def getRandomFighterInt(faction_name):
    return getRandomShipType(fighters[faction_name])+appendName(faction_name)

def getRandomEscorteeInt(faction_name):
    try:
        shiptype = getRandomShipType(escortableships[faction_name])+appendName(faction_name)
    except:
        shiptype = getRandomShipType(capitols[faction_name])+appendName(faction_name)
    return shiptype

def getNumCapitol(faction_name):
    return len(capitols[faction_name])

def getNumFighters(faction_name):
    lst = fighters[faction_name]
    return len(lst)

# note that getcapital never gets the append name, so NO capital ship blanks... good.

def getCapitol(faction_name, fighter):
    caplist = capitols[faction_name]
    caplist = caplist[fighter]
    return caplist

def getRandomCapitolInt(faction_name):
    lst = capitols[faction_name]
    return getRandomShipType(lst)

def getRandomBaseInt(faction_name):
    lst = bases[faction_name]
    return getRandomShipType(lst)

def getParentFactionInt(faction_name):
    lst = parentfaction[faction_name]
    return getRandomShipType(lst)

def getRandomFighter(faction):
    return getRandomFighterInt(factionToInt(faction))

def getParentFaction(faction):
    return getParentFactionInt(factionToInt(faction))

def getRandomCapitol(faction):
    return getRandomCapitolInt(factionToInt(faction))

def getRandomEscortee(faction):
    return getRandomEscorteeInt(factionToInt(faction))

launch_distance_factor=.03
max_radius=500
ProductionRateMult = 1
