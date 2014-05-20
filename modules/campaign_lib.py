# -*- coding: utf-8 -*-
import Base
import Director
import VS
#import custom
import debug
import fixers
import quest


class Condition:
    def __init__(self):
        pass

    def __call__(self):
        return True

def checkSaveValue (playernum,questname, value):
    return quest.checkSaveValue(playernum,questname,value)

def setSaveValue (playernum,name,value):
    quest.removeQuest(playernum,name,value);

def incSaveValue(playernum,name):
    mylen = Director.getSaveDataLength(int(playernum),str(name))
    val=0
    if (mylen>0):
        val=Director.getSaveData(int(playernum),str(name),mylen-1)
    val+=1
    setSaveValue(playernum,name,val)


class SaveVariableCondition(Condition):
    def __init__(self,varname,varvalue):
        Condition.__init__(self)
        self.name=str(varname)
        self.value=int(varvalue)

    def __call__(self):
        debug.debug("*** Checking \'%s : %d\'"%(self.name,self.value))
        checked=checkSaveValue(VS.getCurrentPlayer(),self.name,self.value)
        debug.debug("*** Returning: " + str(checked))
        return checked


class HaveCredits(Condition):
    def __init__(self,numcreds):
        Condition.__init__(self)
        self.creds=numcreds

    def __call__(self):
        un=VS.getPlayer()
        if not un.isNull():
            cc=un.getCredits()
            ret= (cc>=self.creds)
            debug.debug("Have at least "+str(self.creds)+" credits? "+str(cc)+" >= it? "+str(ret))
            return ret
        return False


class InSystemCondition(Condition):
    def __init__(self,system,shipname=None):
        Condition.__init__(self)
        self.system=None
        if system:
            if len(system):
                self.system=system.lower().replace(' ','_').split('/')
        self.dockedshipname=None
        if shipname:
            self.dockedshipname=shipname.replace(' ','_').lower()

    def __call__(self):
        if self.system:
            sys=VS.getSystemFile().split('/')
            debug.debug('System: '+str(sys)+'==?=='+str(self.system))
            for i in range(-1,-min(len(self.system),len(sys))-1,-1):
                if sys[i].lower()!=self.system[i]:
                    debug.debug(str(sys[i])+'!='+str(self.system[i]))
                    debug.debug('*** insystem return false: not in system!!')
                    return False
        if self.dockedshipname:
            if type(self.dockedshipname)==str:
                debug.debug('*** Test if docked to: '+ self.dockedshipname)
                iter = VS.getUnitList()
                while (not iter.isDone()):
                    testun = next(iter)
                    #debug.debug("iter.next()")
                    if (not testun.isNull() or VS.getPlayer().isDocked(testun) or testun.isDocked(VS.getPlayer())):
                        #Not sure why both have to be checked, it seems to second gives a more consistantly correct response
                        #find unit with name and check
                        debug.info('*** Compare ' + testun.getName().replace(' ','_').lower() + " == " + self.dockedshipname)
                        debug.info('    Compare ' + testun.getFullname().replace(' ','_').lower() + " == " + self.dockedshipname)
                        if (testun.getName().replace(' ','_').lower() == self.dockedshipname or testun.getFullname().replace(' ','_').lower() == self.dockedshipname):
                            debug.debug('*** inSystem return true')
                            return True
                    else:
                        debug.info(testun.getName() + ' not docked to unit')
        else:
            debug.debug('*** inSystem return true, no self.dockedshipname')
            return True
        debug.debug('*** insystem return false!!')
        return False


fixerloaded=0

class HasUndocked(Condition):
    def __init__(self):
        Condition.__init__(self)
        self.count=-1

    def __call__(self):
        global fixerloaded
        debug.debug('*** HasUndocked check false')
        if self.count==-1:
            self.count=fixerloaded
            return False
        else:
            debug.debug("FIXER LOADED:"+str(fixerloaded)+', '+str(self.count))
            return fixerloaded!=self.count


class CargoSpaceCondition(Condition):
    def __init__(self,type,num=1):
        Condition.__init__(self)
        self.type=type
        self.num=num

    def __call__(self):
        you=VS.getPlayer()
        mpart=VS.GetMasterPartList()
        carg=mpart.GetCargo(self.type)
        carg.SetContent(self.type)
        carg.SetQuantity(self.num)
        numcarg=you.addCargo(carg)
        you.removeCargo(self.type,numcarg,True)
        if numcarg<self.num:
            debug.debug('*** CargoSpace return false::IGNORED')
            #return False
        debug.debug('*** CargoSpace return true')
        return True


class AtMostActiveMissionsCondition(Condition):
    def __init__(self,num=0):
        Condition.__init__(self)
        self.num=num

    def __call__(self):
        debug.debug('*** have at most (<=) active missions ?')
        debug.debug('*** '+str(VS.numActiveMissions()-1)+' <= '+str(self.num))
        isactive=((VS.numActiveMissions()-1)<=self.num)
        debug.debug('*** '+str(isactive))
        return isactive


class AtLeastActiveMissionsCondition(Condition):
    def __init__(self,num=1):
        Condition.__init__(self)
        self.num=num

    def __call__(self):
        debug.debug('*** have at least (>=) active missions ?')
        debug.debug('*** '+str(VS.numActiveMissions()-1)+' >= '+str(self.num))
        isactive=((VS.numActiveMissions()-1)>=self.num)
        debug.debug('*** '+str(isactive))
        return isactive


class OrCondition(Condition):
    def __init__(self,conds,cond2=None):
        Condition.__init__(self)
        if cond2:
            self.conds=[conds,cond2]
        else:
            self.conds=conds

    def __call__(self):
        for c in self.conds:
            if c():
                return True
        return False


class AndCondition(Condition):
    def __init__(self,conds,cond2=None):
        Condition.__init__(self)
        if cond2:
            self.conds=[conds,cond2]
        else:
            self.conds=conds

    def __call__(self):
        for c in self.conds:
            if not c():
                return False
        return True


class InvertCondition(Condition):
    def __init__(self,cond):
        Condition.__init__(self)
        self.cond=cond

    def __call__(self):
        if self.cond():
            return False
        return True


InverseCondition=InvertCondition
NotCondition=InvertCondition

def tohex(r,g,b):
    def bytehex(num):
        def bytehex2(num):
            num = int(num)%16
            if num<10:
                return chr((num+ord('0')) % 256)
            else:
                return chr((num+ord('a')-10) % 256)
        return bytehex2(num/16)+bytehex2(num%16)
    return '#'+bytehex(int(r*255))+bytehex(int(g*255))+bytehex(int(b*255))

def getcolor(strs):
    h=((hash(strs) % 2147483647) / 2147483647.0 + 1) / 2
    if h > 1.0:
        h = 1.0
    if h < 0.0:
        h = 0.0
    if h < 0.1666666:
        return tohex(0, h / 0.1666666, 1)
    elif h < 0.3333333:
        return tohex(0, 1, 1 - ((h - 0.1666666) / 0.1666666))
    if h < 0.5:
        return tohex((h - 0.3333333) / 0.1666666, 1, 0)
    elif h < 0.6666666:
        return tohex(1, 1 - ((h - 0.5) / 0.1666666), 0)
    elif h < 0.8333333:
        return tohex(1, 0, (h - 0.6666666) / 0.1666666)
    else:
        return tohex(1 - (( h - 0.8333333) / 0.1666666), 0, 1)

def textline(strs):
    if type(strs) is list or type(strs) is tuple:
        if len(strs)>1:
            sound=None
            ret1=True
            if len(strs)>2:
                sound=strs[2]
            elif strs[1][-4:]=='.wav':
                sound=strs[1]
                ret1=False
            if sound and sound!='':
                VS.StopAllSounds()
                debug.debug("playing sound "+str(sound))
                VS.playSound (sound, (0.,0.,0.), (0.,0.,0.))
            if ret1:
                return getcolor(str(strs[0]))+str(strs[0])+": #000000"+str(strs[1])
        return strs[0]
    return "#00ff00"+str(strs)

#depends on Base
def displayText(room,textlist,enqueue=False):
    debug.debug("displayText()")
    debug.debug("Displaying campaign text:\n%s" % (debug.pp(textlist)))
    if room==-1:
        debug.debug("Room is -1!!!")
    room = Base.GetCurRoom()
    func=Base.MessageToRoom
    if enqueue:
        func=Base.EnqueueMessageToRoom
    if type(textlist) is str:
        if textlist!='':
            debug.debug('*** Base.message('+textlist+')')
            func(room,textline(textlist))
    else:
        if textlist and len(textlist):
            debug.debug('*** Base.message('+str(textlist[0])+')')
            #Base.MessageToRoom(room,str(textlist[0]))
            stri=''
            if enqueue:
                for x in textlist:
                    func(room,textline(x))
            else:
                for x in textlist:
                    stri+=textline(x)+"\n"
                func(room,stri);
            #   debug.debug('*** Base.enqueuEmessage('+str(x)+')')
            #   Base.EnqueueMessageToRoom(room,str(x))


class Script:
    def __init__(self,nextscript=None):
        self.nextscript=nextscript
    def __call__(self,room,subnodes):
        debug.debug('**************** CALL SCRIPT')
        if self.nextscript:
            debug.debug('***************** CALL NEXT SCRIPT'+str(self.nextscript))
            self.nextscript(room,subnodes)
        return True


class EnqueueMoreText(Script):
    def __init__(self,text,nextscript=None):
        Script.__init__(self,nextscript)
        self.text=text
    def __call__(self,room,subnodes):
        Script.__call__(self,room,subnodes)
        displayText(room,self.text,True)


# Should use this with GoToSubnodeIfTrue.
class RemoveCargo(Script):
    def __init__(self,name,num,missionflag,nextscript=None):
        Script.__init__(self,nextscript)
        self.cargname=name
        self.cargnum=num
        self.missionflag=missionflag
    def __call__(self,room,subnodes):
        Script.__call__(self,room,subnodes)
        you=VS.getPlayer()
        removenum=you.removeCargo(self.cargname,self.cargnum,True)
        if self.missionflag:
            has=you.hasCargo(self.cargname)
            if (has):
                mpart=VS.GetMasterPartList()
                newcarg=mpart.GetCargo(self.cargname)
                has=you.removeCargo(self.cargname,has,bool(1))
                newcarg.SetMissionFlag(0)
                newcarg.SetContent(self.cargname)
                newcarg.SetQuantity(has)
                you.addCargo(newcarg) #It seems that removing and then adding it again is the only way...
        debug.debug('*********** Remove cargo '+self.cargname+'('+str(self.cargnum)+')')
        if removenum<self.cargnum:
            debug.debug('        ...strict failed to remove cargo')
            return False #since we force add all cargo, we can fail if not all is removed
        if removenum<1:#self.cargnum less strict
            debug.debug('        ...really failed :-(')
            return False
        return True


# Should use this with GoToSubnodeIfTrue.
class AddCargo(Script):
    def __init__(self,name,num,missionflag,nextscript=None):
        Script.__init__(self,nextscript)
        self.cargname=name
        self.cargnum=num
        self.missionflag=missionflag
    def __call__(self,room,subnodes):
        Script.__call__(self,room,subnodes)
        if True or CargoSpaceCondition(self.cargname,self.cargnum):
            you=VS.getPlayer()
            mpart=VS.GetMasterPartList()
            carg=mpart.GetCargo(self.cargname)
            carg.SetQuantity(self.cargnum)
            if carg.GetContent()=='':
                carg.SetMass(0.01)
                carg.SetVolume(1)
                carg.SetPrice(0)
            carg.SetContent(self.cargname)
            carg.SetMissionFlag(self.missionflag)
            numsofar=you.addCargo(carg)
            debug.debug("Successfully added "+str(numsofar))
            numadded=0
            if (numsofar<self.cargnum):
                rang=list(range(you.numCargo()))
                rang.reverse()
                for i in rang:
                    karg=you.GetCargoIndex(i)
                    if (not karg.GetMissionFlag()):
                        if (karg.GetCategory().find("upgrades")==-1):
                            content=karg.GetContent()
                            debug.debug("testing "+ content)
                            diff=self.cargnum-numsofar-numadded
                            quant=karg.GetQuantity()
                            if (quant>0):
                                if (quant>diff):
                                    diff=quant
                                p=karg.GetPrice()
                                diff=you.removeCargo(content,diff,True)
                                numadded+=diff
                                you.addCredits(p*diff)
                                debug.debug("Took away "+str(diff)+" of "+content)
                                if (numadded+numsofar>=self.cargnum):
                                    break;
                carg.SetQuantity(self.cargnum-numsofar)
                debug.debug("attempting to add "+str(self.cargnum-numsofar)+" of "+carg.GetContent())
                num=you.addCargo(carg)
                debug.debug("added "+str(num)+" cargo after removing some")
                if (num+numsofar<self.cargnum):
                    debug.debug("force add 1 cargo")
                    carg.SetQuantity(self.cargnum-num-numsofar)
                    you.forceAddCargo(carg)

            debug.debug('*********** Added cargo '+self.cargname+'('+str(self.cargnum)+')')
            return True
        return False


class SetSaveVariable(Script):
    def __init__(self,varname,varvalue,nextscript=None):
        Script.__init__(self,nextscript)
        self.name=str(varname)
        self.value=int(varvalue)

    def __call__(self,room,subnodes):
        Script.__call__(self,room,subnodes)
        debug.debug("*** Setting \'%s : %d\'"%(self.name,self.value))
        setSaveValue(VS.getCurrentPlayer(),self.name,self.value)
        return True


class IncSaveVariable(Script):
    def __init__(self,varname,nextscript=None):
        Script.__init__(self,nextscript)
        self.name=str(varname)

    def __call__(self,room,subnodes):
        Script.__call__(self,room,subnodes)
        debug.debug("*** Incrementing \'%s \'"%self.name)
        incSaveValue(VS.getCurrentPlayer(),self.name)
        return True


class AddTechnology(Script):
    def __init__(self,technology,nextscript=None):
        Script.__init__(self,nextscript)
        self.tech=technology
    def __call__(self,room,subnodes):
        Script.__call__(self,room,subnodes)
        import universe
        universe.addTechLevel(self.tech)


class AdjustRelation(Script):
    def __init__(self,us,them,change,nextscript=None):
        Script.__init__(self,nextscript)
        self.us=us
        self.them=them
        self.change=change
    def __call__(self,room,subnodes):
        Script.__call__(self,room,subnodes)
        VS.AdjustRelation(self.us,self.them,self.change,1.0)
        return True


class ClearFactionRecord(Script):
    def __init__(self,fac,newrelation,nextscript=None):
        Script.__init__(self,nextscript)
        self.faction=fac
        self.newval=newrelation
    def __call__(self,room,subnodes):
        Script.__call__(self,room,subnodes)
        rel=VS.GetRelation(self.faction,"privateer")
        VS.AdjustRelation(self.faction,"privateer",self.newval-rel,1.0)
        rel=VS.GetRelation("privateer",self.faction)
        VS.AdjustRelation("privateer",self.faction,self.newval-rel,1.0)


class ClearRecord(Script):
    def __init__(self,nextscript=None):
        Script.__init__(self,nextscript)
    def FixRelation(self,fac,room,subnodes):
        ClearFactionRecord(fac,1.0)(room,subnodes)
    def __call__(self,room,subnodes):
        Script.__call__(self,room,subnodes)
        self.FixRelation("pirates",room,subnodes)
        self.FixRelation("confed",room,subnodes)
        self.FixRelation("militia",room,subnodes)
        self.FixRelation("merchant",room,subnodes)
        self.FixRelation("hunter",room,subnodes)


class PushRelation(Script):
    def __init__(self,faction,nextscript=None):
        Script.__init__(self,nextscript)
        self.faction=faction
    def __call__(self,room,subnodes):
        Script.__call__(self,room,subnodes)
        cp=VS.getCurrentPlayer()
        key=self.faction+"_relation_stack"
        Director.pushSaveData(cp,key,VS.GetRelation(self.faction,"privateer"))


class PopRelation(Script):
    def __init__(self,faction,nextscript=None):
        Script.__init__(self,nextscript)
        self.faction=faction
    def __call__(self,room,subnodes):
        Script.__call__(self,room,subnodes)
        cp=VS.getCurrentPlayer()
        key=self.faction+"_relation_stack"
        length=Director.getSaveDataLength(cp,key)
        ClearFactionRecord(self.faction,Director.getSaveData(cp,key,length-1))(room,subnodes)
        Director.eraseSaveData(cp,key,length-1);


class LaunchWingmen(Script):
    def __init__(self,faction,shiptype,num,nextscript=None):
        Script.__init__(self,nextscript)
        self.faction=faction
        self.shiptype=shiptype
        self.num=num
    def __call__(self,room,subnodes):
        Script.__call__(self,room,subnodes)
        you=VS.getPlayer()
        import launch
        wing=launch.launch_wave_around_unit("Wingmen",
                        self.faction,
                        self.shiptype,
                        "default",
                        self.num,
                        500,
                        1000,
                        you)
        wing.setFgDirective('A')
        wing.setFlightgroupLeader(you)


class ChangeSystemOwner(Script):
    def __init__(self,system,faction,nextscript=None):
        Script.__init__(self,nextscript)
        self.faction=faction
        self.system=system
    def __call__(self,room,subnodes):
        Script.__call__(self,room,subnodes)
        VS.SetGalaxyFaction(self.system,self.faction);


class ChangeShipOwners(Script):
    def __init__(self,oldfaction,faction,nextscript=None):
        Script.__init__(self,nextscript)
        self.faction=faction
        self.oldfaction=oldfaction
    def __call__(self,room,subnodes):
        Script.__call__(self,room,subnodes)
        i = VS.getUnitList()
        while(not i.isDone()):
            un = next(i)
            if (not un.isNull()) and un.getFactionName()==self.oldfaction:
                un.setFactionName(self.faction)

            
class AddCredits(Script):
    def __init__(self,numcreds,nextscript=None):
        Script.__init__(self,nextscript)
        self.creds=numcreds
        self.added=False
    def __call__(self,room,subnodes):
        Script.__call__(self,room,subnodes)
        un=VS.getPlayer()
        if not un.isNull():
            if not self.added:
                un.addCredits(self.creds)
                self.added=True
        return True


class SaveVariableGreaterScript(Script):
    def __init__(self,var,val,nextscript=None):
        Script.__init__(self,nextscript)
        self.var=var
        self.val=val
    def __call__(self,room,subnodes):
        Script.__call__(self,room,subnodes)
        playernum=VS.getCurrentPlayer()
        mylen=Director.getSaveDataLength(playernum,self.var)
        if (mylen>0):
            myfloat=Director.getSaveData(playernum,self.var,0)
        else:
            myfloat=0
        debug.debug("myfloat %.3f > self.val %.3f ?" % (myfloat, self.val))
        return myfloat>self.val


class DisplayTextIfTrueScript(Script):
    def __init__(self,text,nextscript=None):
        Script.__init__(self,nextscript)
        self.text=text
    def __call__(self,room,subnodes):
        val=False
        if self.nextscript:
            val=self.nextscript(room,subnodes)
        debug.debug("VAL "+str(val))
        if val:
            displayText(room,self.text)
        return val


class RemoveCredits(Script):
    def __init__(self,numcreds,nextscript=None):
        Script.__init__(self,nextscript)
        self.creds=numcreds
    def __call__(self,room,subnodes):
        Script.__call__(self,room,subnodes)
        un=VS.getPlayer()
        if not un.isNull():
            un.addCredits(-self.creds)
        return True


class SetCredits(Script):
    def __init__(self,numcreds,nextscript=None):
        Script.__init__(self,nextscript)
        self.creds=numcreds
    def __call__(self,room,subnodes):
        Script.__call__(self,room,subnodes)
        un=VS.getPlayer()
        if not un.isNull():
            un.addCredits(self.creds-un.getCredits())
        return True


class PushCredits(Script):
    def __init__(self,nextscript=None):
        Script.__init__(self,nextscript)
    def __call__(self,room,subnodes):
        Script.__call__(self,room,subnodes)
        cp=VS.getCurrentPlayer()
        un=VS.getPlayerX(cp)
        if not un.isNull():
            creds=un.getCredits()
            key="credits_stack"
            Director.pushSaveData(cp,key,creds)
        return True


class PopCredits(Script):
    def __init__(self,nextscript=None):
        Script.__init__(self,nextscript)
    def __call__(self,room,subnodes):
        Script.__call__(self,room,subnodes)
        cp=VS.getCurrentPlayer()
        un=VS.getPlayerX(cp)
        if not un.isNull():
            key="credits_stack"
            length=Director.getSaveDataLength(cp,key)
            un.addCredits(Director.getSaveData(cp,key,length-1))
            Director.eraseSaveData(cp,key,length-1);
        return True


class PushNews(Script):
    def __init__(self,story,nextscript=None):
        Script.__init__(self,nextscript)
        self.story=story
    def __call__(self,room,subnodes):
        Script.__call__(self,room,subnodes)
        cp=VS.getCurrentPlayer()
        Director.pushSaveString(cp,"dynamic_news",'#'+self.story)


#LoadMission(varname,missionname,missionargs,SetSaveVariable(varname,2,script)) # jay
class LoadMission(Script):
    def __init__(self,name,missionname,missionargs,nextscript=None):
        Script.__init__(self,nextscript)
        self.mname=missionname
        self.args=missionargs
        self.name=name
    def __call__(self,room,subnodes):
        Script.__call__(self,room,subnodes)
        import mission_lib
        mission_lib.AddNewMission(self.name,self.args,self.mname)
        mission_lib.SetLastMission(self.name)
        debug.debug('*** Loading the mission!')
        debug.debug('*** '+str(self.mname)+'('+str(self.args)+')')
        #VS.LoadMission('internal_mission_lib.mission')
        mission_lib.LoadLastMission()
        return True


class AddSprite(Script):
    def __init__(self,name,sprite,pos,nextscript=None):
        Script.__init__(self,nextscript)
        self.name=name
        self.sprite=sprite
        if self.sprite.find('/')==-1:
                self.sprite=('bases/fixers/'+self.sprite)
        self.pos=pos
#       debug.debug('************ Init add sprite '+ repr(self.name)+', '+repr(self.sprite)+', '+repr(self.pos))

    def __call__(self,room,subnodes):
        debug.debug('***************** ADD THE SPRITE')
        Script.__call__(self,room,subnodes)
        debug.debug('*** AddSprite: Base.Texture'+str((room,self.name,self.sprite,self.pos[0],self.pos[1])))
        Base.Texture(room,self.name,self.sprite,self.pos[0],self.pos[1])
        return True


class AddPythonSprite(AddSprite):
    def __init__(self,name,sprite,center_position,widthheight,text,python,nextscript=None):
        AddSprite.__init__(self,name,sprite,center_position,nextscript)
        self.widthheight=widthheight
        self.text=text
        self.python=python

    def __call__(self,room,subnodes):
        AddSprite.__call__(self,room,subnodes)
        debug.debug("Creating a new python in room %d, %s (%f,%f), %fx%f"%(room,self.sprite,self.pos[0],self.pos[1],self.widthheight[0],self.widthheight[1]))
        Base.Python(room,self.name,self.pos[0]-(self.widthheight[0]/2.), self.pos[1]-(self.widthheight[1]/2.),
            self.widthheight[0], self.widthheight[1], self.text, self.python, True)
        return True

def AddRemovingSprite(name,sprite,center_position,widthheight,text,nextscript=None):
    return AddPythonSprite(name,sprite,center_position,
        widthheight,text,"#\nimport Base\nBase.EraseLink(Base.GetCurRoom(), "+repr(name)+")\nBase.EraseObj(Base.GetCurRoom(), "+repr(name)+")\n",nextscript)

def AddConversationStoppingSprite(name,sprite,center_position,widthheight,text,nextscript=None):
    return AddPythonSprite(name,sprite,center_position,
        widthheight,text,"#\nimport Base\nBase.EraseLink(Base.GetCurRoom(), "+repr(name)+")\nBase.EraseObj(Base.GetCurRoom(), "+repr(name)+")\nimport VS\nVS.StopAllSounds()\nBase.Message('')\n",nextscript)

def doTalkingHeads():
    try:
        talkp=VS.vsConfig("graphics","talking_heads","true")
        talk= (talkp=="true" or talkp=="1")
    except:
        talk=True
        debug.debug("recovered:")
        import sys
        debug.debug(str(sys.exc_info()[0])+str(sys.exc_info()[1]))
    return talk

do_not_play_music=False

class Cutscene(AddPythonSprite):
    def __init__(self,name,sprite,center_position,widthheight,text,BaseMessage,music,origlist=None,nextscript=None):
        scripts="#\nimport Base, campaign_lib, VS\nBase.EraseLink(Base.GetCurRoom(), '"+name+"')\nBase.EraseObj(Base.GetCurRoom(), '"+name+"')\nBase.EraseObj(Base.GetCurRoom(), '"+name+"_black')\nVS.StopAllSounds()\nBase.Message('')\n"
        if (origlist):
            scripts+="campaign_lib.do_not_play_music=False\nlist=VS.musicAddList("+repr(origlist)+")\nVS.musicPlayList(list)"
        AddPythonSprite.__init__(self,name,sprite,center_position,widthheight,text,scripts,nextscript)
        BaseMessage.append('                                        <Click to exit cutscene>')
        self.BaseMessage=BaseMessage
        self.music=music
        self.origSong=origlist
        self.enqueue=False
    def MakeEnqueue(self):
        self.enqueue=True
        return self
    def __call__(self,room,subnodes):
        global do_not_play_music
        do_not_play_music=True
        VS.musicStop()
        Base.Texture(0, self.name+"_black", "black.spr", 0, 0);
        AddPythonSprite.__call__(self,0,subnodes)
        displayText(0,self.BaseMessage,self.enqueue)
        if self.origSong:
            slist=VS.musicAddList(self.music)
            VS.musicPlayList(slist)
        else:
            VS.musicPlaySong(self.music)
        return True


class GoToSubnodeIfTrue(Script):
    def __init__(self,script,iftrue=0,iffalse=-1):
        Script.__init__(self,script)
        self.iftrue=iftrue
        self.iffalse=iffalse
    def __call__(self,room,subnodes):
        ret=False
        if self.nextscript:
            ret=self.nextscript(room,subnodes)
        if ret:
            debug.debug('*** True! '+str(self.iftrue))
            return self.iftrue
        else:
            debug.debug('*** False! '+str(self.iffalse))
            return self.iffalse


class TrueSubnode(Script):
    def __init__(self,nextscript=None):
        Script.__init__(self,nextscript)
    def __call__(self,room,subnodes):
        Script.__call__(self,room,subnodes)
        for i in range(len(subnodes)):
            if subnodes[i].checkPreconditions():
                return i
        return -1


class TrueBackwardsSubnode(Script):
    def __init__(self,nextscript=None):
        Script.__init__(self,nextscript)
    def __call__(self,room,subnodes):
        Script.__call__(self,room,subnodes)
        for i in range(len(subnodes)-1,-1,-1):
            if subnodes[i].checkPreconditions():
                return i
        return -1


class GoToSubnode(Script):
    def __init__(self,const,nextscript=None):
        Script.__init__(self,nextscript)
        self.const=const
    def __call__(self,room,subnodes):
        debug.debug('************* Goto before script call')
        Script.__call__(self,room,subnodes)
        debug.debug('************* Goto after script call')
        return self.const

YES_SPRITE='yes.spr'
NO_SPRITE='no.spr'


class Campaign:
    def __init__(self,savegamename,rootnode=None):
        self.name=savegamename
        self.root=rootnode
        self.current=rootnode
        self.savegame=[]

    def Init(self,rootnode):
        self.root=rootnode
        self.current=rootnode
        # Note: Init() will not evaluate the first node because it probably is not in a base.
        # The root note therefore sould probably be a CampaignClickNode

    #depends on Base... should remove dependencies?
    def setCurrentNode(self,room,newnodenum):
        debug.debug('*** Going to branch number '+str(newnodenum))
        if newnodenum>=0:
            if newnodenum>=len(self.current.subnodes):
                debug.debug('Error: cannot go to node '+str(newnodenum))
                debug.debug('Failed node has text:')
                debug.debug(str(self.current.text))
                return
            self.current=self.current.subnodes[newnodenum]
            self.savegame.append(newnodenum)
            Director.pushSaveData(VS.getCurrentPlayer(),self.name,float(newnodenum))
        elif newnodenum==-2:
            if not self.current.contingency:
                debug.debug('Error: cannot go to contingency node!')
                debug.debug('Failed node has text:')
                debug.debug(str(self.current.text))
                return
            debug.debug('*** Going to contingency!')
            self.current=self.current.contingency
            self.savegame.append(-2)
            Director.pushSaveData(VS.getCurrentPlayer(),self.name,float(-2))
        self.current.evaluate(room)

    def readPositionFromSavegame(self):
        self.savegame=[]
        self.current=self.root
        plr=VS.getCurrentPlayer()
        length=Director.getSaveDataLength(plr,self.name)
        for i in range(length):
            newnodenum=int(Director.getSaveData(plr,self.name,i))
            if newnodenum>=0:
                if newnodenum>=len(self.current.subnodes):
                    debug.debug('Error: save game index out of bounds: '+str(newnodenum))
                    return
                debug.debug(self.current)
                self.current=self.current.subnodes[newnodenum]
            elif newnodenum==-2:
                if not self.current.contingency:
                    debug.debug('Error: save game moves to invalid contengency node!')
                    return
                debug.debug(self.current)
                self.current=self.current.contingency
            self.savegame.append(newnodenum)
        debug.debug('*** read position from save game: for '+self.name+': '+str(self.savegame))
        debug.debug(self.current)

    #depends on Base... should remove dependencies?
    def getCurrentNode(self,room):
        debug.debug('*** getting current node')
        plr=VS.getCurrentPlayer()
        if Director.getSaveDataLength(plr,self.name)!=len(self.savegame):
            self.readPositionFromSavegame()
        else:
            debug.debug('*** read stuff from savegame')
            for i in range(len(self.savegame)):
                if int(Director.getSaveData(plr,self.name,i))!=self.savegame[i]:
                    self.readPositionFromSavegame()
                    break
        debug.debug("*** :-) ***")
        debug.debug("savegame state:\n%s" % (self.savegame))
        while True:
            try:
                if self.current.checkPreconditions():
                    if room>=0:
                        self.current.evaluate(room)
                        debug.debug('*** current room evaluated')
                    return self.current
                if not self.current.contingency:
                    debug.debug('*** no contingency!')
                    return None
                debug.debug('*** current room contingency!')
                self.setCurrentNode(room,-2)
            except Exception as inst:
                debug.debug("!!! Error evaluating room: '" + str(room) + "'")
                import traceback
                traceback.print_stack()
                traceback.print_exc()
                return None
        debug.warn('*** Your Python is broken. Please fix it now!!!!')
        return None


class CampaignNode:
    def __init__(self):
        pass
    def IsCampaignChoiceNode(self):
        return False
    def Init(self,campaign,preconditions,text,spritelink,script,contingency,subnodes):
        self.campaign=campaign
        self.preconditions=preconditions
        self.text=text
        self.talkinghead=None
        self.spritelink=spritelink
        self.script=script
        self.subnodes=[]
        if self.spritelink:
            if len(self.spritelink)>2:
                self.talkinghead=self.spritelink[2]
            if self.spritelink[0].find('/')==-1:
                self.spritelink=('bases/fixers/'+self.spritelink[0],self.spritelink[1])
        for i in subnodes:
            self.subnodes.append(i)
        self.contingency=contingency
        return self
    def checkPreconditions(self):
        if self.preconditions:
            for cond in self.preconditions:
                if not cond():
                    return False
        return True
    #depends on Base
    def getFixer(self,room):
        if self.spritelink and self.checkPreconditions():
            debug.debug('*** create fixer'+ str(self.spritelink))
            tmpscript="#\nimport campaign_lib\n"
            if self.talkinghead and doTalkingHeads():
                tmpscript+="campaign_lib.AddConversationStoppingSprite('Talking',"+repr(self.talkinghead)+",(0,0),(3.2,2.0),'Return_To_Bar').__call__("+str(room)+",None)\n"
            return fixers.Fixer(self.spritelink[1].split(' ')[-1].lower(),self.spritelink[1],[],
                self.spritelink[0],tmpscript+"campaign_lib.clickFixer("+str(room)+")\n")
        debug.debug('*** Not returning a sprite for the fixer.')
        return None
    #depends on Base
    def gotoChoice(self,room,num):
        self.campaign.setCurrentNode(room,num)
    #depends on Base
    def clickFixer(self,room):
        CampaignNode.evaluate(self,room)
    #depends on Base... should remove dependencies?
    def evaluate(self,room):
        if self.checkPreconditions():
            displayText(room,self.text)
            debug.debug('subnodes: '+str(self.subnodes))
            num=self.script(room,self.subnodes)
            if num>=0 and num<len(self.subnodes):
                self.gotoChoice(room,num)


class CampaignClickNode(CampaignNode):
    def __init__(self):
        CampaignNode.__init__(self)
    def Init(self,campaign,preconditions,text,spritelink,script,contingency,subnodes):
        CampaignNode.Init(self,campaign,preconditions,text,spritelink,script,contingency,subnodes)
        return self
    #depends on Base... should remove dependencies?
    def evaluate(self,room):
        pass


class CampaignChoiceNode(CampaignNode):
    def __init__(self):
        CampaignNode.__init__(self)
    def IsCampaignChoiceNode(self):
        return True
    def Init(self,campaign,preconditions,text,spritelink,contingency,choices):
        tmp=[]
        tmpchoices=[]
        for i in choices:
            tmp.append(i[1])
            if i[0][0].find('/')==-1:
                tmpchoices.append(('bases/fixers/'+i[0][0],i[0][1]))
            else:
                tmpchoices.append(i[0])
        CampaignNode.Init(self,campaign,preconditions,text,spritelink,None,contingency,tmp)
        self.choices=tmpchoices
        return self
    def gotoChoice(self,room,num):
        self.campaign.setCurrentNode(room,num)
    def clickFixer(self,room):
        displayText(room,self.text)
    #depends on Base... should remove dependencies?
    def evaluate(self,room):
        debug.debug('***')
        debug.debug('***')
        debug.debug(debug.pp(self.text))
        displayText(room,self.text)
        arr=[]
        debug.debug('*** create buttons +'+str(self.choices))
        for x in range(len(self.choices)):
            arr.append(fixers.Choice(self.choices[x][0],"#\nimport campaign_lib\ncampaign_lib.clickChoice("+str(room)+","+str(x)+")\n",self.choices[x][1]))
        fixers.DestroyActiveButtons()
        fixers.CreateChoiceButtons(room,arr)
        debug.debug('***')
        debug.debug('***')

def CampaignEndNode(campaign):
    return CampaignNode().Init(campaign,[],[],None,GoToSubnode(0),None,[CampaignNode().Init(campaign,[InSystemCondition("NeverNeverLand/neverhere")],[],None,GoToSubnode(-1),None,[])])

#class CampaignEndNode(CampaignNode):
#   def __init__(self):
#       CampaignNode.__init__(self)
#   def Init(self,campaign):
#       CampaignNode.Init(self,campaign,[],[],None,GoToSubnode(0),None,[CampaignNode(campaign,).Init()])
#       debug.debug('End Node init')
#       return self
#   def checkPreconditions(self):
#       debug.debug('end check precondtions')
#       return True
#   def getFixer(self,room):
#       debug.debug('end get fixer')
#       return None
#   def gotoChoice(self,room,num):
#       debug.debug('end node goto')
#   def clickFixer(self,room):
#       debug.debug('end node click')
#   def evaluate(self,room):
#       debug.debug('end node eval')


def IfThenElse (A,B,C):
    if (A):
        return B
    return C

def AskToAcceptMission(campaign,sprite,conditiontoappear,conditiontobegin,scriptonclick,speech,RejectNode,FlyMission,MissionRefusal=None,SeedClickNode=None):
    if (not SeedClickNode):
        SeedClickNode=CampaignClickNode()
    if (not MissionRefusal):
        MissionRefusal=CampaignClickNode()
    MissionFirstRefusal=CampaignChoiceNode()
    ret=SeedClickNode.Init(campaign,
        conditiontoappear,
        [],
        sprite,
        TrueSubnode(scriptonclick),
        None,
        [CampaignChoiceNode().Init(campaign,
            conditiontobegin,
            speech["intro"],#if its not there python error at tree-compile, not runtime
            sprite,
            None,
            [((NO_SPRITE,"Refuse_Mission"),CampaignNode().Init(campaign,
                [],
                speech["reject1"],
                sprite,
                GoToSubnode(0),
                None,
                [CampaignClickNode().Init(campaign,
                    conditiontobegin,
                    [],
                    sprite,
                    GoToSubnode(0),
                    None,
                    [MissionFirstRefusal.Init(campaign,conditiontobegin,
                    speech["reconsider"],
                    sprite,
                    None,
                    [((NO_SPRITE,"Refuse_Mission"),CampaignNode().Init(campaign,
                        [],
                        speech["reject2"],
                        sprite,
                        TrueSubnode(),
                        None,
                        [MissionRefusal.Init(campaign,
                            conditiontobegin,
                            [],
                            sprite,
                            #TrueSubnode(),
                            GoToSubnode(0),
                            None,
                            [IfThenElse(RejectNode,RejectNode,MissionFirstRefusal)])])),
                    ((YES_SPRITE,"Accept_Mission"),FlyMission)])])])),
             ((YES_SPRITE,"Accept_Mission"),FlyMission)])])
    return ret


def MakeVariableMission(campaign,sprite,conditiontobegin,conditiontoend,scriptonclick,scriptbegin,varname,speech,RejectNode,FailureNode,SuccessNode,SeedClickNode=None):
    if (not SeedClickNode):
        SeedClickNode=CampaignClickNode()
    MissionRefusal=CampaignClickNode()
    FlyMission=CampaignNode()
    FlyMissionContingency=CampaignNode()
    ret=AskToAcceptMission(campaign,
        sprite,
        conditiontobegin,
        conditiontobegin,
        scriptonclick,
        speech,
        RejectNode,
        FlyMission,
        MissionRefusal,
        SeedClickNode)
    FlyMission.Init(campaign,
            [],
            speech["accept"],
            sprite,
            IfThenElse(scriptbegin,GoToSubnodeIfTrue(scriptbegin,iftrue=1,iffalse=0),GoToSubnode(1)),
            None,
            [MissionRefusal,
            CampaignNode().Init(campaign,
                [],
                [],
                None,
                TrueSubnode(SetSaveVariable(varname,2)),
                None,
                [FlyMissionContingency.Init(campaign,
                    [],
                    [],
                    None,
                    TrueSubnode(),
                    None,
                    [CampaignClickNode().Init(campaign,
                        conditiontobegin+[SaveVariableCondition(varname,-1)],
                        speech["failure"],
                        sprite,
                        GoToSubnode(0),
                        None,
                        [FailureNode]),
                     CampaignNode().Init(campaign,
                        conditiontoend+[SaveVariableCondition(varname,1)],
                        [],
                        None,
                        GoToSubnode(0),
                        None,
                        [SuccessNode]),
                     CampaignClickNode().Init(campaign,
                        conditiontobegin+[AndCondition(InvertCondition(OrCondition([SaveVariableCondition(varname,1)])),InvertCondition(SaveVariableCondition(varname,-1))),AtMostActiveMissionsCondition()],
                        speech["reminder"],
                        sprite,
                        TrueSubnode(scriptbegin),
                        FlyMissionContingency,#stuck in a click node, not in ND
                        []),
                     CampaignClickNode().Init(campaign,
                        conditiontobegin+[AndCondition(InvertCondition(OrCondition([SaveVariableCondition(varname,1)])),InvertCondition(SaveVariableCondition(varname,-1))),AtLeastActiveMissionsCondition()],
                        speech["reminder"],
                        sprite,
                        TrueSubnode(),
                        FlyMissionContingency,#stuck in a click node, not in ND
                        [])])])])
    return ret

def MakeNoFailureCargoMission(campaign,sprite,conditiontobegin,conditiontoend,scriptonclick,script,cargoNameQuantity,varname,speech,RejectNode,FailureNode,SuccessNode,SeedClickNode=None):
    if (not SeedClickNode):
        SeedClickNode=CampaignClickNode()
    cargoMissionFlag=True
    if len(cargoNameQuantity)>2:
        cargoMissionFlag=cargoNameQuantity[2]
    MissionRefusal=CampaignClickNode()
    FlyMission=CampaignNode()
    FlyMissionContingency=CampaignNode()
    ret=AskToAcceptMission(campaign,
        sprite,
        conditiontobegin+[CargoSpaceCondition(cargoNameQuantity[0],cargoNameQuantity[1])],
        conditiontobegin,
        scriptonclick,
        speech,
        RejectNode,
        FlyMission,
        MissionRefusal,
        SeedClickNode)
    FlyMission.Init(campaign,
            [],
            speech["accept"],
            sprite,
            GoToSubnodeIfTrue(AddCargo(cargoNameQuantity[0],cargoNameQuantity[1],cargoMissionFlag,SetSaveVariable(varname,2,script)),iftrue=1,iffalse=0),
            None,
            [MissionRefusal,
            FlyMissionContingency.Init(campaign,
                [],
                [],
                None, #(fac, 0, numcargos, diff, creds, launchcap, 0, category, str(path), ''))
                TrueSubnode(), # jay
                None,
                [CampaignClickNode().Init(campaign,
                    conditiontobegin+[AtMostActiveMissionsCondition()],
                    speech["reminder"],
                    sprite,
                    TrueSubnode(script),
                    FlyMissionContingency,#stuck in a click node, not in ND
                    []),#got advice, go back to click node
                CampaignNode().Init(campaign,
                    conditiontoend,
                    [],
                    None,
                    GoToSubnodeIfTrue(RemoveCargo(cargoNameQuantity[0],cargoNameQuantity[1],cargoMissionFlag,SetSaveVariable(varname,1)),iftrue=1,iffalse=0),
                    None,
                    [FailureNode,
                     SuccessNode]),
                CampaignClickNode().Init(campaign,
                    conditiontobegin+[AtLeastActiveMissionsCondition()],
                    speech["reminder"],
                    sprite,
                    TrueSubnode(),
                    FlyMissionContingency,#stuck in a click node, not in ND
                    [])#got advice, go back to click node
                ])])
    return ret

def MakeCargoMission(campaign,sprite,conditiontobegin,conditiontoend,scriptonclick,script,cargoNameQuantity,varname,speech,RejectNode,FailureNode,SuccessNode,SeedClickNode=None):
    return MakeNoFailureCargoMission(campaign,
        sprite,
        conditiontobegin,
        conditiontoend,
        scriptonclick,
        script,
        cargoNameQuantity,
        varname,
        speech,
        RejectNode,
        CampaignClickNode().Init(campaign,
                    conditiontobegin,
                    speech["failure"],
                    sprite,
                    GoToSubnode(0,SetSaveVariable(varname,-1)),
                    None,
                    [FailureNode]),
        SuccessNode,
        SeedClickNode)

def MakeNoFailureMission(campaign, sprite, conditiontobegin, conditiontoend, scriptonclick, script, missionname, missionargs, varname, speech, rejectnode, failurenode, succeednode, node=None, missiondesc="MakeNoFailureMission"):
    #debug.debug("called MakeNoFailureMission with missiondesc := %s" % (missiondesc))
    if missiondesc == "MakeNoFailureMission":
        missiondesc += " " + varname
    if not node:
        node=CampaignClickNode()
    getthemission=CampaignNode()
    reject2node=CampaignClickNode()
    ret=AskToAcceptMission(campaign,
        sprite,
        conditiontobegin,
        conditiontobegin,
        scriptonclick,
        speech,
        rejectnode,
        getthemission,
        reject2node,
        node)
    contingency=CampaignNode()
    getthemission.Init(campaign,
        conditiontobegin,
        speech["accept"],
        sprite,
        TrueSubnode(LoadMission(missiondesc,missionname,missionargs,SetSaveVariable(varname,2,script))),
        contingency,
        [contingency.Init(campaign,
            [],
            [],
            None,
            TrueSubnode(),
            None,
            [CampaignClickNode().Init(campaign,
                conditiontobegin+[NotCondition(SaveVariableCondition(varname,-1)),NotCondition(SaveVariableCondition(varname,1)),AtMostActiveMissionsCondition()],
                [],
                sprite,
                TrueSubnode(),
                contingency,
                [getthemission,contingency]),
             CampaignClickNode().Init(campaign,
                conditiontobegin+[NotCondition(OrCondition(SaveVariableCondition(varname,-1),SaveVariableCondition(varname,1))),AtLeastActiveMissionsCondition()],
                speech["reminder"],
                sprite,
                TrueSubnode(script),
                contingency,
                []),
             CampaignNode().Init(campaign,
                [SaveVariableCondition(varname,-1)],
                [],
                None,
                GoToSubnode(0),
                None,
                [failurenode]),
             CampaignNode().Init(campaign,
                conditiontoend+[SaveVariableCondition(varname,1)],
                [],
                None,
                TrueSubnode(),
                None,
                [succeednode])])])
    return node

def MakeMission(campaign, sprite, conditiontobegin, conditiontoend, scriptonclick, script, missionname, missionargs, varname, speech, rejectnode, failurenode, succeednode, node=None, missiondesc="MakeMission"):
    #debug.debug("Called MakeMission with missiondesc := %s" % (missiondesc))
    if missiondesc == "MakeMission":
        missiondesc += " " + varname
    return MakeNoFailureMission(campaign,sprite,conditiontobegin,conditiontoend,scriptonclick,script,missionname,missionargs,varname,speech,rejectnode,
        CampaignClickNode().Init(campaign,
                    conditiontobegin,
                    speech["failure"],
                    sprite,
                    GoToSubnode(0),
                    None,
                    [failurenode]),succeednode,node,missiondesc)

def getCampaignList():
    import campaigns
    return campaigns.getCampaigns()

def getActiveCampaignNodes(room):
    campaigns=getCampaignList()
    clist=[]
    debug.debug("there are "+str(len(campaigns))+" campaigns")
    for campaign in campaigns:
        curnode=campaign.getCurrentNode(room)
        if curnode:
            debug.debug('*** found active node in campaign '+campaign.name)
            clist.append(curnode)
            debug.debug('checking contingency: '+str(curnode.checkPreconditions()))
            #return clist # The bar shouldn't have more than one campaign at a time.
        else:
            debug.debug('*** no active node for '+campaign.name)
    if (len(clist)):
        debug.debug('Nodes '+str(len(clist)))
    else:
        debug.debug('*** No node')

    for index in range(len(clist)):
        if (clist[index].spritelink):
            if (index!=0):
                tmp = clist[index]
                del clist[index]
                clist = [tmp]+clist;
            break
        if (clist[index].text and len(clist[index].text) and index!=0):
            tmp = clist[index]
            del clist[index]
            clist = [tmp]+clist;# doesn't change list length
    debug.debug(str(clist))
    return clist

#depends on Base
def getFixersToDisplay(room):
    debug.debug('*** Get the fixers to display!!!')
    global fixerloaded
    fixerloaded+=1
    cnodelist=getActiveCampaignNodes(room)
    fixerlist=[]
    for cnode in cnodelist:
        debug.debug('*** display it.')
        newfixer=cnode.getFixer(room)
        if newfixer:
            fixerlist.append(newfixer)
    return fixerlist

#depends on Base
def clickFixer(room):
    debug.debug('*** Clicked a fixer!!!')
    cnodelist=getActiveCampaignNodes(room)
    # Should only evaluate first one?
    for c in cnodelist:
        c.clickFixer(room)

#depends on Base
def clickChoice(room,choicenum):
    cnodelist=getActiveCampaignNodes(-1)
    # Should only evaluate first one?
    VS.StopAllSounds()
    for c in cnodelist:
        debug.debug('*** clicked on choice +'+str(choicenum)+': '+cnodelist[0].campaign.name)
        if (c.IsCampaignChoiceNode()):
            c.gotoChoice(room,choicenum)
            fixers.DestroyActiveButtons()
            break
