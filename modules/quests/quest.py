import Director
import debug


def getQuestLength(playernum, questname):
    return Director.getSaveDataLength(int(playernum),str(questname))

def findQuest (playernum, questname, value=1):
    debug.debug("finding nonpersistent quest: "+questname)
    mylen=getQuestLength(playernum,questname)
    debug.debug("mylen: %d" % (mylen))
    if (mylen>0):
        myfloat=Director.getSaveData(int(playernum),str(questname),0)
        debug.debug("myfloat: %f" % (myfloat))
        if (myfloat==value):
            return 1
    return 0

def checkSaveValue(playernum,questname,value=1):
    mylen=Director.getSaveDataLength(playernum,questname)
    debug.debug("mylen: %d" % (mylen))
    if (mylen>0):
        myfloat=Director.getSaveData(playernum,questname,0)
    else:
        myfloat=0
    if (myfloat==value):
        return 1
    return 0

def persistentQuest (playernum,questname):
    debug.debug("finding quest: "+questname)
    return findQuest (playernum,questname,-1)

def notLoadedQuest(playernum,questname):
    debug.debug("finding nonloaded quest: "+questname)
    return not persistentQuest(playernum,questname) and not findQuest(playernum,questname)

def removeQuest (playernum,questname,value=1):
    debug.debug("removing quest")
    mylen=Director.getSaveDataLength(int(playernum),str(questname))
    if (mylen>0):
        Director.putSaveData(int(playernum),str(questname),0,float(value))
    else:
        Director.pushSaveData(int(playernum),str(questname),float(value))


class quest:
    def NoSignificantsNear(self):
        pass
    def SignificantsNear(self,significant):
        pass
    def setOwner(self,playernum,questname):
        self.name=questname
        self.playernum=playernum
    def removeQuest(self,value=1):
        removeQuest(self.playernum,self.name,value)
    def makeQuestPersistent(self):
        self.removeQuest(-1)
    def isPersistent (self):
        return persistentQuest (self.playernum,self.name)
    def Execute(self):
        debug.debug("default")
        return 1


class quest_factory:
    def __init__(self,questname,remove_quest_on_run=0):
        self.removequest=remove_quest_on_run
        self.name=questname
    def __eq__(self,oth):
        return self.name==oth.name
    def create (self ):
        return quest()
    def precondition (self,playernum):
        return 1
    def persistent_factory(self,playernum):
        if (persistentQuest(playernum,self.name)):
            debug.debug("persistent_factory")
            return self.private_create(playernum)
        return
    def private_create (self,playernum):
        newquest=self.create()
        newquest.setOwner(playernum,self.name)
        if (self.removequest):
            removeQuest(playernum,self.name)
        return newquest
    def factory (self,playernum):
        if (self.precondition(playernum)):
            if (notLoadedQuest (playernum,self.name)):
                debug.debug("nonpfact")
                return self.private_create(playernum)
        return

class test_quest (quest):
    def __init__ (self):
        self.i=0
    def Execute (self):
        debug.debug("self.i: %d" % (self.i))
        self.i+=1
        if (self.i>100):
            self.removeQuest()
            return 0
        return 1

class test_quest_factory (quest_factory):
    def __init__ (self):
        quest_factory.__init__ (self, "drone_quest")
    def create (self):
        return test_quest()
