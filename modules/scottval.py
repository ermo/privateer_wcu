import campaign_lib
from campaign_lib import *
scottspeech1={"intro":[("Burrows","I'm looking for work."),
                            ("Governor_Scott","Thank goodness! You're hired!"),
                            ("Burrows","But..."),
                            ("Governor_Scott","We're about to send out a freighter. It is about to be intercepted by a large pirate force. Defend it until it reaches the jump point. I'll pay 50000 credits."),
                            ("Burrows","I'm..."),
                            ("Governor_Scott","Will you do the job, or not?")],
                "reject1":[("Burrows","Listen, I usually tend to inform myself better."),
                            ("Governor_Scott","We have no time for that!")],
                "reconsider":[("Burrows","Okay, tell me about the mission again."),
                            ("Governor_Scott","Defend our freighter from Pirates. I'll pay 50000 credits.")],
                "reject2":[("Burrows","That's not enough information."),
                            ("Governor_Scott","You fool! It's already too late. The freighter has been destroyed!")],
                "accept":[("Burrows","I'm on my way!"),
                            ("Governor_Scott","Thanks! Thanks alot!")],
                "accept2":[("Governor_Scott","C'mon now, launch!")],
                "reminder":[("Governor_Scott","What are you doing here?"),
                            ("Burrows","Just wandering around. What's the hurry?"),
                            ("Governor_Scott","We need that deal! The freighter could be destroyed any moment! Move out NOW!"),
                            ("Burrows","Cool down, I'm a man who usually fulfills his mission objectives. I'll leave now.")],
                "failure":[("Governor_Scott","The freighter is destroyed! It will take us months to recover from this loss! Get away before I have you arrested!")]
                }
scottspeech2={"intro":[("Governor_Scott","The freighter... the freighter..."),
                            ("Burrows","The freighter has moved out. Cool down."),
                            ("Governor_Scott","Thank goodness. We put all our hopes into this run. If we hadn't managed to bring the freighter out to New Caledonia, the base would have lost a lot of money."),
                            ("Burrows","Yeah, whatever you say, Mr...?"),
                            ("Governor_Scott","I'm sorry for my impoliteness. My name is Mr. Scott, I am Governor of the Prasepe system and the head of this base."),
                            ("Burrows","Wow, a high-ranking authority. Nice to meet you. Tell me, why are you in such desperate need of privateers like me? Shouldn't you have a task force on your own?"),
                            ("Governor_Scott","We had one, as well as an insys militia squadron. They're all gone. Many of their ships were stolen. The Pirates and the Retros finished off the rest."),
                            ("Burrows","You mean you lost all your forces to thieves, pirates and fanatical nutcases?"),
                            ("Governor_Scott","The problem is that our foes seem to have an infinite source of ships. Most likely, they were purchased from Governor Menesch, a corrupt Governor selling confed ships. I also think he managed to steal my ships. You may have heard about him."),
                            ("Burrows","Erm... yes, isn't that the guy who is flooding the sector with Talons?"),
                            ("Governor_Scott","Superficially. The last thing I heard of him was that he brought some Ferrets to the open market. And he'll surely make some extra credits by selling my Scimitars. But I don't think that is his primary goal."),
                            ("Burrows","You're implying that he is not in this business for the money, right?"),
                            ("Governor_Scott","Menesch is presumably one of the richest humans alive, already. He doesn't need to make more money. My guess is that he is trying to gain influence within the Pirate clans, maybe within the Retros, and I even believe that he'd also be unscrupulous enough to deal with the Kilrathi."),
                            ("Burrows","That's a nice story, but how can I help you?"),
                            ("Governor_Scott","Ah yes. In case you want to keep on working for me, I have another mission for you. We need to take the heat away from Saratov. Therefore I need you to take out a Pirate ship operating in this system."),
                            ("Burrows","What's the wages?"),
                            ("Governor_Scott","I'll pay 25000 credits. It's a Drayman and I don't know anything about its escort. But I can spare a wingman for you.")],
                "reject1":[("Burrows","A talon-flying wing-man? Thanks; but.. no thanks; that's a liability."),
                ("Governor_Scott","I was going to offer you a Hornet-flying wing-man, but I can smell a chicken when I see one. Have a good day.")],
                "reconsider":[("Burrows","Okay, what was that mission again?"),
                            ("Governor_Scott","Track down a pirate Drayman in Prasepe. You'll get 25000 credits and a Hornet-flying wingman.")],
                "reject2":[("Burrows","No thanks; I'm not sure a Hornet would do much good."),
                            ("Governor_Scott","Whatever you say.")],
                "accept":[("Burrows","Sounds good. Consider it done.")],
                "accept2":[("Governor_Scott","Good.")],
                "reminder":[("Governor_Scott","Don't try to fool me. That Drayman is still out there...")],
                "failure":[("Governor_Scott","The Drayman is still active. The mission shouldn't have been that difficult. I can get far better pilots for that much money.")]
                }
scottspeech3={"intro":[("Governor_Scott","The Drayman is history. Good job."),
                            ("Burrows","Yeah. Tell me, why are the Pirates bald-headed enough to fly around in New Caledonia?"),
                            ("Governor_Scott","Because they nearly took control of it. The region around New Caledonia and J900 is infested with pirates and retros."),
                            ("Burrows","And you're about to change that?"),
                            ("Governor_Scott","Haha, no; I cannot deal with it on my own. If the Confederation doesn't see a problem... I'm just here to keep my base running."),
                            ("Burrows","So, what else can I do to help keep your base running?"),
                            ("Governor_Scott","Our last action caught additional attention within Menesch's corrupt strike teams. An assault force is approaching our base. We're currently assembling a defense squadron but I'd like you to help them out."),
                            ("Burrows","I need more details, please."),
                            ("Governor_Scott","Sensors show 6 Demons coming from the jump point. All we have left is two Scimitars; I want you to lead the defense."),
                            ("Burrows","What is the pay?"),
                            ("Governor_Scott","20,000 credits. It'll be tight, but Menesch's forces are known to be badly trained and disorganized so don't expect them to pop up all at once. I doubt you'll have too much trouble in this case.")],
                "reject1":[("Burrows","3 against 6? I'm not too sure I like those odds all that much, Governor."),
                            ("Governor_Scott","We have no other choice. And you can't compare a Demon to a Scimitar... C'mon!")],
                "reconsider":[("Burrows","Okay, what was that mission again?"),
                            ("Governor_Scott","2 Scimitars and you against 6 Demons. Payoff is 20000")],
                "reject2":[("Burrows","No, that doesn't sound smart."),
                            ("Governor_Scott","You're being a pain in the ass!")],
                "accept":[("Burrows","Okay, I'll save your base."),
                            ("Governor_Scott","Thank you. Your wingmen are already waiting for you.")],
                "accept2":[("Governor_Scott","Good.")],
                "reminder":[("Governor_Scott","Please leave before the lights go out at this base.")],
                "failure":[("Governor_Scott","Unbelievable! They raided the base! We barely have enough to eat. Go away!")]
                }
scottspeech4={"intro":[("Governor_Scott","Nice flying."),
                            ("Burrows","Thanks. What's next?"),
                            ("Governor_Scott","I've located the flagship of one of the top dealers for Menesch. This is a unique chance to interrupt the illegal business in this quadrant."),
                            ("Burrows","You want me to take this dealer out."),
                            ("Governor_Scott","Yes. I've learned that his ship is en route to a secret meeting with a corrupt administrator from my base. We've arrested our guy, and are going to send you to kick their asses instead."),
                            ("Burrows","I assume this top dealer won't be stumbling around in an old Tarsus?"),
                            ("Governor_Scott","A Paradigm; plus escorts. I can offer 3 Scimitars with my 3 remaining pilots, which happen to be my best 3 pilots, as your personal escort. I'd suggest you order them to take care of the escorts while you take on the Paradigm."),
                            ("Burrows","What's the pay?"),
                            ("Governor_Scott","This fish is worth 75,000 credits to me.")],
                "reject1":[("Burrows","That's an awful lot of money, but I doubt there's any chance we will succeed."),
                            ("Governor_Scott","As I said, this is a unique chance. Please reconsider.")],
                "reconsider":[("Burrows","Okay, I've reconsidered."),
                            ("Governor_Scott","For 75,000, kill the dealer's Paradigm. You have 3 Scimitar-flying wingmen.")],
                "reject2":[("Burrows","...and no bombers? Forget it."),
                            ("Governor_Scott","Man, I need you for that!")],
                "accept":[("Burrows","75,000! Wow! I'm in!"),
                            ("Governor_Scott","Good. Please hurry up.")],
                "accept2":[("Governor_Scott","Good. Please hurry up.")],
                "reminder":[("Governor_Scott","Did you manage to destroy the Paradigm?"),
                            ("Burrows","I haven't left yet. I just wanted to make sure I heard you right. 'Paradigm' you said? That's a destroyer!"),
                            ("Governor_Scott","A destroyer the likes of which most have been destroyed... No wonder the Confeds are letting the rest go... Just move out and do your job; would you?"),
                            ("Burrows","Relax, I'll take off immediately.")],
                "failure":[("Governor_Scott","The Paradigm managed to escape. The slowest destroyer ever designed, in fact; and it gets away from you! I'm sorry, this was the last mission for you.")]
                }
scottsuccess=[("UNLOCKED: Scimitar."),
            ("Governor_Scott","Awesome job! Here is your money. And good news: Our Insys forces have found a freighter full of our stolen ships."),
            ("Burrows","Ferrets?"),
            ("Governor_Scott","No. Imagine that, we found our own Scimitars. We've got our full fighter squadron back! Since we're a lot safer now, I'm going to sell some of those ships to benefit the base. You're welcome to also buy one if you like."),
            ("Burrows","I'll think about it. I assume we're done?"),
            ("Governor_Scott","Yes. Spend your money wisely."),
            ("Burrows","I will. Take care.")]

def LoadScottCampaign():
    SCOTT_SPRITE  = ("sandoval.spr","Talk_to_Governor_Scott","bases/heads/scott.spr") #sprite file for the fixer
    ScottMission1 = CampaignClickNode() # Initialize each node
    ScottMission2 = CampaignClickNode() # Initialize each node
    ScottMission3 = CampaignClickNode() # Initialize each node
    ScottMission4 = CampaignClickNode() # Initialize each node
    ScottFinish = CampaignNode()

    priv=Campaign("scott_campaign") # Name of the save game variable for the entire campaign. Can't contain spaces
    priv.Init(ScottMission1) # the first node.
    
    MakeMission(priv, # Creates a cargo mission
        SCOTT_SPRITE, # Campaign, sprite
        [InSystemCondition("Gemini/Prasepe","Saratov")], # Where fixer meets you to start the mission
        [InSystemCondition("Gemini/Prasepe","Saratov")], # Where the mission ends. Usually the same as starting point for next fixer.
        ClearFactionRecord('militia',1.0,PushRelation('militia')), # Script to be run as you click on the fixer. A common use is to AddCredits() for the previous mission.
        None,
        'escort_local',('pirates_',0,4,0,3000,0,False,'militia__',(),priv.name+"_mission",'','talon','','draymanCVL',["Another voidsucker!"]),
        priv.name+"_mission", # Script to be set on completion. -1=Failure, 0=Not Accepted, 1=Succeed, 2=In progress
        scottspeech1, # Dictionary containing what the fixer says.
        None, # If you reject the mission twice. "None" means that he continues asking you forever until you accept
        CampaignEndNode(priv), # If you lose the mission
        ScottMission2, # If you win the mission. Usually points to the next mission
        ScottMission1) # The current mission node.
    MakeMission(priv, # Creates any type of mission
        SCOTT_SPRITE, # Campaign, sprite
        [InSystemCondition("Gemini/Prasepe","Saratov")], # Where fixer meets you to start the mission
        [InSystemCondition("Gemini/Prasepe","Saratov")], # Where the mission ends. Usually the same as starting point for next fixer.
        AddCredits(50000), # Script to be run as you click on the fixer. A common use is to AddCredits() for the previous mission.
        LaunchWingmen("militia__","hornet",1), # Script to be run to start the mission (usually None if you don't have a script. Do NOT load an ambush mission here.)
        'bounty_leader',(0,0,0,False,3,'pirates_',(),priv.name+"_mission",'','drayman',False,'','talon',["Arrr mates, guess who is coming for dinner?"]), # Mission arguments.
        priv.name+"_mission", # Script to be set on completion. -1=Failure, 0=Not Accepted, 1=Succeed, 2=In progress
        scottspeech2, # Dictionary containing what the fixer says.
        None, # If you reject the mission twice. "None" means that he continues asking you forever until you accept
        CampaignEndNode(priv), # If you lose the mission
        ScottMission3, # If you win the mission. Usually points to the next mission
        ScottMission2) # The current mission node.
    MakeMission(priv, # Creates any type of mission
        SCOTT_SPRITE, # Campaign, sprite
        [InSystemCondition("Gemini/Prasepe","Saratov")], # Where fixer meets you to start the mission
        [InSystemCondition("Gemini/Prasepe","Saratov")], # Where the mission ends. Usually the same as starting point for next fixer.
        AddCredits(25000), # Script to add your credits
        LaunchWingmen("militia__","scimitar",2), # Script to be run to start the mission (usually None if you don't have a script. Do NOT load an ambush mission here.)
        'defend',('pirates_',0,1,5000,123456.789,0,False,True,'Saratov',(),priv.name+"_mission",'','demon','',6), # Mission arguments.
        priv.name+"_mission", # Script to be set on completion. -1=Failure, 0=Not Accepted, 1=Succeed, 2=In progress
        scottspeech3, # Dictionary containing what the fixer says.
        None, # If you reject the mission twice. "None" means that he continues asking you forever until you accept
        CampaignEndNode(priv), # If you lose the mission
        ScottMission4, # If you win the mission. Usually points to the next mission
        ScottMission3) # The current mission node.
    MakeMission(priv, # Creates any type of mission
        SCOTT_SPRITE, # Campaign, sprite
        [InSystemCondition("Gemini/Prasepe","Saratov")], # Where fixer meets you to start the mission
        [InSystemCondition("Gemini/Prasepe","Saratov")], # Where the mission ends. Usually the same as starting point for next fixer.
        AddCredits(20000), # Script to be run as you click on the fixer. A common use is to AddCredits() for the previous mission.
        LaunchWingmen("militia__","scimitar",3), # Script to be run to start the mission (usually None if you don't have a script. Do NOT load an ambush mission here.)
        'bounty_leader',(0,0,0,False,2,'pirates_',(),priv.name+"_mission",'','paradigm',False,'','fireblade',["You won't get a chance to witness our presence here, Privateer!"]), # Mission arguments.
        priv.name+"_mission", # Script to be set on completion. -1=Failure, 0=Not Accepted, 1=Succeed, 2=In progress
        scottspeech4, # Dictionary containing what the fixer says.
        None, # If you reject the mission twice. "None" means that he continues asking you forever until you accept
        CampaignEndNode(priv), # If you lose the mission
        ScottFinish, # If you win the mission. Usually points to the next mission
        ScottMission4) # The current mission node.
    ScottFinish.Init(priv,
        [],
        None,
        None,
        GoToSubnode(0),
        None,
        [CampaignClickNode().Init(priv,
            [InSystemCondition("Gemini/Prasepe","Saratov")],
            scottsuccess,
            SCOTT_SPRITE,
            TrueSubnode(AddCredits(75000,AddTechnology("scott"))),
            None,
            [CampaignEndNode(priv)])]) # YOU WIN!!!
    return priv #return the newly created campaign back.
