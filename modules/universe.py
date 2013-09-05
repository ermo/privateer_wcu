##import ai_flyto_jumppoint
##current_system=""
##last_system=""
##old_system=""
##system_map={}
##outstr=""

import VS
import vsrandom
import faction_ships
import Director
import launch
def catInCatList (cat,catlist):
    for i in catlist:
        loc =cat.find (i)
        if (loc==0):
            return 1
        return 0

def adjustUnitCargo(un,cat,pr,qr):
    numcargo = un.numCargo()
    carglist =[]
    for i in range(numcargo):
        carg = un.GetCargoIndex(i)
        if (len(cat)==0 or catInCatList(carg.GetCategory(),cat)):
            carg.SetPrice (pr*carg.GetPrice())
            carg.SetQuantity (int(qr*carg.GetQuantity()))
        carglist += [carg]
    for i in range (numcargo):
        un.removeCargo (carglist[i].GetCategory(),carglist[i].GetQuantity(),1)
    for i in range (numcargo):
        un.addCargo(carglist[i])
    carglist=0
#universe.systemCargoDemand (("Natural_Products","starships",),.0001,1000)
def systemCargoDemand (category,priceratio,quantratio,ships=1,planets=1):
    i = VS.getUnitList()
    un = i.current()
    while (not un.isNull()):
        if (un.isPlayerStarship()==-1):
            isplanet = un.isPlanet()
            if ( (isplanet and planets) or ((not isplanet) and ships)):
                adjustUnitCargo(un,category,priceratio,quantratio)
        i.advance()
        un=i.current()

def setFirstSaveData(player,key,val):
    mylen = Director.getSaveDataLength(player,key)
    if (mylen>0):
        Director.putSaveData(player,key,0,val)
    else:
        Director.pushSaveData(player,key,val)

def getAdjacentSystems (currentsystem, sysaway, jumps=(),preferredfaction=''):
    """returns a tuple in the format ("[lastsystem]",(system1,system2,system3,...))"""
    if preferredfaction=='':
        preferredfaction=VS.GetGalaxyProperty(currentsystem,"faction")
    max=VS.GetNumAdjacentSystems(currentsystem)
    if ((sysaway<=0) or (max<=0)):
#       _io.message (1,"game","all","Your final destination is %s" % (currentsystem))
        return (currentsystem,jumps)
    else:
        syslist=[]
        numadj=VS.GetNumAdjacentSystems(currentsystem)
        for i in range(numadj):
            cursys=VS.GetAdjacentSystem(currentsystem,i)
            if preferredfaction!=None:
                if VS.GetGalaxyProperty(cursys,"faction")!=preferredfaction:
                    continue
            if ((cursys in jumps) or (cursys == VS.getSystemFile())):
                continue
            syslist.append(cursys)
        if not len(syslist):
            return getAdjacentSystems(currentsystem,0,jumps)
        nextsystem=syslist[vsrandom.randrange(0,len(syslist))]
#       _io.message (1,"game","all","Jump from %s to %s." % (currentsystem,nextsystem))
        return getAdjacentSystems(nextsystem,sysaway-1,jumps+(nextsystem,))

#def getAdjacentSystems (currentsystem, num_systems_away):
# return nearsys (currentsystem,num_systems_away,())

def getAdjacentSystemList (tothissystem):
    list=[]
    max=VS.GetNumAdjacentSystems(tothissystem);
    for i in range(max):
        list.append(VS.GetAdjacentSystem(tothissystem,i))
    return list

def getRandomJumppoint():
    jp_list=getJumppointList()
    size=len(jp_list)
    if (size>0):
        return jp_list[vsrandom.randrange(0,size)]
    else:
        return VS.Unit()

def getJumppointList():
    jp_list=()
    ship_nr=0
    uni=VS.getUnit(0)
    while(uni):
        if(uni.isJumppoint()):
            jp_list+=(uni,)
        ship_nr+=1
        uni=VS.getUnit(ship_nr)
    return jp_list

def getMessagePlayer(un):
    num=un.isPlayerStarship()
    if (num<0):
        return "all"
    else:
        return "p"+str(num)

def punish (you,faction,difficulty):
    VS.AdjustRelation(you.getFactionName(),faction,difficulty*-.01,1)
    if (difficulty>=2):
        VS.IOmessage (0,"mission",getMessagePlayer(you),"#ff0000Your idiocy will be punished.")
        VS.IOmessage (0,"mission",getMessagePlayer(you),"#ff0000You had better run for what little life you have left.")
        for i in range(difficulty):
            un=faction_ships.getRandomFighter(faction)
            newunit=launch.launch_wave_around_unit("shadow", faction, un, "default", 1, 200.0,400.0,you)
            newunit.setFgDirective("B")
            newunit.SetTarget(you)

def _tmpint(str,default):
    try:
        return int(str)
    except:
        return default

def significantUnits():
    uni = VS.getUnitList()
    un = uni.current()
    ret = []
    while (not uni.isDone()):
        if (un):
            if (un.isSignificant()):
                ret += [un]
        un = uni.next()
    return ret

def GetNumSignificantsForSystem (cursys):
    numjmp=VS.GetNumAdjacentSystems(cursys)
    return _tmpint(VS.GetGalaxyProperty(cursys,"num_planets"),3)+_tmpint(VS.GetGalaxyProperty(cursys,"num_moons"),4)+_tmpint(VS.GetGalaxyProperty(cursys,"num_gas_giants"),2)+_tmpint(VS.GetGalaxyProperty(cursys,"num_starbases"),1)+numjmp
#use go_somewhere_significant instead:
##def __init__(): #(?)
##  outstr=_string.new()
##  current_system=_std.GetSystemName()
##  last_system=_std.GetSystemName()
##  old_system=_std.GetSystemName()
##  system_map=_omap.new()
##  _omap.set(system_map,current_system,current_system)
##
##def Execute():
##  jumped=false
##  current_system=_std.GetSystemName()
##  if(current_system!=last_system):
##      // we have jumped
##      _io.sprintf(outstr,"jumped from %s to %s",last_system,current_system)
##      _io.message(0,"game","all",outstr)
##      old_system=last_system
##      last_system=_std.GetSystemName()
##      jumped=true
##  return jumped

def greet(greetingText, enemy=None, you=None, friendly=None):
    enemycolor = "#EF2929"
    playercolor = "#729FCF"
    friendlycolor = "#73D216"
    if type(enemy) == str and enemy != "":
        enemyname = enemy
    elif (enemy): # enemy.getName() is the ship type
        enemyname = enemy.getFlightgroupName()+"#000000"
    else:
        enemyname = "[Unidentified]"
    if type(you) == str and you != "":
        playername = you
    elif (you): # getMessagePlayer(you) gives p0 for first player
        playername = you.getFlightgroupName() #Player flightgroup is the name, e.g. Burrows
    else:
        playername = "all"
    if type(friendly) == str and friendly != "":
        friendlyname = friendly
    elif (friendly):
        friendlyname = friendly.getFlightgroupName()+"#000000"
    else:
        friendlyname = "[Unidentified]"
    for i in range(len(greetingText)):
        isfromplayer = False
        isfriendly = False
        fromname = ""
        toname = ""
        text=greetingText[i]
        if type(text)==tuple or type(text)==list:
            if len(text) == 0:
                continue
            if len(text)>1:
                isfromplayer = text[1]
            if len(text)>2 and text[2]:
                VS.playSound(text[2],(0.,0.,0.),(0.,0.,0.))
            if len(text)>3:
                isfriendly = text[3]
            text=text[0]
        elif type(text)==dict:
            isfromplayer = text.get("isfromplayer", isfromplayer)
            isfriendly = text.get("isfriendly", isfriendly)
            if "sound" in text:
                VS.playSound(text["sound"],(0.,0.,0.),(0.,0.,0.))
            text=text.get("text", "")
        if type(text) != str or text == "": # If it's not text at this point or empty, put default text.
            text = "(garbled)"
        # Todo: It would be nice to dynamically change the color based on relations with ship. To do after making it possible to have friendly time with ships before they attack.
        if isfromplayer: # from player
            fromcolor = playercolor
            fromname = playername
            if isfriendly: # to friendly
                tocolor = friendlycolor
                toname = friendlyname
            else: # to enemy
                tocolor = enemycolor
                toname = enemyname
        else: # to player
            tocolor = playercolor
            if isfriendly: # from friendly
                fromcolor = friendlycolor
                fromname = friendlyname
            else: # from enemy
                fromcolor = enemycolor
                fromname = enemyname
            toname = playername
        VS.IOmessage (8+i*4,fromcolor+fromname,tocolor+toname,fromcolor+text+"#000000")

def getDockedBase():
    uni = VS.getUnitList()
    while (not uni.isDone()):
        if VS.getPlayer().isDocked(uni.current()) or uni.current().isDocked(VS.getPlayer()):
            return uni.current()
        uni.advance()
    return uni.current()

def getDockedBaseName():
    un = getDockedBase()
    if (un):
        return (un.getName(),un.getFullname())
    return ('','')


def addTechLevel(level, addToBase=True):
    try:
        import earnable_upgrades
        upgrades=earnable_upgrades.earnable_upgrades[level]
    except:
        print "No tech level named "+str(level)
        return
    bas=getDockedBase()
    if (not bas):
        import unit
        import vsrandom
        print "getting significant for upgrade addage"
        bas = unit.getSignificant(vsrandom.randrange(1,20),1,0);
    for upgrade in upgrades:
        if (len(upgrade)<5):
            print "Upgrade list not big enough to add to tech"
            print upgrade
            continue
        import Director
        import VS
        cp = VS.getCurrentPlayer()
        siz = Director.getSaveStringLength(cp,"master_part_list_content")
        doIt=True
        for index in range (siz):
            if (Director.getSaveString(cp,"master_part_list_content",index)==upgrade[0]):
                doIt=False
        if (doIt):
            print "added UPGRADE AS FOLLOWS to tech level "
            print upgrade
            Director.pushSaveString(cp,"master_part_list_content",str(upgrade[0]))
            Director.pushSaveString(cp,"master_part_list_category",str(upgrade[1]))
            Director.pushSaveString(cp,"master_part_list_price",str(upgrade[2]))
            Director.pushSaveString(cp,"master_part_list_mass",str(upgrade[3]))
            Director.pushSaveString(cp,"master_part_list_volume",str(upgrade[4]))
            if (len(upgrade)>5):
                Director.pushSaveString(cp,"master_part_list_description",str(upgrade[5]))              
            else:
                Director.pushSaveString(cp,"master_part_list_description","No description")             
            if (bas and addToBase):
                print " adding "+str(upgrade[0]) +" to base "+bas.getName()
                cargo=VS.Cargo(str(upgrade[0]),str(upgrade[1]),float(upgrade[2]),1,float(upgrade[3]),float(upgrade[4]))
                bas.forceAddCargo(cargo)
