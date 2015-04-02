import campaign_lib
from campaign_lib import *
irenespeech1={"intro":[("Irene","Greetings, Captain. You look like you've seen your share of adventure. I don't suppose you could help me get out of a bit of a tight spot?"),
                            ("Burrows","Probably. Go on."),
                            ("Irene","My name is Irene, consider me what Insys calls a pirate. I'm doing some major business around New Caledonia and the 'Grey Zone', mostly ship dealing and smuggling."),
                            ("Burrows","Why are you telling me all this? I could be confed or militia."),
                            ("Irene","Two reasons. One: The first time I saw you I knew you're a man of action. Two: I'm trapped here."),
                            ("Burrows","You mean the militia wants your ass and you can't take off on your own?"),
                            ("Irene","Right. I went down to Troy to do some business at Hector, but the authorities were already waiting for me. I barely made it to Helen, my ship cannot be repaired, and I know the police is still looking for me. I need someone to bring me to Hector."),
                            ("Burrows","You want me to help you reach Hector? Shouldn't be a big deal."),
                            ("Irene","It is a big deal, with two militia Talons breathing down your neck. But I have faith in your skills."),
                            ("Burrows","You have no other choice, I guess."),
                            ("Irene","Erm... yes. Anyway, I'll offer 10000 credits if you can escort me safely to Hector.")],
                "reject1":[("Burrows","Don't expect me to deal with the Militia."),
                            ("Irene","Pah, I thought you were a real man. My fault.")],
                "reconsider":[("Burrows","I've reconsidered."),
                            ("Irene","Good. Bring me to Hector. I'll pay 10000 credits."),
                            ("Burrows","What sort of resitance can I expect?"),
                            ("Irene","Two militia Talons.")],
                "reject2":[("Burrows","No. I won't fight the authorities."),
                            ("Irene","Haha, one day you will, trust me!")],
                "accept":[("Burrows","As long as I don't have the proper equipment to leave this system, I might as well earn some money here."),
                            ("Irene","A wise move, friend. Let's climb aboard your ship and get the hell out of here!")],
                "accept2":[("Irene","Glad you reconsidered. Let's leave ASAP.")],
                "reminder":[("Irene","I'm ready to launch. What are you waiting for?"),
                            ("Burrows","I had some repairs scheduled, but we can leave now."),
                            ("Irene","Good. Let's go.")],
                "failure":[("Irene","What's the deal? I barely made it back here alive! Man, don't expect any money from me!")]
                }
irenespeech2={"intro":[("Irene","Thanks ace, I owe you a one. Those Militias were quite nasty."),
                            ("Burrows","Woo-hoo! I like the feeling of kicking a cop's butt. Do you have more where that came from?"),
                            ("Irene","Plenty. I told you that I'm dealing in ships. My main employer is the former Governor Menesch. He is known for dealing in confed ships."),
                            ("Burrows","Wow! I didn't know that corruption on this scale existed within the Gemini Sector."),
                            ("Irene","Pah, Menesch is nothing compared to other folks. I don't like him, his illegal network caused some quarrels between different pirate groups. You probably know Tayla, we were looting cargo back in the good old days. But ever since I started working for Menesch, she didn't even know me any more."),
                            ("Burrows","Now don't tell me you Pirates got ethics."),
                            ("Irene","Tayla doesn't respect authorities, but she isn't crooked like Menesch."),
                            ("Burrows","So why are you working for a guy like this if you actually don't like him."),
                            ("Irene","Because work is scarce for pirates. Tayla is flooding Potter with her Brilliance. There's not much left for smaller operators like me."),
                            ("Burrows","I see. What can I do for you next?"),
                            ("Irene","The reason I needed to go to Hector was that I am waiting for a certain 'customer' who is willing to sell Menesch's Ferrets all across Gemini. We've already completed all the formalities and my customers are on their way back home. I need you to escort their Drayman to theirjumppoint."),
                            ("Burrows","Are we expecting resistance?"),
                            ("Irene","Most likely not. They're legal ship dealers with a white jacket. You'll get the usual 10000 credits.")],
                "reject1":[("Burrows","This situation stinks. You wouldn't offer 10000 credits for nothing."),
                            ("Irene","I offer 10000 credits for an unknown, most likely safe situation. Please reconsider.")],
                "reconsider":[("Burrows","Okay, I'm back again."),
                            ("Irene","Great. Escort a drayman with my trading partners to their jumppoint. I'll pay 10000 credits.")],
                "reject2":[("Burrows","No thanks."),
                            ("Irene","A pity.")],
                "accept":[("Burrows","Sounds like easy money."),
                            ("Irene","It is.")],
                "accept2":[("Irene","Great. They're already waiting for you.")],
                "reminder":[("Irene","The Drayman is already waiting for you. Please move out.")],
                "failure":[("Irene","The Drayman is destroyed. My deal with Menesch is cancelled. You've failed.")]
                }
irenespeech3={"intro":[("Irene","The Drayman has left the system. Good work."),
                            ("Burrows","Yeah, no thanks to the Hunters waiting in ambush for us."),
                            ("Irene","Ah well, I guess the Militia hired them because they didn't have enough evidence to allow them to intercept the Drayman themselves. Good job."),
                            ("Burrows","Thanks."),
                            ("Irene","I've completed the deal and will leave this system soon. It is a matter of days until the Ferrets will be available on the open market. Nobody will be able to trace them back to the illegal source."),
                            ("Burrows","But those are confed ships! This will surely raise suspicions!"),
                            ("Irene","Sure, but who do they want to blame it on? They can't take the ships away from the market. The whole system would collapse then, and the Feds know this! The small ship dealers are innocent and they've legally paid for the ships. Guess where I got my Talon from?"),
                            ("Burrows","A former confed ship sold by Menesch?"),
                            ("Irene","Indeed - the only difference with the Ferrets now is that he doesn't sell them to rogue groups directly, but to normal people. If the Feds intervene now, they'll damage their own economy, not that of the Pirates."),
                            ("Burrows","I see."),
                            ("Irene","Now back to work. Before I leave, I need to make sure that nobody is following me. There have been reports about increased Retro activity around. I need you to destroy them. You'll get two pirate wingmen."),
                            ("Burrows","Are the Retros searching for you?"),
                            ("Irene","No, that's a coincidence. Menesch once told me that he's working on a deal with them so that they won't touch his employees, so I'll send you to check out if the deal already stands. I'll pay 20000 credits.")],
                "reject1":[("Burrows","I'm sorry, but dealing with the Retros seems a bit too risky to me."),
                            ("Irene","Whatever you say.")],
                "reconsider":[("Burrows","Tell me about the mission again."),
                            ("Irene","For 10000 credits and with two pirate wingmen, search for a group of Retro ships and destroy them if they don't stick to the deal with Menesch.")],
                "reject2":[("Burrows","No, too risky."),
                            ("Irene","Then leave!")],
                "accept":[("Burrows","Consider it done."),
                            ("Irene","Thank you, make haste!")],
                "accept2":[("Irene","Great. Move out.")],
                "reminder":[("Irene","What about the Retros?"),
                            ("Burrows","I haven't left yet."),
                            ("Irene","They won't go away by themselves."),
                            ("Burrows","I know. I'll leave soon.")],
                "failure":[("Irene","You've failed. The Retros are still there, and I cannot leave the system.")]
                }
irenesuccess=[("UNLOCKED: Ferret, Ferret CVL."),
            ("Irene","Did the Retros attack you?"),
            ("Burrows","Yes. Obviously they didn't even know about Menesch. We managed to erase them."),
            ("Irene","Great. I've got good news. The Ferret is in the stores. Check it out if you like, it's no superior fighter but it is a real bargain."),
            ("Burrows","Thanks, I'll consider buying one."),
            ("Irene","I'll leave now. Thank you for all your efforts. And trust me, we'll meet again."),
            ("Burrows","Wait... what can I do next?"),
            ("Irene","I have no more work for you. However, I've heard that Prasepe in Saratov has some trouble with Pirates. You should go there next, maybe there's some work for you."),
            ("Burrows","YOU are sending me out to fight PIRATES?"),
            ("Irene","They aren't with my clan, friend...")]

def LoadIreneCampaign():
    IRENE_SPRITE  = ("pirate.spr","Talk_to_Irene","bases/heads/syrai.spr")
    IRENE1_SPRITE  = ("pirate.spr","Talk_to_Irene","bases/heads/irenehelen.spr")
    IreneMission1 = CampaignClickNode() # Initialize each node
    IreneMission2 = CampaignClickNode() # Initialize each node
    IreneMission3 = CampaignClickNode() # Initialize each node
    IreneFinish = CampaignNode()

    priv=Campaign("irene_campaign") # Name of the save game variable for the entire campaign. Can't contain spaces
    priv.Init(IreneMission1) # the first node.

    mission_desc="Irene_1:_Get_Irene_to_Hector"
    MakeCargoMission(priv, # Creates a cargo mission
        IRENE1_SPRITE, # Campaign, sprite
        [InSystemCondition("Gemini/Troy","Helen")], # Where fixer meets you to start the mission
        [InSystemCondition("Gemini/Troy","Hector")], # Where the mission ends. Usually the same as starting point for next fixer.
        ClearFactionRecord('pirates',1.0,PushRelation('pirates')),
        LoadMission(mission_desc,"ambush",(priv.name+"_mission",("Gemini/Troy",),0,'militia_',2,'talon','InSys_Militia',[("Irene! You've made your final mistake!")],['Gemini/Troy'], 'Hector')),
        ("Irene",1), # Mission arguments.
        priv.name+"_mission", # Script to be set on completion. -1=Failure, 0=Not Accepted, 1=Succeed, 2=In progress
        irenespeech1, # Dictionary containing what the fixer says.
        None, # If you reject the mission twice. "None" means that he continues asking you forever until you accept
        CampaignEndNode(priv), # If you lose the mission
        IreneMission2, # If you win the mission. Usually points to the next mission
        IreneMission1) # The current mission node.

    mission_desc="Irene_2:_Escort_Drayman_to_jump_point"
    MakeMission(priv, # Creates any type of mission
        IRENE_SPRITE, # Campaign, sprite
        [InSystemCondition("Gemini/Troy","Hector")], # Where fixer meets you to start the mission
        [InSystemCondition("Gemini/Troy","Hector")], # Where the mission ends.
        AddCredits(10000), # Script to add your credits
        LoadMission(mission_desc,"ambush",(priv.name+"_mission",("Gemini/Troy",),0,'hunter_',1,'fireblade','',[("You're escorting a bunch of criminals. I cannot allow that!")],['Gemini/Troy'], 'Jump_To_Regallis')),
        'escort_local',('hunter_',0,1,0,3000,0,False,'pirates__',(),priv.name+"_mission",'','demon','','drayman',["Escort, I'd suggest to divert from your course. As soon as I've dismantled that Drayman, you'll be next if you're still here."]),
        priv.name+"_mission", # Script to be set on completion. -1=Failure, 0=Not Accepted, 1=Succeed, 2=In progress
        irenespeech2, # Dictionary containing what the fixer says.
        None, # If you reject the mission twice. "None" means that he continues asking you forever until you accept
        CampaignEndNode(priv), # If you lose the mission
        IreneMission3, # If you win the mission. Usually points to the next mission
        IreneMission2) # The current mission node.

    mission_desc="Irene_3:_Hunt_down_Retros"
    MakeMission(priv, # Creates any type of mission
        IRENE_SPRITE, # Campaign, sprite
        [InSystemCondition("Gemini/Troy","Hector")], # Where fixer meets you to start the mission
        [InSystemCondition("Gemini/Troy","Hector")], # Where the mission ends.
        AddCredits(10000), # Script to add your credits
        LaunchWingmen("pirates__","talon",2), # Script to be run to start the mission (usually None if you don't have a script. Do NOT load an ambush mission here.)
        'bounty_leader',(0,0,0,False,2,'retro_',(),priv.name+"_mission",'','sparrowhawk',False,'','talon',[("#bb4400Sinners! Prepare to taste the fire of the lord!",False),("#996600Hailing Retro leader. We're employees of Governor Menesch. Cease fire!",True),("#bb4400Negatory. Cease your existence!")]),
        priv.name+"_mission", # Script to be set on completion. -1=Failure, 0=Not Accepted, 1=Succeed, 2=In progress
        irenespeech3, # Dictionary containing what the fixer says.
        None, # If you reject the mission twice. "None" means that he continues asking you forever until you accept
        CampaignEndNode(priv), # If you lose the mission
        IreneFinish, # If you win the mission. Usually points to the next mission
        IreneMission3) # The current mission node.
    IreneFinish.Init(priv,
        [],
        None,
        None,
        GoToSubnode(0),
        None,
        [CampaignClickNode().Init(priv,
            [InSystemCondition("Gemini/Troy","Hector")],
            irenesuccess,
            IRENE_SPRITE,
            TrueSubnode(AddCredits(20000,AddTechnology("irene"))),
            None,
            [CampaignEndNode(priv)])]) # YOU WIN!!!
    return priv #return the newly created campaign back.
