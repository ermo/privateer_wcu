import campaign_lib
from campaign_lib import *
sligorspeech1={"intro":[("Sligor","Good day, privateer. My name is Sligor, the merchant guild affiliate on Speke."),
                            ("Burrows","My name is Grayson Burrows. How may I be of service?"),
                            ("Sligor","I'm looking for privateers to help establish the Guild HQ on Speke. We've already established a capital on this base, as you might have noticed."),
                            ("Burrows","Yeah.  The skyline looks quite impressive. It looks like a lot of money."),
                            ("Sligor","Yes. We've had many investors in the past. Junction is the main traffic point for Gemini, as well as the most secure connection to Sol. We now want to show the investors that their expenditures have proven profitable."),
                            ("Burrows","Sounds to me like Junction isn't that safe at all."),
                            ("Sligor","Although we are quite removed from cat space, pirate--and especially Retro--activity is on the rise. We know virtually nothing concerning their purposes or even if we are a target.  We believe the Retro attacks are side-effects of their siege at Oxford."),
                            ("Burrows","And you want me to find out what's going on."),
                            ("Sligor","Exactly. Since we want to make Speke a major trade center, we can't afford sudden ambushes on our freighters. We know about the hidden pirate base in the Pentonville system. I want you to show the pirates that they had better not try to take a foothold in Junction. I need you to wipe out the pirates in Pentonville."),
                            ("Burrows","I'm not too sure if that would be so easy."),
                            ("Sligor","I didn't say it would be easy, but you would be doing me a favor, and we are not prepared to fight on two fronts at this time.  We can concentrate on the Retros after we slow down the pirates. I'll pay you 20000 credits for this.")],
                "reject1":[("Burrows","No thanks. I won't run into the open arms of murderers."),
                            ("Sligor","Your loss, mate; there are many privateers out there who will jump at such a lucrative opportunity.")],
                "reconsider":[("Burrows","I've reconsidered."),
                            ("Sligor","That's good. Erase Pentonville of any pirate craft. Payment is 20000 credits.")],
                "reject2":[("Burrows","Too risky.")],
                "accept":[("Burrows","This isn't the first time I've danced with the pirates. I think I can handle it."),
                            ("Sligor","Great. See you soon.")],
                "accept2":[("Sligor","Thanks. Please move out.")],
                "reminder":[("Sligor","Did you erase the pirates?"),
                            ("Burrows","Actually, I haven't launched yet."),
                            ("Sligor","Listen. I have a great deal of other business to attend to and no time to hold your hand. Please destroy the pirates as you promised."),
                            ("Burrows","Keep your pants on. I'll do the job.")],
                "failure":[("Sligor","Fool! The pirates have survived. Now we must deal with two factions instead of just one, and i'm sure your utter failure has angered the pirates even more, which will undoubtedly cause them to escalate their attack plans. You'll never get a job from me again!")]
            }
sligorspeech2={"intro":[("Sligor","Did you manage to erase the foes?"),
                            ("Burrows","Pentonville is quiet and dark, but I have a feeling I destroyed a massing ambush force on the way to Speke. I doubt you didn't know about this, Sligor."),
                            ("Sligor","I told you what you needed to know. But, I'm a fair man: for your efforts, you get an extra bonus of 5000 credits. Your strike should delay further pirate operations for weeks, which gives us time to concentrate on the Retros. We need to find out why so many armed forces are cruising through Junction."),
                            ("Burrows","You said something about being a possible target..."),
                            ("Sligor","Normally the Retros concentrate on technology centers--this is just a trading base. Still, the possibility remains that the retros have realized the importance of Junction."),
                            ("Burrows","What do you want me to do?"),
                            ("Sligor","We have an undercover agent within the Retros. Meet him at Valhalla; he might have some news for us."),
                            ("Burrows","You have a Retro working for the Guild? Are you kidding?"),
                            ("Sligor","He somewhat 'depends' on our good will. If you bring him some goods for exchange, he will certainly speak. I will pay 20000 credits again.")],
                "reject1":[("Burrows","I don't like dating Retros, Sligor.")],
                "reconsider":[("Burrows","What was it you wanted me to do?"),
                            ("Sligor","Deliver some goods to our retro contact on Valhalla; bring back his information and earn 20000 credits for it.")],
                "reject2":[("Burrows","No thanks.")],
                "accept":[("Burrows","Sounds easy. I'm in.")],
                "accept2":[("Sligor","Thank you.")],
                "reminder":[("Sligor","What are you doing here?"),
                            ("Burrows","Did you already load my ship with the exchange goods?"),
                            ("Sligor","Of course! Now leave!")],
                "failure":[("Sligor","I don't know how you messed it up, but it surely was a performance in itself. You're fired!")]
                }

sligorpaulspeech={"intro":[("Paul","Do... do you have the stuff?"),
                            ("Burrows","Here you are. Give me the information."),
                            ("Paul","It's... all on this... on this disc... Along with my... my new cockpit editor!"),
                            ("Burrows","Cockpit editor? Man, what are you talking about? You should really keep your nose away from that Ultimate. Tell me, why doesn't your glorious god prevent you from toasting your brain?"),
                            ("Paul","None of... your business... Just take your disc... disc and go away...")],
                "reject1":[("Burrows","I don't think you have the goods for me, brother."),
                            ("Paul","I don't... care... got what I... what I wanted...")],
                "reconsider":[("Burrows","Do you still have the disc?"),
                            ("Paul","Take it...")],
                "reject2":[("Burrows","No thanks, I don't think it'll contain anything usable..."),
                            ("Paul","Okay... now leave... leave me alone...")],
                "accept":[("Burrows","Give me the disc. I can't see this anymore."),
                            ("Paul","Hehe... you... you don't know what... what you miss...")],
                "accept2":[("Paul","Here is... is the disc...")],
                "reminder":[("Paul","You got... got your disc... now leave me... me alone...")],
                "failure":[("Paul","You lost... lost the disc? Not my... my problem... Your employer... will certainly... certainly fire you for that... that...")]
                }

sligorspeech4={"intro":[("Sligor","Do you have the information?"),
                            ("Burrows","Yeah. You didn't tell me that your 'informant' was an Ultimate junkie!"),
                            ("Sligor","You didn't ask me."),
                            ("Burrows","Well, the militia did! I nearly got toasted over an unannounced smuggling run for you!"),
                            ("Sligor","Relax. I needed to fool you. If I used an official freighter, the guild would be in deep trouble now."),
                            ("Burrows","Yeah, but now i'm the one in deep trouble. I don't like being manipulated, Sligor!"),
                            ("Sligor","You survived, and you've got your payment, so stop blubbering. Don't tell me you've never done anything illegal. Now, listen. Thanks to the information you brought us, we now know we are not the Retros' primary target."),
                            ("Burrows","This should be good news to you."),
                            ("Sligor","Sadly enough, we are the secondary target. The Retros consider Speke a center of sins for its pleasure-base heritage."),
                            ("Burrows","Not to mention your trading efforts helping to spread those sins."),
                            ("Sligor","You name it. The retros, for some reason, seem able to afford higher fleet expenses, and they now pose a serious threat to us--maybe to the whole sector."),
                            ("Burrows","So what's next--Running Ultimate to Bethlehem to make them all quiet?"),
                            ("Sligor","Not exactly. According to the disc you brought back, I need you to defend Junction from a Retro attack: several capital ships are planning to invade the system, and I don't know which planet they'll start with. I'll pay 20000 if you will defend their target. Since this is relatively new information, and since we haven't had time to do a comprehensive analysis, I can only give you one Gunship as escort.  We can't afford to gamble by sending our entire force.")],
                "reject1":[("Burrows","You think you can fool me, and then profit from me again? I'm not that dumb, man."),
                            ("Sligor","Business sometimes requires immoral decisions. You should learn that.")],
                "reconsider":[("Burrows","Okay, what was that mission again?"),
                            ("Sligor","Defend Junction with the help of a Galaxy Gunship escort from a retro invasion force. Payoff is 20000")],
                "reject2":[("Burrows","You're not worth the trust I put in you. No chance."),
                            ("Sligor","We shall see about that.")],
                "accept":[("Burrows","Okay, I'll save the system, but be aware I am disappointed concerning your deception on the last mission."),
                            ("Sligor","what you feel does not concern me, privateer. Now leave. Your only concern is the job you promised to do.  Now get to it!")],
                "accept2":[("Sligor","Good. Now leave.")],
                "reminder":[("Sligor","What are you doing here? There are news reports of Retro ships on the move!"),
                            ("Burrows","I'm still angry over the Ultimate, Sligor."),
                            ("Sligor","Man, swallow your pride and fight those Retros before you have some serious worries; right now they breathe down our necks, and you are here complaining!")],
                "failure":[("Sligor","The retros have landed on important bases in this system thanks to your incompetence. You're fired.")]
                }
sligorspeech5={"intro":[("Burrows","Okay. The Retros have reached their ultimate destination--heaven. It was fun, by the way.  I've never seen so many troop transports look that surprised after having lost the initial strike advantage."),
                            ("Sligor","Glad you had some fun. You have impressively shown what you are able to do; perhaps you are not completely incompetent after all. I have another mission for you. Did you notice Rangrior in orbit?"),
                            ("Burrows","Yeah.  I was wondering what the Militia is doing here."),
                            ("Sligor","The Guild has a contract with the Militia: they protect our HQ in exchange for free trading runs. This time, we'll need a bit more than that. A massive Retro armada is moving towards Speke. A militia strike force is supposed to intercept them. We could use your help.  I'll pay you 30000 credits."),
                            ("Burrows","Rubbing elbows with militia, eh?  Where do I meet them?"),
                            ("Sligor","Some Hornets and a DraymanCVL will be massing near Speke.  The DraymanCVL will be bait for the Retros, so there's a good chance it has already left. Protect the DraymanCVL until the Retros are toast.")],
                "reject1":[("Burrows","No thanks, I'm not interested in helping the police at all.  They have more than enough reasons to haul me in as it is."),
                            ("Sligor","This doesn't quite fit with your attitude concerning Ultimate, does it not?")],
                "reconsider":[("Burrows","What was that mission again?"),
                            ("Sligor","For 30000, and with support from a militia assault force, wipe out the massive Retro armada.")],
                "reject2":[("Burrows","'Massive retro armada' sounds a bit risky. No thanks.")],
                "accept":[("Burrows","I can use the spare change. I'll do it.")],
                "accept2":[("Sligor","Good.")],
                "reminder":[("Sligor","The ships are still waiting for you. Please leave, or all will be lost!")],
                "failure":[("Sligor","The flagship is destroyed, and the Retros are invading the system! Our contract with the Militia has been cancelled. You're definatively FIRED!!!")]
                }
sligorspeech6={"intro":[("UNLOCKED: Hornet, Hornet CVL."),
                            ("Sligor","Thanks for wiping out the armada. Those Hornet pilots were quite impressed with your performance. You've gained the Speke Militia Freelancer Medal, along with some friends in the Hornet Squadron who are willing to give you access to the brand new HornetCVL."),
                            ("Burrows","So I kinda can get my own police car? Hehe. No more tickets! Gonna visit a ship dealer soon..."),
                            ("Sligor","Your last performance has gained additional attention from within the Militia. They want you to escort their delegation to Speke."),
                            ("Burrows","Being nanny for the police? This is the job I always dreamed of."),
                            ("Sligor","You are to visit the delegation on New Iberia in the Pyrenees System. From there, escort their DraymanCVL, the SS Knickerbocker, to Speke. In the name of the Militia, I'll pay 50000 for this escort."),
                            ("Burrows","We'll be flying through systems infected by pirate scum; I suppose they'll just let us walk right on by."),
                            ("Sligor","A DraymanCVL is quite capable of defending itself, I assure you.  You are being sent to make sure things go smoothly. How about it?")],
                "reject1":[("Burrows","If the Militia thought they could handle this, they wouldn't have asked for me.  Sounds like a death sentence."),
                            ("Sligor","They are impressed with your prowess, privateer. Please reconsider.")],
                "reconsider":[("Burrows","Okay, I've reconsidered. 50000 is quite a lot."),
                            ("Sligor","Fly to New Iberia in Pyrenees, pick up the DraymanCVL, and escort it here.")],
                "reject2":[("Burrows","No thanks. I don't like babysitting.")],
                "accept":[("Burrows","50000 credits, here I come!")],
                "accept2":[("Sligor","Good. You can launch at any time.")],
                "reminder":[("Sligor","Please make haste--the Militia is a valuable business partner.  We can't afford to lose their support.")],
                "failure":[("Sligor","You failed to visit the delegation. What's your problem--been breathing laser gas too long?  Get out of here!")]
                }

sligorspeech7={"intro":[("Onyx_Paladin","Good day, Privateer. My name is Onyx Paladin. I'm working for the Militia. You were sent to escort our delegation to Speke, correct?"),
                            ("Burrows","Right. But I'm afraid I won't do it for free, mate. You'll have to throw in something."),
                            ("Onyx_Paladin","We transfered 100000 credits to Sligor! What happened to the money?"),
                            ("Burrows","100000 credits?!? Uhm... I don't know, but he doesn't pay me a single credit."),
                            ("Onyx_Paladin","Very well, we'll take care of him later. I can offer access to the Militia's newest ship, the DraymanCVL. Although it is not yet ready for the open market, I could give you access to the prototype on Speke; besides, you would be a reliable test pilot, so it's a win-win for both of us."),
                            ("Burrows","I think that'll be adequate."),
                            ("Onyx_Paladin","Okay then... can we leave?")],
                "reject1":[("Burrows","I have some other business to do right now. Just wait for me here.")],
                "reconsider":[("Onyx_Paladin","Can we leave now?")],
                "reject2":[("Burrows","No.  I'm still busy.")],
                "accept":[("Burrows","Prepare to launch.")],
                "accept2":[("Onyx_Paladin","Launch preparations are underway.")],
                "reminder":[("Onyx_Paladin","I'm ready to go.")],
                "failure":[("Onyx_Paladin","We waited as long as we could. I've booked another escort. Maybe you are not so tough at all.")]
                }

sligorsuccess=[("UNLOCKED: Drayman CVL."),
            ("Onyx_Paladin","Thank you for transfering us to the base. As I promised, look up the local ship dealer and get yourself a DraymanCVL."),
            ("Burrows","Thanks.  But... where is Sligor?"),
            ("Onyx_Paladin","We've learned everything about Sligor's Ultimate shipments, as well as his inadequate payments for his employees. He has lost his job within the Guild."),
            ("Burrows","Uhm... good to see one more criminal scum out."),
            ("Onyx_Paladin","We know you are involved as well. You tried to fool us--Sligor has promised 50000 credits, not zero; and you were the one shipping the Ultimate. Even though you were in the dark about the shipment, you continued to work for him instead of reporting him to the proper authorities."),
            ("Burrows","I can explain that..."),
            ("Onyx_Paladin","Relax... you're not being accused. Although you're no less in for profit than Sligor, I'll close my eyes because of your satisfactory performance thus far. Unfortunately, the credits have been locked away as evidence. You won't see a single credit you were promised."),
            ("Burrows","Well, easy come, easy go--at least I'm not sitting in prison right now. Thank you for keeping your mouth shut. I hope your HQ will be a success. Goodbye.")]

def LoadSligorCampaign():
    SLIGOR_SPRITE  = ("sligor.spr","Talk_to_Sligor","bases/heads/sligor.spr") #sprite file for the fixer
    PAUL_SPRITE    = ("paul.spr","Talk_to_Paul","bases/heads/paul.spr")
    ONYX_SPRITE    = ("monte0.spr","Talk_to_Onyx_Paladin","bases/heads/onyx.spr")
    sligormission1 = CampaignClickNode() # Initialize each node
    sligormission2 = CampaignClickNode() # Initialize each node
    slipaulmission = CampaignClickNode() # Initialize each node
    sligormission4 = CampaignClickNode() # Initialize each node
    sligormission5 = CampaignClickNode() # Initialize each node
    sligormission6 = CampaignClickNode() # Initialize each node
    sligormission7 = CampaignClickNode() # Initialize each node
    sligormission8 = CampaignClickNode() # Initialize each node
    sligorfinish = CampaignNode()

    priv=Campaign("sligor_campaign") # Name of the save game variable for the entire campaign. Can't contain spaces
    priv.Init(sligormission1) # the first node.
    
    MakeMission(priv, # Creates a cargo mission
        SLIGOR_SPRITE, # Campaign, sprite
        [InSystemCondition("Gemini/Junction","Speke")], # Where fixer meets you to start the mission
        [InSystemCondition("Gemini/Junction","Speke")], # Where the mission ends. Usually the same as starting point for next fixer.
        None, # Script to be run as you click on the fixer. A common use is to AddCredits() for the previous mission.
        None,
        'cleansweep',(0,8,2000,0,('Gemini/119ce','Gemini/Pentonville',),priv.name+"_mission",1,2,.9,0,['pirates_'],1,1),#FIXME needs testing!
        priv.name+"_mission", # Script to be set on completion. -1=Failure, 0=Not Accepted, 1=Succeed, 2=In progress
        sligorspeech1, # Dictionary containing what the fixer says.
        None, # If you reject the mission twice. "None" means that he continues asking you forever until you accept
        CampaignEndNode(priv), # If you lose the mission
        sligormission2, # If you win the mission. Usually points to the next mission
        sligormission1) # The current mission node.
    MakeCargoMission(priv, # Creates any type of mission
        SLIGOR_SPRITE, # Campaign, sprite
        [InSystemCondition("Gemini/Junction","Speke")], # Where fixer meets you to start the mission
        [InSystemCondition("Gemini/Valhalla","Valkyrie")], # Where the mission ends.
        AddCredits(25000), # Script to be run as you click on the fixer. A common use is to AddCredits() for the previous mission.
        LoadMission("ambush","ambush",(priv.name+"_mission",("Gemini/J900",),0,'milita_',6,'','',[("#bb4400Ultimate runner, you're violating the law. Stop now!",False),("#996600Ultimate? I swear I didn't know my cargo was Ultimate!",True),("#bb4400It's always the same story we hear. Alas, I'mafraid we'll have to dump your cargo by destroying your ship."),("#bb4400I'm afraid that won't work, buddy.")],['Gemini/J900', 'Gemini/Telar', 'Gemini/Valhalla'], 'Valkyrie')), # Script to be run to start the mission (usually None if you don't have a script, but ambush is also common.)
        ("Ultimate",15), # Mission arguments.
        priv.name+"_mission", # Script to be set on completion. -1=Failure, 0=Not Accepted, 1=Succeed, 2=In progress
        sligorspeech2, # Dictionary containing what the fixer says.
        None, # If you reject the mission twice. "None" means that he continues asking you forever until you accept
        CampaignEndNode(priv), # If you lose the mission
        slipaulmission, # If you win the mission. Usually points to the next mission
        sligormission2) # The current mission node.
    MakeCargoMission(priv, # Creates any type of mission
        PAUL_SPRITE, # Campaign, sprite
        [InSystemCondition("Gemini/Valhalla","Valkyrie")], # Where fixer meets you to start the mission
        [InSystemCondition("Gemini/Junction","Speke")], # Where the mission ends.
        None, # Script to add your credits
        LoadMission("ambush","ambush",(priv.name+"_mission",("Gemini/J900",),0,'retro_',6,'','',[("#bb4400Sinner! You are transporting information concerning retro operations!",False),("#996600Weren't you wearing a militia helmet last time?",True),("#bb4400The lord will prevent you from delivering that disc!"),("#996600I wonder how the lord keeps such an empty system so populated, but don't worry: I'll clean it up for him.")],['Gemini/Telar', 'Gemini/J900', 'Gemini/Junction'], 'Speke')), # Script to be run to start the mission (usually None if you don't have a script, but ambush is also common.)
        ("Operations_disc",1), # Mission arguments.
        priv.name+"_mission", # Script to be set on completion. -1=Failure, 0=Not Accepted, 1=Succeed, 2=In progress
        sligorpaulspeech, # Dictionary containing what the fixer says.
        None, # If you reject the mission twice. "None" means that he continues asking you forever until you accept
        CampaignEndNode(priv), # If you lose the mission
        sligormission4, # If you win the mission. Usually points to the next mission
        slipaulmission) # The current mission node.
    MakeMission(priv, # Creates any type of mission
        SLIGOR_SPRITE, # Campaign, sprite
        [InSystemCondition("Gemini/Junction","Speke")], # Where fixer meets you to start the mission
        [InSystemCondition("Gemini/Junction","Speke")], # Where the mission ends.
        AddCredits(20000), # Script to be run as you click on the fixer. A common use is to AddCredits() for the previous mission.
        LaunchWingmen("hunter__","galaxygs",1), # Script to be run to start the mission (usually None if you don't have a script. Do NOT load an ambush mission here.)
        'defend',('retro_',0,6,5000,123456.789,0,False,True,'merchant__',(),priv.name+"_mission",'','drayman','',1), # Mission arguments.
        priv.name+"_mission", # Script to be set on completion. -1=Failure, 0=Not Accepted, 1=Succeed, 2=In progress
        sligorspeech4, # Dictionary containing what the fixer says.
        None, # If you reject the mission twice. "None" means that he continues asking you forever until you accept
        CampaignEndNode(priv), # If you lose the mission
        sligormission5, # If you win the mission. Usually points to the next mission
        sligormission4) # The current mission node.
    MakeMission(priv, # Creates any type of mission
        SLIGOR_SPRITE, # Campaign, sprite
        [InSystemCondition("Gemini/Junction","Speke")], # Where fixer meets you to start the mission
        [InSystemCondition("Gemini/Junction","Speke")], # Where the mission ends.
        AddCredits(20000), # Script to be run as you click on the fixer. A common use is to AddCredits() for the previous mission.
        LaunchWingmen("militia__","hornet",4), # Script to be run to start the mission (usually None if you don't have a script. Do NOT load an ambush mission here.)
        'escort_local',('retro_',0,6,0,3000,0,False,'militia__',(),priv.name+"_mission",'','sparrowhawk','','draymanCVL',["Hornet Leader hailing Privateer, protect the flagship until all enemy targets are destroyed!"]),
        priv.name+"_mission", # Script to be set on completion. -1=Failure, 0=Not Accepted, 1=Succeed, 2=In progress
        sligorspeech5, # Dictionary containing what the fixer says.
        None, # If you reject the mission twice. "None" means that he continues asking you forever until you accept
        CampaignEndNode(priv), # If you lose the mission
        sligormission6, # If you win the mission. Usually points to the next mission
        sligormission5) # The current mission node.
    MakeCargoMission(priv, # Creates a cargo mission
        SLIGOR_SPRITE, # Campaign, sprite
        [InSystemCondition("Gemini/Junction","Speke")], # Where fixer meets you to start the mission
        [InSystemCondition("Gemini/Pyrenees","New_Iberia")], # Where the mission ends. Usually the same as starting point for next fixer.
        AddCredits(30000,AddTechnology("hornetcvl")), # Script to be run as you click on the fixer. A common use is to AddCredits() for the previous mission.
        LoadMission("directions_mission","directions_mission",(priv.name+"_mission",['Gemini/Penders_Star', 'Gemini/Troy', 'Gemini/Pyrenees'], 'New_Iberia')), # Script to be run to start the mission (usually None if you don't have a script, but ambush is also common.) (having no destination will call significant unit.. oakham should be the only dockable significant in that system
        ("Escort_ID_card",1), # Mission arguments.
        priv.name+"_mission", # Script to be set on completion. -1=Failure, 0=Not Accepted, 1=Succeed, 2=In progress
        sligorspeech6, # Dictionary containing what the fixer says.
        None, # If you reject the mission twice. "None" means that he continues asking you forever until you accept
        CampaignEndNode(priv), # If you lose the mission
        sligormission7, # If you win the mission. Usually points to the next mission
        sligormission6) # The current mission node.
    MakeMission(priv, # Creates a cargo mission
        ONYX_SPRITE, # Campaign, sprite
        [InSystemCondition("Gemini/Pyrenees","New_Iberia")], # Where fixer meets you to start the mission
        [InSystemCondition("Gemini/Junction","Speke")], # Where the mission ends. Usually the same as starting point for next fixer.
        None,
        LoadMission("ambush","ambush",(priv.name+"_mission",("Gemini/Penders_Star",),0,'retro_',6,'krant','',[("#bb4400Ha! Once more you've taken steps to lure you into the trap of the LORD!")],['Gemini/Troy', 'Gemini/Penders_Star', 'Gemini/Junction'], 'Speke')), # Script to be run to start the mission (usually None if you don't have a script, but ambush is also common.)
        "escort_mission",("militia__",0,0,0,1500,0,0,0,("Gemini/Troy","Gemini/Penders_Star","Gemini/Junction"),priv.name+"_mission",'','draymanCVL'),
        priv.name+"_mission", # Script to be set on completion. -1=Failure, 0=Not Accepted, 1=Succeed, 2=In progress
        sligorspeech7, # Dictionary containing what the fixer says.
        None, # If you reject the mission twice. "None" means that he continues asking you forever until you accept
        CampaignEndNode(priv), # If you lose the mission
        sligorfinish,
        sligormission7) # The current mission node.
    sligorfinish.Init(priv,
        [],
        None,
        None,
        GoToSubnode(0),
        None,
        [CampaignClickNode().Init(priv,
            [InSystemCondition("Gemini/Junction","Speke")],
            sligorsuccess,
            ONYX_SPRITE,
            TrueSubnode(AddTechnology("dmcvl")),
            None,
            [CampaignEndNode(priv)])]) # YOU WIN!!!

    return priv #return the newly created campaign back.