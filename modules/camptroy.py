import campaign_lib, quest, VS
from campaign_lib import *
stahlspeech1={
    "intro":[("Captain_Stahl","Welcome to the Gemini Sector! I hope you had a good flight."),
        ("Burrows","Excuse me?"),
        ("Captain_Stahl","I'm sorry, I forgot to introduce myself. My name is Captain Stahl."),
        ("Burrows","Are you with the Confed, or just a privateer?"),
        ("Captain_Stahl","Something in between; it's a long story. I worked for the Exploratory Service for many years, but currently I'm doing business for myself. I saw you got a new ship, and thought you might be interested in some work."),
        ("Burrows","Possibly. What kind of work?"),
        ("Captain_Stahl","My business associates and I are currently trying to expand business around Troy. Since pirate assaults have become frequent we want to introduce better ships, and not just for Merchant Guild affiliates."),
        ("Burrows","So you're selling ships?"),
        ("Captain_Stahl","I'm not a salesman, more like a representative. My connections in the ES have allowed me to obtain a license to introduce the new TarsusMk2 to the civilian market, and I came to Troy to expedite this operation."),
        ("Burrows","Tell me more about the operation."),
        ("Captain_Stahl","The ES has chosen Helen in this system as the headquarters for this project. It is a hotspot area, where lightly-armed merchants encounter a lot of pirates. The ES board of directors thinks that business opportunities are the best around here, and they want Helen to be prepared for the boom. The Achilles base governor has pledged a capital investment in the form of gems that our company will deposit at a bank in Helen as collateral for a line of credit. We will use that credit to order a starting stock of TarsusMk2 for the show room - as soon as the diamonds are safe in Helen."),
        ("Burrows","Wouldn't it be smarter to start in a safer place?"),
        ("Captain_Stahl","Not so. The big bucks are waiting here; the 'eastern' quadrants already have a good merchant force."),
        ("Burrows","So what am I supposed to do, deliver gems?"),
        ("Captain_Stahl","Exactly. We delegate such missions to privateers, since we have currently none of our own freighters in this quadrant. Your mission is to deliver 10 cases of gems to Helen. It pays 2500 credits."),
        ("Burrows","Excuse me, but that's a ridiculous payment. If I wanted to make so little money, I could find a job as a male nurse on good old Earth. Tell me why I shouldn't just take those gems and run away?"),
        ("Captain_Stahl","Because I can offer a lot more than just money. Without contacts you're Nobody in Gemini. If your performance is good, we'll be 'friends', and the friends of ES delegates usually don't have problems getting one of the rare jump drives at a ship dealer, got it?"),
        ("Burrows","Yeah, but with 2500 credits I can't even afford a hand laser, let alone a jump drive!"),
        ("Captain_Stahl","If you prove reliable we'll have better paying missions for you, and I can offer you constant work. Plus, you'll eventually gain access to the TarsusMk2."),
        ("Burrows","Okay then, back to the mission specs. Do I need to expect resistance?"),
        ("Captain_Stahl","GNN has reported a pirate Talon orbiting Helen. It might be waiting in ambush for you. Nothing a good pilot with a ship like yours shouldn't be able to handle. What do you say?")],
    "reject1":[("Burrows","Sorry, but the payment is way too low."),
        ("Captain_Stahl","I'm afraid I can't offer more. Come back if you reconsider.")],
    "reconsider":[("Burrows","I've reconsidered."),
        ("Captain_Stahl","Great! I need you to deliver 10 boxes of gems to Helen. The mission pays 2500 credits."),
        ("Burrows","Any foes out there?"),
        ("Captain_Stahl","A pirate Talon orbiting Helen, just avoid it.")],
    "reject2":[("Burrows","No thanks."),
        ("Captain_Stahl","Then please, don't waste my time!")],
    "accept":[("Burrows","Okay, I'm in. But I'd like to see more credits soon."),
        ("Captain_Stahl","I'll offer easy work and an adequate payment. For now, your ship is being loaded and you'll get your money as soon as you're back from Helen")],
    "accept2":[("Captain_Stahl","Excellent. Your ship is already being loaded. After you deliver the gems to Helen, come back afterwards for the 250 credits.")],
    "reminder":[("Captain_Stahl","What the...? What are you doing here?"),
        ("Burrows","Um... I just came in for a drink and..."),
        ("Captain_Stahl","Listen, you have a JOB to do and you will get MONEY for that."),
        ("Burrows","Hey, 2500 credits... that's great MONEY!"),
        ("Captain_Stahl","Isn't it? Now MOVE IT!"),
        ("Burrows","Cool down mate. I just wanted to visit my pet rabbit at the pet hotel and tell him that I'm going on a journey to another planet, but that I'll be back soon with a big, fresh carrot. I'll take off immediately."),
        ("Captain_Stahl","There's still a lot for you to learn, privateer.")],
    "failure":[("Captain_Stahl","I can't believe you failed such an easy job. I'll give the contract to someone else. Goodbye.")]
}
stahlspeech2={
    "intro":[("Captain_Stahl","Glad to see you again. Did everything go well?"),
        ("Burrows","Yes, and you were right: a pirate in a Talon tried to intercept me."),
        ("Captain_Stahl","By 'tried' I suppose you mean he failed?"),
        ("Burrows","Otherwise I wouldn't be standing here."),
        ("Captain_Stahl","Good. You have proved your abilities, then. But this also shows that we have a traitor in our ranks."),
        ("Burrows","Oh, come on! You think that the pirates would go such lengths as to plant a spy in your company - just to intercept a shipment?"),
        ("Captain_Stahl","I think they're worried that the introduction of the TarsusMk2 will turn their way of earning a living into a deadly gamble. And they should worry..."),
        ("Burrows","So, first thing is we need to stop this guy from transmitting information."),
        ("Captain_Stahl","You're learning fast. But I've checked the Achilles com logs and found that the information is not being transmitted. I believe one of my affiliates meets the pirates directly in this system."),
        ("Burrows","Who could it be?"),
        ("Captain_Stahl","I signed a contract with a merchant, a Tarsus pilot, who has been acting suspicious. He's often late, offering strange excuses like engine problems. And while you were flying your mission, we tracked his ship going to a nav point, meeting with pirate Talons, and then moving on without a fight."),
        ("Burrows","How do we plan to persuade this fellow to straighten up?"),
        ("Captain_Stahl","I'm afraid he's beyond reforming, and needs to be stopped by violent means - hooking up with the pirates is a capital offence, anyway. I want you to search Troy and kill this traitor."),
        ("Burrows","That'll cost you a bit more than 2500 creds - my good reputation might suffer from attacking a ship that appears as merchant friendly in the public nav database."),
        ("Captain_Stahl","Of course. Since you now have proved your loyalty to this project, I'm happy to offer the official bounty of 8000 credits to you.")],
    "reject1":[("Burrows","I don't think I can afford attacking a merchant, at least not for such low pay."),
        ("Captain_Stahl","I know that there are better bounties out there. Please come back if you change your mind.")],
    "reconsider":[("Burrows","I'm back; changed my mind."),
        ("Captain_Stahl","That's good. Search Troy for a rogue Tarsus merchant ship and destroy it. Afterwards return here for 8000 credits.")],
    "reject2":[("Burrows","Nah."),
        ("Captain_Stahl","Running cargo is one thing. But if you want to make real money in Gemini, you'll have to kill a lot of people. Believe me.")],
    "accept":[("Burrows","Sounds good. I'll do it."),
        ("Captain_Stahl","That's great. See you soon.")],
    "accept2":[("Captain_Stahl","Good. Please hurry.")],
    "reminder":[("Captain_Stahl","Did you destroy the Tarsus?"),
        ("Burrows","Actually, I haven't found it yet."),
        ("Captain_Stahl","Might it be because you haven't launched yet?"),
        ("Burrows","Sounds like a valid hypothesis, come to think of it."),
        ("Captain_Stahl","Listen, this is NO GAME. The whole quadrant might benefit from what we are planning to do."),
        ("Burrows","Alright, alright; I'll do it right away."),
        ("Captain_Stahl","I hope so.")],
    "failure":[("Captain_Stahl","If you need to be flying a Confederation class dreadnought to beat a Tarsus, you won't survive long in Gemini. I'm afraid I have no further jobs for an incompetent flyboy.")]
}
stahlspeech3={
    "intro":[("Captain_Stahl","I have no time to congratulate you enough. Here is your money, along with the next mission."),
        ("Burrows","What's the hurry?"),
        ("Captain_Stahl","The pirates are mobilizing against us. We've detected new Talons jumping into the Troy system, even as some are already patrolling the area around Helen, ready to attack our freighters."),
        ("Burrows","How many of them?"),
        ("Captain_Stahl","We don't know that. But since they've lost their informant they probably don't know that I have delayed the first freighter's arrival."),
        ("Burrows","So we are cleaning out the whole system from pirates, right?"),
        ("Captain_Stahl","Well, I hoped we'd have more time in which to do it, but yes. I need you to help wipe out the pirate ships."),
        ("Burrows","Sounds cool, I'll climb into my rusty ship and wipe out the whoooole system immediately."),
        ("Captain_Stahl","Stop whining, you only need to clean the area around Helen and you won't be alone. I've managed to get a wingman to fly under your command."),
        ("Burrows","And I assume this will lower my payment..."),
        ("Captain_Stahl","I have an emergency budget for such cases. We're low on ships, but not that low on funds. I'll offer you 12,000 for this mission."),
        ("Burrows","That's not too much for an unknown number of foes."),
        ("Captain_Stahl","You've got a Gladius fighter for your wing; it's quite capable of doing much of the work. You should be able to distract the Talons by doing evasive maneuvers while your wingman finishes them off."),
        ("Burrows","I hope you won't mind if I have my fun launching a missile from time to time."),
        ("Captain_Stahl","I don't care how you do it, just do it.")],
    "reject1":[("Burrows","Well, this sounds more like playing bait, but bait often gets bitten."),
        ("Captain_Stahl","You're busting the whole project. I need you now more than ever!")],
    "reconsider":[("Burrows","Okay, what was that whack-a-pirate stuff again?"),
        ("Captain_Stahl","Hook up with your wingman and attack the incoming pirates for 12000 credits.")],
    "reject2":[("Burrows","No, too risky. I don't mean the pirates, I mean the Gladius. I don't think I could take the friendly fire."),
        ("Captain_Stahl","You fool, you have no idea! This system could drift into pirate hands any time if we don't intervene!")],
    "accept":[("Burrows","Okay, for the sake of our glorious sector!"),
        ("Captain_Stahl","Thank you; make haste!")],
    "accept2":[("Captain_Stahl","Thanks goodness.")],
    "reminder":[("Captain_Stahl","What are you doing here?"),
        ("Burrows","I never launch before lunch at the lounge; didn't you know that?"),
        ("Captain_Stahl","You'd better launch now or you may never finish your lunch."),
        ("Burrows","You'll have me arrested? Where's your army?"),
        ("Captain_Stahl","We have a contract, and I know people at Insys; I could give your wingman new orders. You'd better climb into your ship now."),
        ("Burrows","You desperately need to see a doctor."),
        ("Captain_Stahl","Yeah, but if you don't leave now, you'll be seen by a desperate doctor first.")],
    "failure":[("Captain_Stahl","The pirates have gained control over vital trading routes in this system. The project has failed. I don't need you anymore. Goodbye.")]
}
stahlspeech4={
    "intro":[("Captain_Stahl","Thank you for helping, ace."),
        ("Burrows","No problem. What's next?"),
        ("Captain_Stahl","The first freighter transporting the TarsusMk2 will arrive soon, and I want you to protect it."),
        ("Burrows","Protect it from what? The pirates are vaporized!"),
        ("Captain_Stahl","Dumb people never learn anything, Mr. Burrows. Some pirates don't want to give up yet."),
        ("Burrows","Alas, that'll be their end, then."),
        ("Captain_Stahl","I hope so. Long range sensors have detected a squadron of 3 Talons. I'm willing to send you into a direct duel."),
        ("Burrows","You mean no surprise ambush?"),
        ("Captain_Stahl","No. But since the pirates have lost their informant, they'll certainly be a bit disorganized and coming in one at a time. I want you to destroy them one by one."),
        ("Burrows","What's the payoff?"),
        ("Captain_Stahl","10000 credits."),
        ("Burrows","That's lower pay than before."),
        ("Captain_Stahl","Of course. This one is not financed by the emergency budget."),
        ("Burrows","You're a real business man, Captain."),
        ("Captain_Stahl","Glad you finally noticed. Are you in?")],
    "reject1":[("Burrows","I don't see any reason for lowering my payment - I've been quite reliable, and proved myself able. I'm out."),
        ("Captain_Stahl","Oh come on! This mission is not that dangerous. Please reconsider.")],
    "reconsider":[("Burrows","Please tell me about your mission again."),
        ("Captain_Stahl","Protect my freighter from 3 pirates. Payment is 10000.")],
    "reject2":[("Burrows","Not enough credits."),
        ("Captain_Stahl","Alright, I'm getting tired of this conversation, anyway.")],
    "accept":[("Burrows","Okay, let's shoot those pirates to hell and back."),
        ("Captain_Stahl","That's my pilot!")],
    "accept2":[("Burrows","Ah, what the heck..."),
        ("Captain_Stahl","Good. I'll inform the freighter's captain.")],
    "reminder":[("Captain_Stahl","Why do I see your face here?"),
        ("Burrows","Perhaps because I'm standing in front of you?"),
        ("Captain_Stahl","Listen, unless you destroy those Talons, you won't see the 10,000 credits."),
        ("Burrows","Relax, I'm just wandering around while my ship is having an oil change."),
        ("Captain_Stahl","I hope it's synthetic oil and the filter replacement is included."),
        ("Burrows","It is, don't worry; I'm about to launch."),
        ("Captain_Stahl","That's good. The freighter is already awaiting you.")],
    "failure":[("Captain_Stahl","The freighter is destroyed, along with its cargo. I'm out of money and out of business. I hope you'll be vaporized some day.")]
}
stahlspeech5={
    "intro":[("Captain_Stahl","Thank you for protecting the freighter. The ships have reached Helen in crates, and are about to be assembled."),
        ("Burrows","So what's next?"),
        ("Captain_Stahl","We have learned that the ship which gathered the information from the rogue Tarsus is currently in this system. It seems that it has surveyed the last attack."),
        ("Burrows","What sort of ship exactly?"),
        ("Captain_Stahl","It's an Tarsus class ship. Since it threw most of its escort into the freighter attack, it is now only protected by one remaining Talon."),
        ("Burrows","This still sounds like danger, and if I don't get any wingmen, the odds are not stellar."),
        ("Captain_Stahl","You'll get your wingman. Since the Confederation is quite happy with our success, they have sent a decommissioned Broadsword to help us with the attack. And I'll pay you 15,000 credits if you succeed.")],
    "reject1":[("Burrows","Two against two is still a risk. I'm out."),
        ("Captain_Stahl","That's too bad. We could really use your help with stabilizing this system now.")],
    "reconsider":[("Burrows","Please tell me about the mission again."),
        ("Captain_Stahl","For 15,000 credits and aided by a Broadsword, find and destroy a pirate Tarsus guarded by a Talon.")],
    "reject2":[("Burrows","Never trust a Confed, my mommy always said."),
        ("Captain_Stahl","I'll see to it you get a Kilrathi wingcat next time.")],
    "accept":[("Burrows","A Broadsword heavy bomber?, WOW! That ship should really kick their asses."),
        ("Captain_Stahl","That would be my assumption, as well. However, don't forget that a Broadsword is not as maneuverable as Talons. You'd surely be of some help, keeping the Talon busy. Have fun anyway.")],
    "accept2":[("Burrows","Been thinking... Broadswords aren't just bombers; they are also classed as heavy fighters. I guess I'm in."),
        ("Captain_Stahl","Good. The Broadsword is already waiting for you.")],
    "reminder":[("Captain_Stahl","Have you eliminated the Tarsus?"),
        ("Burrows","Not yet... I'm still trying to come up with a clever plan."),
        ("Captain_Stahl","I'll give you a hint: Seek and destroy!"),
        ("Burrows","Not too bad. I'll give that a try.")],
    "failure":[("Captain_Stahl","The Tarsus has managed to flee! It will surely reassemble a fleet to strike again! I can't afford this risk. The project has failed, thanks to you.")]
}
stahlspeech6={
    "intro":[("Captain_Stahl","Thank you for busting their flagship. We have now gained safety along Troy's shipping lanes. The remaining pirates shouldn't be able to do much harm anymore."),
        ("Burrows","Can I be of any further help?"),
        ("Captain_Stahl","The Achilles local government has decided to invest heavily into our company - they aim to acquire 49% of the float, using gems as payment, rather than cash. I have chosen you for the first delivery."),
        ("Burrows","Lucky me! Details please."),
        ("Captain_Stahl","Deliver 20 boxes of gems to Helen. I anticipate a final pirate assault. I'll pay you 20,000 for this run.")],
    "reject1":[("Burrows","Pirates again? I'm not interested."),
        ("Captain_Stahl","Not interested in a high payment? You're so unpredictable.")],
    "reconsider":[("Burrows","Please tell me about the mission again."),
        ("Captain_Stahl","For 20,000 credits, deliver 20 boxes of gems to Helen. Be aware of potential pirate raiders.")],
    "reject2":[("Burrows","I'm bored sick of dealing with pirates, I dream of Talons every night."),
        ("Captain_Stahl","Then I'll find somebody else for the job, be sure!")],
    "accept":[("Burrows","That's good money. Deal me in."),
        ("Captain_Stahl","Good. Your ship is being loaded. Good luck Captain!")],
    "accept2":[("Burrows","I've reconsidered; maybe I can use the money to get a better ship and find more challenging work, like along the frontier. Deal me in."),
("Captain_Stahl","Good! I'll have your ship loaded right now. You can launch at any time - after lunch if you like.")],
    "reminder":[("Captain_Stahl","The gems are not yet on Helen."),
        ("Burrows","Yeah, I thought that after all those hurry-up-missions, I could take things slower, spend some quality time with my pet rabbit..."),
        ("Captain_Stahl","That's right, but why wait for the big money?"),
        ("Burrows","Good point. I'll take off soon.")],
    "failure":[("Captain_Stahl","I would never have thought you'd be unable to do such an easy job, after all we've been through. Your failure is preposterous. Goodbye.")]
}
stahlspeech7={
    "intro":[("UNLOCKED: TarsusMk2, Jump Drive."),
        ("Captain_Stahl","The gems are safely in a bank vault at Helen, and the first TarsusMk2's are just coming off the assembly line. Our business is within budget and on schedule. It is with pleasure and honor that I hand over these 20000 creds to you."),
        ("Burrows","I like sentences containing the words 'credits' and 'you'."),
        ("Captain_Stahl","The gems-for-shares deal is now formalized and I've made sure that you are given first priority in future shipments. Further loads are necessary but now the pirates won't bother us anymore. You can make easy money by just flying gems from Achilles to Helen, back and forth. I'll pay 1200 credits for every successful trip."),
        ("Burrows","Low pay... but then again, a quick and easy route."),
        ("Captain_Stahl","Yes. By the way, you should pass by the ship dealer and check out the TarsusMk2 for yourself. A great ship that's not yet available anywhere but right here."),
        ("Burrows","Any other stuff to go with it? I mean... are we 'friends' now?"),
        ("Captain_Stahl","Ah yes, I've programmed your Quine with ES VIP information. Just enter any ship dealer and show it, and you'll be able to get a jump drive wherever there is one available. About the job, are you still interested?")],
    "reject1":[("Burrows","1200 credits is not enough."),
        ("Captain_Stahl","I know that you're capable of earning more elsewhere. Thanks anyway.")],
    "reconsider":[("Burrows","I could use some extra cash. What was this mission again?"),
        ("Captain_Stahl","Fly 10 boxes of gems from here to Helen. Payment is 1200 credits, no pirates expected.")],
    "reject2":[("Burrows","The money sucks."),
        ("Captain_Stahl","Whatever you say.")],
    "accept":[("Burrows","Easy flying, I'm in."),
        ("Captain_Stahl","Okay, see you later.")],
    "accept2":[("Burrows","Okay, what the heck..."),
        ("Captain_Stahl","Good. You can launch at any time - even after lunch time.")],
    "reminder":[("Captain_Stahl","The gems are not yet on Helen."),
        ("Burrows","Oops! I was talking to the bartender and totally forgot about that. I'll do it soon.")],
    "failure":[("Captain_Stahl","I would never have thought you'd fail such an easy job, after all you have done. We're through. Goodbye.")]
}
stahlspeech8={
    "intro":[("Captain_Stahl","Here is your payment of 1200 credits. Another run?"),
        ("Burrows","Please remind me of the details again."),
        ("Captain_Stahl","10 boxes of gems from here to Helen, 1200 credits, no hassles.")],
    "reject1":[("Burrows","What about boredom compensation?"),
        ("Captain_Stahl","We've been through this crap already. Thanks anyway.")],
    "reconsider":[("Burrows","I could use a bit more cash. What was this mission again?"),
        ("Captain_Stahl","10 boxes of gems. Helen. 1200 credits.")],
    "reject2":[("Burrows","I'd get more if I applied for welfare."),
        ("Captain_Stahl","You told me enough times, already.")],
    "accept":[("Burrows","Easy money, I'm in."),
        ("Captain_Stahl","Good, see you later.")],
    "accept2":[("Burrows","Oh, what the heck..."),
        ("Captain_Stahl","Good. You can launch at any time - after lunch if you like.")],
    "reminder":[("Captain_Stahl","The gems are not yet on Helen."),
        ("Burrows","Oops! I got into an argument with the upgrades booth people and totally forgot. I'll get on it.")],
    "failure":[("Captain_Stahl","I would never have thought you'd fail such an easy job after all you've done. Your failure is incomprehensible. Goodbye.")]
}
def LoadTroyCampaign():
    STAHL_SPRITE  = ("stahl.spr","Talk_to_Captain_Stahl","bases/heads/stahl.spr") #sprite file for the fixer
    StahlMission1 = CampaignClickNode() # Initialize each node
    StahlMission2 = CampaignClickNode() # Initialize each node
    StahlMission3 = CampaignClickNode() # Initialize each node
    StahlMission4 = CampaignClickNode() # Initialize each node
    StahlMission5 = CampaignClickNode() # Initialize each node
    StahlMission6 = CampaignClickNode() # Initialize each node
    StahlMission7 = CampaignClickNode() # Initialize each node
    StahlMission8 = CampaignClickNode() # Initialize each node

    priv=Campaign("troy_campaign") # Name of the save game variable for the entire campaign. Can't contain spaces
    priv.Init(StahlMission1) # the first node.

    mission_desc="Stahl_1:_Deliver_gems_past_pirate_ship"
    MakeCargoMission(priv, # Creates a cargo mission
        STAHL_SPRITE, # Campaign, sprite
        [InSystemCondition("Gemini/Troy","Achilles")], # Where fixer meets you to start the mission
        [InSystemCondition("Gemini/Troy","Helen")], # Where the mission ends. Usually the same as starting point for next fixer.
        None, # Script to be run as you click on the fixer. A common use is to AddCredits() for the previous mission.
        LoadMission(mission_desc,'ambush',(priv.name+"_mission",('Gemini/Troy'),25,'pirates_',1,'talon','Pirate_interceptor',[("Hailing merchant craft!",False),"These gems will never reach Helen!","Stop your engines and dump your cargo!"],['Gemini/Troy'], 'Helen')), # Script to be run to start the mission (usually None if you don't have a script, but ambush is also common.)
        ("Gems",10), # Mission arguments.
        priv.name+"_mission", # Script to be set on completion. -1=Failure, 0=Not Accepted, 1=Succeed, 2=In progress
        stahlspeech1, # Dictionary containing what the fixer says.
        None, # If you reject the mission twice. "None" means that he continues asking you forever until you accept
        CampaignEndNode(priv), # If you lose the mission
        StahlMission2, # If you win the mission. Usually points to the next mission
        StahlMission1) # The current mission node.

    mission_desc="Stahl_2:_Find_pirate_spy"
    MakeMission(priv, # Creates any type of mission
        STAHL_SPRITE, # Campaign, sprite
        [InSystemCondition("Gemini/Troy","Achilles")], # Where fixer meets you to start the mission
        [InSystemCondition("Gemini/Troy","Achilles")], # Where the mission ends.
        AddCredits(2500), # Script to add your credits
        None, # Script to be run to start the mission (usually None if you don't have a script. Do NOT load an ambush mission here.)
        'bounty_leader',(0,0,0,False,0,'merchant_',(),priv.name+"_mission",'Pirate_spy','tarsus.begin',False,'Pirate_spy_escort','',["So you've finally found me.","But I'm afraid your employer will never find YOU again!"]), # Mission arguments.
        priv.name+"_mission", # Script to be set on completion. -1=Failure, 0=Not Accepted, 1=Succeed, 2=In progress
        stahlspeech2, # Dictionary containing what the fixer says.
        None, # If you reject the mission twice. "None" means that he continues asking you forever until you accept
        CampaignEndNode(priv), # If you lose the mission
        StahlMission3, # If you win the mission. Usually points to the next mission
        StahlMission2, # The current mission node.
        mission_desc # Name that describes the mission in flight and in the mission computer.
        )

    mission_desc="Stahl_3:_Defend_Helen"
    MakeMission(priv, # Creates any type of mission
        STAHL_SPRITE, # Campaign, sprite
        [InSystemCondition("Gemini/Troy","Achilles")], # Where fixer meets you to start the mission
        [InSystemCondition("Gemini/Troy","Achilles")], # Where the mission ends.
        AddCredits(8000), # Script to add your credits
        LaunchWingmen("merchant__","gladius",1), # Script to be run to start the mission (usually None if you don't have a script. Do NOT load an ambush mission here.)
        'defend',('pirates_',0,1,5000,123456.789,0,False,True,'merchant',(),priv.name+"_mission",'Pirate_reinforcement','talon','Helen',3), # Mission arguments.
        priv.name+"_mission", # Script to be set on completion. -1=Failure, 0=Not Accepted, 1=Succeed, 2=In progress
        stahlspeech3, # Dictionary containing what the fixer says.
        None, # If you reject the mission twice. "None" means that he continues asking you forever until you accept
        CampaignEndNode(priv), # If you lose the mission
        StahlMission4, # If you win the mission. Usually points to the next mission
        StahlMission3, # The current mission node.
        mission_desc # Name that describes the mission in flight and in the mission computer.
        )

    mission_desc="Stahl_4:_Rescue_freighter_carrying_TarsusMk2"
    MakeMission(priv, # Creates any type of mission
        STAHL_SPRITE, # Campaign, sprite
        [InSystemCondition("Gemini/Troy","Achilles")], # Where fixer meets you to start the mission
        [InSystemCondition("Gemini/Troy","Achilles")], # Where the mission ends.
        AddCredits(12000), # Script to add your credits
        None, # Script to be run to start the mission (usually None if you don't have a script. Do NOT load an ambush mission here.)
        'escort_local',('pirates_',0,1,1,3000,0,True,'merchant__',(),priv.name+"_mission",'Pirate_interceptor','talon.blank','TarsusMk2_freighter','drayman',[("We are to prevent this ship from unloading its cargo. Get out of our way!")]), # Mission arguments.
        priv.name+"_mission", # Script to be set on completion. -1=Failure, 0=Not Accepted, 1=Succeed, 2=In progress
        stahlspeech4, # Dictionary containing what the fixer says.
        None, # If you reject the mission twice. "None" means that he continues asking you forever until you accept
        CampaignEndNode(priv), # If you lose the mission
        StahlMission5, # If you win the mission. Usually points to the next mission
        StahlMission4, # The current mission node.
        mission_desc # Name that describes the mission in flight and in the mission computer.
        )

    mission_desc="Stahl_5:_Find_and_destroy_pirate_commander"
    MakeMission(priv, # Creates any type of mission
        STAHL_SPRITE, # Campaign, sprite
        [InSystemCondition("Gemini/Troy","Achilles")], # Where fixer meets you to start the mission
        [InSystemCondition("Gemini/Troy","Achilles")], # Where the mission ends.
        AddCredits(10000), # Script to add your credits
        LaunchWingmen("confed__","broadsword",1), # Script to be run to start the mission (usually None if you don't have a script. Do NOT load an ambush mission here.)
        'bounty_leader',(0,0,0,False,1,'pirates_',(),priv.name+"_mission",'Pirate_flagship','tarsus',False,'Pirate_escort','talon',["You've made your final mistake, flyboy!","We will blast you away like...","What's that?","Escort, break and distract the confed ship!"]), # Mission arguments.
        priv.name+"_mission", # Script to be set on completion. -1=Failure, 0=Not Accepted, 1=Succeed, 2=In progress
        stahlspeech5, # Dictionary containing what the fixer says.
        None, # If you reject the mission twice. "None" means that he continues asking you forever until you accept
        CampaignEndNode(priv), # If you lose the mission
        StahlMission6, # If you win the mission. Usually points to the next mission
        StahlMission5, # The current mission node.
        mission_desc # Name that describes the mission in flight and in the mission computer.
        )

    mission_desc="Stahl_6:_Deliver_gems_and_seal_the_deal"
    MakeCargoMission(priv, # Creates a cargo mission
        STAHL_SPRITE, # Campaign, sprite
        [InSystemCondition("Gemini/Troy","Achilles")], # Where fixer meets you to start the mission
        [InSystemCondition("Gemini/Troy","Helen")], # Where the mission ends. Usually the same as starting point for next fixer.
        AddCredits(15000), # Script to be run as you click on the fixer. A common use is to AddCredits() for the previous mission.
        LoadMission(mission_desc,'ambush',(priv.name+"_mission",('Gemini/Troy'),25,'pirates_',2,'talon','Pirate_interceptor',[("Enough of this!",False),"You've disturbed our operations for the longest time!","Those ships must not be assembled! Prepare to die!"],['Gemini/Troy'], 'Helen')), # Script to be run to start the mission (usually None if you don't have a script, but ambush is also common.)
        ("Gems",20), # Mission arguments.
        priv.name+"_mission", # Script to be set on completion. -1=Failure, 0=Not Accepted, 1=Succeed, 2=In progress
        stahlspeech6, # Dictionary containing what the fixer says.
        None, # If you reject the mission twice. "None" means that he continues asking you forever until you accept
        CampaignEndNode(priv), # If you lose the mission
        StahlMission7, # If you win the mission. Usually points to the next mission
        StahlMission6) # The current mission node.

    mission_desc="Stahl_7:_One_more_gem_delivery"
    MakeCargoMission(priv, # Creates a cargo mission
        STAHL_SPRITE, # Campaign, sprite
        [InSystemCondition("Gemini/Troy","Achilles")], # Where fixer meets you to start the mission
        [InSystemCondition("Gemini/Troy","Helen")], # Where the mission ends. Usually the same as starting point for next fixer.
        AddCredits(20000,AddTechnology("troy")), # Script to be run as you click on the fixer. A common use is to AddCredits() for the previous mission.
        LoadMission(mission_desc,"directions_mission",(priv.name+"_mission",["Gemini/Troy"],"Helen")), # Script to be run to start the mission (usually None if you don't have a script, but ambush is also common.)
        ("Gems",10), # Mission arguments.
        priv.name+"_mission", # Script to be set on completion. -1=Failure, 0=Not Accepted, 1=Succeed, 2=In progress
        stahlspeech7, # Dictionary containing what the fixer says.
        None, # If you reject the mission twice. "None" means that he continues asking you forever until you accept
        CampaignEndNode(priv), # If you lose the mission
        StahlMission8, # If you win the mission. Usually points to the next mission
        StahlMission7) # The current mission node.

    mission_desc="Stahl:_Yet_another_gem_delivery"
    MakeCargoMission(priv, # Creates a cargo mission
        STAHL_SPRITE, # Campaign, sprite
        [InSystemCondition("Gemini/Troy","Achilles")], # Where fixer meets you to start the mission
        [InSystemCondition("Gemini/Troy","Helen")], # Where the mission ends. Usually the same as starting point for next fixer.
        AddCredits(1200,quest.removeQuest(VS.getPlayer().isPlayerStarship(),priv.name+"_mission",0)), # Script to be run as you click on the fixer. A common use is to AddCredits() for the previous mission.
        LoadMission(mission_desc,"directions_mission",(priv.name+"_mission",["Gemini/Troy"],"Helen")), # Script to be run to start the mission (usually None if you don't have a script, but ambush is also common.)
        ("Gems",10), # Mission arguments.
        priv.name+"_mission", # Script to be set on completion. -1=Failure, 0=Not Accepted, 1=Succeed, 2=In progress
        stahlspeech8, # Dictionary containing what the fixer says.
        None, # If you reject the mission twice. "None" means that he continues asking you forever until you accept
        CampaignEndNode(priv), # If you lose the mission
        StahlMission8, # If you win the mission. Usually points to the next mission
        StahlMission8) # The current mission node.
    return priv #return the newly created campaign back.
