import campaign_lib
from campaign_lib import *
avalonspeech1={"intro":[("Burrows","Good day. May I introduce myself?"),
                            ("Avalon","No."),
                            ("Burrows","Alas, I like women with a sense of humour. My name is Grayson Burrows."),
                            ("Avalon","I don't care for your name, nor for your presence, nor for the reason for you presence, nor for your existence. Why don't you simply go away? I got loads of problems..."),
                            ("Burrows","You sound like my ideal partner... You see, I suffer from a problem-deficiency... I'm a privateer. Can I help you?"),
                            ("Avalon","Okay then... since obviously you're not going to leave... But never call me your 'partner' again! My name is Avalon, I'm working for Azuma weapons, energy section; and I'm indeed in need of a good privateer. But I doubt you are capable enough of helping me."),
                            ("Burrows","My performance increases forever linearly with the money, Avalon."),
                            ("Avalon","I could get more than just money for you. Remember we are Azuma Weapons..."),
                            ("Burrows","Do you mean that you can give me access to technologies?"),
                            ("Avalon","The probability increases linearly with your performance."),
                            ("Burrows","Okay then, you got my attention. What's the first problem?"),
                            ("Avalon","I forgot to pack some spare parts with our last shipment to New Constantinople, and since there's nobody else around, I guess I'll let you complete the run. Fly a load of spare parts to NewCon. Come back here afterwards."),
                            ("Burrows","Are you out of freighters? Why do you give this job to me? The Merchants' Guild would charge you less."),
                            ("Avalon","We're producing at Beaconsfield, and that's quite a long route to the major bases; and the shipment was already late when I realized the spares were left out of the crate. I need fast delivery. I'll pay 10000 credits."),
                            ("Burrows","10000 is not exactly the level I was hoping for; but, what about that technology access?"),
                            ("Avalon","Consider this easy mission as a first step; the bigger reward would come at the end. It is only 10000 because no opposition is expected. There will be more challenging --and higher-paying-- missions later Are you in?")],
                "reject1":[("Burrows","No thanks. I'm not a milkman."),
                            ("Avalon","That's not milk, Burrows.")],
                "reconsider":[("Burrows","I've reconsidered."),
                            ("Avalon","Nice. I'll pay 10000 for delivering my spare parts to New Constantinople.")],
                "reject2":[("Burrows","That's not the kind of work I'm looking for.")],
                "accept":[("Burrows","I'm in."),
                            ("Avalon","Okay. Get going, then.")],
                "accept2":[("Avalon","Good.")],
                "reminder":[("Avalon","The cargo has been transferred to your ship. What's wrong?"),
                            ("Burrows","Nothing. I thought I'd drink up before leaving."),
                            ("Avalon","It's an easy run. Don't get cold feet."),
                            ("Burrows","I'll think about your warm words when I'm out there, Avalon.")],
                "failure":[("Avalon","Don't expect me to give you a payment after this miserable show. I had a bad feeling about you from the first moment you showed up here.")]
                }
avalonspeech2={"intro":[("Burrows","NewCon is equipped."),
                            ("Avalon","Fine. I hope I didn't promise too much with stating that it is an easy cruise, did I?"),
                            ("Burrows","You did, actually. I was ambushed by pirates near Liverpool."),
                            ("Avalon","What? PIRATES?"),
                            ("Burrows","Yeah, pirates. Never heard of them? They wear funny hats, have hooks and..."),
                            ("Avalon","I know who the pirates are! But we never get ambushed by them, --intentionally. Usually hired Mercs, but we never had a real pirate assault. I wonder what they wanted to achieve with that."),
                            ("Burrows","Maybe they wanted to get your cargo?"),
                            ("Avalon","Are you really that dumb? Guess what happens when you shoot at a ship full of energy cells? It explodes! That makes no sense!"),
                            ("Burrows","Calm down! I didn't know I was transporting explosive cargo. Do you have a better theory?"),
                            ("Avalon","No, but we could try to find out more about it. There seems to be an employer... I want you to go back to where you were ambushed. Dock at Liverpool and check the bar, see if you can get any information from the locals."),
                            ("Burrows","Even if they were dumb enough to hang out in the bar there, they'd surely not talk to me."),
                            ("Avalon","Since we have no other hints, let's try it anyways. I'll pay you 20000 for... well... for trying.")],
                "reject1":[("Burrows","I'm sorry; I'm getting bored.")],
                "reconsider":[("Burrows","Tell me about the mission again."),
                            ("Avalon","For 20000, check Liverpool in Newcastle for hints about the last pirate attack.")],
                "reject2":[("Burrows","No. First an explosive milk run with an ambush; now you want me to play Sam Spade?")],
                "accept":[("Burrows","Okay, but without a guarantee that I find anything.")],
                "accept2":[("Avalon","I'm awaiting your return.")],
                "reminder":[("Avalon","Listen, I doubt that the pirates will wait for your return."),
                            ("Burrows","I know. I'll take off in a minute."),
                            ("Avalon","I'll wait here.")],
                "failure":[("Avalon","Since you cannot make up your mind in time, I'll send out somebody else. Our business relation ends here.")]
                }

avalonspeech3={"intro":[("Avalon","Did you find out anything?"),
                            ("Burrows","No... the bar in Liverpool was empty and all I encountered was some Retros."),
                            ("Avalon","Damn!"),
                            ("Burrows","On the other hand, maybe the pirate ambush was just coincidence."),
                            ("Avalon","Well, as long as we have no other indication, I must concur."),
                            ("Burrows","Okay then, back to routine. Another explosive run?"),
                            ("Avalon","Not for you. Since you did a good job I'd like to promote you to collecting our payments."),
                            ("Burrows","Oh sweet! Makes me feel like Al Capone..."),
                            ("Avalon","Your first run leads you on the standard route. Take this ID card and fly to New Constantinople. Meet a contact there and collect the payment. Come back here afterwards."),
                            ("Burrows","Why shouldn't I just run away with the money?"),
                            ("Avalon","Because the Confederation and the Militia are our primary customers, so all I'd need to do is make a single com call to make Kilrah the safest place for you."),
                            ("Burrows","Good argument."),
                            ("Avalon","Fine. I'll pay 20000 credits. What do you say?")],
                "reject1":[("Burrows","I say no. I must admit that this pirate stuff made me nervous somehow."),
                            ("Avalon","Okay then, come back as soon as your pants are dry again.")],
                "reconsider":[("Burrows","Washed my pants. Tell me about your mission again."),
                            ("Avalon","For 20000; collect our payment; New Constantinople.")],
                "reject2":[("Burrows","Mmmh... no thanks.")],
                "accept":[("Burrows","I say yes, and see you later.")],
                "accept2":[("Burrows","Got it. I'm on my way.")],
                "reminder":[("Avalon","You got the ID card. Move it!")],
                "failure":[("Avalon","Okay then... no money, no ID card. No payment for you, buddy.")]
                }

avalonspeech4={"intro":[("Avalon","Where's the money?"),
                            ("Burrows","No idea. I was visiting the bar in New Constantinople, spent several hours there, but nobody was around."),
                            ("Avalon","Nobody was around? Are you trying to fool me? You stole the money!"),
                            ("Burrows","I didn't. Check the ID card, I told the truth."),
                            ("Avalon","Indeed. What the hell is going on here?"),
                            ("Burrows","I'm not sure, but there might be a connection to those pirates... --who ambushed me, once again."),
                            ("Avalon","Pirates again?! It seems we understated the problem. There's something going on in the background."),
                            ("Burrows","You should check NewCons flight info for discrepancies."),
                            ("Avalon","Good idea. Let's see... flight records indicate that a transport has wiped out some information of its flight plan. Hey, we're lucky! The ship currently is docked at Beaconsfield. I'll get to talk to their captain about that."),
                            ("Burrows","Fine, and afterwards I can go out and find this contact of yours."),
                            ("(A person suddenly jumps up from his table and runs out of the bar.)"),
                            ("Avalon","What was that?"),
                            ("Burrows","I guess that was the captain of the named ship."),
                            ("Avalon","He... he is running to the landing pad! Follow him!"),
                            ("Burrows","Piano... we haven't talked about my payment yet."),
                            ("Avalon","50000! Now follow him!")],
                "reject1":[("Avalon","Idiot! He already launched!")],
                "reconsider":[("Burrows","We need to talk about my payment again."),
                            ("Avalon","50000! NOW MOVE!")],
                "reject2":[("Burrows","I've got loads of time.")],
                "accept":[("Burrows","Man... my lungs...")],
                "accept2":[("Burrows","Okay okay... I was just kidding...")],
                "reminder":[("Avalon","What the FUCK?!? FOLLOW THE SHIP IMMEDIATELY!!!"),
                            ("Burrows","We need to talk about the way we communicate with each others. You're too loud."),
                            ("Avalon","MOVE OUT OR YOU'LL HEAR HOW LOUD I REALLY CAN TALK TO YOU!")],
                "failure":[("Avalon","The ship disappeared from the sensors. You missed a unique chance to learn more about the ambushes. You're fired.")]
                }
avalonspeech5={"intro":[("Burrows","Hi, I'm back from my cruise."),
                            ("Avalon","Did you get him?"),
                            ("Burrows","Yes I did. Fortunately, the pirates wanted to silence him for good; so he gave me all his info in exchange for my saving his ass."),
                            ("Avalon","Nice job. What did he say?"),
                            ("Burrows","I know the name of the guy we're looking for; Loki. They've taken him to the pirate base in KM-252."),
                            ("Avalon","Well done. Here's your money. We can only assume that Loki has sold them information about our flight routes; what else he got?; --not that I understand the pirates' interest?"),
                            ("Burrows","We know who has the answer."),
                            ("Avalon","Yes! I want you to get that answer, and I'll pay 40000 for that. Tell him that he's in deep trouble if he doesn't come willingly.")],
                "reject1":[("Burrows","Sorry? You want ME to dock at a pirate base, ask Loki about his criminal motivations, and await for a reply? Hahaha...")],
                "reconsider":[("Burrows","Erm... what was the payment again?"),
                            ("Avalon","40000. Visit Loki and talk to him.")],
                "reject2":[("Burrows","Not without a militia troop transport covering my back; sorry.")],
                "accept":[("Burrows","Okay, I'll do it; but don't expect him to jump into my ship. I wouldn't if I were in his shoes.")],
                "accept2":[("Avalon","Glad you reconsidered. You're the man for this job.")],
                "reminder":[("Avalon","You need to talk to Loki. I know it's risky to go to a pirate base, but I need you to do it.")],
                "failure":[("Avalon","You're a good pilot; but you might not be that good in the art of persuasion. I understand this; so, no hard feelings; but I'll have to find somebody else.")]
                }
avalonspeech6={"intro":[("Burrows","You're Loki, right?"),
                            ("Loki","Correct. Who are you?, and what do you want?"),
                            ("Burrows","I'm a privateer. Avalon sent me here. He believes you sold information to pirates!"),
                            ("Loki","News travels fast... Well, I was stuck here already, anyways."),
                            ("Burrows","Why did you do it? You're a fugitive now. Was it worth it?"),
                            ("Loki","I was sick of my old life! A nobody, messing with numbers all day, creating tables and presentations nobody would ever read. Now I'm a mean who gets the respect he deserves!"),
                            ("Burrows","Respect?! You abused your position for... Anyways, Avalon wants to know who are your employers, and what are their motivations; then she'll have your head; --unless you return willingly."),
                            ("Loki","Listen up: you're at a pirate base here. What are you going to do? Call the militias?"),
                            ("Burrows","I'm offering you perhaps the only chance you'll get to get off this base... aboard my ship; and maybe Avalon won't take you to court..."),
                            ("Loki","I'm not entirely sure you could leave this place alive."),
                            ("Burrows","Don't worry for me; I've been here before. So, who's your employer?"),
                            ("Loki","You don't want to meet him; your encounter could prove deadly."),
                            ("Burrows","Heard that many times... So, who and where is he?"),
                            ("Loki","Ah well... since you have such a death wish, I'll give you his flight plan, and you can ask him about his motivations. As for me, I'm staying here, okay?"),
                            ("Burrows","But if you're so sure I won't succeed; couldn't sharing his flight plan with me get you in trouble?"),
                            ("Loki","You assume that he knows I have his flight plan... He doesn't; he'll suspect his pals, instead, which will be good for me... Anyways, have we a deal?")],
                "reject1":[("Burrows","That's not enough. If necessary I'll beat you into my ship."),
                            ("Loki","With all my pirate pals around me? Try it!")],
                "reconsider":[("Loki","I'll give you my employer's flight plan if you'll agree to leave me alone... deal?")],
                "reject2":[("Burrows","Climb into my ship or you'll regret it!")],
                "accept":[("Loki","Here you are buddy. And tell Avalon that I won't be coming back; --no matter who she sends for me.")],
                "accept2":[("Burrows","Alright, give me that flight plan. I'll leave.")],
                "reminder":[("Loki","You got the flight plan. Now, I'll wish you good luck; you'll need it.")],
                "failure":[("Loki","Okay, you had your fun for the longest time. Better leave now, or I'll alert my mates.")]
                }

avalonspeech7={"intro":[("Avalon","Where is Loki?"),
                            ("Burrows","He wouldn't leave; I think he's too scared of the pirates around him."),
                            ("Avalon","And you allowed him to stay?"),
                            ("Burrows","What did you expect me to do? Defeat an entire pirate base in close combat, while dragging an unwilling passenger, all the way from the bar to my ship on the pad?"),
                            ("Avalon","Okay, maybe not... But now we're at a dead end."),
                            ("Burrows","Not exactly. We can ask his employer a few questions. I managed to get his flight plan. Here..."),
                            ("Avalon","That's fantastic! According to this, his convoy should be passing through Newcastle very soon!"),
                            ("Burrows","Yeah, I could go there and ask him about his plans..."),
                            ("Avalon","Ask? Kill him first; then ask."),
                            ("Burrows","Erm... That's not a good idea, Avalon. We'd kill the only person who could tell us more."),
                            ("Avalon","Man, if we killed the employer, we'll get rid of our whole problem! Forget about the information."),
                            ("Burrows","What about Loki?"),
                            ("Avalon","At the moment the pirates will find out that he gave you the flight plan, guess what will happen to him?"),
                            ("Burrows","Nice... I haven't thought about that! But there's still a problem... Loki talked something about a 'deadly encounter'. I guess this guy won't be flying around in a Tarsus."),
                            ("Avalon","I see what you're getting at... I'll get a Militia Raptor to take out the employer, while you deal with the escorts. And I'll pay 80000 for the end of this sad story. How's that?")],
                "reject1":[("Burrows","I'm not willing to run into an unknown number of foes... not again. Sorry.")],
                "reconsider":[("Avalon","Come on. You'll get 80000 credits and a Raptor wingman. What else could you want?")],
                "reject2":[("Burrows","As I said, I don't want to end up as space dust. We went far enough.")],
                "accept":[("Burrows","Right on. Let's end this story.")],
                "accept2":[("Avalon","Great!")],
                "reminder":[("Avalon","Please don't spend too much time around here - you got a mission.")],
                "failure":[("Avalon","I understand the mission was quite hard, but failure wasn't an option. You're fired.")]
                }

avalonspeech8={"intro":[("UNLOCKED: Shield Level 1.5, Shield Level 2.5, Shield Level 3.5, Shield Level 4.5."),
                            ("Burrows","Mission complete."),
                            ("Avalon","Fantastic. Here's your money. And as I promised, the access to our stuff."),
                            ("Burrows","Thanks. Okay, since this was the final mission..."),
                            ("Avalon","Wait! I made up my mind, I actually do want to know more about the whole story. I want you to bring Loki back."),
                            ("Burrows","He said he won't leave. Or... do you have a new idea?"),
                            ("Avalon","Yes. Go back to KM-252 and tell him about the death of his employer; and that he's responsible for it; and that you'll tell the pirates about this if he won't come with you."),
                            ("Burrows","What's the pay?"),
                            ("Avalon","15000 should be enough."),
                            ("Burrows","I really don't like using blackmail..."),
                            ("Avalon","Alright; 20000. Take it or leave it.")],
                "reject1":[("Burrows","It is not enough. Sorry.")],
                "reconsider":[("Avalon","For 20000 credits, will you get Loki back from KM-252?")],
                "reject2":[("Burrows","No.")],
                "accept":[("Burrows","I'm on my way.")],
                "accept2":[("Avalon","Good.")],
                "reminder":[("Avalon","Get Loki and bring him here.")],
                "failure":[("Avalon","Loki is dead. We were about to unveil the whole story. Sorry, I cannot pay you for that.")]
                }

avalonspeech9={"intro":[("Loki","Oh no... it's you again! Didn't I express myself correctly?"),
                            ("Burrows","I met your employer. You were absolutely right; it was a deadly encounter..."),
                            ("Loki","You mean that he... HE is dead?"),
                            ("Burrows","That's correct. By the way, thanks for the flight plan. I would have never found him without it."),
                            ("Loki","Oh my god..."),
                            ("Burrows","I'll leave now, if you so wish; but I wanted to warn you that Avalon, a militia pilot, as well as a few others know how I got the flight plan. The word will get around, if it hasn't already... You're no longer safe, here."),
                            ("Loki","Damn! ....... Alright; I guess you win; I'd rather die quickly aboard your ship than be interrogated here slowly..."),
                            ("Burrows","Hey, this is what you wanted; isn't it? A not-so-boring life. I hope you're enjoying it."),
                            ("Loki","Stop that! Please get me out of here, quick!")],
                "reject1":[("Burrows","Forget it. You shall pay for your treachery.")],
                "reconsider":[("Loki","Please, get me out of here!")],
                "reject2":[("Burrows","I think you deserve what you'll get here. Have a nice death.")],
                "accept":[("Burrows","Get on my ship and let's go.")],
                "accept2":[("Burrows","Okay, I had my fun. But don't expect me to bring you to Jolson.")],
                "reminder":[("Loki","Come on... let's hurry...")],
                "failure":[("Some pirates start surrounding Loki's table. They grab him and push him out of the bar. You hear some loud talks, a man whining, and suddenly some shots out of a blaster. The pirates come back, putting Loki's dead body back onto his seat. One of the pirates silently tells you to leave or you could be Loki's table neighbour.")]
                }

avalonsuccess=[("UNLOCKED: Raptor, Reactor Level 6 to 9, Shield Level 6 to 9."),
            ("Avalon","Thanks for bringing Loki back. He's currently being interrogated. It seems that a rival company caused all this trouble. We'll see them in court."),
            ("Burrows","Good to know. Can I do anything else for you?"),
            ("Avalon","No... but I think you've earned yourself an extra reward. Azuma Weapons reserves some special items for special customers, and since you've saved our business, I'd like to give you access to it as well. We've given you the access codes that will allow you to purchase power reactors and shields of up to level 9, which are not usually available to civilians..."),
            ("Burrows","Wow! Wouldn't it be fun if I snatched up a Paradigm in my next mission!"),
            ("Avalon","And until you can afford a Paradigm, you could as well buy one of our Raptors. We've also given you access to it. We were using them for testing new stuff, but switched to other ships lately. So, here is the access. Feel free to buy a Raptor at a store holding them. It may be a bit old but it is still a solid ship."),
            ("Burrows","So many presents! It almost feels like Christmas... Thanks! I really appreciate it."),
            ("Avalon","You surely deserve it. Take care.")]

def LoadAvalonCampaign():
    AVALON_SPRITE    = ("murphy.spr", "Talk_to_Avalon","bases/heads/murphy.spr")
    LOKI_SPRITE    = ("monte1.spr","Talk_to_Loki","bases/heads/monte.spr")
    avalonmission1 = CampaignClickNode() # Initialize each node
    avalonmission2 = CampaignClickNode() # Initialize each node
    avalonmission3 = CampaignClickNode() # Initialize each node
    avalonmission4 = CampaignClickNode() # Initialize each node
    avalonmission5 = CampaignClickNode() # Initialize each node
    avalonmission6 = CampaignClickNode() # Initialize each node
    avalonmission7 = CampaignClickNode() # Initialize each node
    avalonmission8 = CampaignClickNode() # Initialize each node
    avalonmission9 = CampaignClickNode() # Initialize each node
    avalonfinish = CampaignNode()

    priv=Campaign("avalon_campaign") # Name of the save game variable for the entire campaign. Can't contain spaces
    priv.Init(avalonmission1) # the first node.
    
    MakeCargoMission(priv,
        AVALON_SPRITE,
        [InSystemCondition("Gemini/Auriga","Beaconsfield")], # Where fixer meets you to start the mission
        [InSystemCondition("Gemini/New_Constantinople","New_constantinople")], # Where the mission ends.
        ClearFactionRecord('militia',1.0,PushRelation('militia')),
        LoadMission("ambush","ambush",(priv.name+"_mission",("Gemini/Newcastle"),0,'pirates_',3,'talon','',[("Escort, your cargo shall not reach its destination!")],['Gemini/Newcastle', 'Gemini/New_Constantinople'], 'New_constantinople')),
        ("spare_parts",5), # "escort_mission",("militia",0,0,0,1500,0,0,0,("Gemini/Newcastle","Gemini/New_Constantinople"),priv.name+"_mission",'','draymanCVL'),
        priv.name+"_mission", # Script to be set on completion. -1=Failure, 0=Not Accepted, 1=Succeed, 2=In progress
        avalonspeech1, # Dictionary containing what the fixer says.
        None, # If you reject the mission twice. "None" means that he continues asking you forever until you accept
        CampaignEndNode(priv), # If you lose the mission
        avalonmission2, # If you win the mission. Usually points to the next mission
        avalonmission1) # The current mission node.
    MakeCargoMission(priv,
        AVALON_SPRITE,
        [InSystemCondition("Gemini/Auriga","Beaconsfield")],
        [InSystemCondition("Gemini/Newcastle","Liverpool")],
        AddCredits(10000),
        LoadMission("ambush","ambush",(priv.name+"_mission",("Gemini/Newcastle"),0,'retro_',3,'talon','',[("#bb4400Sinner! The Church of Man will wipe out all opposition!",False),("#996600Yeah... but excuse me, did you see some pirates around?",True),("#bb4400Your ridiculous tasks are insignificant compared to the grand plan of the Lord! Die!"),("#996600Okay guys, you asked for it...")],['Gemini/Newcastle'], 'Liverpool')),
        ("Investigate_Liverpool",1),
        priv.name+"_mission",
        avalonspeech2, # Dictionary containing what the fixer says.
        None,
        CampaignEndNode(priv),
        avalonmission3, # If you win the mission. Usually points to the next mission
        avalonmission2) # The current mission node.
    MakeCargoMission(priv, # Creates any type of mission
        AVALON_SPRITE, # Campaign, sprite
        [InSystemCondition("Gemini/Auriga","Beaconsfield")], # Where fixer meets you to start the mission
        [InSystemCondition("Gemini/New_Constantinople","New_constantinople")], # Where the mission ends.
        AddCredits(20000), 
        LoadMission("ambush","ambush",(priv.name+"_mission",("Gemini/Newcastle",),0,'pirates_',2,'talon','',[("There is the ship with the key to the money! Blow it up!")],['Gemini/Newcastle', 'Gemini/New_Constantinople'], 'New_Constantinople')),
        ("ID_card",1), # Mission arguments.
        priv.name+"_mission", # Script to be set on completion. -1=Failure, 0=Not Accepted, 1=Succeed, 2=In progress
        avalonspeech3, # Dictionary containing what the fixer says.
        None, # If you reject the mission twice. "None" means that he continues asking you forever until you accept
        CampaignEndNode(priv), # If you lose the mission
        avalonmission4, # If you win the mission. Usually points to the next mission
        avalonmission3) # The current mission node.
    MakeMission(priv, # Creates any type of mission
        AVALON_SPRITE, # Campaign, sprite
        [InSystemCondition("Gemini/Auriga","Beaconsfield")], # Where fixer meets you to start the mission
        [InSystemCondition("Gemini/Auriga","Beaconsfield")], # Where the mission ends.
        AddCredits(20000), 
        None,
        'escort_local',('pirates_',0,3,1,3000,0,False,'pirates__',(),priv.name+"_mission",'','sparrowhawk','','tarsus',[("#bb4400Help me! My buddies want my head!",False),("#996600Where is Loki?",True),("#bb4400We brought him to a hidden pirate base in KM-252. Help me!"),("#996600Hold your horses, I will help you.")]),
        priv.name+"_mission",
        avalonspeech4,
        None,
        CampaignEndNode(priv),
        avalonmission5,
        avalonmission4)
    MakeCargoMission(priv,
        AVALON_SPRITE,
        [InSystemCondition("Gemini/Auriga","Beaconsfield")],
        [InSystemCondition("Gemini/KM-252","Smallville")],
        AddCredits(50000),
        LoadMission("directions_mission","directions_mission",(priv.name+"_mission",['Gemini/Newcastle', 'Gemini/New_Constantinople', 'Gemini/Junction', 'Gemini/Nexus', 'Gemini/KM-252'], 'Smallville')),
        ("Message_for_Loki",1),
        priv.name+"_mission",
        avalonspeech5,
        None,
        CampaignEndNode(priv),
        avalonmission6,
        avalonmission5)
    MakeCargoMission(priv, # Creates a cargo mission
        LOKI_SPRITE, # Campaign, sprite
        [InSystemCondition("Gemini/KM-252","Smallville")], # Where fixer meets you to start the mission
        [InSystemCondition("Gemini/Auriga","Beaconsfield")], # Where the mission ends. Usually the same as starting point for next fixer.
        None,
        LoadMission("directions_mission","directions_mission",(priv.name+"_mission",['Gemini/Nexus', 'Gemini/Junction', 'Gemini/New_Constantinople', 'Gemini/Newcastle', 'Gemini/Auriga'], 'Beaconsfield')),
        ("Response",1), # Mission arguments.
        priv.name+"_mission", # Script to be set on completion. -1=Failure, 0=Not Accepted, 1=Succeed, 2=In progress
        avalonspeech6, # Dictionary containing what the fixer says.
        None,
        CampaignEndNode(priv), # If you lose the mission
        avalonmission7, # If you win the mission. Usually points to the next mission
        avalonmission6) # The current mission node.
    MakeMission(priv, # Creates a cargo mission
        AVALON_SPRITE, # Campaign, sprite
        [InSystemCondition("Gemini/Auriga","Beaconsfield")],
        [InSystemCondition("Gemini/Auriga","Beaconsfield")],
        AddCredits(40000), # Script to be run as you click on the fixer. A common use is to AddCredits() for the previous mission.
        LaunchWingmen("militia__","raptor",1),
        'bounty_leader',(0,0,0,False,2,'pirates_',(),priv.name+"_mission",'','paradigm',False,'','talon',[("Our meeting is busted... well, at least we can get rid of some problems right now...")]), # Mission arguments.
        priv.name+"_mission", # Script to be set on completion. -1=Failure, 0=Not Accepted, 1=Succeed, 2=In progress
        avalonspeech7, # Dictionary containing what the fixer says.
        None,
        CampaignEndNode(priv), # If you lose the mission
        avalonmission8,
        avalonmission7) # The current mission node.
    MakeCargoMission(priv, # Creates a cargo mission
        AVALON_SPRITE, # Campaign, sprite
        [InSystemCondition("Gemini/Auriga","Beaconsfield")], # Where fixer meets you to start the mission
        [InSystemCondition("Gemini/KM-252","Smallville")], # Where the mission ends.
        AddCredits(80000,AddTechnology("avalon1")),
        LoadMission("directions_mission","directions_mission",(priv.name+"_mission",['Gemini/Newcastle', 'Gemini/New_Constantinople', 'Gemini/Junction', 'Gemini/Nexus', 'Gemini/KM-252'], 'Smallville')),
        ("Message_for_Loki",1), # Mission arguments.
        priv.name+"_mission", # Script to be set on completion. -1=Failure, 0=Not Accepted, 1=Succeed, 2=In progress
        avalonspeech8, # Dictionary containing what the fixer says.
        None, # If you reject the mission twice. "None" means that he continues asking you forever until you accept
        CampaignEndNode(priv), # If you lose the mission
        avalonmission9,
        avalonmission8) # The current mission node.
    MakeCargoMission(priv, # Creates a cargo mission
        LOKI_SPRITE, # Campaign, sprite
        [InSystemCondition("Gemini/KM-252","Smallville")],
        [InSystemCondition("Gemini/Auriga","Beaconsfield")],
        None,
        LoadMission("ambush","ambush",(priv.name+"_mission",("Gemini/KM-252"),0,'pirates_',4,'sparrowhawk','',[("We've learnt you are carrying Loki the traitor. Dump him into the void or share his fate!")],['Gemini/Nexus', 'Gemini/Junction', 'Gemini/New_Constantinople', 'Gemini/Newcastle', 'Gemini/Auriga'], 'Beaconsfield')),
        ("Loki",1), # Mission arguments.
        priv.name+"_mission", # Script to be set on completion. -1=Failure, 0=Not Accepted, 1=Succeed, 2=In progress
        avalonspeech9, # Dictionary containing what the fixer says.
        None,
        CampaignEndNode(priv), # If you lose the mission
        avalonfinish, # If you win the mission. Usually points to the next mission
        avalonmission9) # The current mission node.
    avalonfinish.Init(priv,
        [],
        None,
        None,
        GoToSubnode(0),
        None,
        [CampaignClickNode().Init(priv,
            [InSystemCondition("Gemini/Auriga","Beaconsfield")],
            avalonsuccess,
            AVALON_SPRITE,
            TrueSubnode(AddCredits(20000,AddTechnology("avalon2"))),
            None,
            [CampaignEndNode(priv)])]) # YOU WIN!!!

    return priv #return the newly created campaign back.
