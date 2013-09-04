import campaign_lib
from campaign_lib import *
zoolspeech1={"intro":[("Burrows","Greetings.  My name is Grayson Burrows; I'm looking for work."),
                            ("Zool","You're in luck, cause I'm hiring. My name is Zool, unaffiliated Hunter."),
                            ("Burrows","How may I be of service?"),
                            ("Zool","Me and my guild-mates have ordered new types of Orion ships from 'Rilke Shipyards' on this base. They took the money and didn't deliver anything. I was sent to look up the status, and now, well, they're gone. I'm currently looking up this agricultural base, with little hope."),
                            ("Burrows","You mean they took your money and ran?"),
                            ("Zool","Maybe, which would endanger my position a lot. The engineering personnel are gone. I need to know where they are."),
                            ("Burrows","I could help you find out, for the right price."),
                            ("Zool","I'd appreciate that. It is possible the engineers were kidnapped. I need you to clarify that.  If they exist, establish contact with the kidnappers--maybe we can convince them to free the hostages."),
                            ("Burrows","Okay... where can I find them?"),
                            ("Zool","That's what I don't know, but I can give you an initial hint. A rival company, the potential kidnapper, is based in New Detroit. If I were them, I would likely try to hide the hostages in one of the surrounding systems, perhaps on an unpopulated base."),
                            ("Burrows","That's not much information, but with adequate payment, I could do the job."),
                            ("Zool","How does 30000 sound to you?")],
                "reject1":[("Burrows","Like charity. Do you know how many bases are around New Detroit?"),
                            ("Zool","Yes.  It's an easy job. Do it for me, pal.")],
                "reconsider":[("Burrows","I've reconsidered."),
                            ("Zool","That's good. For 30000, look up the surrounding systems of New Detroit and establish contact with the kidnappers.")],
                "reject2":[("Burrows","I still don't want it.")],
                "accept":[("Burrows","Sounds good to me."),
                            ("Zool","Great. Meet me back here as soon as you're done.")],
                "accept2":[("Zool","Thanks. Please move out.")],
                "reminder":[("Zool","Have you found the kidnappers?"),
                            ("Burrows","Actually, I haven't launched yet."),
                            ("Zool","Listen, I'm not too sure what will happen to the hostages, they may even be dead already!"),
                            ("Burrows","Patients, friend; I'll find those kidnappers.")],
                "failure":[("Zool","I don't know what kind of problems you had, but the hostages are dead. I'm sorry I ever met you.")]
                }
zoolspeech2={"intro":[("Burrows","My name is Burrows, I represent Hunter Zool."),
                            ("Micol","Yeah? So what's the bounty for my head?"),
                            ("Burrows","None, actually. I'm here to negotiate. What do you want to set the hostages free?"),
                            ("Micol","Why should I fool my employer?"),
                            ("Burrows","Because you're corrupt scum and just in it for the money."),
                            ("Micol","Sorry, but my employer is quite capable of killing me if I don't fulfill my contract. I won't help you."),
                            ("Burrows","I've found you. Tell me why we shouldn't just organize a force to conquer this base!"),
                            ("Micol","Tell Zool this base is fortified; an invasion won't be easy.  We'll kill the hostages the second we see a vapor trail coming through the jump gate.  Is that clear?")],
                "reject1":[("Burrows","I won't deliver Zool such bad news. And I won't leave until I have a positive answer.")],
                "reconsider":[("Burrows","Are you still sticking to your old employer?"),
                            ("Micol","Yes.  Tell yours not to make any mistakes or the hostages will die, understood?")],
                "reject2":[("Burrows","As I said, my good reputation won't allow me to deliver such news.")],
                "accept":[("Burrows","Yes. I'll deliver the message.")],
                "accept2":[("Zool","Yes. I'll deliver the message.")],
                "reminder":[("Micol","Why are you still wasting my time?"),
                            ("Burrows","Because I think you are willing to negotiate."),
                            ("Micol","Listen, if my employer gets a whiff of our meeting, I'm not sure what my next orders will be. You'd better leave now.")],
                "failure":[("Micol","You should have left when you had the chance. The hostages are as good as dead.")]
                }

zoolspeech3={"intro":[("Zool","Have you found them?"),
                            ("Burrows","Yes. They're at the Vincent moon around New Reno. You were right, they are hostages. The kidnappers seem to be hired mercenaries."),
                            ("Zool","That's too bad. The moon is quite fortified. We won't be able to invade it without endangering the hostages."),
                            ("Burrows","I have an idea. If we could weaken the position of the kidnappers' employers, we might me able to convince them to cooperate with us."),
                            ("Zool","You mean they are willing to negotiate, but their boss is leaning on them?"),
                            ("Burrows","Well, I have the feeling they will cooperate if the other party is not quite as dangerous."),
                            ("Zool","You wouldn't believe who the other party is, mate."),
                            ("Burrows","Tell me."),
                            ("Zool","AVR ships."),
                            ("Burrows","AVR? Whoa! What's their problem with the new ships then? They have a monopoly for selling ships in New Detroit!"),
                            ("Zool","They have the largest stock of 'elder' ships in the sector; with all the new ships coming out, they will sell fewer of their quantity. I think they are starting to put pressure on the smaller companies producing new ships to gain enough time to sell the old ships."),
                            ("Burrows","I see. Again, how can we weaken AVR's position?"),
                            ("Zool","By attacking them. I've heard about an AVR freighter crossing this system. They have an escort. Destroy the freighter."),
                            ("Burrows","Uh huh...how much is it worth to you?"),
                            ("Zool","I'll pay 20000 credits.  It should be an easy run.")],
                "reject1":[("Burrows","I usually don't attack free-trade ships, Zool.  Sounds too much like piracy to me."),
                            ("Zool","They're part of a criminal syndicate. Please reconsider.")],
                "reconsider":[("Burrows","Tell me about your mission again."),
                            ("Zool","Take out a freighter in this system. Payment is 20000.")],
                "reject2":[("Burrows","No thanks, give that mission to one of your hunter friends.")],
                "accept":[("Burrows","Okay. Let's hope this will catch the attention of the kidnappers.")],
                "accept2":[("Burrows","Okay. Let's hope that'll catch the attention of the kidnappers.")],
                "reminder":[("Zool","Unless you destroy that freighter, nothing will happen. Now leave.")],
                "failure":[("Zool","The frighter has reached its destination! What was the problem? Next time I'll put my trust into my hunter mates!")]
                }

zoolspeech4={"intro":[("Zool","Good work, the freighter is toast."),
                            ("Burrows","Yeah. What's next?"),
                            ("Zool","I'm afraid we have caught additional attention from within AVR: a strike force has entered Varnus. They're looking for us. Destroy them."),
                            ("Burrows","All alone?"),
                            ("Zool","No... some of my guild mates will join you. I'll pay 50000 for saving my ass.")],
                "reject1":[("Burrows","I missed the part where this is my problem.")],
                "reconsider":[("Burrows","What was that again? 50000 for saving your ass?"),
                            ("Zool","Yes. Plus you'll get help from two Centurions.")],
                "reject2":[("Burrows","No chance.")],
                "accept":[("Burrows","Consider your ass saved."),
                            ("Zool","Thanks, man!")],
                "accept2":[("Zool","Thank you. Make haste!")],
                "reminder":[("Zool","What are you doing here?"),
                            ("Burrows","I'm looking for my wingmen."),
                            ("Zool","They already are in orbit, idiot! And if you aren't there soon, I'll be kicking your ass straight into one of their cargo holds!")],
                "failure":[("Zool","The enemy has found me. I have to duck out of here. I hope they catch you and bar-be-cue your ass in molasses!")]
                }
zoolspeech5={"intro":[("Burrows","AVR now has a space debris storage in Varnus."),
                            ("Zool","Ha! Nice work. Now listen. I've learned about an AVR force in ND-57. My intelligence reports tell me they are the ones holding the engineers. The ship must be stopped. The destruction of the ship will give us quite an advantage."),
                            ("Burrows","What kind of resistance can I expect?"),
                            ("Zool","They are using a Paradigm, maybe fighter or gunship escorts as well. You'll earn 30000 for destroying that Paradigm."),
                            ("Burrows","And then what?"),
                            ("Zool","Afterwards, land on the New Reno moon and negotiate with the kidnappers again; perhaps they will be more willing to listen this time.")],
                "reject1":[("Burrows","Attacking a Paradigm is suicide, I must reject.")],
                "reconsider":[("Burrows","What was that mission again?"),
                            ("Zool","For 30000, destroy the target Paradigm in ND-57, and then land on the New Reno moon to meet the kidnappers again.")],
                "reject2":[("Burrows","No, too dangerous.")],
                "accept":[("Burrows","The money is good. I'll do it.")],
                "accept2":[("Zool","Good.")],
                "reminder":[("Zool","Hurry up man! If that Paradigm picks up the hostages, we won't be able to free!")],
                "failure":[("Zool","The hostages are gone. You have failed.")]
                }
zoolspeech6={"intro":[("Micol","I should have known you were responsible for this."),
                            ("Burrows","And I know that you're not a killer. You have the chance to change sides now!"),
                            ("Micol","But... what if AVR learns about this?"),
                            ("Burrows","Open your eyes! The Paradigm is nothing more than smoking debris! They will believe you're dead!"),
                            ("Micol","Very well. But we need a transport to bring the hostages back. Plus, Zool will need to pay 500000 to cover the expenses of my flight.")],
                "reject1":[("Burrows","I don't think Zool will pay that much."),
                            ("Micol","If he wants to see the hostages set free, he will have to.")],
                "reconsider":[("Burrows","Again, what do you want?"),
                            ("Micol","A transport along with 500000 credits.")],
                "reject2":[("Burrows","You're crazy. If your 'friends' come up with similar requests, we'll need a money-printing machine to take care of the bill.")],
                "accept":[("Burrows","I'll tell Zool.")],
                "accept2":[("Burrows","I'll tell Zool.")],
                "reminder":[("Micol","Please hurry up! I don't know when the AVR guys will come back.")],
                "failure":[("Micol","An AVR task force has landed on the moon. You had your chance; it's too late now!")]
                }

zoolspeech7={"intro":[("Zool","What did they say?"),
                            ("Burrows","The leader is willing to cooperate with us. But she'll need a transport to evacuate the hostages, along with 500000 credits to cover her expenses."),
                            ("Zool","500000?!? Uhm... why do girls always want money?"),
                            ("Burrows","I don't know, but we need to hurry up. If AVR gets there before we do, she won't be able to evacuate the hostages."),
                            ("Zool","I see. I can offer a GalaxyHK--it should have enough cargo space to carry the engineers. You'll get 50000 credits for bringing the engineers back.")],
                "reject1":[("Burrows","A GalaxyHK will be shot up in seconds. Too risky.")],
                "reconsider":[("Zool","Will you do the escort for 50000 credits or not?")],
                "reject2":[("Burrows","As I said, the money is not the problem, but I think a GalaxyHK is too light for such a mission.")],
                "accept":[("Burrows","I'll leave immediately.")],
                "accept2":[("Zool","Okay, We have no time to wait. I'll leave immediately.")],
                "reminder":[("Zool","The GalaxyHK is already waiting for you. Hurry!")],
                "failure":[("Zool","I understand the mission was quite hard, but failure wasn't an option. You're fired.")]
                }

zoolspeech8={"intro":[("Burrows","Are we in time?"),
                            ("Micol","The engineers are already climbing into the transport. We need to launch immediately before one of my mates realizes what's going on.")],
                "reject1":[("Micol","Not the best time to get cold feet. We need you as an escort!")],
                "reconsider":[("Micol","Will you escort us or not?")],
                "reject2":[("Micol","Coward!")],
                "accept":[("Burrows","Let's go!")],
                "accept2":[("Micol","Thank goodness!")],
                "reminder":[("Micol","We're ready to leave.")],
                "failure":[("Micol","We've lost the transport. AVR has located me. I've got to bail. Goodbye, and good riddance.")]
                }

zoolspeech9={"intro":[("Zool","Did everyone make it back?"),
                            ("Burrows","Yeah. All the engineers are okay, thanks to Micol."),
                            ("Zool","I've already spoken with her and thanked her. She's currently organizing a transport to take her into hiding."),
                            ("Burrows","Good to hear it. Now, Where's my money?"),
                            ("Zool","It's here, along with a final 'mission' - head to Rilke refinery and meet up with the engineers. They have a something for you.")],
                "reject1":[("Burrows","I have other business to do. I'll meet you later.")],
                "reconsider":[("Zool","The guys on Rilke want to thank you personally. Will you visit them?")],
                "reject2":[("Burrows","Later.")],
                "accept":[("Burrows","I always look forward to praise. Goodbye, Zool.")],
                "accept2":[("Burrows","Okay, I'll visit them now. Thank you.")],
                "reminder":[("Zool","I don't want to spoil the surprise. Visit the bar at Rilke to see what the guys have for you..")],
                "failure":[("Zool","Those engineers wanted to show you their Orion variants. But since you didn't want to visit them, they forgot about you. Sorry. I can't do anything else for you.")]
                }

zoolsuccess=[("UNLOCKED: OrionMk2."),
            ("Melonhead","Are you the pilot who escorted us back to Varnus?"),
            ("Burrows","Yes. My name is Burrows, Grayson Burrows."),
            ("Melonhead","Just call me Melonhead. I am the lead engineer for the Orion variant series at Rilke that we are producing exclusively for high-ranking members of the Mercenaries Guild."),
            ("Burrows","Zool said you have a surprise for me."),
            ("Melonhead","Yes. We want to thank you for your bold escort. The Orion variants are restricted to certain persons who have proven themselves loyal, and we want to reward you by giving you access to the OrionMK2. Look up any ship dealer in the sector; your Quine 4000 will give you unrestricted access."),
            ("Burrows","Sweet deal. Thank you!")]

def LoadZoolCampaign():
    ZOOL_SPRITE  = ("sandoval.spr","Talk_to_Zool","bases/heads/zool.spr") #sprite file for the fixer
    MICOL_SPRITE = ("taryn.spr","Talk_to_Micol","bases/heads/cross.spr")
    MELONHEAD_SPRITE = ("monkhouse.spr","Talk_to_Melonhead","bases/heads/melonhead.spr")
    zoolmission1 = CampaignClickNode() # Initialize each node
    zoolmission2 = CampaignClickNode() # Initialize each node
    zoolmission3 = CampaignClickNode() # Initialize each node
    zoolmission4 = CampaignClickNode() # Initialize each node
    zoolmission5 = CampaignClickNode() # Initialize each node
    zoolmission6 = CampaignClickNode() # Initialize each node
    zoolmission7 = CampaignClickNode() # Initialize each node
    zoolmission8 = CampaignClickNode() # Initialize each node
    zoolmission9 = CampaignClickNode() # Initialize each node
    zoolfinish = CampaignNode()

    priv=Campaign("zool_campaign") # Name of the save game variable for the entire campaign. Can't contain spaces
    priv.Init(zoolmission1) # the first node.

    mission_desc="Zool_1:_Find_the_engineers"
    MakeCargoMission(priv,
        ZOOL_SPRITE, # Campaign, sprite
        [InSystemCondition("Gemini/Varnus","Rodin")], # Where fixer meets you to start the mission
        [InSystemCondition("Gemini/ND-57","Vincent_Moon")], # Where the mission ends.
        ClearFactionRecord('hunter',1.0,PushRelation('hunter')),
        None,
        ("Search_around_New_Detroit",1),
        priv.name+"_mission", # Script to be set on completion. -1=Failure, 0=Not Accepted, 1=Succeed, 2=In progress
        zoolspeech1, # Dictionary containing what the fixer says.
        None, # If you reject the mission twice. "None" means that he continues asking you forever until you accept
        CampaignEndNode(priv), # If you lose the mission
        zoolmission2, # If you win the mission. Usually points to the next mission
        zoolmission1) # The current mission node.

    mission_desc="Zool_2:_Report_hostage_location"
    MakeCargoMission(priv,
        MICOL_SPRITE,
        [InSystemCondition("Gemini/ND-57","Vincent_Moon")],
        [InSystemCondition("Gemini/Varnus","Rodin")],
        None,
        LoadMission("directions_mission","directions_mission",(priv.name+"_mission",['Gemini/New_Detroit', 'Gemini/New_Constantinople', 'Gemini/Varnus'], 'Rodin')),
        ("Message_for_Zool",1),
        priv.name+"_mission", # Script to be set on completion. -1=Failure, 0=Not Accepted, 1=Succeed, 2=In progress
        zoolspeech2, # Dictionary containing what the fixer says.
        None, # If you reject the mission twice. "None" means that he continues asking you forever until you accept
        CampaignEndNode(priv), # If you lose the mission
        zoolmission3, # If you win the mission. Usually points to the next mission
        zoolmission2) # The current mission node.

    mission_desc="Zool_3:_Destroy_AVR_freighter"
    MakeMission(priv, # Creates any type of mission
        ZOOL_SPRITE, # Campaign, sprite
        [InSystemCondition("Gemini/Varnus","Rodin")], # Where fixer meets you to start the mission
        [InSystemCondition("Gemini/Varnus","Rodin")], # Where the mission ends.
        AddCredits(30000), 
        None,
        'bounty_leader',(0,0,0,False,3,'merchant_',(),priv.name+"_mission",'','drayman',False,'','orion',["Rogue mercenary ship, don't touch the frighter!"]), # Mission arguments.
        priv.name+"_mission", # Script to be set on completion. -1=Failure, 0=Not Accepted, 1=Succeed, 2=In progress
        zoolspeech3, # Dictionary containing what the fixer says.
        None, # If you reject the mission twice. "None" means that he continues asking you forever until you accept
        CampaignEndNode(priv), # If you lose the mission
        zoolmission4, # If you win the mission. Usually points to the next mission
        zoolmission3, # The current mission node.
        mission_desc # Name that describes the mission in flight and in the mission computer.
        )

    mission_desc="Zool_4:_Destroy_AVR_strike_force"
    MakeMission(priv, # Creates any type of mission
        ZOOL_SPRITE, # Campaign, sprite
        [InSystemCondition("Gemini/Varnus","Rodin")], # Where fixer meets you to start the mission
        [InSystemCondition("Gemini/Varnus","Rodin")], # Where the mission ends.
        AddCredits(20000), 
        LaunchWingmen("hunter__","centurion",2), # Script to be run to start the mission (usually None if you don't have a script. Do NOT load an ambush mission here.)
        'defend',('merchant_',0,6,5000,123456.789,0,False,True,'merchant',(),priv.name+"_mission",'','orion','',0), # Mission arguments.
        priv.name+"_mission", # Script to be set on completion. -1=Failure, 0=Not Accepted, 1=Succeed, 2=In progress
        zoolspeech4, # Dictionary containing what the fixer says.
        None, # If you reject the mission twice. "None" means that he continues asking you forever until you accept
        CampaignEndNode(priv), # If you lose the mission
        zoolmission5, # If you win the mission. Usually points to the next mission
        zoolmission4, # The current mission node.
        mission_desc # Name that describes the mission in flight and in the mission computer.
        )

    mission_desc="Zool_5:_Destroy_Paradigm_and_negotiate_on_Vincent_Moon"
    MakeMission(priv, # Creates any type of mission
        ZOOL_SPRITE, # Campaign, sprite
        [InSystemCondition("Gemini/Varnus","Rodin")], # Where fixer meets you to start the mission
        [InSystemCondition("Gemini/ND-57","Vincent_Moon")], # Where the mission ends.
        AddCredits(50000), # Script to be run as you click on the fixer. A common use is to AddCredits() for the previous mission.
        LoadMission(mission_desc,"directions_mission",(priv.name+"_mission",['Gemini/New_Constantinople', 'Gemini/New_Detroit', 'Gemini/Varnus'], 'Vincent_Moon')), # Script to be run to start the mission (usually None if you don't have a script, but ambush is also common.) (having no destination will call significant unit.. oakham should be the only dockable significant in that system
        'bounty_leader',(0,0,0,False,1,'merchant_',('Gemini/New_Constantinople','Gemini/New_Detroit','Gemini/ND-57'),priv.name+"_mission",'','paradigm',False,'','orion',["Unidentified vessel. You're disturbing a corporate operation. Withdraw!"]), # Mission arguments.
        priv.name+"_mission", # Script to be set on completion. -1=Failure, 0=Not Accepted, 1=Succeed, 2=In progress
        zoolspeech5, # Dictionary containing what the fixer says.
        None, # If you reject the mission twice. "None" means that he continues asking you forever until you accept
        CampaignEndNode(priv), # If you lose the mission
        zoolmission6, # If you win the mission. Usually points to the next mission
        zoolmission5, # The current mission node.
        mission_desc # Name that describes the mission in flight and in the mission computer.
        )

    mission_desc="Zool_6:_Relay_release_offer_to_Zool"
    MakeCargoMission(priv, # Creates a cargo mission
        MICOL_SPRITE, # Campaign, sprite
        [InSystemCondition("Gemini/ND-57","Vincent_Moon")], # Where fixer meets you to start the mission
        [InSystemCondition("Gemini/Varnus","Rodin")], # Where the mission ends. Usually the same as starting point for next fixer.
        None,
        LoadMission(mission_desc,"directions_mission",(priv.name+"_mission",['Gemini/New_Detroit', 'Gemini/New_Constantinople', 'Gemini/Varnus'], 'Rodin')),
        ("Micols_Requests",1), # Mission arguments.
        priv.name+"_mission", # Script to be set on completion. -1=Failure, 0=Not Accepted, 1=Succeed, 2=In progress
        zoolspeech6, # Dictionary containing what the fixer says.
        None, # If you reject the mission twice. "None" means that he continues asking you forever until you accept
        CampaignEndNode(priv), # If you lose the mission
        zoolmission7, # If you win the mission. Usually points to the next mission
        zoolmission6) # The current mission node.

    mission_desc="Zool_7:_Escort_transport_to_Vincent_Moon"
    MakeMission(priv, # Creates a cargo mission
        ZOOL_SPRITE, # Campaign, sprite
        [InSystemCondition("Gemini/Varnus","Rodin")], # Where fixer meets you to start the mission
        [InSystemCondition("Gemini/ND-57","Vincent_Moon")], # Where the mission ends. Usually the same as starting point for next fixer.
        AddCredits(30000), # Script to be run as you click on the fixer. A common use is to AddCredits() for the previous mission.
        LoadMission(mission_desc,"ambush",(priv.name+"_mission",("Gemini/New_Detroit",),0,'merchant_',4,'orion','',[("Enemy convoy on screen! Engage!")],['Gemini/New_Detroit', 'Gemini/ND-57'], 'Vincent_Moon')), # Script to be run to start the mission (usually None if you don't have a script, but ambush is also common.)
        "escort_mission",("hunter__",0,0,0,1500,0,0,0,("Gemini/New_Constantinople","Gemini/New_Detroit","Gemini/ND-57"),priv.name+"_mission",'','galaxyhk'),
        priv.name+"_mission", # Script to be set on completion. -1=Failure, 0=Not Accepted, 1=Succeed, 2=In progress
        zoolspeech7, # Dictionary containing what the fixer says.
        None, # If you reject the mission twice. "None" means that he continues asking you forever until you accept
        CampaignEndNode(priv), # If you lose the mission
        zoolmission8, # If you win the mission. Usually points to the next mission
        zoolmission7, # The current mission node.
        mission_desc # Name that describes the mission in flight and in the mission computer.
        )

    mission_desc="Zool_8:_Escort_transport_back_to_Rodin"
    MakeMission(priv, # Creates a cargo mission
        MICOL_SPRITE, # Campaign, sprite
        [InSystemCondition("Gemini/ND-57","Vincent_Moon")], # Where the mission ends. Usually the same as starting point for next fixer.
        [InSystemCondition("Gemini/Varnus","Rodin")], # Where fixer meets you to start the mission
        ClearFactionRecord('hunter',1.0,PopRelation('hunter')),
        LoadMission(mission_desc,"ambush",(priv.name+"_mission",("Gemini/ND-57",),0,'pirates_',4,'talon','',[("Micol!! She has changed sides and is trying to flee with our hostages! Buddies, track them down!")],['Gemini/New_Detroit', 'Gemini/New_Constantinople', 'Gemini/Varnus'], 'Rodin')), # Script to be run to start the mission (usually None if you don't have a script, but ambush is also common.)
        "escort_mission",("hunter__",0,0,0,1500,0,0,0,("Gemini/New_Detroit","Gemini/New_Constantinople","Gemini/Varnus"),priv.name+"_mission",'','galaxyhk'),
        priv.name+"_mission", # Script to be set on completion. -1=Failure, 0=Not Accepted, 1=Succeed, 2=In progress
        zoolspeech8, # Dictionary containing what the fixer says.
        None, # If you reject the mission twice. "None" means that he continues asking you forever until you accept
        CampaignEndNode(priv), # If you lose the mission
        zoolmission9, # If you win the mission. Usually points to the next mission
        zoolmission8, # The current mission node.
        mission_desc # Name that describes the mission in flight and in the mission computer.
        )

    mission_desc="Zool_9:_"
    MakeCargoMission(priv, # Creates a cargo mission
        ZOOL_SPRITE, # Campaign, sprite
        [InSystemCondition("Gemini/Varnus","Rodin")], # Where the mission ends. Usually the same as starting point for next fixer.
        [InSystemCondition("Gemini/Varnus","Rilke")], # Where the mission ends. Usually the same as starting point for next fixer.
        AddCredits(50000), # Script to be run as you click on the fixer. A common use is to AddCredits() for the previous mission.
        LoadMission(mission_desc,"directions_mission",(priv.name+"_mission",['Gemini/Varnus'], 'Rilke')), # Script to be run to start the mission (usually None if you don't have a script, but ambush is also common.)
        ("Zools_Recommendations",1), # Mission arguments.
        priv.name+"_mission", # Script to be set on completion. -1=Failure, 0=Not Accepted, 1=Succeed, 2=In progress
        zoolspeech9, # Dictionary containing what the fixer says.
        None, # If you reject the mission twice. "None" means that he continues asking you forever until you accept
        CampaignEndNode(priv), # If you lose the mission
        zoolfinish, # If you win the mission. Usually points to the next mission
        zoolmission9) # The current mission node.

    zoolfinish.Init(priv,
        [],
        [],
        None,
        GoToSubnode(0),
        None,
        [CampaignClickNode().Init(priv,
            [InSystemCondition("Gemini/Varnus","Rilke")],
            zoolsuccess,
            MELONHEAD_SPRITE,
            TrueSubnode(AddTechnology("orionvar")),
            None,
            [CampaignEndNode(priv)])]) # YOU WIN!!!

    return priv #return the newly created campaign back.
