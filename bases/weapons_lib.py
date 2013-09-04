import Base
import VS

TalkToStanForExtraShips = 1  # move generic shipdealer to showroom from upgrades

def CanX(disallowed):
    import universe
    sys = VS.getSystemFile()
    (name,fullname)=universe.getDockedBaseName()
    if sys in disallowed or (sys,name) in disallowed or (sys,fullname) in disallowed or name in disallowed or fullname in disallowed:
        return False
    return True
def CanRepair():
    norepair={
        "Liverpool":1,  #Gemini/Newcastle
        "Edom":1,   #Gemini/New_Constantinople
        "Oakham":1, #Gemini/Gemini/Pentonville
        "Rilke":1,  #Gemini/Varnus
        "Matahari":1,   #Gemini/Aldebran
        "Oresville":1,  #Gemini/Hinds_Variable_N
        "Joplin":1, #Gemini/XXN-1927
        "Erewhon":1,    #Gemini/Shangri_La
        "Trinsic":1,    #Gemini/Raxis
        "Elysia":1, #Gemini/Auriga
        "Wickerton":1,  #Gemini/Manchester
        "New_Reno":1,   #Gemini/ND-57
        "Vincent_Moon":1,   #Gemini/ND-57
        "Burton":1, #Gemini/Junction
        "Speke":1,  #Gemini/Junction
        "Romulus":1,    #Gemini/Castor
        "Remus":1,  #Gemini/Pollux
        "Saratov":1,    #Gemini/Prasepe
        "New_Iberia":1, #Gemini/Pyrenees
        "Kronecker":1,  #Gemini/Regallis
        "Megiddo":1,    #Gemini/Telar
        "Remus":1,  #Gemini/Pollux
        "Valkyrie":1,   #Gemini/Valhalla
        "Gaea":1,   #Gemini/Eden
        "Glasgow":1,    #Gemini/New_Caledonia
        "Smallville":1, #Gemini/KM-252
        "Drake":1,  #Gemini/Capella
        "Tuck's":1, #Gemini/Sherwood
        "Macabee":1,    #Gemini/Nexus
        "Munchen":1,    #Gemini/Tingerhoff
        "Charon":1, #Gemini/Hyades
        "Siva":1,   #Gemini/Rikel
        "Mjolnar":1,    #Gemini/Ragnarok
        }
    return CanX(norepair)

def MakeWeapon(concourse,timeofdayignored='_day', dealername="bases/repair_upgrade/shipdealer",upgradename='bases/repair_upgrade/shipupgrade',use_ship_320_240_upgrade=True):
    import VS
    VS.AdjustRelation("retro","privateer",-0.1,1.0)
    VS.AdjustRelation("kilrathi","privateer",-0.02,1.0)
    VS.AdjustRelation("pirates","privateer",-0.005,1.0)
    room = Base.Room ('Ship_Dealer')
    room1 = room
    Base.Texture (room, 'background', dealername+'.spr', 0, 0)
    Base.Texture (room, 'sd', 'bases/repair_upgrade/sd.spr', 0.002, -.0775)
    room = Base.Room ('Repair/Upgrade')
    room0 = room
    software= Base.Room('Software')
    Base.Texture(software,'background', 'bases/repair_upgrade/software.spr', 0, 0) #.582,-.2716)
    x=0.0
    y=0.0
    if use_ship_320_240_upgrade:
        x=0.0
        y=0.0
    Base.Texture (room, 'background', upgradename+'.spr', x, y)

    if use_ship_320_240_upgrade:
        Base.Ship (room, 'my_ship', (1.0,0.12,1.5), (0, 1, 0), (-0.85, 0.03, -0.89))


    if TalkToStanForExtraShips: # move generic shipdealer to showroom from upgrades
        Base.Comp (room0, 'my_comp_id', -0.855, -0.81, 0.6325, 0.663333, 'Upgrade/Repair', 'Upgrade Info ')
        Base.Comp (room1, 'my_comp_id3', -0.999, -.965, 0.35, 0.35,  'Look At Other Ships', 'ShipDealer Info ')
        else:
        Base.Comp (room0, 'my_comp_id', -0.855, -0.81, 0.6325, 0.663333, 'Upgrade/Repair', 'Upgrade ShipDealer Info ')
    Base.Link (room0, 'my_comp_id', -0.15, 0.2, 0.3375, 0.24, 'Software', software)
    Base.Comp (software, 'my_comp_id', -1, -0.75, 2.0, 1, 'Upgrade Computer(Radar Purchases)', 'Upgrade Info ')
    Base.Link (software, 'my_comp_id', -1, -.97333, 2.0, .2, 'Upgrade/Repair Room', room0)
    farris='#\nimport quest\nimport Base\nimport VS\ncp=VS.getCurrentPlayer()\nif (VS.getPlayer().getCredits()>2000):\n\tVS.getPlayer().addCredits(-2000)\n\tBase.Message("Thank you for purchasing the Farris quadrant map. 2000 credits has been deducted from your account.")\n\tquest.removeQuest(cp,"visited_Gemini/New_Caledonia",1.0)\n\tquest.removeQuest(cp,"visited_Gemini/Castor",1.0)\n\tquest.removeQuest(cp,"visited_Gemini/Sherwood",1.0)\n\tquest.removeQuest(cp,"visited_Gemini/Death",1.0)\n\tquest.removeQuest(cp,"visited_Gemini/Rygannon",1.0)\n\tquest.removeQuest(cp,"visited_Gemini/Xyanti",1.0)\n\tquest.removeQuest(cp,"visited_Gemini/Palan",1.0)\n\tquest.removeQuest(cp,"visited_Gemini/War",1.0)\n\tquest.removeQuest(cp,"visited_Gemini/J900",1.0)\n\tquest.removeQuest(cp,"visited_Gemini/KM-252",1.0)\n\tquest.removeQuest(cp,"visited_Gemini/Pestilence",1.0)\n\tquest.removeQuest(cp,"visited_Gemini/Telar",1.0)\n\tquest.removeQuest(cp,"visited_Gemini/Crab-12",1.0)\n\tquest.removeQuest(cp,"visited_Gemini/17-ar",1.0)\n\tquest.removeQuest(cp,"visited_Gemini/",1.0)\n\tquest.removeQuest(cp,"visited_Gemini/Capella",1.0)\n\tquest.removeQuest(cp,"visited_Gemini/Nexus",1.0)\n\tquest.removeQuest(cp,"visited_Gemini/Famine",1.0)\n\tquest.removeQuest(cp,"visited_Gemini/Regallis",1.0)\n\tquest.removeQuest(cp,"visited_Gemini/Valhalla",1.0)\nelse:\n\tBase.Message("Sorry, you don\'t have enough credits to buy this map. She sure is a fine map isn\'t she? I want to make a sale, you want to make a purchase. Lets look at the facts. I could use your other maps for tradein... plus your cash on hand--that still leaves you short.  Come back to me when you have more cash and we\'ll deal. And don\'t be embarrassed...these things happen.")\n'
    humboldt='#\nimport quest\nimport Base\nimport VS\ncp=VS.getCurrentPlayer()\nif (VS.getPlayer().getCredits()>2000):\n\tVS.getPlayer().addCredits(-2000)\n\tBase.Message("Thank you for purchasing the Humboldt quadrant map. 2000 credits has been deducted from your account.")\n\tquest.removeQuest(cp,"visited_Gemini/Freyja",1.0)\n\tquest.removeQuest(cp,"visited_Gemini/Junction",1.0)\n\tquest.removeQuest(cp,"visited_Gemini/Pollux",1.0)\n\tquest.removeQuest(cp,"visited_Gemini/Varnus",1.0)\n\tquest.removeQuest(cp,"visited_Gemini/CM-N1054",1.0)\n\tquest.removeQuest(cp,"visited_Gemini/Penders_Star",1.0)\n\tquest.removeQuest(cp,"visited_Gemini/Prasepe",1.0)\n\tquest.removeQuest(cp,"visited_Gemini/Padre",1.0)\n\tquest.removeQuest(cp,"visited_Gemini/Pyrenees",1.0)\n\tquest.removeQuest(cp,"visited_Gemini/119ce",1.0)\n\tquest.removeQuest(cp,"visited_Gemini/Troy",1.0)\nelse:\n\tBase.Message("Sorry, you don\'t have enough credits to buy this map. She sure is a fine map isn\'t she? I want to make a sale, you want to make a purchase. Lets look at the facts. I could use your other maps for tradein... plus your cash on hand--that still leaves you short.  Come back to me when you have more cash and we\'ll deal. And don\'t be embarrassed...these things happen")\n'
    clarke='#\nimport quest\nimport Base\nimport VS\ncp=VS.getCurrentPlayer()\nif (VS.getPlayer().getCredits()>2000):\n\tVS.getPlayer().addCredits(-2000)\n\tBase.Message("Thank you for purchasing the Clarke quadrant map. 2000 credits has been deducted from your account.")\n\tquest.removeQuest(cp,"visited_Gemini/Perry",1.0)\n\tquest.removeQuest(cp,"visited_Gemini/CMF-A",1.0)\n\tquest.removeQuest(cp,"visited_Gemini/Rikel",1.0)\n\tquest.removeQuest(cp,"visited_Gemini/Sumn_Kpta",1.0)\n\tquest.removeQuest(cp,"visited_Gemini/Surtur",1.0)\n\tquest.removeQuest(cp,"visited_Gemini/Midgard",1.0)\n\tquest.removeQuest(cp,"visited_Gemini/Blockade_Point_Tango",1.0)\n\tquest.removeQuest(cp,"visited_Gemini/Ragnarok",1.0)\n\tquest.removeQuest(cp,"visited_Gemini/Tingerhoff",1.0)\n\tquest.removeQuest(cp,"visited_Gemini/Lisacc",1.0)\n\tquest.removeQuest(cp,"visited_Gemini/Hyades",1.0)\n\tquest.removeQuest(cp,"visited_Gemini/Mah_Rahn",1.0)\n\tquest.removeQuest(cp,"visited_Gemini/Nitir",1.0)\n\tquest.removeQuest(cp,"visited_Gemini/Blockade_Point_Charlie",1.0)\n\tquest.removeQuest(cp,"visited_Gemini/Tr_Pakh",1.0)\n\tquest.removeQuest(cp,"visited_Gemini/Blockade_Point_Alpha",1.0)\nelse:\n\tBase.Message("Sorry, you don\'t have enough credits to buy this map. She sure is a fine map isn\'t she? I want to make a sale, you want to make a purchase. Lets look at the facts. I could use your other maps for tradein... plus your cash on hand--that still leaves you short.  Come back to me when you have more cash and we\'ll deal. And don\'t be embarrassed...these things happen")\n'
    potter='#\nimport quest\nimport Base\nimport VS\ncp=VS.getCurrentPlayer()\nif (VS.getPlayer().getCredits()>2000):\n\tVS.getPlayer().addCredits(-2000)\n\tBase.Message("Thank you for purchasing the Potter quadrant map. 2000 credits has been deducted from your account.")\n\tquest.removeQuest(cp,"visited_Gemini/Shangri_La",1.0)\n\tquest.removeQuest(cp,"visited_Gemini/Raxis",1.0)\n\tquest.removeQuest(cp,"visited_Gemini/XXN-1927",1.0)\n\tquest.removeQuest(cp,"visited_Gemini/ND-57",1.0)\n\tquest.removeQuest(cp,"visited_Gemini/Newcastle",1.0)\n\tquest.removeQuest(cp,"visited_Gemini/Oxford",1.0)\n\tquest.removeQuest(cp,"visited_Gemini/Manchester",1.0)\n\tquest.removeQuest(cp,"visited_Gemini/New_Detroit",1.0)\n\tquest.removeQuest(cp,"visited_Gemini/Hinds_Variable_N",1.0)\n\tquest.removeQuest(cp,"visited_Gemini/New_Constantinople",1.0)\n\tquest.removeQuest(cp,"visited_Gemini/DN-N1912",1.0)\n\tquest.removeQuest(cp,"visited_Gemini/Saxtogue",1.0)\n\tquest.removeQuest(cp,"visited_Gemini/Auriga",1.0)\n\tquest.removeQuest(cp,"visited_Gemini/Aldebran",1.0)\n\tquest.removeQuest(cp,"visited_Gemini/41-gs",1.0)\n\tquest.removeQuest(cp,"visited_Gemini/Metsor",1.0)\n\tquest.removeQuest(cp,"visited_Gemini/44-p-im",1.0)\nelse:\n\tBase.Message("Sorry, you don\'t have enough credits to buy this map. She sure is a fine map isn\'t she? I want to make a sale, you want to make a purchase. Lets look at the facts. I could use your other maps for tradein... plus your cash on hand--that still leaves you short.  Come back to me when you have more cash and we\'ll deal. And don\'t be embarrassed...these things happen")\n'
    Base.Python(software,'my_python_id',-1,.5,.4,.5,'Buy_Humboldt_Quadrant_Map',humboldt,True)
    Base.Python(software,'my_python_id',-.6,.5,.4,.5,'Buy_Farris_Quadrant_Map',farris,True)
    Base.Python(software,'my_python_id',-.2,.5,.4,.5,'Buy_Potter_Quadrant_Map',potter,True)
    Base.Python(software,'my_python_id',.2,.5,.4,.5,'Buy_Clarke_Quadrant_Map',clarke,True)
    Base.Python(software,'my_python_id',.6,.5,.4,.5,'Buy_All_Maps',"#\nimport VS\nVS.getPlayer().addCredits(2000)\n"+humboldt+farris+potter+clarke+"Base.Message('Thank you for purchasing all map quadrants.')",True)
    Base.Link (room0, 'my_link_id', -0.975, 0.26, 0.4375, 0.353333, 'Ship_Dealer', room1)
    Base.Python (room1, 'my_comp_id', -0.9925, -0.263333, 0.8875, 0.56, 'Buy Centurion', '#\nimport weapons_lib\nweapons_lib.ShipPurchase(\'centurion\')\n',True)
    Base.Python (room1, 'my_comp_id', -0.6825, -0.973333, 0.77, 0.516667, 'Buy Orion', '#\nimport weapons_lib\nweapons_lib.ShipPurchase(\'orion\')\n',True)
    Base.Python (room1, 'my_comp_id', 0.2925, -0.96, 0.68, 0.733333, 'Buy Galaxy', '#\nimport weapons_lib\nweapons_lib.ShipPurchase(\'galaxy\')\n',True)
    Base.Link (room1, 'my_to_sd_concourse_id',  -0.27, 0.466667, 0.1725, 0.293333, 'Return_To_Concourse',concourse)
    Base.Link (room1, 'my_to_upgrade_concourse_id',  0.415, 0.0533333, 0.3175, 0.24, 'Return_To_Concourse',concourse)
    Base.Link (room1, 'my_link_id', -0.0175, 0.336667, 0.66, 0.45, 'Upgrade_Ship', room0)
    return room1
def ShipPurchase(shipname):
    import Base
    import VS
    import fixers
    import campaign_lib
    campaign_lib.AddConversationStoppingSprite("Ship_Dealer","bases/heads/shipdealer.spr",(0,0),(3.2,2.0),"Return_To_Showroom").__call__(Base.GetCurRoom(),None)
    VS.StopAllSounds()
    if (VS.getPlayer().getName()==shipname or VS.getPlayer().getName()+".blank"==shipname or VS.getPlayer().getName()==shipname+".blank"):
        VS.playSound("sales/pitch"+shipname+"duplicate.wav",(0,0,0),(0,0,0))
    elif CanBuyShip(shipname+".blank"):
        fixers.CreateChoiceButtons(Base.GetCurRoom(),[
            fixers.Choice("bases/fixers/yes.spr","#\nimport fixers\nfixers.DestroyActiveButtons ()\nimport weapons_lib\nimport VS\nVS.StopAllSounds()\nweapons_lib.BuyShip('"+shipname+".blank')\n","Purchase "+shipname.capitalize()),
            fixers.Choice("bases/fixers/no.spr","#\nimport fixers\nfixers.DestroyActiveButtons ()\nimport VS\nVS.StopAllSounds()\nVS.playSound('sales/pitch"+shipname+"reject.wav',(0,0,0),(0,0,0))\n","Decline Purchasing")])
        VS.playSound("sales/pitch"+shipname+".wav",(0,0,0),(0,0,0))
    else:
        VS.playSound("sales/pitchnotenoughmoney.wav",(0,0,0),(0,0,0))
        Base.Message("I hate to break it to you, but we've checked your account, and you don't have enough credits to buy this ship. She sure is a fine ship though, isn't she? Listen, I want to make a sale, you want to make a purchase, lets look at the facts. You know the retail of this ship--we can use your ship for tradeins, plus extras--including your cash on hand, that still leaves you short.  Go get some more cash, and come back when you have more cash, and don't feel embarrassed: these things happen!")
def ShipValue(shipname, used):
    import VS
    carg=VS.GetMasterPartList().GetCargo(shipname)
    price=carg.GetPrice()
    if used:
        try:
            price*=float(VS.vsConfig("economics","ship_sellback_price",".5"))
        except:
            price*=.5
    return price
def CargoValue(un):
    numcarg=un.numCargo()
    tot=0
    for i in range(numcarg):
        c=un.GetCargoIndex(i)
        if c.GetCategory().find("upgrades")==0:
            tot+=c.GetPrice()*c.GetQuantity()*.5
    return tot;
def CanBuyShip(shipname):
    import VS
    creds=VS.getPlayer().getCredits()
    return creds+ShipValue(VS.getPlayer().getName(),True)+CargoValue(VS.getPlayer())>=ShipValue(shipname,False)
def BuyShip(shipname):
    import VS
    import Base
    name=VS.getPlayer().getName()
    value=CargoValue(VS.getPlayer())+ShipValue(name,True)
    oldcargo=[]
    oldun=VS.getPlayer()
    for i in range(oldun.numCargo()):
        c=oldun.GetCargoIndex(i)
        if c.GetCategory().find("upgrades")!=0:
            oldcargo.append(c)
    #print value
    #print VS.getPlayer().getCredits()
    success=Base.BuyShip(shipname,False,True)
    if (success!=False):
        
                VS.getPlayer().addCredits(value)
        Base.SellShip(name)
        #print VS.getPlayer().getCredits()
        #VS.getPlayer().addCredits(-ShipValue(shipname,False))
        #print VS.getPlayer().getCredits()
        #for carg in oldcargo:
        #   VS.getPlayer().addCargo(carg)
        where=shipname.find(".blank")
        if (where!=-1):
            shipname=shipname[0:where]
        VS.playSound('sales/pitch'+shipname+'accept.wav',(0,0,0),(0,0,0))
        return True
    else:
        where=shipname.find(".blank")
        if (where!=-1):
            shipname=shipname[0:where]
        VS.playSound("sales/pitch"+shipname+"duplicate.wav",(0,0,0),(0,0,0))        
        return False
