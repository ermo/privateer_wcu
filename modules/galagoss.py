import campaign_lib
from campaign_lib import *
gosshawkspeech1={"intro":[("Gosshawk","Good day Captain. Are you looking for work?"),
                            ("Burrows","Maybe -- you're hiring?"),
                            ("Gosshawk","Indeed. My name is Captain Gosshawk, I'm a Privateer for myself. I've got my fingers deep into major Guild operations."),
                            ("Burrows","Of which of the Guilds are you talking about? I just want to make sure your promises are as big as your talks."),
                            ("Gosshawk","Both guilds - I've been in that business for quite a long time. I'm to fulfill a contract of both the Merchant's and the Mercenary's Guild with the Confederation. We're sent to fortify the Blockade Point colonies by any means."),
                            ("Burrows","I see - in the glorious tradition of the feds, we'll go out and roast some cats."),
                            ("Gosshawk","Superficially. The job also requires the delivery of goods as well as escorting confederate strike forces - so you're not on your own."),
                            ("Burrows","I knew that the feds are hiring, but I didn't know that they give the real big jobs into private hands."),
                            ("Gosshawk","The war is turning out to be bad for the Confederation. They're stuck at the Blockade Point systems, while a lot of cat ships manage to break deep into confed space. Did you notice the concentration in New Detroit?"),
                            ("Burrows","Yep, although the cats usually don't stand a chance noticing me. So how do I come in? Blowing up Kilrah with a large bomb?"),
                            ("Gosshawk","Not yet... but I'll tell you as soon as we've pushed the border near enough to Kilrah. As a competency test, I need you to clean up our back rows in New Detroit. The ambushes there have become severe and the whole system is infected with raiding parties. Destroy all cat ships. I'll pay 15000 credits for that.")],
                "reject1":[("Burrows","You're kidding. I can get such payments from the mission computer as well."),
                            ("Gosshawk","If you prove reliable, you'll get bigger cuts from my astronomic budget afterwards.")],
                "reconsider":[("Burrows","I got your astronomic budget in mind again."),
                            ("Gosshawk","Okay then. For 15000, liberate New Detroit from kilrathi presence.")],
                "reject2":[("Burrows","Nah.")],
                "accept":[("Burrows","Too easy to me."),
                            ("Gosshawk","We shall see about that.")],
                "accept2":[("Gosshawk","Good.")],
                "reminder":[("Gosshawk","Did you visit New Detroit?"),
                            ("Burrows","Not yet..."),
                            ("Gosshawk","The cats won't give up that fast. You'll at least need to go there. If you're lucky, they'll self-destruct when they see your face."),
                            ("Burrows","I could also transmit your photo, but I think I'll take them out manually. Bye-bye.")],
                "failure":[("Gosshawk","The competency test is complete, or shall I rather say: incomplete? Consider yourself incompetent. Goodbye.")]
                }
gosshawkspeech2={"intro":[("Burrows","New Detroit is free from the furball menace."),
                            ("Gosshawk","Quite a good performance, captain. I think I can introduce you into the risky operations."),
                            ("Burrows","As long a I get the profitable operations, I'm satisfied."),
                            ("Gosshawk","You won't be disappointed. We have a Kamekh which broke through the frontier line, assumably heading for Nitir. It is guarded by some Gothris. Your task will be to make the fighters busy while two confed Broadswords take out the Kamekh."),
                            ("Burrows","What's the wages?"),
                            ("Gosshawk","30000 credits.")],
                "reject1":[("Burrows","That's not the money I expected.")],
                "reconsider":[("Burrows","I've got some appetite for roasted cat meat again."),
                            ("Gosshawk","That's nice - you'll get 30000 for the barbecue. Take out a Kamekh in this system, aided by two Broadswords.")],
                "reject2":[("Burrows","Sorry, the payoff sounds more like a salad diet to me.")],
                "accept":[("Burrows","I'll do it.")],
                "accept2":[("Gosshawk","I'll be back for dinner.")],
                "reminder":[("Gosshawk","What about the Kamekh?"),
                            ("Burrows","I'm currently preparing myself mentally for the strike."),
                            ("Gosshawk","Listen, I have plenty of work and no time to hold your hand. The Kamekh heads for the planet, so stop whining and get rid of the cats.")],
                "failure":[("Gosshawk","The Kamekh has reached Nitir and caused severe destruction in our space. I've lost my contract with the feds. You had your chance, buddy. You passed it.")]
                }

gosshawkspeech3={"intro":[("Gosshawk","The Kamekh?"),
                            ("Burrows","Dust in the wind."),
                            ("Gosshawk","You performed quite well. I now have another mission for you. We have a problem on Mjolnar in Ragnarok. They people there are sick of all the bombings and attacks by the cats and they're considering to surrender the planet to them, for they feel left alone by the Confederation."),
                            ("Burrows","You mean they're going to pack their bags and leave the planet? That's serious. What can we do against that?"),
                            ("Gosshawk","I'm going to show them how seriously the Confederation is willing to help them. They're not low on supplies, just on defense. The Confederation is delegating a squadron, led under the command of Captain Halwinder, to Mjolnar. You're to escort Halwinder there for we have detected a Kamekh blocking the jump point."),
                            ("Burrows","Your sense of humour is starting to annoy me - even if I would be capable of destroying that Kamekh, I wouldn't be able to do it soon enough just before your Captain bites the dust."),
                            ("Gosshawk","I know that the job is risky, but the people on Mjolnar need a sign from the Confederation. The bombers are all busy elsewhere. No matter what happens, you need to make the Kamekhs busy until Captain Halwinder and his pilots made it through."),
                            ("Burrows","Tell me, how can you afford to request suicide from your pilots?!?"),
                            ("Gosshawk","By paying 70000 credits for breaking through the blockade.")],
                "reject1":[("Burrows","You could offer a million credits, but it won't help if I won't survive."),
                            ("Gosshawk","I will find another pilot who is crazy enough to try it...")],
                "reconsider":[("Burrows","Okay then, maybe I'm indeed the crazy pilot you're looking for."),
                            ("Gosshawk","The specs again: Halwinder and you versus a Kamekh in Ragnarok. Payment is 70000.")],
                "reject2":[("Burrows","Forget it.")],
                "accept":[("Burrows","Did anybody mention suicide? Of course I won't pass that much money."),
                            ("Gosshawk","Be sure to take a drink for me at the bar in Mjolnar after you succeed.")],
                "accept2":[("Burrows","Okay, I'm convinced."),
                            ("Gosshawk","Be sure to take a drink for me at the bar in Mjolnar after you succeed.")],
                "reminder":[("Gosshawk","If you got wet pants, just think of the 70000 and all the applause you'll both get at Mjolnar.")],
                "failure":[("Gosshawk","Solon was a friend of mine. Now he is dead. I can't believe he payed for this. Get out of my sight!")]
                }
gosshawkspeech4={"intro":[("Burrows","Hey, what are you doing here?"),
                            ("Gosshawk","I didn't want to miss the party, so I took my private shuttle. The people around here are quite impressed by your performance."),
                            ("Burrows","Good stuff. Although it seems I missed the party while I visited the Grayson-Burrows-Parade."),
                            ("Gosshawk","Hehe. Glad that you managed to help Solon getting away from the Kamekh. He usually tends to attack the cats."),
                            ("Burrows","He did, actually. He insisted on destroying the Kamekh and behaved as if it was his objective. If you'd tell me such things earlier, I could launch with adequate equipment, man!"),
                            ("Gosshawk","Im sorry. Now back to real work. I'm also here because the next mission starts from Mjolnar. I need you for an extremely dangerous patrol."),
                            ("Burrows","You're not that good in sweetening objectives, are you?"),
                            ("Gosshawk","I am simply being straight forward. The Feds are currently preparing strikes in Tr'Pakh, Sumn-Kp'ta and Mah'Rahn. Those systems need a patrol. I had originally chosen you to patrol only Mah'Rahn, but since you were that successful last time, I've recommended you for the large run."),
                            ("Burrows","Be honest man, are you trying to get rid of me? Flying a loop through cat space?!?"),
                            ("Gosshawk","Stop whining... you'll get a GalaxyHKs as your personal escort, among with a payment of 60000 credits. Just make sure you both make it back to Hyades, where the patrol ends and the patrol data is being retrieved. Safe enough?")],
                "reject1":[("Burrows","No... considering all those capships we met recently, the chance is good for us being toast.")],
                "reconsider":[("Burrows","I just thought of those 60000 creds again."),
                            ("Gosshawk","To get them, pick up your GalaxyHK wingman and fly a loop through the kilrathi border systems, ending at Hyades.")],
                "reject2":[("Burrows","Too risky.")],
                "accept":[("Burrows","Yes. We'll meet again."),
                            ("Gosshawk","I hope so.")],
                "accept2":[("Gosshawk","Thank you. Make haste!")],
                "reminder":[("Gosshawk","Did you complete the patrol?"),
                            ("Burrows","Not yet..."),
                            ("Gosshawk","The Feds are preparing for the strike. Move on!")],
                "failure":[("Gosshawk","Without the enemy fleet positions, the strike cannot be done. You're fired!")]
                }
gosshawkspeech5={"intro":[("Burrows","That wingmen wasn't quite too capable, Gosshawk. Didn't you have any real pilots for this job?"),
                            ("Gosshawk","Not everyone has your piloting skills, Grayson."),
                            ("Burrows","Wow, only good friends call me Grayson. You may call me Mister Burrows."),
                            ("Gosshawk","You're not quite the man to make friendship with, right?"),
                            ("Burrows","Correct, as long as you are not Miss November or have a large amount of money to spend on me. Talking about money: We're done... were you looking for a specific target?"),
                            ("Gosshawk","Not directly... I see that you deleted something from your flight disc storing the Tr'Pakh patrol. Did you find anything?"),
                            ("Burrows","Among the usual furball patrols, we disturbed a Kamkekh on a standard system loop. The thing in Tr'Pakh is nothing that should concern you, I'll leave this information exclusively to... me."),
                            ("Gosshawk","Very well, I'll trust you in this case. The Kamekh encounter fits the other scanning routes. While we're talking the feds are already doing the strikes. And here you're coming in again."),
                            ("Burrows","Now what? Are you telling me that the confeds are out of ships and I need to attack Kilrah?"),
                            ("Gosshawk","No. The strikes are going quite well. The first ships are coming back. We have a Broadsword in orbit who has lost its wingmen and escorts and therefore retreated to Hyades. It now needs an escort back to confed space, namely Surtur."),
                            ("Burrows","I guess it wouldn't need an escort if there weren't some tough furballs in its neck."),
                            ("Gosshawk","You're right. It seems that the cats quickly reinforced their rows with some old fighters. Sensors have showed an indefinite number of Sarthas approaching Hyades, obviously sent to track down that Broadsword and any other confed ship willing to take this route."),
                            ("Burrows","What's so special about this single Broadsword?"),
                            ("Gosshawk","Nothing, except of that Admiral Terrell needs to show every single one of their pilots that they care for them, so you'll get 40000 credits if the Broadsword makes it to Surtur in one piece.")],
                "reject1":[("Burrows","I'm sick of risking my life for the Feds. It's their war, not mine.")],
                "reconsider":[("Burrows","Please tell me about the mission again."),
                            ("Gosshawk","For 40000, escort a Broadsword to Surtur and protect it from a pursuing fighter force.")],
                "reject2":[("Burrows","Thanks, but if I wanted to participate in the war, I'd have enlisted.")],
                "accept":[("Burrows","For 40000, I'd even cut the Emperor's claws. I'm in."),
                            ("Gosshawk","Excellent. I'll meet you on Surtur then.")],
                "accept2":[("Gosshawk","Okay, I'll give it a try. See you on Surtur.")],
                "reminder":[("Gosshawk","Listen, the closer you are to confed space, the better the chance is you'll get help with those fighters.")],
                "failure":[("Gosshawk","The Broadsword is destroyed! Guess what the other confed pilots will think now! Your failure is inacceptable for your further employment.")]
                }
gosshawkspeech6={"intro":[("Gosshawk","Good work, pilot. The operation is over, most of the strike force made it back, and everybody is happy."),
                            ("Burrows","Except of the Kilrathi - but we cannot satisfy everybody."),
                            ("Gosshawk","Our performance has caught attention within the Confederation. We're about to get our own base defense contract within Hyades. That'll mean the Guilds will get payments for regularly providing Charon with goods and defense systems. The Confeds can forget about that base and focus on other things."),
                            ("Burrows","Where do I come in there?"),
                            ("Gosshawk","The base will need some goods and ships from us. You are to escort a Drayman freighter to Charon. It contains spareparts for GalaxyHKs and Gunships which should be tough enough to hold the base. I'll pay 50000. Meet me at Charon later.")],
                "reject1":[("Burrows","I'm getting sick of all those escort missions, Gosshawk."),
                            ("Gosshawk","Come back if you change your mind.")],
                "reconsider":[("Burrows","I've changed my mind."),
                            ("Gosshawk","Great - escort a Drayman to Charon in Hyades. I'll pay 50000")],
                "reject2":[("Burrows","I still don't want it.")],
                "accept":[("Burrows","With the cats decimated, this should be an easy cruise. We'll meet at Charon.")],
                "accept2":[("Burrows","Fine, I'll do it.")],
                "reminder":[("Gosshawk","I'll leave soon, and I expect to see you at Charon in time.")],
                "failure":[("Gosshawk","The freighter is lost! I can't believe it! You're FIRED!!!")]
                }

gosshawkspeech7={"intro":[("Gosshawk","Welcome on Charon! The freighter is currently being unloaded."),
                            ("Burrows","Yeah, no reason to give me warm thanks! It was just another Kamekh I had to destroy, nothing too exciting."),
                            ("Gosshawk","I'm sorry, maybe the Feds have become a bit lazy now that we have our base contract. By the way, this caught some attention among the cats... it looks like they think we're an easy bait now that the Feds have left Hyades. I want you to convince them from the opposite."),
                            ("Burrows","Details please."),
                            ("Gosshawk","Another Kamekh, escorted by some Sarthas, has entered the system. It is most likely a troop transport. I'll give you an escort of four Gunships to wipe those furballs out! The payment is 50000.")],
                "reject1":[("Burrows","That's out of my league. Plus, I prefer working alone. I'm out.")],
                "reconsider":[("Gosshawk","Will you help the Gunships destroying the Kamekh for 50000 credits or not?")],
                "reject2":[("Burrows","No thanks... I think I have seen enough Kamekhs lately. You'll have to make your way alone.")],
                "accept":[("Burrows","Another day, another Kamekh. Consider it done.")],
                "accept2":[("Gosshawk","Very well, I'm convinced. I'll do it.")],
                "reminder":[("Gosshawk","Drink up, man! You have a mission to fly!")],
                "failure":[("Gosshawk","That wasn't too good... the base has suffered from major damages. I can't afford to give you further jobs. Goodbye.")]
                }

gosshawkspeech8={"intro":[("Burrows","Scratch another Kamekh."),
                            ("Gosshawk","Thanks. I have an emergency mission. Deliver this message to a contact in this system. You'll get 10000 and a GalaxyHK escort.")],
                "reject1":[("Burrows","I usually don't play paperboy, and 10000 is nothing for me.")],
                "reconsider":[("Gosshawk","Will you deliver my message or not?")],
                "reject2":[("Gosshawk","Man, this message is important.")],
                "accept":[("Burrows","I'll leave immediately.")],
                "accept2":[("Gosshawk","Great! Move out!")],
                "reminder":[("Gosshawk","My contact is in deep trouble. Deliver the message!")],
                "failure":[("Gosshawk","Man, if I can't rely on you, you're worth nothing to me. You're out.")]
                }

gosshawkspeech9={"intro":[("Gosshawk","Did you transmit the message?"),
                            ("Burrows","No... your contact is dead. Some Hunters have killed him. We took off their leading ship, but I'd like to hear what has happened here, Gosshawk!"),
                            ("Gosshawk","Damn! I wanted to warn my friend, but we were too late."),
                            ("Burrows","What did he do? Why did the Hunters want his head?"),
                            ("Gosshawk","I sent him out to patrol the area, when I suddenly saw the rival Hunters on screen. There is currently a quarrel about which faction may patrol which area."),
                            ("Burrows","So you sent me out to defend him? That was not how we dealt, man!"),
                            ("Gosshawk","I've sent you out to call him back! I wanted to avoid the conflict with the other Hunters. I didn't expect a fight!"),
                            ("Burrows","I have problems believing that, Gosshawk. However, let's forget about it for the moment. What's my next mission?"),
                            ("Gosshawk","We'll have to 'clarify' some things with those Hunters. I need you to take out their base of operations, a ship which hides out in Hyades. I don't know what it is, and if it is guarded. I'll give you three galaxyHKs as an escort."),
                            ("Burrows","What's the payoff?"),
                            ("Gosshawk","75000 credits.")],
                "reject1":[("Burrows","No thanks... I won't participate in your personal war.")],
                "reconsider":[("Gosshawk","I need you to destroy a rogue hunter capship in this system. I'll pay 75000 and throw in three GalaxyHKs as Wingmen.")],
                "reject2":[("Burrows","Nope.")],
                "accept":[("Burrows","I'll do it.")],
                "accept2":[("Burrows","Okay...")],
                "reminder":[("Gosshawk","Please stick to your mission objectives. Your wingmen are already waiting for you.")],
                "failure":[("Gosshawk","If you cannot destroy the enemy ship, I'll find someone else who can!")]
                }

gosshawksuccess=[("UNLOCKED: GalaxyGS, GalaxyHK."),
            ("Gosshawk","Glad to see the Hunters are gone. Thank you for your fine work. We've established a safe base now and should be able to repel any medium cat force."),
            ("Burrows","Glad to hear that we're done. I'll leave now."),
            ("Gosshawk","Hold on, captain! I've talked to my Guild friends and set up a special arrangement for you. For your great help in this cause, the guilds have agreed to give you access to the GalaxyHK and Galaxy Gunship Gemini-wide. I'll program your Quine to give you access. Visit any ship dealer to buy one of the ships."),
            ("Burrows","Oh man, thanks! Those ships were of great help! I'll try them out!")]

def LoadGosshawkCampaign():
    GOSSHAWK_SPRITE  = ("sandoval.spr","Talk_to_Gosshawk","bases/heads/zool.spr") #sprite file for the fixer
    GOSSHAWK1_SPRITE  = ("sandoval.spr","Talk_to_Gosshawk","bases/heads/scott.spr") #sprite file for the fixer
    gosshawkmission1 = CampaignClickNode() # Initialize each node
    gosshawkmission2 = CampaignClickNode() # Initialize each node
    gosshawkmission3 = CampaignClickNode() # Initialize each node
    gosshawkmission4 = CampaignClickNode() # Initialize each node
    gosshawkmission5 = CampaignClickNode() # Initialize each node
    gosshawkmission6 = CampaignClickNode() # Initialize each node
    gosshawkmission7 = CampaignClickNode() # Initialize each node
    gosshawkmission8 = CampaignClickNode() # Initialize each node
    gosshawkmission9 = CampaignClickNode() # Initialize each node
    gosshawkfinish = CampaignNode()

    priv=Campaign("gosshawk_campaign") # Name of the save game variable for the entire campaign. Can't contain spaces
    priv.Init(gosshawkmission1) # the first node.

    mission_desc="Gosshawk_1:_Clean_sweep_kilrathi"
    MakeMission(priv,
        GOSSHAWK_SPRITE,
        [InSystemCondition("Gemini/Nitir","Nitir")],
        [InSystemCondition("Gemini/Nitir","Nitir")],
        None,
        None,
        'cleansweep',(0,8,2000,0,('Gemini/Perry','Gemini/New_Detroit',),priv.name+"_mission",1,2,.9,0,['kilrathi_'],1,1),#FIXME needs testing!
        priv.name+"_mission",
        gosshawkspeech1,
        None,
        CampaignEndNode(priv),
        gosshawkmission2,
        gosshawkmission1,
        mission_desc)

    mission_desc="Gosshawk_2:_Destroy_Kamekh"
    MakeMission(priv,
        GOSSHAWK_SPRITE,
        [InSystemCondition("Gemini/Nitir","Nitir")],
        [InSystemCondition("Gemini/Nitir","Nitir")],
        AddCredits(15000), 
        LaunchWingmen("confed__","broadsword",2),
        'bounty_leader',(0,0,0,False,3,'kilrathi_',(),priv.name+"_mission",'','kamekh',False,'','gothri',["Apes! You are disturbing a kilrathi operation! Prepare to die!"]), # Mission arguments.
        priv.name+"_mission",
        gosshawkspeech2,
        None,
        CampaignEndNode(priv),
        gosshawkmission3,
        gosshawkmission2,
        mission_desc)

    mission_desc="Gosshawk_3:_Escort_Captain_Halwinder"
    MakeMission(priv,
        GOSSHAWK_SPRITE,
        [InSystemCondition("Gemini/Nitir","Nitir")],
        [InSystemCondition("Gemini/Ragnarok","Mjolnar")],
        AddCredits(30000),
        LoadMission(mission_desc,"ambush",(priv.name+"_mission",("Gemini/Ragnarok",),0,'kilrathi_',1,'kamekh','',[("Solon Halwinder hailing escort, let's finish this Kamekh off! Break formation and attack!")],['Gemini/Perry', 'Gemini/Ragnarok'], 'Mjolnar')),
        "escort_mission",("confed__",0,0,0,1500,0,0,0,("Gemini/Perry","Gemini/Ragnarok"),priv.name+"_mission",'','sabre'),
        priv.name+"_mission",
        gosshawkspeech3,
        None,
        CampaignEndNode(priv),
        gosshawkmission4,
        gosshawkmission3,
        mission_desc)

    mission_desc="Gosshawk_4:_Patrol_kilrathi_controlled_space"
    MakeMission(priv,
        GOSSHAWK_SPRITE,
        [InSystemCondition("Gemini/Ragnarok","Mjolnar")],
        [InSystemCondition("Gemini/Hyades","Charon")],
        AddCredits(70000),
    LoadMission(mission_desc+"_part_1","ambush",(priv.name+"_mission",("Gemini/Sumn_Kpta",),0,'kilrathi_',1,'kamekh','',[("Humans! You're dead meat!")],['Gemini/Blockade_Point_Alpha', 'Gemini/Tr_Pakh', 'Gemini/Sumn_Kpta', 'Gemini/Hyades'], 'Charon')),
        "escort_mission",("hunter",0,0,0,1500,0,0,0,("Gemini/Blockade_Point_Alpha","Gemini/Tr_Pakh","Gemini/Sumn_Kpta","Gemini/Hyades"),priv.name+"_mission",'','galaxyhk'),
        priv.name+"_mission",
        gosshawkspeech4,
        None,
        CampaignEndNode(priv),
        gosshawkmission5,
        gosshawkmission4,
        mission_desc+"_part_2")

    mission_desc="Gosshawk_5:_Save_Broadsword"
    MakeMission(priv,
        GOSSHAWK1_SPRITE,
        [InSystemCondition("Gemini/Hyades","Charon")],
        [InSystemCondition("Gemini/Surtur","Surtur")],
        AddCredits(60000),
        LoadMission(mission_desc,"ambush",(priv.name+"_mission",("Gemini/Blockade_Point_Charlie",),0,'kilrathi_',6,'sartha','',[("Ape, we will track down any terran confederation ship in this system. Get out of our way!")])),
        "escort_mission",("confed__",0,0,0,1500,0,0,0,("Gemini/Blockade_Point_Charlie","Gemini/Surtur"),priv.name+"_mission",'','broadsword'),
        priv.name+"_mission",
        gosshawkspeech5,
        None,
        CampaignEndNode(priv),
        gosshawkmission6,
        gosshawkmission5,
        mission_desc)

    mission_desc="Gosshawk_6:_Escort_freighter"
    MakeMission(priv,
        GOSSHAWK_SPRITE,
        [InSystemCondition("Gemini/Surtur","Surtur")],
        [InSystemCondition("Gemini/Hyades","Charon")],
        AddCredits(40000),
        LoadMission(mission_desc,"ambush",(priv.name+"_mission",("Gemini/Blockade_Point_Charlie",),0,'kilrathi_',1,'kamekh','',[("This freighter and all its crew is hereby sentenced to death by command of the Kilrathi Gemini High Command!")])),
        "escort_mission",("merchant__",0,0,0,1500,0,0,0,("Gemini/Blockade_Point_Charlie","Gemini/Hyades"),priv.name+"_mission",'','drayman'),
        priv.name+"_mission",
        gosshawkspeech6,
        None,
        CampaignEndNode(priv),
        gosshawkmission7,
        gosshawkmission6,
        mission_desc)

    mission_desc="Gosshawk_7:_Destroy_troop_transport"
    MakeMission(priv,
        GOSSHAWK1_SPRITE,
        [InSystemCondition("Gemini/Hyades","Charon")],
        [InSystemCondition("Gemini/Hyades","Charon")],
        AddCredits(50000,ChangeSystemOwner("Gemini/Hyades","merchant")),
        LaunchWingmen("hunter__","galaxygs",4),
        'bounty_leader',(0,0,0,False,5,'kilrathi_',(),priv.name+"_mission",'','kamekh',False,'','sartha',["Your luck has run out, ape! The glorious Kilrathi Empire will take over this system NOW!"]),
        priv.name+"_mission",
        gosshawkspeech7,
        None,
        CampaignEndNode(priv),
        gosshawkmission8,
        gosshawkmission7,
        mission_desc)

    mission_desc="Gosshawk_8:_Deliver_message"
    MakeMission(priv,
        GOSSHAWK1_SPRITE,
        [InSystemCondition("Gemini/Hyades","Charon")],
        [InSystemCondition("Gemini/Hyades","Charon")],
        AddCredits(50000),
        LaunchWingmen("hunter__","galaxyhk",1),
        'bounty_leader',(0,0,0,False,4,'hunter_',(),priv.name+"_mission",'','centurion',False,'','fireblade',["Are you looking for your friend? We will bring you to him!"]),
        priv.name+"_mission",
        gosshawkspeech8,
        None,
        CampaignEndNode(priv),
        gosshawkmission9,
        gosshawkmission8,
        mission_desc)

    mission_desc="Gosshawk_9:_Destroy_rival_Hunters"
    MakeMission(priv,
        GOSSHAWK1_SPRITE,
        [InSystemCondition("Gemini/Hyades","Charon")],
        [InSystemCondition("Gemini/Hyades","Charon")],
        AddCredits(10000),
        LaunchWingmen("hunter__","galaxyhk",3),
        'bounty_leader',(0,0,0,False,3,'hunter_',(),priv.name+"_mission",'','draymanCVL',False,'','centurion',["We will not allow Gosshawk to take over the business on Charon!"],['Gemini/Blockade_Point_Charlie', 'Gemini/Hyades'], 'Charon'),
        priv.name+"_mission",
        gosshawkspeech9,
        None,
        CampaignEndNode(priv),
        gosshawkfinish,
        gosshawkmission9,
        mission_desc)

    gosshawkfinish.Init(priv,
        [],
        None,
        None,
        GoToSubnode(0),
        None,
        [CampaignClickNode().Init(priv,
            [InSystemCondition("Gemini/Hyades","Charon")],
            gosshawksuccess,
            GOSSHAWK_SPRITE,
            TrueSubnode(AddCredits(75000,AddTechnology("galavar"))),
            None,
            [CampaignEndNode(priv)])])

    return priv
