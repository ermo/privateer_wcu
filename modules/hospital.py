import campaign_lib
from campaign_lib import *
natespeech1={"intro":[("Dr._Nate","Ah good, just put your thumb on this pad and we'll unload your ship."),
                            ("Burrows","Excuse me, Mr...?"),
                            ("Dr._Nate","Doctor! Dr. Nate! Where are the medical supplies?"),
                            ("Burrows","I'm sorry, but I guess I am not the person you expected."),
                            ("Dr._Nate","Damn it! Without the supplies, we cannot help our patients. Why are you still wasting my time?"),
                            ("Burrows","Maybe I can help you, Dr. Nate. My name is Grayson Burrows and I'll be of service, at least if you offer an adequate payment."),
                            ("Dr._Nate","I don't think you can be of service, unless you have a spaceship on your own."),
                            ("Burrows","As a matter of fact, I'm having one. I'm a Privateer."),
                            ("Dr._Nate","You're a Privateer? Thanks goodness, you're the person I've been waiting for so long!"),
                            ("Burrows","Yeah, skip the flowers. Tell me more about this place."),
                            ("Dr._Nate","In 2668, the Confederation decided to build up a space hospital at the frontier. Multiple pilots got shot down, their eject pods retrieved, but most of them couldn't be helped in time. That's why we are here."),
                            ("Burrows","Wow, I didn't know that the feds are that nice to their pilots. I heard that being retrieved and healed is a service for pilots working on carriers only."),
                            ("Dr._Nate","Pah, don't sweeten the situation. Take a look around, this is a pisspoor base. We are in desperate need of nearly everything. No confed ships stationed here. They just thought giving us a base is enough to calm down their conscience."),
                            ("Burrows","Surprise, surprise. Well, you told me that I've been the one you've been waiting for all your life. So I guess you're talking about a mission for me, at least I hope you do not want to marry me."),
                            ("Dr._Nate","Sorry sweetheart, but my job eats up all of my spare time. Now listen. I told you about this medical equipment shipment which we've been awaiting. Last thing we've heard is that the ship entered the system, but this was 20 hours ago. It should be at least in sensor range right now."),
                            ("Burrows","You want me to find out what has happened."),
                            ("Dr._Nate","Yes. I assume that it was intercepted by a pirate squadron. We need that confirmed. I'll pay 5000 for bringing the frighter back or erasing the person responsible for that."),
                            ("Burrows","5000 is not quite my usual income, Dr. Nate."),
                            ("Dr._Nate","It's all I can offer. Our funds are limited, and we need this problem solved once and for all.")],
                "reject1":[("Burrows","That's not enough money, Doctore."),
                            ("Dr._Nate","That's too bad... for both of us.")],
                "reconsider":[("Burrows","Okay, I've reconsidered. I'll catch those pirates for 10000 credits, no less."),
                            ("Dr._Nate","You'll get 5000 credits, and not a single credit more."),
                            ("Burrows","8000 credits. My final offer."),
                            ("Dr._Nate","You seem to suffer from an acute hear loss. It's 5-0-0-0 C-R-E-D-I-T-S and a free ear operation.")],
                "reject2":[("Burrows","Don't mess around with me, man!"),
                            ("Dr._Nate","I told you I cannot offer more right now. Stop whining!")],
                "accept":[("Burrows","Okay, but don't expect me to do too much of this charity work."),
                            ("Dr._Nate","I expect nothing else than success from you, and you can expect the money I promised.")],
                "accept2":[("Burrows","You're hard to negotiate with. I like that. I'll do it.")],
                "reminder":[("Dr._Nate","Did you find anything out?"),
                            ("Burrows","Not yet... I'm currently still busy wandering around your base."),
                            ("Dr._Nate","Listen, we need those medicals, or the heads of those pirates, or this hospital will cease existing."),
                            ("Burrows","Cool down! There are loads of beauty clinics on the pleasure bases where you could get a more lucrative job."),
                            ("Dr._Nate","Unfortunately, I'm enlisted and I don't want to be degraded in my age. So simply move out.")],
                "failure":[("Dr._Nate","Thanks to your slowness, the frighter is destroyed AND the pirates are gone. Don't expect me to pay your expenses. Now leave!")]
                }
natespeech2={"intro":[("Dr._Nate","Did you find out anything?"),
                            ("Burrows","Yes, your ship has been destroyed. But I managed to kill the ship responsible for that. Unfortunately, it seems that the cargo already has been taken off-system."),
                            ("Dr._Nate","Well, at least you managed to destroy those pirates. Good job. Here is your money. If you're interested, I have another mission for you."),
                            ("Burrows","Another whack-a-pirate for an apple and an egg?"),
                            ("Dr._Nate","No... the medical goods are gone, but I have spoken with the sickbay at Perry. They're willing to send us another shipment, and I want you to take care of it."),
                            ("Burrows","What's the payment?"),
                            ("Dr._Nate","I now can offer 10000 credits. Fly to Anapolis, meet Captain Goodin there and take over the cargo. Afterwards, come back and deliver the cargo back to Mah'Rahn."),
                            ("Burrows","Do you expect any resistance?"),
                            ("Dr._Nate","There are surely some cats out there, but if you mean pirates, you already killed them.")],
                "reject1":[("Burrows","Sorry, but hopping around the border should bring more than 10000 credits."),
                            ("Dr._Nate","If you thinks so, I'll find another person.")],
                "reconsider":[("Burrows","I've got nothing to do right now, so I'm reconsidering your offer."),
                            ("Dr._Nate","Okay. For 10000, fly to Anapolis in Perry, pick up some cargo there and deliver it to us.")],
                "reject2":[("Burrows","Nah."),
                            ("Dr._Nate","Then leave me alone!")],
                "accept":[("Burrows","Sounds good."),
                            ("Dr._Nate","Great. Make haste.")],
                "accept2":[("Dr._Nate","Good. Please make haste.")],
                "reminder":[("Dr._Nate","Back so soon? Where's the cargo?"),
                            ("Burrows","Uhm... I haven't left yet."),
                            ("Dr._Nate","You'd better leave now unless you don't want to be the protagonist in a RECTAL EXAMINATION!!!")],
                "failure":[("Dr._Nate","Another shipment of medical equipment is gone. The Confederation will close down this facility. Leave me before I forget about my ethics.")]
                }
natespeech3={"intro":[("Goodin","Good day Mr. Burrows, I've been expecting you. If you agree, I'll immediately order to load your ship with the goods.")],
                "reject1":[("Burrows","I currently got other things to do. We need to delay this."),
                            ("Goodin","Delay? Are you crazy? Man, Dr. Nate will hear about that!")],
                "reconsider":[("Burrows","Sorry for the delay."),
                            ("Goodin","Okay, can I load your ship now?")],
                "reject2":[("Burrows","Not yet... I'm still having other business."),
                            ("Goodin","Alright Burrows, I don't think Nightingale station can afford waiting for you. You lost your contract, someone else will do the run. You've failed.")],
                "accept":[("Burrows","Sure, go ahead."),
                            ("Goodin","Alright. You can launch.")],
                "accept2":[("Goodin","Good. Don't waste Dr. Nate's time any more and launch immediately.")],
                "reminder":[("Goodin","Some of the patients are in an unstable situation. Hurry up man!"),
                            ("Burrows","Cool down Captain! I just had some other business to do and will leave immediately."),
                            ("Goodin","You're risking the life of confed pilots and officers!")],
                "failure":[("Goodin","I've just contacted Dr. Nate. You're fired."),
                            ("Burrows","Fired? But... I'm ready to launch now!"),
                            ("Goodin","While you were doing your 'other business', two of his patients died because of the missing medical equipment. Be happy that you're not going to court for that!")]
                }
natespeech5={"intro":[("Dr._Nate","Aah, just in time. Thank you very much!"),
                            ("Burrows","No problem. What's next?"),
                            ("Dr._Nate","A Paradigm has entered the system. It is loaded with wounded and being chased by several Gothris. Defend it and bring it in."),
                            ("Burrows","What's the payment?"),
                            ("Dr._Nate","In the name of the Confederation, I can offer 30000 credits for the safe rescue."),
                            ("Burrows","Your funds seemed to have increased suddenly."),
                            ("Dr._Nate","Those are not my funds. Will you do it?")],
                "reject1":[("Burrows","Sorry Doc, but I feel fooled after all these little payments."),
                            ("Dr._Nate","Great. You behave like a woman who is insulted because she didn't get her flowers earlier. I'll look out for a real man.")],
                "reconsider":[("Burrows","I like your attitude towards women, Doctor. So I'm reconsidering."),
                            ("Dr._Nate","For 30000, bring in a Paradigm which is being chased by several Gothris.")],
                "reject2":[("Burrows","No thanks. I can't tell which of my aversions is preventing me, the one against the cats or the one against the Feds."),
                            ("Dr._Nate","It doesn't matter any more, I just got a message that the Paradigm got destroyed, thanks to your delays. You've failed.")],
                "accept":[("Burrows","Sure."),
                            ("Dr._Nate","Okay, I'll inform the others.")],
                "accept2":[("Dr._Nate","I'll leave immediately")],
                "reminder":[("Dr._Nate","Where are the wounded?"),
                            ("Burrows","I haven't left yet. Personal business, you know."),
                            ("Dr._Nate","Look, a bottle of Oxygene in my left hand. Medical laser scissors in my right hand. Do you think we have carneval around here?!?"),
                            ("Burrows","I got it Doctor. I'm leaving.")],
                "failure":[("Dr._Nate","The Paradigm is destroyed! Not quite a good performance for a hospital to loose all of their patients. Nor for you. You're fired.")]
                }
natespeech6={"intro":[("Dr._Nate","Thanks for the rescue flight. We've managed to stabilize all wounded."),
                            ("Burrows","I'm once again glad to be of service for the great cause, Doctor."),
                            ("Dr._Nate","Yes, yes. I now have a mission for you, but you must promise to keep your mouth shut about that."),
                            ("Burrows","I'll do. Go on."),
                            ("Dr._Nate","I need you to pick up a load of medical goods. I'll pay 50000 if you bring it in to Mah'Rahn."),
                            ("Burrows","What's the deal to keep it secret?"),
                            ("Dr._Nate","You'll need to pick up the goods in KM-252."),
                            ("Burrows","Wow, that's quite a distance and... hold on! That's a pirate system! YOU'RE DEALING WITH THE PIRATES!"),
                            ("Dr._Nate","QUIET!!! Listen, we could never get those medical goods that cheap if we bought it from the Feds. We need the pirates, otherwised we'd be forced to close down this facility!"),
                            ("Burrows","Man, you ought to know that those pirates are tracking down innocent merchants to acquire those medicals."),
                            ("Dr._Nate","I know, but they'd do it anyway, and the deal just ensures that the medicals reach the frontier. I need you for that, Captain Burrows!")],
                "reject1":[("Burrows","You must be joking. I cannot afford to participate in illegal dealings, especially not with the confeds checking my flight discs."),
                            ("Dr._Nate","Oh come on! As if you've never done something illegal! Farewell, I'll ask somebody else.")],
                "reconsider":[("Burrows","I've reconsider. 50000 is good money."),
                            ("Dr._Nate","To earn the cash, pick up a load of medical goods in KM-252 and bring the cargo back to me.")],
                "reject2":[("Burrows","Nah. This has been a silly idea right from the beginning."),
                            ("Dr._Nate","Your opinion.")],
                "accept":[("Burrows","I guess I could revive some old friendships to keep my neck dry."),
                            ("Dr._Nate","Very good. Tayla will be waiting for you at a hidden mining base.")],
                "accept2":[("Dr._Nate","Very good. Tayla will be waiting for you at a hidden mining base.")],
                "reminder":[("Dr._Nate","You're back? Fantastic! Didn't you have any trouble with the cargo?"),
                            ("Burrows","I haven't left yet. Should I expect any trouble with a load of medical goods."),
                            ("Dr._Nate","No, no, no trouble. Just leave."),
                            ("Burrows","Why are you so nervous, Doc? I'll bring in your cargo, have no doubt.")],
                "failure":[("Dr._Nate","You wouldn't believe how important this cargo was for us. This money was a major investment we won't get back. I cannot afford to give you any further work. Goodbye.")]
                }
natespeech7={"intro":[("Tayla","Are you here to pick up the goods for Dr. Nate?")],
                "reject1":[("Burrows","No."),
                            ("Tayla","In this case we never met around here, got it?")],
                "reconsider":[("Burrows","Excuse me... but didn't you mention Dr. Nate?"),
                            ("Tayla","Yes I did. Why didn't you tell me you're my contact right from the beginning?")],
                "reject2":[("Burrows","Because I'm not your contact. I was just interested. He is a friend of mine."),
                            ("Tayla","This is not the place to make friendship. If you are unable to bring the cargo to Dr. Nate, you'll need to explain this to him, not me. I already got my payment. You have failed. Move out or taste my Hand Laser!")],
                "accept":[("Burrows","Yes."),
                            ("Tayla","Good. Your ship is being loaded.")],
                "accept2":[("Burrows","I'm sorry, I was a bit nervous. Please load my ship.")],
                "reminder":[("Tayla","Your ship is loaded. You can move out.")],
                "failure":[("Tayla","If you are unable to bring the cargo to Dr. Nate, you'll need to explain this to him, not me. I already got my payment.")]
                }

natesuccess=[("UNLOCKED: Talon (unique chance)."),
            ("Dr._Nate","Thanks for the intact delivery. I would have never thought that you're capable of helping us with that."),
            ("Burrows","Yeah, and if you told me in advance that I'm transporting Ultimate, I would probably have never accepted."),
            ("Dr._Nate","Probably. I didn't lie, those goods are of medical use for us. We did some experiments with it and are expecting to be able to produce a successor to the obsolete morphine medicals soon."),
            ("Burrows","Man, you mean I won't see all those nice colors again when I'm in the sickbay? If that was my contribution, I'll leave ashamed. My money, please."),
            ("Dr._Nate","Here it is - and a special offer just for you. I'm going to sell my private ship since we're always low on funds, so it's your chance to get it."),
            ("Burrows","What kind of ship is that?"),
            ("Dr._Nate","It's Talon. It might be used and old but..."),
            ("Burrows","You mean your fantastic offer is a Talon? You'd better have skipped that part."),
            ("Dr._Nate","Hey, I could as well have offered a job in our hospital."),
            ("Burrows","Since I don't like wearing white skirts, I'm happy with your first offer Doc. Take care."),
            ("Dr._Nate","I wish you good luck, Captain. Oh and be aware that you can make good money if you bring us ejected pilots, freed slaves, pets for our experiments, food, medicals, or contraband for out medical research."),
            ("Burrows","I'll remember that. Goodbye.")]


def LoadNateCampaign():
    NATE_SPRITE  = ("monkhouse.spr","Talk_to_Dr._Nate","bases/heads/nate.spr")
    GOODIN_SPRITE    = ("goodin.spr", "Talk_to_Goodin","bases/heads/goodinanapolis.spr")
    TAYLA_SPRITE = ("tayla.spr","Talk_to_Tayla","bases/heads/taylapirate.spr")
    NateMission1 = CampaignClickNode() # Initialize each node
    NateMission2 = CampaignClickNode() # Initialize each node
    NateMission3 = CampaignClickNode() # Initialize each node
# Mission 4 skipped. I was too lazy to change all numbers. - Dilloh
    NateMission5 = CampaignClickNode() # Initialize each node
    NateMission6 = CampaignClickNode() # Initialize each node
    NateMission7 = CampaignClickNode() # Initialize each node
    NateFinish = CampaignNode()

    priv=Campaign("nate_campaign") # Name of the save game variable for the entire campaign. Can't contain spaces
    priv.Init(NateMission1) # the first node.
    
    MakeMission(priv, # Creates a cargo mission
        NATE_SPRITE, # Campaign, sprite
        [InSystemCondition("Gemini/Mah_Rahn","Nightingale_Station")], # Where fixer meets you to start the mission
        [InSystemCondition("Gemini/Mah_Rahn","Nightingale_Station")], # Where the mission ends. Usually the same as starting point for next fixer.
        None, # Script to be run as you click on the fixer. A common use is to AddCredits() for the previous mission.
        None,
        'bounty_leader',(0,0,0,False,3,'pirates_',(),priv.name+"_mission",'','centurion',False,'','talon',["You're coming too late. Those medical goods are already in our hold and will make a good price!"]),
        priv.name+"_mission", # Script to be set on completion. -1=Failure, 0=Not Accepted, 1=Succeed, 2=In progress
        natespeech1, # Dictionary containing what the fixer says.
        None, # If you reject the mission twice. "None" means that he continues asking you forever until you accept
        CampaignEndNode(priv), # If you lose the mission
        NateMission2, # If you win the mission. Usually points to the next mission
        NateMission1) # The current mission node.
    MakeCargoMission(priv, # Creates any type of mission
        NATE_SPRITE, # Campaign, sprite
        [InSystemCondition("Gemini/Mah_Rahn","Nightingale_Station")], # Where fixer meets you to start the mission
        [InSystemCondition("Gemini/Perry","Anapolis")], # Where the mission ends.
        AddCredits(5000), # Script to be run as you click on the fixer. A common use is to AddCredits() for the previous mission.
        LoadMission("directions_mission","directions_mission",(priv.name+"_mission",['Gemini/Blockade_Point_Tango', 'Gemini/Nitir', 'Gemini/Perry'], 'Anapolis')),
        ("Shipment_ID_card",1), # Mission arguments.
        priv.name+"_mission", # Script to be set on completion. -1=Failure, 0=Not Accepted, 1=Succeed, 2=In progress
        natespeech2, # Dictionary containing what the fixer says.
        None, # If you reject the mission twice. "None" means that he continues asking you forever until you accept
        CampaignEndNode(priv), # If you lose the mission
        NateMission3, # If you win the mission. Usually points to the next mission
        NateMission2) # The current mission node.
    MakeCargoMission(priv, # Creates any type of mission
        GOODIN_SPRITE, # Campaign, sprite
        [InSystemCondition("Gemini/Perry","Anapolis")], # Where fixer meets you to start the mission
        [InSystemCondition("Gemini/Mah_Rahn","Nightingale_Station")], # Where the mission ends.
        None,
        LoadMission("ambush","ambush",(priv.name+"_mission",("Gemini/Mah_Rahn",),0,'pirates_',4,'talon','',["Those medicals would fit fine in our cargo space. Consider dumping them, Privateer!"],['Gemini/Nitir', 'Gemini/Blockade_Point_Tango', 'Gemini/Mah_Rahn'], 'Nightingale_Station')),
        ("Medical_Equipment",20), # Mission arguments.
        priv.name+"_mission", # Script to be set on completion. -1=Failure, 0=Not Accepted, 1=Succeed, 2=In progress
        natespeech3, # Dictionary containing what the fixer says.
        CampaignEndNode(priv), # If you reject the mission twice. "None" means that he continues asking you forever until you accept
        CampaignEndNode(priv), # If you lose the mission
        NateMission5, # If you win the mission. Usually points to the next mission
        NateMission3) # The current mission node.
    MakeMission(priv, # Creates a cargo mission
        NATE_SPRITE, # Campaign, sprite
        [InSystemCondition("Gemini/Mah_Rahn","Nightingale_Station")],
        [InSystemCondition("Gemini/Mah_Rahn","Nightingale_Station")],
        AddCredits(10000), # Script to be run as you click on the fixer. A common use is to AddCredits() for the previous mission.
        None,
        'escort_local',('kilrathi_',0,3,0,3000,0,False,'confed__',(),priv.name+"_mission",'','gothri','','paradigm',["Human! Those wounded apes abord that ship are already close to death! Don't waste your life on trying to save those you cannot save!"]),
        priv.name+"_mission", # Script to be set on completion. -1=Failure, 0=Not Accepted, 1=Succeed, 2=In progress
        natespeech5, # Dictionary containing what the fixer says.
        CampaignEndNode(priv),
        CampaignEndNode(priv), # If you lose the mission
        NateMission6, # If you win the mission. Usually points to the next mission
        NateMission5) # The current mission node.
    MakeCargoMission(priv, # Creates any type of mission
        NATE_SPRITE, # Campaign, sprite
        [InSystemCondition("Gemini/Mah_Rahn","Nightingale_Station")], # Where fixer meets you to start the mission
        [InSystemCondition("Gemini/KM-252","Smallville")], # Where the mission ends.
        AddCredits(30000), # Script to be run as you click on the fixer. A common use is to AddCredits() for the previous mission.
        LoadMission("directions_mission","directions_mission",(priv.name+"_mission",['Gemini/Blockade_Point_Tango', 'Gemini/Nitir', 'Gemini/CMF-A', 'Gemini/Tingerhoff', 'Gemini/Nexus', 'Gemini/KM-252',"Smallville"])),
        ("ID-card_for_Tayla",1), # Mission arguments.
        priv.name+"_mission", # Script to be set on completion. -1=Failure, 0=Not Accepted, 1=Succeed, 2=In progress
        natespeech6, # Dictionary containing what the fixer says.
        None, # If you reject the mission twice. "None" means that he continues asking you forever until you accept
        CampaignEndNode(priv), # If you lose the mission
        NateMission7, # If you win the mission. Usually points to the next mission
        NateMission6) # The current mission node.
    MakeCargoMission(priv,
        TAYLA_SPRITE,
        [InSystemCondition("Gemini/KM-252","Smallville")],
        [InSystemCondition("Gemini/Mah_Rahn","Nightingale_Station")],
        None,
        LoadMission("ambush","ambush",(priv.name+"_mission",("Gemini/CMF-A",),0,'milita_',8,'','',["Damned Ultimate runner, we'll have no mercy with you. You'll find your cold and silent grave here!"],['Gemini/Nexus', 'Gemini/Tingerhoff', 'Gemini/CMF-A', 'Gemini/Nitir', 'Gemini/Blockade_Point_Tango', 'Gemini/Mah_Rahn'], 'Nightingale_Station')),
        ("Ultimate",30),
        priv.name+"_mission", # Script to be set on completion. -1=Failure, 0=Not Accepted, 1=Succeed, 2=In progress
        natespeech7, # Dictionary containing what the fixer says.
        CampaignEndNode(priv), # If you reject the mission twice. "None" means that he continues asking you forever until you accept
        CampaignEndNode(priv), # If you lose the mission
        NateFinish,
        NateMission7)
    NateFinish.Init(priv,
        [],
        None,
        None,
        GoToSubnode(0),
        None,
        [CampaignClickNode().Init(priv,
            [InSystemCondition("Gemini/Mah_Rahn","Nightingale_Station")],
            natesuccess,
            NATE_SPRITE,
            TrueSubnode(AddCredits(50000,AddTechnology("bands"))),
            None,
            [CampaignEndNode(priv)])]) # YOU WIN!!!

    return priv #return the newly created campaign back.
