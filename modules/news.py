import VS
import vsrandom
import universe
import Director
import dynamic_news
global dnewsman_
dnewsman_ = dynamic_news.NewsManager()
def saveVal(str):
    return Director.getSaveData(VS.getMissionOwner(),str,0)

class NotZero:
    def __init__ (self,str):
        self.str = str
    def __nonzero__ (self):
        print 'nonzeroing'
        return saveVal(self.str)!=0
class IsZero:
    def __init__ (self,str):
        self.str = str
    def __nonzero__ (self):
        print 'nonzeroing'
        return saveVal(self.str)==0
class GreaterZero:
    def __init__ (self,str):
        self.str = str
    def __nonzero__ (self):
        print 'nonzeroing'
        return saveVal(self.str)>0
class LessZero:
    def __init__ (self,str):
        self.str = str
    def __nonzero__ (self):
        print 'nonzeroing'
        return saveVal(self.str)<0


news =( ('hoffman_blobs',(NotZero('NEVAH_THIS_WILL_NEVER_BE_TRUE_TILL_THE_HOMEBOY_DIES'),),"HOFFMAN'S BLOBS SPOTTED:   A flock of the strange space creatures known as 'Hoffman's Blobs' were observed in the Galileo System, resulting in the sixth sighting of these bizarre interstellar beings since they were first seen by Bruno Hoffman in Barnard's Star 53 years ago. Scientists are now flocking to study the seemingly non-sentient creatures before they leave, attempting to determine how it is that they are able to sustain themselves in the void of space. From previous observations, it appears they travel in flocks of about a dozen units, often varying in size with the largest being as large as a space cruiser, and the smallest only the size of a shuttlecraft. The animals make their way through the cosmos by 'warping' through space in a way that baffles the scientists."),
        )
def newNews():
    if (vsrandom.randrange(0,2)!=0):
        return
    newsitem = vsrandom.randrange (0,len(news))
    newsitem = news[newsitem]
    player = VS.getMissionOwner()
    for conditional in newsitem[1]:
        print 'conditioning'
        if (not conditional):
            return
    universe.setFirstSaveData(player,newsitem[0],1)
    import Director
    Director.pushSaveString(player,"dynamic_news",'#'+newsitem[2])
#    VS.IOmessage(0,"game","news",newsitem[2])


def eraseNews(plr):
    import Director
    len = Director.getSaveStringLength(plr,"news")
    for i in range(len):
        Director.eraseSaveString(plr,"news",len-i-1)

def processNews(plr):
    eraseNews(plr)
    import Director
    howmuchnews=Director.getSaveStringLength(plr,"dynamic_news")
    minnews=0
    print "Processing News"
    global dnewsman_
    dnewsman_.updateDockedAtFaction()
    if (howmuchnews>4000):
        minnews=howmuchnews-4000
    for i in range (minnews,howmuchnews):
        noos=Director.getSaveString(plr,"dynamic_news",i)
        if (len(noos)):
            if (noos.startswith('#')):
                Director.pushSaveString(plr,"news",noos[1:])
            elif dnewsman_.isStoryRelevant(noos):
                noos = dnewsman_.translateDynamicString(noos)
                if noos:
                    Director.pushSaveString(plr,"news",noos)

def eraseNewsItem(plr,item):
    """removes the first news item matching the given item from
    plr's "dynamic_news" save variable"""
#    print "FIXME: someone please write a function to this spec! Every thing I try seems to produce some random result :-/"
    import Director
    for i in range (Director.getSaveStringLength(plr,"dynamic_news")):
        noos=Director.getSaveString(plr,"dynamic_news",i)
        if noos == item:
            Director.eraseSaveString(plr,"dynamic_news",i)
            return
