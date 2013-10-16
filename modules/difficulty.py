import Director
import VS
import debug
import sys

def usingDifficulty():
    return (VS.GetDifficulty()!=1.0)

def SetDiff(diff):
    if (diff>VS.GetDifficulty()):
        VS.SetDifficulty(diff)

unbounddiff=[]
_key="31337ness"

def getPlayerUnboundDifficulty (playa):
    global unbounddiff
    debug.debug('unbound diff '+str(unbounddiff)+' player '+str(playa))
    if (playa>=len(unbounddiff)):
        debug.info('Error: no difficulty set')
        return 0
    return unbounddiff[playa]

class difficulty:
    def SetDiff(self,diff):
        if (diff>VS.GetDifficulty()):
            VS.SetDifficulty(diff)

    def __init__(self,credsMax):
        debug.debug("init difficulty")
        global unbounddiff
        self.diff=[]
        unbounddiff=[]
        self.creds=[]
        self.credsToMax=credsMax
        debug.debug("unlogical start")
        un=VS.getPlayerX(0)
        debug.debug("unlogical end")
        self.i=0
        while (not un.isNull()):
            newunbounddiff=0
            newdiff=0
            debug.debug("get save data length")
            #(open ("/tmp/vswroteship","w")).close()
            diffsavelen=Director.getSaveDataLength(self.i,_key)
            if (diffsavelen):
                #(open ("/tmp/vsgotdata","w")).close()
                debug.debug("get save data")
                newdiff=Director.getSaveData(self.i,_key,0)
                if (diffsavelen>1):
                    newunbounddiff=Director.getSaveData(self.i,_key,1)
                else:
                    newunbounddiff=newdiff
                    Director.pushSaveData(self.i,_key,newunbounddiff)
                debug.debug("get save data end")
            else:
                #(open ("/tmp/vsmakedata","w")).close()
                debug.debug("get difficulty start")
                newdiff=VS.GetDifficulty()
                debug.debug("get difficulty done")
                Director.pushSaveData(self.i,_key,newdiff)
                newunbounddiff=newdiff
                Director.pushSaveData(self.i,_key,newunbounddiff)
            debug.debug("done director")
            #(open ("/tmp/vsdonedir","w")).close()
            #(open ("/tmp/vssetdifficulty","w")).close()
            self.diff.append(newdiff)
            unbounddiff.append(newunbounddiff)
            debug.debug("set diff start")
            SetDiff(newdiff)
            debug.debug("set diff end")
            self.creds+=[un.getCredits()]
            self.i+=1
            debug.debug("save unit")
            un=VS.getPlayerX(self.i)
            debug.debug("done init diff")
            #(open ("/tmp/vsdoneinitdiff","w")).close()
            debug.debug("done init diff FINAL")

    def usingDifficulty(self):
        return (VS.GetDifficulty()!=1.0)

    def getPlayerDifficulty(self,playa):
        return self.diff[playa]

    def Execute(self):
        global unbounddiff
        if (self.i>=len(self.creds)):
            self.i=0
        else:
            un=VS.getPlayerX(self.i)
            if (un):
                newcreds=un.getCredits()
                if (self.creds[self.i]!=newcreds):
                    if (self.creds[self.i]<newcreds):
                        delta=((newcreds-self.creds[self.i])/self.credsToMax)
                        newdiff=self.getPlayerDifficulty(self.i)+delta
                        debug.debug("delta: %.4f, newdiff: %.4f" % (delta, newdiff))
                        if (newdiff>.5999):
                            debug.debug("Clamped difficulty to 0.5999")
                            newdiff=.5999
                            #newdiff=1
                        Director.putSaveData(self.i,_key,0,newdiff)
                        SetDiff(newdiff)
                        unbounddiff[self.i]+=delta
                        Director.putSaveData(self.i,_key,1,unbounddiff[self.i])
                    self.creds[self.i]=newcreds
            self.i+=1
