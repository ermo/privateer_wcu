#Changing the order of factions or removing any without starting a new game is not recommended. Adding to the end of this list should be fine.
factions = ["confed","kilrathi","nephilim","merchant","retro","pirates","hunter","militia","unknown","landreich","border_worlds","firekkan","AWACS", "confed_", "confed__", "kilrathi_", "kilrathi__", "merchant_", "merchant__", "retro_", "retro__", "pirates_", "pirates__", "hunter_", "hunter__", "militia_", "militia__", "civilian"]
notfactions = [] #Factions in factions.xml but not in the above for whatever reason.
import VS
for i in range (VS.GetNumFactions()):
    fac = VS.GetFactionName(i)
    if fac not in factions:
        notfactions += [fac]
#notfactions += ["neutral","privateer","steltek","upgrades","planets","seelig","kroiz","miggs","toth","garrovick","reismann"]

missionfactions = [] #List of factions used only in missions
factiondict={} #Dictionary to find the faction number from its name
for i in range(len(factions)):
    factiondict[factions[i]]=i
    #Generate variables named as the faction names with the index values.
    exec(factions[i]+"="+str(i))
    if factions[i].endswith("_"): #Those that end with _ are mission factions
        missionfactions.append(factions[i])

generateRandomShips={} # Should we randomly generate ships of this faction anywhere?
for f in factions:
    generateRandomShips[f]=False #Put default false value.
for f in notfactions:
    generateRandomShips[f]=False #Put default false value.
#Put back to true for those we want to generate.
generateRandomShips["confed"]=True
generateRandomShips["kilrathi"]=True
generateRandomShips["merchant"]=True
generateRandomShips["retro"]=True
generateRandomShips["pirates"]=True
generateRandomShips["hunter"]=True
generateRandomShips["militia"]=True
generateRandomShips["AWACS"]=True

factionsToGenerate=[] #Make a list of factions that generate ships.
for f in factions:
    if f in generateRandomShips and generateRandomShips[f]:
        factionsToGenerate.append(f)
factionsInNormalMissions=factionsToGenerate #List of factions that offer missions.

at_least_one_producer={"AWACS":1,"retro":1}
#fortress_systems={"Gemini/Perry":1-.0625, "Gemini/New_Constantinople":1-.0625, "Gemini/New_Detroit":1-.0625, "Gemini/Troy":.3125,"Gemini/Eden":1.0,"Gemini/Beta":1.0,"Gemini/Delta":1.0,"Gemini/Gamma":1.0,"Gemini/Palan":1.0,"Gemini/Delta_Prime":1.0,"Gemini/Sherwood":1.0,"Gemini/Pentonville":1.0,"Gemini/Tr_Pakh":0.5}
#fortress_systems={"Gemini/Perry":.3125, "Gemini/New_Constantinople":.3125, "Gemini/New_Detroit":.3125, "Gemini/Troy":.3125,"Gemini/Eden":1.0,"Gemini/Beta":1.0,"Gemini/Delta":1.0,"Gemini/Gamma":1.0,"Gemini/Palan":1.0,"Gemini/Delta_Prime":1.0,"Gemini/Sherwood":1.0,"Gemini/Pentonville":1.0,"Gemini/Tr_Pakh":0.5}
fortress_systems={"Gemini/Eden":1.0}

max_flightgroups={"Gemini/Troy":2,"Gemini/Penders_Star":3,"Gemini/Junction":6,"Gemini/New_Detroit":12,"Gemini/New_Constantinople":12,"Gemini/Perry":6}
min_flightgroups={"Gemini/Troy":0,"Gemini/Penders_Star":0,"Gemini/Junction":2,"Gemini/New_Detroit":4,"Gemini/New_Constantinople":4,"Gemini/Perry":2}

invincible_systems={
    "Gemini/119ce":1,
    "Gemini/17-ar":1,
    "Gemini/41-gs":1,
    "Gemini/44-p-im":1,
    "Gemini/Aldebran":1,
    "Gemini/Auriga":1,
    "Gemini/Beta":1,
    "Gemini/Blockade_Point_Alpha":1,
    "Gemini/Blockade_Point_Tango":1,
    "Gemini/Capella":1,
    "Gemini/Castor":1,
    "Gemini/CM-N1054":1,
    "Gemini/CMF-A":1,
    "Gemini/Crab-12":1,
    "Gemini/Death":1,
    "Gemini/Delta":1,
    "Gemini/Delta_Prime":1,
    "Gemini/DN-N1912":1,
    "Gemini/Eden":1,
    "Gemini/Famine":1,
    "Gemini/Freyja":1,
    "Gemini/Gamma":1,
    "Gemini/Gemini":1,
    "Gemini/Hinds_Variable_N":1,
    "Gemini/Hyades":1,
    "Gemini/J900":1,
    "Gemini/Junction":1,
    "Gemini/KM-252":1,
    "Gemini/Lisacc":1,
    "Gemini/Mah_Rahn":1,
    "Gemini/Manchester":1,
    "Gemini/Metsor":1,
    "Gemini/Midgard":1,
    "Gemini/ND-57":1,
    "Gemini/New_Caledonia":1,
    "Gemini/New_Constantinople":1,
    "Gemini/New_Detroit":1,
    "Gemini/Newcastle":1,
    "Gemini/Nexus":1,
    "Gemini/Nitir":1,
    "Gemini/Oxford":1,
    "Gemini/Padre":1,
    "Gemini/Palan":1,
    "Gemini/Penders_Star":1,
    "Gemini/Pentonville":1,
    "Gemini/Perry":1,
    "Gemini/Pestilence":1,
    "Gemini/Pollux":1,
    "Gemini/Prasepe":1,
    "Gemini/Pyrenees":1,
    "Gemini/Ragnarok":1,
    "Gemini/Raxis":1,
    "Gemini/Regallis":1,
    "Gemini/Rikel":1,
    "Gemini/Rygannon":1,
    "Gemini/Saxtogue":1,
    "Gemini/Shangri_La":1,
    "Gemini/Sherwood":1,
    "Gemini/Sumn_Kpta":1,
    "Gemini/Surtur":1,
    "Gemini/Telar":1,
    "Gemini/Tingerhoff":1,
    "Gemini/Tr_Pakh":1,
    "Gemini/Troy":1,
    "Gemini/Valhalla":1,
    "Gemini/Varnus":1,
    "Gemini/War":1,
    "Gemini/XXN-1927":1,
    "Gemini/Xytani":1,
    "TrkPahn/SumnHhra":1,
    "TrkPahn/SumTlor":1,
    "TrkPahn/TKTarak":1,
    "TrkPahn/NDerPak":1,
    "TrkPahn/Draga":1,
    "TrkPahn/Zarnobian":1,
    "TrkPahn/TrkPhan":1,
    "TrkPahn/Bukrag":1,
    "VukarTag/KvtTag(4)":1,
    "VukarTag/KvtTag(2)":1,
    "VukarTag/Jugara":1,
    "Kilrah/Khrissak":1,
    "Kilrah/Kssak":1,
    "Kilrah/HrissthHrissith":1,
    "Kilrah/Kilrah":1,
    "Kilrah/TlanMeth":1,
    "Kilrah/KCris":1,
    "Kilrah/Mshren":1,
    "Kilrah/GwrissKrazna":1,
    "Kilrah/Kurukhag(3)":1,
    "Kilrah/Hrekkah":1,
    "Kilrah/HhrassTGhor":1,
    "Kilrah/KnTqal":1,
    "MShrak/TrKHhra(1)":1,
    "MShrak/Gorth":1,
    "MShrak/Paghk":1,
    "MShrak/Dathque(4)":1,
    "Epsilon/Ingraya":1,
    "Epsilon/Jakal":1,
    "Epsilon/Asgard":1,
    "Epsilon/Dvdtang":1,
    "Epsilon/KkThan":1,
    "Epsilon/KkTahn":1,
    "Epsilon/Shariha":1,
    "Epsilon/Khar-Sa":1,
    "Epsilon/TvxAq":1,
    "Landreich/Halgkrak(4)":1,
    "Landreich/Hralgkrak(4)":1,
    "Landreich/Vordran":1,
    "Landreich/Jigada":1,
    "Landreich/Khrovat":1,
    "Landreich/Halgkrak(9)":1,
    "Landreich/Hralgkrak(9)":1,
    "Landreich/M421A":1,
    "Sol/Mastif":1,
    "Sol/Arcturus":1,
    "Sol/ProximaCentauri":1,
    "Sol/Sol":1,
    "Sol/Tikopal":1,
    "Sol/Luyten":1,
    "Sol/Beacon":1,
    "Enigma/Vespus":1,
    "Enigma/AxiusAxis":1,
    "Enigma/FiddlersGreen":1,
    "Enigma/CallimachusCallmachius":1,
    "Enigma/HeavensGate":1,
    "Enigma/Salayna":1,
    "Enigma/Adams":1,
    "Enigma/Blake":1,
    "Enigma/Heinlein":1,
    "Enigma/Dyson":1,
    "Argent/Benford":1,
    }

siegingfactions={
#   "confed":77, #500,
#   "kilrathi":77, #1600,
#   "merchant":77, #500,
#   "retro":77, #1000,
#   "pirates":77, #1000,
#   "hunter":77, #500,
#   "militia":77, #1000,
#   "landreich":77, #10000,
#   "border_worlds":77, #4000,
#   "AWACS":77, #30,
    }

fightersPerFG={
    "confed":3,
    "kilrathi":3,
    "merchant":2,
    "retro":2,
    "pirates":2,
    "hunter":2,
    "militia":2,
    "landreich":2,
    "border_worlds":2,
    "firekkan":2,
    "AWACS":2,
    }

staticFighterProduction={"retro":1, "pirates":1, "default":0}

fighterProductionRate={
    "confed":0.05,
    "landreich":0.00001,
    "border_worlds":0.00001,
    "kilrathi":0.03,
    "retro":0.03,
    "merchant":0.03,
    "pirates":0.05,
    "hunter":0.05,
    "militia":0.03,
    "default":0.05,
    "firekkan":0.00001,
    "AWACS":0.02,
    }

capitalProductionRate={
    "confed":0.007,
    "landreich":0.001,
    "border_worlds":0.001,
    "kilrathi":0.004,
    "retro":0.00001,
    "merchant":0.08,
    "pirates":0.00001,
    "hunter":0.00001,
    "militia":0.00001,
    "default":0.002,
    "firekkan":0.003,
    "AWACS":0.0025,
    }

homeworlds={
    "confed":"Sol/Sol",
    "kilrathi":"Kilrah/Kilrah",
    "nephilim":"Enigma/Shanha",
    "pirates":"Gemini/Pentonville",
    "merchant":"Gemini/New_Detroit",
    "militia":"Gemini/Junction",
    "retro":"Gemini/Eden",
    "hunter":"Sol/AlphaCentauri",
    "firekkan":"Epsilon/Firekka",
    "border_worlds":"Epsilon/Deneb",
    "landreich":"Landreich/Landreich",
    "AWACS":"Gemini/Auriga",
    "civilian":"Gemini/Metsor"
    }

production_centers={
    "confed":["Gemini/Perry","Gemini/New_Constantinople","Gemini/Ragnarok","Gemini/Nitir","Gemini/Surtur","Gemini/Tingerhoff","Gemini/Blockade_Point_Alpha","Gemini/Blockade_Point_Charlie","Gemini/Blockade_Point_Tango"],
    "kilrathi":["Gemini/Gamma","Gemini/Tr_Pakh","Gemini/Sumn_Kpta","Gemini/Mah_Rahn","Gemini/Lisacc","Gemini/ND-57"],
    "nephilim":["Enigma/Shanha"],
    "pirates":["Gemini/Pentonville","Gemini/KM-252","Gemini/Sherwood","Gemini/Telar","Gemini/Capella","Gemini/Delta","Gemini/Pestilence","Gemini/Penders_Star"],
    "merchant":["Gemini/J900","Gemini/Pyrenees","Gemini/Freyja","Gemini/Junction","Gemini/Aldebran","Gemini/Oxford","Gemini/New_Detroit","Gemini/Palan"],
    "militia":["Gemini/New_Constantinople","Gemini/XXN-1927","Gemini/Junction","Gemini/Regallis","Gemini/NewCaledonia"],
    "retro":["Gemini/Eden","Gemini/Shangri_La"],
    "hunter":["Gemini/Palan","Gemini/Penders_Star","Gemini/New_Detroit"],
    "firekkan":["Epsilon/Firekka"],
    "border_worlds":["Epsilon/Deneb"],
    "landreich":["Landreich/Landreich"],
    "AWACS":["Gemini/Auriga","Gemini/XXN-1927"],
        "civilian":[]
    }

useBlank = [] #If the faction should use the .blank version of ships.
for i in range(len(factions)): useBlank.append(0) #Add default values so entries below can be in arbitrary order.
useBlank[confed]=0
useBlank[kilrathi]=0
useBlank[nephilim]=0
useBlank[merchant]=0
useBlank[retro]=0
useBlank[pirates]=0
useBlank[hunter]=0
useBlank[militia]=0
useBlank[unknown]=0
useBlank[landreich]=0
useBlank[border_worlds]=0
useBlank[firekkan]=0
useBlank[AWACS]=0
#Keep entries who reference other entries below those referenced! Actual array position is set by the first parameter.
useBlank[confed_]=useBlank[confed]
useBlank[confed__]=useBlank[confed]
useBlank[kilrathi_]=useBlank[kilrathi]
useBlank[kilrathi__]=useBlank[kilrathi]
useBlank[merchant_]=useBlank[merchant]
useBlank[merchant__]=useBlank[merchant]
useBlank[retro_]=useBlank[retro]
useBlank[retro__]=useBlank[retro]
useBlank[pirates_]=useBlank[pirates]
useBlank[pirates__]=useBlank[pirates]
useBlank[hunter_]=useBlank[hunter]
useBlank[hunter__]=useBlank[hunter]
useBlank[militia_]=useBlank[militia]
useBlank[militia__]=useBlank[militia]
useBlank[civilian]=useBlank[merchant]

enemies = []
for i in range(len(factions)): enemies.append([unknown]) #Add default values so entries below can be in arbitrary order.
enemies[confed]=[kilrathi,kilrathi,kilrathi,kilrathi,kilrathi,kilrathi,kilrathi,kilrathi,retro,retro,retro,retro,retro,retro,retro,pirates]
enemies[kilrathi]=[confed,confed,confed,confed,confed,confed,militia,militia,militia,militia,hunter,hunter,hunter,merchant,merchant,pirates]
enemies[nephilim]=[kilrathi,kilrathi,kilrathi,kilrathi,kilrathi,kilrathi,kilrathi,kilrathi,pirates,retro,retro,retro,retro,retro,hunter]
enemies[merchant]=[pirates,pirates,retro,kilrathi]
enemies[retro]=[hunter,hunter,hunter,hunter,hunter,militia,militia,militia,pirates,pirates]
enemies[pirates]=[merchant,merchant,merchant,merchant,merchant,merchant,merchant,merchant,merchant,merchant,merchant,retro,retro,militia]
enemies[hunter]=[pirates,pirates,pirates,pirates,pirates,retro,retro,retro,kilrathi,kilrathi]
enemies[militia]=[retro,pirates,retro,pirates,retro,pirates,kilrathi,kilrathi]
enemies[unknown]=[confed,kilrathi,merchant,retro,pirates,hunter,militia]
enemies[landreich]=[kilrathi,kilrathi,kilrathi,kilrathi,kilrathi,kilrathi,kilrathi,kilrathi,retro,pirates]
enemies[border_worlds]=[kilrathi,kilrathi,kilrathi,kilrathi,kilrathi,kilrathi,kilrathi,kilrathi,retro,pirates]
enemies[firekkan]=[kilrathi,kilrathi,kilrathi,kilrathi,kilrathi,kilrathi,kilrathi,kilrathi,retro,pirates]
enemies[AWACS]=[confed,confed,confed,confed,confed,militia,militia,militia,militia,hunter,hunter,hunter,kilrathi,kilrathi,retro,retro]
#Keep entries who reference other entries below those referenced! Actual array position is set by the first parameter.
enemies[confed_]=enemies[confed]
enemies[confed__]=enemies[confed]
enemies[kilrathi_]=enemies[kilrathi]
enemies[kilrathi__]=enemies[kilrathi]
enemies[merchant_]=enemies[merchant]
enemies[merchant__]=enemies[merchant]
enemies[retro_]=enemies[retro]
enemies[retro__]=enemies[retro]
enemies[pirates_]=enemies[pirates]
enemies[pirates__]=enemies[pirates]
enemies[hunter_]=enemies[hunter]
enemies[hunter__]=enemies[hunter]
enemies[militia_]=enemies[militia]
enemies[militia__]=enemies[militia]
enemies[civilian]=enemies[merchant]

rabble = []
for i in range(len(factions)): rabble.append([unknown]) #Add default values so entries below can be in arbitrary order.
rabble[confed]=[retro,retro,retro,retro,pirates,pirates,pirates,pirates,pirates,pirates,pirates,pirates,pirates,retro,retro,retro,retro,pirates,pirates,pirates,pirates,pirates,pirates,pirates,pirates,pirates,retro,retro,retro,retro,pirates,pirates,pirates,pirates,pirates,pirates,pirates,pirates,pirates] #confed
rabble[kilrathi]=[pirates,pirates,pirates,hunter,hunter,pirates,pirates,pirates,hunter,hunter]
rabble[nephilim]=[pirates,pirates,pirates,pirates,kilrathi,confed,hunter,hunter,hunter]
rabble[merchant]=[pirates,retro,pirates,retro,pirates,hunter,merchant]
rabble[retro]=[unknown,unknown,unknown,pirates,hunter]
rabble[pirates]=[hunter,retro,retro,pirates,pirates,pirates,merchant]
rabble[hunter]=[pirates,retro,hunter,hunter,hunter]
rabble[militia]=[retro,retro,pirates,pirates,pirates]
rabble[unknown]=[pirates,pirates,pirates,pirates,retro,kilrathi]
rabble[landreich]=[retro,militia]
rabble[border_worlds]=[retro,retro,retro,kilrathi]
rabble[firekkan]=[retro,retro,pirates]
rabble[AWACS]=[confed,militia,retro,retro,hunter,hunter,hunter]
#Keep entries who reference other entries below those referenced! Actual array position is set by the first parameter.
rabble[confed_]=rabble[confed]
rabble[confed__]=rabble[confed]
rabble[kilrathi_]=rabble[kilrathi]
rabble[kilrathi__]=rabble[kilrathi]
rabble[merchant_]=rabble[merchant]
rabble[merchant__]=rabble[merchant]
rabble[retro_]=rabble[retro]
rabble[retro__]=rabble[retro]
rabble[pirates_]=rabble[pirates]
rabble[pirates__]=rabble[pirates]
rabble[hunter_]=rabble[hunter]
rabble[hunter__]=rabble[hunter]
rabble[militia_]=rabble[militia]
rabble[militia__]=rabble[militia]
rabble[civilian]=rabble[merchant]

insysenemies = enemies

friendlies=[]
for i in range(len(factions)): friendlies.append([unknown]) #Add default values so entries below can be in arbitrary order.
friendlies[confed]=[confed,confed,confed,confed,confed,confed,confed,confed,confed,confed,militia,militia,militia,militia,merchant,merchant,merchant,merchant,merchant]
friendlies[kilrathi]=[kilrathi,kilrathi,kilrathi,kilrathi,kilrathi,kilrathi,kilrathi,kilrathi,kilrathi,kilrathi,kilrathi,kilrathi,kilrathi,kilrathi]
friendlies[nephilim]=[merchant,nephilim,nephilim,nephilim,nephilim,merchant,nephilim,nephilim,nephilim,nephilim]
friendlies[merchant]=[confed,militia,militia,militia,militia,merchant,merchant,merchant,merchant,merchant,hunter,hunter]
friendlies[retro]=[retro,retro,retro,unknown]
friendlies[pirates]=[pirates,pirates,pirates,pirates,pirates]
friendlies[hunter]=[confed,confed,militia,militia,merchant,hunter,hunter,hunter,hunter,hunter,merchant]
friendlies[militia]=[confed,confed,confed,militia,militia,militia,militia,merchant,merchant,merchant,merchant,merchant]
friendlies[unknown]=[pirates,retro,retro,retro,retro,retro,retro,retro,retro,unknown]
friendlies[landreich]=[landreich,landreich,pirates,merchant,merchant,merchant,border_worlds,border_worlds,border_worlds,border_worlds]
friendlies[border_worlds]=[landreich,landreich,militia,merchant,merchant,border_worlds,border_worlds,border_worlds,border_worlds]
friendlies[firekkan]=[confed,confed,confed,militia,militia,militia,militia,merchant,merchant,merchant,merchant,merchant,landreich,border_worlds,firekkan,firekkan]
friendlies[AWACS]=[AWACS,AWACS,merchant]
#Keep entries who reference other entries below those referenced! Actual array position is set by the first parameter.
friendlies[confed_]=friendlies[confed]
friendlies[confed__]=friendlies[confed]
friendlies[kilrathi_]=friendlies[kilrathi]
friendlies[kilrathi__]=friendlies[kilrathi]
friendlies[merchant_]=friendlies[merchant]
friendlies[merchant__]=friendlies[merchant]
friendlies[retro_]=friendlies[retro]
friendlies[retro__]=friendlies[retro]
friendlies[pirates_]=friendlies[pirates]
friendlies[pirates__]=friendlies[pirates]
friendlies[hunter_]=friendlies[hunter]
friendlies[hunter__]=friendlies[hunter]
friendlies[militia_]=friendlies[militia]
friendlies[militia__]=friendlies[militia]
friendlies[civilian]=friendlies[merchant]

fighters = []
for i in range(len(factions)): fighters.append(["talon"]) #Add default values so entries below can be in arbitrary order.
fighters[confed]=["stiletto","stiletto","stiletto","stiletto","gladius","gladius","gladius","gladius","broadsword","broadsword","sabre","scimitar","hornet","raptor"] #confed
fighters[kilrathi]=["dralthi","dralthi","dralthi","dralthi","dralthi","dralthi","dralthi","dralthi","dralthi","dralthi","gothri","gothri","gothri","gothri","krant","sartha","grikath"] #kilrathi
fighters[nephilim]=["steltek_fighter"] #nephilim
fighters[merchant]=["galaxy","galaxy","galaxy","galaxy","galaxy","galaxy","galaxyhk","tarsus","tarsus","tarsus","tarsusMk2","orion","orionMk2"] #merchant
fighters[retro]=["talon"] #retro
fighters[pirates]=["talon"] #pirates
fighters[hunter]=["demon","demon","demon","demon","demon","orion","orion","orionMk2","centurion","centurion","fireblade"] #hunter
fighters[militia]=["talon","talon","talon","talon","talon","talon","talon","talon","talon","gladius","gladius","gladius","ferret","hornet"] #militia
fighters[unknown]=["salthi","salthi.particle"] #unknown
fighters[landreich]=["tarsus","gladius","talon","talon","talon","drayman"]#landreich
fighters[border_worlds]=["tarsus","gladius","talon","talon","talon","drayman"]#border_worlds
fighters[firekkan]=["stiletto"] #firekkan
fighters[AWACS]=["stiletto"] #AWACS
#Keep entries who reference other entries below those referenced! Actual array position is set by the first parameter.
fighters[confed_]=fighters[confed]
fighters[confed__]=fighters[confed]
fighters[kilrathi_]=fighters[kilrathi]
fighters[kilrathi__]=fighters[kilrathi]
fighters[merchant_]=fighters[merchant]
fighters[merchant__]=fighters[merchant]
fighters[retro_]=fighters[retro]
fighters[retro__]=fighters[retro]
fighters[pirates_]=fighters[pirates]
fighters[pirates__]=fighters[pirates]
fighters[hunter_]=fighters[hunter]
fighters[hunter__]=fighters[hunter]
fighters[militia_]=fighters[militia]
fighters[militia__]=fighters[militia]

isBomber = {"broadsword":2,"gladius":4,"gothri":6,"grikath":8}

capitals = []
for i in range(len(factions)): capitals.append(["draymen"]) #Add default values so entries below can be in arbitrary order.
capitals[confed]=["paradigm","paradigm","paradigm","paradigm"]
capitals[kilrathi]=["kamekh","kamekh"]
capitals[nephilim]=["drone"]
capitals[merchant]=["drayman","drayman"]
capitals[retro]=["drayman"]
capitals[pirates]=["drayman"]
capitals[hunter]=["drayman"]
capitals[militia]=["draymanCVL"]
capitals[unknown]=["drayman"]
capitals[landreich]=["drayman"]
capitals[border_worlds]=["paradigm","paradigm","paradigm"]
capitals[firekkan]=["drayman"]
capitals[AWACS]=["drayman","drayman","drayman","paradigm"]
#Keep entries who reference other entries below those referenced! Actual array position is set by the first parameter.
capitals[confed_]=capitals[confed]
capitals[confed__]=capitals[confed]
capitals[kilrathi_]=capitals[kilrathi]
capitals[kilrathi__]=capitals[kilrathi]
capitals[merchant_]=capitals[merchant]
capitals[merchant__]=capitals[merchant]
capitals[retro_]=capitals[retro]
capitals[retro__]=capitals[retro]
capitals[pirates_]=capitals[pirates]
capitals[pirates__]=capitals[pirates]
capitals[hunter_]=capitals[hunter]
capitals[hunter__]=capitals[hunter]
capitals[militia_]=capitals[militia]
capitals[militia__]=capitals[militia]

escortableships = [] # ideally capships with a low combat rating, so transports etc.
for i in range(len(factions)): escortableships.append(["draymen"]) #Add default values so entries below can be in arbitrary order.
escortableships[confed]=["drayman"] #confed
escortableships[kilrathi]=["kamekh"] #kilrathi
escortableships[nephilim]=["drone"] #nephilim
escortableships[merchant]=["drayman"] #merchant
escortableships[retro]=["drayman"] #retro
escortableships[pirates]=["drayman"] #pirates
escortableships[hunter]=["drayman"] #hunter
escortableships[militia]=["drayman"] #militia
escortableships[unknown]=["drayman"] #unknown
escortableships[landreich]=["drayman"] #landreich
escortableships[border_worlds]=["drayman"] #border_worlds
escortableships[firekkan]=["drayman"] #firekkan
escortableships[AWACS]=["drayman"] #AWACS
#Keep entries who reference other entries below those referenced! Actual array position is set by the first parameter.
escortableships[confed_]=escortableships[confed]
escortableships[confed__]=escortableships[confed]
escortableships[kilrathi_]=escortableships[kilrathi]
escortableships[kilrathi__]=escortableships[kilrathi]
escortableships[merchant_]=escortableships[merchant]
escortableships[merchant__]=escortableships[merchant]
escortableships[retro_]=escortableships[retro]
escortableships[retro__]=escortableships[retro]
escortableships[pirates_]=escortableships[pirates]
escortableships[pirates__]=escortableships[pirates]
escortableships[hunter_]=escortableships[hunter]
escortableships[hunter__]=escortableships[hunter]
escortableships[militia_]=escortableships[militia]
escortableships[militia__]=escortableships[militia]

unescortable = ["paradigm","kamekh","gothri","heimdal","hospital_base","large_asteroid","mining_base","new_constantinople","perry","refinery"]

#Make a list of ships from fighters, capitals and escortableships for each faction
allships=[]
for i in range(len(factions)): allships.append([]) #Default in case a faction has no ships of some types.
for i in range(len(fighters)):
    allships[i]=allships[i]+fighters[i]
for i in range(len(escortableships)):
    allships[i]=allships[i]+escortableships[i]
for i in range(len(capitals)):
    allships[i]=allships[i]+capitals[i]

stattable={#SHIPNAME:(CHANCE_TO_HIT,CHANCE_TO_DODGE,DAMAGE,SHIELDS,ORDINANCE_DAMAGE),
    #ships, please keep sorted to weed out duplicates
    "arrow":(0.67,0.7,16,31,64),
    "asteroid_fighter":(0.3,0.2,22.9,168,16),
    "banshee":(0.6,0.68,28,42,52),
    "bengal":(0.26,0.2,68.3,320,66),
    "broadsword":(0.44,0.48,95.8,80,148),
    "caernaven":(0.26,0.2,68.3,220,66),
    "carrier":(0.2,0.2,77.22,260,66),
    "centurion":(0.64,0.6,39,65,38),
    "confedcarrier":(0.2,0.2,77.22,260,66),
    "corvette":(0.2,0.2,77.22,260,66),
    "cutlass":(0.6,0.68,28,42,52),
    "demon":(0.6,0.68,28,42,52),
    "dorkathi":(0.26,0.2,68.3,220,66),
    "dorkritha":(0.05,0.05,16,121,0),
    "dralthi":(0.62,0.66,18,52.5,48),
    "drayman":(0.05,0.05,16,121,0),
    "draymanCVL":(0.05,0.05,16,121,0), #fixme
    "drone":(0.68,0.95,200,470,400),
    "durango_carrier":(0.26,0.2,68.3,320,66),
    "durango_destroyer":(0.26,0.2,68.3,220,66),
    "ferret":(0.67,0.7,16,31,64),
    "fireblade":(0.67,0.7,16,31,64), #fixme
    "fralthi":(0.26,0.2,68.3,320,66),
    "fralthra":(0.2,0.2,77.22,260,66),
    "galaxy":(0.1,0.2,32.8,80,38),
    "galaxygs":(0.1,0.24,34.8,160,38),
    "galaxyhk":(0.1,0.22,32.8,80,40),
    "gladius":(0.48,0.58,19.81,40,52),
    "gothri":(0.45,0.6,56.1,50,68),
    "grikath":(0.66,0.50,40,70,38),
    "hammer":(0.6,0.68,28,42,52),
    "hellcat":(0.67,0.7,16,31,64),
    "hornet":(0.6,0.68,28,42,52),
    "jalthi":(0.6,0.68,28,42,52),
    "kamekh":(0.26,0.2,68.3,220,66),
    "kilrathicarrier":(0.2,0.2,77.22,260,66),
    "krant":(0.6,0.65,28,25,22),
    "kukhri":(0.6,0.70,26,40,62),
    "orion":(0.3,0.2,22.9,168,16),
    "orionMk2":(0.3,0.18,22.9,148,16),
    "paradigm":(0.2,0.2,77.22,260,66),
    "phantom":(0.6,0.68,28,42,52),
    "rapier":(0.64,0.6,39,65,38),
    "sabre":(0.64,0.6,39,65,38),
    "salthi":(0.66,0.68,36,36,32),
    "salthi.fusion":(0.66,0.68,25.2,36,32),
    "salthi.particle":(0.66,0.68,25.2,36,32),
    "salthi.steltek":(0.66,0.68,36,36,32),
    "sartha":(0.64,0.52,20,31,15),
    "scimitar":(0.6,0.68,28,42,52),
    "scramble":(0.67,0.7,16,31,64),
    "shoklar":(0.8,0.6,15.64,60,16),
    "shuttle":(0.26,0.2,68.3,220,66),
    "sickle":(0.6,0.68,28,42,52),
    "sparrowhawk":(0.64,0.56,20,42,15),
    "stiletto":(0.67,0.7,16,31,64),
    "strakha":(0.8,0.6,15.64,60,16),
    "raptor":(0.6,0.68,28,42,52),
    "talon":(0.45,0.38,18.77,36,32),
    "tarsus":(0.1,0.15,10.94,36,32),
    "tarsusMk2":(0.1,0.2,12,56,32),
    "thunderbolt":(0.6,0.68,28,42,52),
    "venture":(0.26,0.2,68.3,220,66),
    #permanent bases, set dodge to 100% so they don't get destroyed
    "heimdal":(0.05,100,16,500,0),
    "hospital_base":(0,100,0,1000,0),
    "large_asteroid":(0,100,0,1000,0),
    "mining_base":(0,100,0,1000,0),
    "new_constantinople":(0,100,0,4000,0),
    "perry":(.5,100,600,6000,500),
    "refinery":(0,100,0,800,0),
    }

# Sketchy subfaction implementation. Seems like child faction help their parent during dynamic battles (siege).
# I don't think we should put factions as parent if they wouldn't help each other in sieges. -wolphin
parentfaction = []
for i in range(len(factions)): parentfaction.append(["unknown","unknown"]) #Add default values so entries below can be in arbitrary order.
parentfaction[confed]=["confed","confed"] #confed
parentfaction[kilrathi]=["kilrathi","kilrathi"] #kilrathi
parentfaction[nephilim]=["nephilim","nephilim"] #nephilim
parentfaction[merchant]=["confed","confed"] #merchant
parentfaction[retro]=["retro","retro"] #retro
parentfaction[pirates]=["pirates","pirates"] #pirates
parentfaction[hunter]=["hunter","hunter"] #hunter
parentfaction[militia]=["confed","confed"] #militia
parentfaction[unknown]=["unknown","unknown"] #unknown
parentfaction[landreich]=["confed","confed"]#landreich
parentfaction[border_worlds]=["confed","confed"]#border_worlds
parentfaction[firekkan]=["confed","confed"] #firekkan
parentfaction[AWACS]=["confed","confed"] #AWACS
#Keep entries who reference other entries below those referenced! Actual array position is set by the first parameter.
parentfaction[confed_]=parentfaction[confed]
parentfaction[confed__]=parentfaction[confed]
parentfaction[kilrathi_]=parentfaction[kilrathi]
parentfaction[kilrathi__]=parentfaction[kilrathi]
parentfaction[merchant_]=parentfaction[merchant]
parentfaction[merchant__]=parentfaction[merchant]
parentfaction[retro_]=parentfaction[retro]
parentfaction[retro__]=parentfaction[retro]
parentfaction[pirates_]=parentfaction[pirates]
parentfaction[pirates__]=parentfaction[pirates]
parentfaction[hunter_]=parentfaction[hunter]
parentfaction[hunter__]=parentfaction[hunter]
parentfaction[militia_]=parentfaction[militia]
parentfaction[militia__]=parentfaction[militia]

# THIS NEEDS MUCH UPDATING!!!! We have a ton of stuff here now. Seriously.
# mining bases are defined in the asteroid file. The ones here will show up WITHOUT ACCOMPANYING ASTEROIDS.
# capships are now handled better, so no transports for big factions these all need a kilrathi equivalent!

generic_bases=["AsteroidFighterBase","naval_base","mining_base","fighterbase","refinery","factory","refinery","refinery","drydock"]
merchant_bases=["capitol_base","refinery","mining_base","factory","refinery2","research","mining_base","mining_base","refinery3","refinery","refinery3"]
confed_bases=["naval_base","fighterbase","naval_base","fighterbase","mining_base","fighterbase","AsteroidFighterBase","AsteroidFighterBase","confedcarrier","refinery","refinery","fighterbase","refinery","refinery2","refinery3","starfortress","naval_base","research","research","drydock","drydock","drydock","factory","factory","factory"]
kilrathi_bases=["kilrathi_starfortress","kilrathi_factory","outpost","kilrathi_base","kilrathi_supply_depot","kilrathi_naval_base","AsteroidFighterBase","kilrathi_naval_base","kilrathicarrier","kilrathi_base","fralthra","kilrathi_superbase","large_asteroid2","AsteroidFighterBase","kilrathi_naval_base","kilrathi_factory","refinery","refinery","outpost","refinery","outpost","refinery"]
kilrathi_insys_bases=["kilrathi_superbase","mining_base","kilrathi_base","kilrathi_supply_depot","kilrathi_factory","kilrathi_base","kilrathi_base","refinery","refinery","outpost","refinery","kilrathi_factory","refinery"]
kilrathi_rebels_bases=["kilrathi_base","mining_base","kilrathi_base","kilrathi_supply_depot","kilrathi_factory","kilrathi_supply_depot","kilrathi_base","outpost","refinery","kilrathi_supply_depot","refinery","kilrathi_factory","refinery"]
kilrathi_merchant_bases=["kilrathi_base","mining_base","kilrathi_base","kilrathi_supply_depot","kilrathi_factory","kilrathi_supply_depot","kilrathi_base","outpost","refinery","kilrathi_supply_depot","refinery","kilrathi_factory","refinery"]
pirate_bases=["mining_base", "mining_base", "drayman", "drayman", "drayman", "AsteroidFighterBase"]
AWACS_bases=["mining_base", "mining_base", "drayman", "venture", "factory", "corvette", "refinery", "refinery2", "AsteroidFighterBase"]
militia_bases=["mining_base", "mining_base", "AsteroidFighterBase", "corvette", "drayman", "corvette", "refinery2", "refinery3", "factory"]
retro_bases=["large_asteroid","drayman","corvette","corvette","corvette"]

bases = []
for i in range(len(factions)): bases.append(generic_bases) #Add default values so entries below can be in arbitrary order.
bases[confed]=confed_bases
bases[kilrathi]=kilrathi_bases
bases[nephilim]=generic_bases
bases[merchant]=merchant_bases
bases[retro]=retro_bases
bases[pirates]=pirate_bases
bases[hunter]=generic_bases
bases[militia]=militia_bases
bases[unknown]=generic_bases
bases[landreich]=generic_bases
bases[border_worlds]=generic_bases
bases[firekkan]=generic_bases
bases[AWACS]=AWACS_bases
#Keep entries who reference other entries below those referenced! Actual array position is set by the first parameter.
bases[confed_]=bases[confed]
bases[confed__]=bases[confed]
bases[kilrathi_]=bases[kilrathi]
bases[kilrathi__]=bases[kilrathi]
bases[merchant_]=bases[merchant]
bases[merchant__]=bases[merchant]
bases[retro_]=bases[retro]
bases[retro__]=bases[retro]
bases[pirates_]=bases[pirates]
bases[pirates__]=bases[pirates]
bases[hunter_]=bases[hunter]
bases[hunter__]=bases[hunter]
bases[militia_]=bases[militia]
bases[militia__]=bases[militia]

#Stub, since the above are not actually implemented.
generic_bases = ("mining_base","mining_base","mining_base","mining_base","mining_base","mining_base","mining_base","mining_base","mining_base","mining_base","refinery","refinery","refinery","refinery","refinery","refinery","drayman","drayman","drayman","hospital_base","large_asteroid")
bases = []
for i in range(len(factions)): bases.append(generic_bases) #Add default values so entries below can be in arbitrary order.

