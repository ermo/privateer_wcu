import campaign_lib
from campaign_lib import *
dillohspeech1={"intro":[("Dilloh","Okay, you've found me. Am I being arrested now?"),
							("Burrows","Excuse me, but did I miss something?"),
							("Dilloh","Oh come on! Are you insys, guild or confed? I bet you're confed."),
							("Burrows","What's up mate? I'm just a privateer looking for work!"),
							("Dilloh","Pardon me. According to your strange clothing, I thought you were a confed secret ops officer."),
							("Burrows","No, I am not! What's wrong with my clothes anyway?"),
							("Dilloh","This exaggerated coolness just doesn't fit with your silly face. But didn't you mention that you're looking for work?"),
							("Burrows","Yes I did, and I hope you still have something for me despite my silly face."),
							("Dilloh","I do, indeed. Let me introduce myself first. My name is Dilloh and I have been a Heckler&Koch engineer and ship designer for many years now."),
							("Burrows","HK? Isn't that a weapons company on Sol? I thought they were just in the market for rifles?"),
							("Dilloh","Ground wars are history, the wars are now decided in open space. The weapons industry has realized that the big bucks are made with ships and their armaments. I was lead designer of the Fireblade ship. You might have seen some in space."),
							("Burrows","Yes, I saw some. Nasty ships. I wonder why they're not for sale. They're not military."),
							("Dilloh","That's what I'm wondering too. Being a patriot, I designed the ship to be on the open market. With the cats getting deeper and deeper into civilian space, everyone has a need to at least be able to run away from them. Unfortunately, the Confederation thought that this ship was too dangerous in civilian hands and stopped my project."),
							("Burrows","And I guess you didn't get yourself a job at Space Burger afterwards, right?"),
							("Dilloh","Of course not. The Fireblade is a ship designed to distract, scout and infiltrate. I wonder how those nuts in uniforms could have ever thought it would be a threat for their warships. So I decided to release the ship on my own, illegally."),
							("Burrows","You must be quite convinced that your ship will be a success if you're willing to risk trouble with the feds to sell it."),
							("Dilloh","Unfortunately, trouble has already found me. I had an exciting ride away from Sol: major loops, several confrontations, you name it. Anyway, you could help me with... 'wiping out my traces'."),
							("Burrows","You mean killing ships that might have scanned you."),
							("Dilloh","Yes. I've chosen the proximity of pirate territory to keep the feds away, but I'd like you to take a brief look at this system and destroy any confed patrols. I'll pay 10000 for this.")],
				"reject1":[("Burrows","Sorry, but fighting the military is in no way better than sleeping with it."),
							("Dilloh","I hope you'll reconsider. I can't rely on the pirates for that.")],
				"reconsider":[("Burrows","I've reconsidered."),
							("Dilloh","That's good. I need you to erase any confed patrol in this system."),
							("Burrows","Payment?"),
							("Dilloh","10000 credits.")],
				"reject2":[("Burrows","No thanks."),
							("Dilloh","Then please, don't waste my time!")],
				"accept":[("Burrows","Sure, I'll help you out for now. But when I'm back, I'll have further questions about your story."),
                            ("Dilloh","If you succeed, I'll be happy to put my faith in you.")],
                "accept2":[("Dilloh","Thanks. Please move out.")],
				"reminder":[("Dilloh","The sensors show a confed patrol."),
							("Burrows","Yes, I just thought it would be reasonable to explain everything to them and..."),
							("Dilloh","Are you crazy? I'm on the list of the top 100 enemies of the state! They're here to kill me!"),
							("Burrows","Okay, but maybe you haven't tried to explain your project to them properly."),
							("Dilloh","Alas, if all they wanted was to be convinced, I would not be sitting here. Now move out!")],
				"failure":[("Dilloh","The confeds have located me, thanks to your failure. You'd better flee now, too!")]
				}
dillohspeech2={"intro":[("Dilloh","Did you manage to erase the patrol?"),
							("Burrows","Yes, they couldn't transmit anything."),
							("Dilloh","That's good. If any other faction surveyed the attack, they will at least not know that you are working for me."),
							("Burrows","Now, please tell me more about the Fireblade. I know it is a slightly faster Demon, but what else is so special about it?"),
							("Dilloh","I'm afraid I wasn't exactly honest with you. The crux of it is: the prototype of the Fireblade contains a cloaking device."),
							("Burrows","Oh my god."),
							("Dilloh","Funny this always causes the same reaction. The device is unfinished yet, and far away from cat technology, but I was about to merge it with a level 1 shield emitter."),
							("Burrows","Now I understand. The confeds didn't want the device to fall into civilian hands."),
							("Dilloh","And to make sure that I wouldn't give it away, I was arrested and forced to work day and night on the cloaking technology, of course exclusively for the Confederation. I got bored of this quite fast; I invented the cloak to be able to spend the rest of my life at a pleasure planet, not in jail..."),
							("Burrows","...and then you managed to escape, eh? Funny tale, but seriously, you don't look like a scientist to me."),
							("Dilloh","I had to change my style for a better cover. Remember, I'm not only a refugee, I'm also planning to sell my ships against all odds."),
							("Burrows","If this is all true, why didn't I ever see a cloaked Fireblade?"),
							("Dilloh","Isn't that what cloaking devices are all about?"),
							("Burrows","Err..."),
							("Dilloh","Just kidding... Unlike the prototype, the Fireblades you see flying around have no cloak. They are the results of the Confederation selling my ship design to civil shipyards."),
							("Burrows","But... couldn't you have sold your ships like that before?"),
							("Dilloh","If I knew that I'd be arrested for my cloak, I would have. But now it's more convenient for them to kill me. Guess what would happen if I found a way to prove that I was illegally arrested, detained and forced to work for confed?"),
							("Burrows","There would surely be a scandal. A lot of heads might roll before congress. I see. Now what do you want me to do?"),
							("Dilloh","I need you to reestablish contact with my friend on New Detroit. He is the only one I trust, plus he has good connections with the authorities, or at the very least he might be able to bringing me off-world. I can't transmit my requests for now, I'd risk being found."),
							("Burrows","I guess the feds will be waiting for me?"),
							("Dilloh","Yes, they've increased patrols around New Detroit. So you'll have to pretend to 'visit your aunt' there, with a 'present' for her, but you will actually be delivering a data pad from me. Wait on New Detroit until my contact takes the 'present' out of your ship. I'd suggest to take the 'pirate route'. Though it leads through Perry, you will be able to avoid many unnecessary scans."),
							("Burrows","What's the payoff?"),
							("Dilloh","I'll give you 30000 for your trouble, since it is a risky route that requires refuelling. Meet me back here for your payment.")],
				"reject1":[("Burrows","Sorry, but I'm not a traitor."),
							("Dilloh","The only traitors out there are those who would keep science locked up for their own benefits.")],
				"reconsider":[("Burrows","I've reconsidered. 30000 credits is a lot."),
							("Dilloh","Yes, and the worst you'll face is a simple blockade at the end. Deliver my data pad to New Detroit and come back afterwards.")],
				"reject2":[("Burrows","Nah."),
							("Dilloh","Whatever you say.")],
				"accept":[("Burrows","Okay, I'll help you again, but you need to tell me more about the cloak later."),
                            ("Dilloh","I'll do so, now leave.")],
                "accept2":[("Dilloh","Good. Please make haste.")],
				"reminder":[("Dilloh","Did you deliver my pad yet?"),
							("Burrows","No, I had other leads to follow."),
							("Dilloh","Please make haste.")],
				"failure":[("Dilloh","My pad is gone, probably in confed hands. This is the end of me.")]
				}
dillohspeech3={"intro":[("Dilloh","Thanks. The pad has reached its destination. I received an encrypted message that everything has been arranged."),
							("Burrows","Arranged? What?"),
							("Dilloh","You don't need to know this part of the story."),
							("Burrows","Okay then, tell me more about the other part of the story."),
							("Dilloh","As I mentioned, there's still a prototype of the Fireblade around."),
							("Burrows","The one with the cloak?"),
							("Dilloh","Yes, I was able to flee using this ship. However, it was still a rough piece of technology and it failed from time to time. I made it to this base and while I was hiding, I managed to make it work perfectly."),
							("Burrows","So, why not climb into your ship, cloak, and fly away?"),
							("Dilloh","Away... but where? I don't want to hide out the rest of my life! I want to live on a pleasure base, didn't I mention that? I have no use for this ship. Maybe I'll give it to a good friend some day."),
							("Burrows","You suddenly caught my attention. Can I bring you a coffee, or may I invite you to dinner?"),
							("Dilloh","I prefer loyalty proved by deeds, not by presents. A freighter is coming in. Normally, we manage to escape detection by transmitting false shipping information. Unfortunately, this freighter has been scanned and its cargo detected. It is being pursued by several Raptors."),
							("Burrows","A freighter containing what?"),
							("Dilloh","Some components I need for my cloaking devices. Tools, spare parts, hammers and nails, things you don't need to worry about. Worry about the Raptors."),
							("Burrows","Raptors are quite tough. I'll need help for that."),
							("Dilloh","I've already organized some support. Since the freighter's escort, two Demons, are already destroyed, I contacted three former customers. They're all flying Fireblades."),
							("Burrows","Not the best ships to dispatch tough bombers."),
							("Dilloh","Hah, you don't know what you're talking about! Those babies have already destroyed the Stiletto trying to transmit the freighter's destination! I'm offering 20000 for the protection of the freighter.")],
				"reject1":[("Burrows","Raptors are some of the toughest ships in this sector. Forget it."),
							("Dilloh","But the odds are good! Please reconsider!")],
				"reconsider":[("Burrows","Okay, what was that mission again?"),
							("Dilloh","Three Fireblades as wingmen with which you are to protect our Drayman from Raptor bombers. The payoff is 20000.")],
				"reject2":[("Burrows","No, that's suicide."),
							("Dilloh","Suicide is painless... but that's a battle you'll never forget!")],
				"accept":[("Burrows","Okay, once more."),
                            ("Dilloh","Thank you. Your wingmen are already waiting for you.")],
                "accept2":[("Dilloh","Thank goodness.")],
				"reminder":[("Dilloh","The freighter isn't here yet."),
							("Burrows","Yes, I was about to take a shower before I leave."),
							("Dilloh","Just make sure your make-up doesn't take longer than the bomber pilots need to erase our freighter.")],
				"failure":[("Dilloh","The freighter has been destroyed. We lost stuff worth several million credits. Consider yourself fired.")]
				}
dillohspeech4={"intro":[("Dilloh","Thank you for saving our freighter."),
							("Burrows","No problem. What's next?"),
							("Dilloh","My contact on New Detroit has been arrested and interrogated. Fortunately, what the Confederation learned from him is that I am willing to keep the cloak away from civilian hands for now."),
							("Burrows","You mean you're about to find a compromise?"),
							("Dilloh","Yes. I've arranged a meeting on Bodensee in Tingerhoff. I want you to tell the feds that I'm willing to share all the information about my finalized cloak, in exchange for a monopoly license for the uncloaked Fireblade as well as the freedom for me and my partners."),
							("Burrows","Why do we need to go so far away from here?"),
							("Dilloh","I'm not totally sure if the offer is honest, and since I'm not about to give away my prototype I've decided to point the feds into the wrong direction."),
							("Burrows","Do you really believe that the feds will deal fairly with you after all what has happened?"),
							("Dilloh","I know Admiral Terrell personally. He is a man of peace and his position is endangered. I don't think he can afford to risk a scandal. By arresting me, chasing me and selling my ships, he's already done much to endanger his reputation. The Fireblade scandal is surely too damageable for them to risk it leaking out, for it would damage the reputation of the whole military"),
							("Burrows","As long as you're willing to live with the results. What's the pay?"),
							("Dilloh","5000 bucks. I don't think you'll face any trouble.")],
				"reject1":[("Burrows","Sorry, but crossing pirate territory is costing me more than 5000 credits."),
							("Dilloh","Well, I could also give this mission to someone else.")],
				"reconsider":[("Burrows","Please tell me about your mission again."),
							("Dilloh","Meet a confed negotiator on Bodensee in Tingerhoff, tell her about my offer, and come back with the reply, for 5000 credits.")],
				"reject2":[("Burrows","Not enough credits."),
							("Dilloh","Alright, I'm getting tired of those conversations anyway.")],
				"accept":[("Burrows","It would sure be nice to see both our reputation cleansed. I'm in."),
                            ("Dilloh","Good. Please hurry up.")],
                "accept2":[("Dilloh","Good. Please hurry up.")],
				"reminder":[("Dilloh","What was the reply?"),
							("Burrows","None so far, I haven't left yet."),
							("Dilloh","Listen, the feds won't wait forever. They'll interpret this delay as a change of my mind."),
							("Burrows","Relax, I'll take off immediately.")],
				"failure":[("Dilloh","You didn't deliver the message, and the confeds are on my trail again. The situation is getting too dangerous. I have no use for you any more.")]
				}
dillohgoodinspeech={"intro":[("Burrows","My name is Grayson Burrows, I represent Dilloh."),
							("Goodin","I am Sandra Goodin, representing Admiral Terrell."),
							("Burrows","Now, here's the deal: Dilloh and his mates will no longer be pursued or arrested, and he wants the monopoly on his uncloaked Fireblade. In exchange, he will hand all information about the finalized cloaking device over to you and stop pursuing its development or sale."),
							("Goodin","He has fled with a prototype. What about this ship?"),
							("Burrows","It won't be duplicated, but it will remain in private hands."),
							("Goodin","I think the Confederation can live with this."),
							("Burrows","Do we have a deal?"),
							("Goodin","Okay, ace. We'll forget about your bad profile with the Confederation. I'm inviting you to visit Anapolis in Perry with your employer."),
							("Burrows","What for?"),
							("Goodin","In order for your to do an official presentation of the Fireblade. Admiral Terrell is really sorry about everything that happened and wants to give Dilloh a show of welcome."),
							("Burrows","It sounds like you're desperate to show your friendship with Dilloh. What's up?"),
							("Goodin","Erm... the scandal was on the news. To be honest, I've been ordered to express an official apology from Admiral Terrell. The officers responsible for the whole damn scandal have been arrested and charged. Free trade is an important principle in the Gemini sector. It was never in the Confederation's gain to prevent it."),
							("Burrows","That's not exactly what experience has taught me...")],
				"reject1":[("Burrows","...and I won't help polish the military's image.")],
				"reconsider":[("Goodin","Bring the reply to Dilloh."),
						("Burrows","I have my doubts about this. It sounds like a trap...")],
				"reject2":[("Burrows","...and therefore I won't help you.")],
				"accept":[("Burrows","...but I will deliver your message."),
						("Goodin","Good. Make haste.")],
			"accept2":[("Burrows","...but I will deliver your message.")],				
				"reminder":[("Goodin","Hurry up man, not everybody involved in this scandal feels like apologizing. There might be still some who are planning to track down Dilloh.")],
				"failure":[("Informant","Your failure has thrown your employer in deep trouble.")]
				}
dillohspeech5={"intro":[("Dilloh","What was the reply?"),
							("Burrows","They apologized, along with an invitation to Anapolis to present your Fireblades. And you may keep the Prototype."),
							("Dilloh","That's great. It's always good to work without foes."),
							("Burrows","Considering that, I have news. It seems that the cats have learned about your cloak efforts. I was ambushed."),
							("Dilloh","I knew this would happen sooner or later. Going closer to cat space doesn't make things easier now."),
							("Burrows","I know, but I'll take care of your health, in return for adequate payment."),
							("Dilloh","Sounds good to me - what about 15000 bucks?")],
				"reject1":[("Burrows","You owe me alot, Dilloh. 15000 isn't quite a payoff worthy of the saviour of your life."),
							("Dilloh","In the end, we're all businessmen. The payoff won't change.")],
				"reconsider":[("Burrows","So again, you still want me to fly you to Perry? Have you reconsidered the payment?"),
							("Dilloh","Yes, and no. I still think 15000 is more than enough.")],
				"reject2":[("Burrows","I don't think so, I'm out."),
							("Dilloh","Finding a transport to Perry shouldn't be a problem. Your loss.")],
				"accept":[("Burrows","Okay, climb into my ship and we'll leave."),
                            ("Dilloh","I always wanted to see you in action.")],
                "accept2":[("Dilloh","Okay, I'm ready to leave.")],
				"reminder":[("Dilloh","Tell me what we're doing here."),
							("Burrows","I was looking for additional opportunities en-route to Perry."),
							("Dilloh","I really wouldn't mind if we started now."),
							("Burrows","Cool down, you'll be able to show your ships soon enough.")],
				"failure":[("Dilloh","The visit to Perry was my only hope to fix things with the feds. Now they're looking for me again. I'll have to hide. Goodbye.")]
				}
dillohspeech6={"intro":[("Dilloh","It was great to see how you dealt with the Kilrathi. I just wonder how you'd perform in a Fireblade. Now about the official presentation. I've set up a squadron of three Fireblades which were meant to fly a loop through the system. But the confeds have reported cats looking for us, so our plan has changed."),
							("Burrows","The task is to destroy them?"),
							("Dilloh","Correct, this will be the best presentation we can think of. Since the ships are meant to be an escort, the presentation will still be a success even if only you survive the attack."),
							("Burrows","I have a feeling you are relying on my piloting skills rather than the Fireblade to survive."),
							("Dilloh","Both. In the end, we will see at least one ship surviving an attack from six Grikaths, and that's what will make the people run to the stores."),
							("Burrows","Six Grikaths? That'll require an awful lot of piloting skills."),
							("Dilloh","I have faith in your abilities to command your wingman properly. The cats seem intent to send obsolete bombers because they think they'll encounter some freighters. They have no idea they'll meet ships ready to dogfight. Since this is going to be the deal of my life, I'll pay 50000 credits for your success.")],
				"reject1":[("Burrows","You must think I'm crazy. Six Grikaths might even be able to take out a Paradigm!"),
							("Dilloh","Oh come on! You can deal with those odds, I'm sure.")],
				"reconsider":[("Burrows","What was that again? Three Fireblades and me versus six Grikaths?"),
							("Dilloh","Yes, for a payoff of 50000 credits.")],
				"reject2":[("Burrows","The credits are inviting, but I'm not looking for disability payments."),
							("Dilloh","Your problem. For this payoff, I'll find an adequate pilot quite soon.")],
				"accept":[("Burrows","50000 credits. Wow. I'm definitely in."),
                            ("Dilloh","Good. Pick up your wingmen and intercept the enemy before they can do any harm to Anapolis.")],
                "accept2":[("Dilloh","Good. You can launch at any time.")],
				"reminder":[("Dilloh","What are you doing here? The cats have nearly reached Anapolis!"),
							("Burrows","I was just wondering if we could make the presentation somewhat easier."),
							("Dilloh","No, we cannot - I've promised the confeds that I'll take care of those Grikaths, and if I don't, my head will roll!"),
							("Burrows","Alright, I'll take care of the cats.")],
				"failure":[("Dilloh","Anapolis is heavily damaged, many people have died. The confeds are blaming me for that. You'd better get out while you can, before you get charged.")]
				}
dillohsuccess=[("UNLOCKED: Fireblade, Fireblade Prototype."),
			("Dilloh","That was one awesome presentation! I'm glad you showed the sector what a Fireblade is capable of doing!"),
			("Burrows","Yeah, not to forget about what *I* am able to do..."),
			("Dilloh","You're right, I totally forgot about that. Here is your final payment. The Fireblade is now available on any Hunter-ship store."),
			("Burrows","Good deal. And you can still fly around with your cloaked prototype."),
			("Dilloh","I could, but the cats might be out to destroy that ship, as well as some confed officers who still think the cloak is a threat. I prefer to spend a life in luxury with all my money. I'm not exactly a hotshot pilot enjoying a good ship."),
			("Burrows","...but I am."),
			("Dilloh","Hmm... heck, I'll give the ship to you. I have no use for it, but you surely have. Collect it at the ship dealer. But take care of it, it's my baby."),
			("Burrows","Thanks, that's very generous."),
			("Dilloh","You've managed to transform me from the enemy of the state into a rich man. I thank you for everything you've done for me and wish you good luck. Have fun spending your money!"),
			("Burrows","I think I'll invest some of it in buying new clothes to compensate for my silly face, Dilloh. Just to prevent someone from thinking I'm a confed agent again. Good luck to you.")]

def LoadDillohCampaign():
	DILLOH2_SPRITE  = ("informant.spr","Talk_to_Dilloh","bases/heads/informant.spr") #sprite file for the fixer
	DILLOH_SPRITE  = ("informant.spr","Talk_to_Dilloh","bases/heads/dilloh.spr") #sprite file for the fixer
	GOODIN_SPRITE  = ("goodin.spr", "Talk_To_Goodin","bases/heads/goodinanapolis.spr")
	DillohMission1 = CampaignClickNode() # Initialize each node
	DillohMission2 = CampaignClickNode() # Initialize each node
	DillohMission3 = CampaignClickNode() # Initialize each node
	DillohMission4 = CampaignClickNode() # Initialize each node
	DillohGoodinMission = CampaignClickNode() # Initialize each node
	DillohMission5 = CampaignClickNode() # Initialize each node
	DillohMission6 = CampaignClickNode() # Initialize each node
	DillohFinish = CampaignNode()

	priv=Campaign("dilloh_campaign") # Name of the save game variable for the entire campaign. Can't contain spaces
	priv.Init(DillohMission1) # the first node.

	mission_desc="Dilloh_1:_Wiping_traces"
	MakeMission(priv, # Creates a cargo mission
		DILLOH_SPRITE, # Campaign, sprite
		[InSystemCondition("Gemini/Pollux","Remus")], # Where fixer meets you to start the mission
		[InSystemCondition("Gemini/Pollux","Remus")], # Where the mission ends. Usually the same as starting point for next fixer.
		None, # Script to be run as you click on the fixer. A common use is to AddCredits() for the previous mission.
		None,
		'defend',('confed_',0,1,5000,123456.789,0,False,True,'merchant',(),priv.name+"_mission",'','ferret','',1), # Mission arguments.
		priv.name+"_mission", # Script to be set on completion. -1=Failure, 0=Not Accepted, 1=Succeed, 2=In progress
		dillohspeech1, # Dictionary containing what the fixer says.
		None, # If you reject the mission twice. "None" means that he continues asking you forever until you accept
		CampaignEndNode(priv), # If you lose the mission
		DillohMission2, # If you win the mission. Usually points to the next mission
		DillohMission1, # The current mission node.
		mission_desc) # Name that describes the mission in flight and in the mission computer.

	mission_desc="Dilloh_2:_Deliver_present"
	MakeCargoMission(priv, # Creates any type of mission
		DILLOH_SPRITE, # Campaign, sprite
		[InSystemCondition("Gemini/Pollux","Remus")], # Where fixer meets you to start the mission
		[InSystemCondition("Gemini/New_Detroit","New_Detroit")], # Where the mission ends.
		AddCredits(10000), # Script to be run as you click on the fixer. A common use is to AddCredits() for the previous mission.
		LoadMission(mission_desc,"ambush",(priv.name+"_mission",("Gemini/New_Detroit",),0,'confed_',4,'','',[("#bb4400We know you're transporting illegal data to New Detroit.",False),("#996600Sorry, I'm just visiting my aunt there. I've got a present for her. Is that a problem?",True),("#bb4400It is. We intend to prevent you from making delivery, with extreme prejudice."),("#996600Alas, that's why I don't like visiting relatives.")],['Gemini/Sherwood', 'Gemini/Capella', 'Gemini/Nexus', 'Gemini/Tingerhoff', 'Gemini/Perry', 'Gemini/New_Detroit'], 'New_Detroit')), # Script to be run to start the mission (usually None if you don't have a script, but ambush is also common.)
		("False_present",1), # Mission arguments.
		priv.name+"_mission", # Script to be set on completion. -1=Failure, 0=Not Accepted, 1=Succeed, 2=In progress
		dillohspeech2, # Dictionary containing what the fixer says.
		None, # If you reject the mission twice. "None" means that he continues asking you forever until you accept
		CampaignEndNode(priv), # If you lose the mission
		DillohMission3, # If you win the mission. Usually points to the next mission
		DillohMission2) # The current mission node.

	mission_desc="Dilloh_3:_Save_freighter"
	MakeMission(priv, # Creates any type of mission
		DILLOH_SPRITE, # Campaign, sprite
		[InSystemCondition("Gemini/Pollux","Remus")], # Where fixer meets you to start the mission
		[InSystemCondition("Gemini/Pollux","Remus")], # Where the mission ends.
		AddCredits(30000), # Script to add your credits
		LaunchWingmen("hunter__","fireblade",3), # Script to be run to start the mission (usually None if you don't have a script. Do NOT load an ambush mission here.)
		'escort_local',('confed_',0,2,2,3000,0,True,'merchant__',(),priv.name+"_mission",'','raptor.blank','','drayman',["Escort ships, give up now.", "Your illegal actions will land you into jail, or much worse if you don't give up!"]), # Mission arguments.
		priv.name+"_mission", # Script to be set on completion. -1=Failure, 0=Not Accepted, 1=Succeed, 2=In progress
		dillohspeech3, # Dictionary containing what the fixer says.
		None, # If you reject the mission twice. "None" means that he continues asking you forever until you accept
		CampaignEndNode(priv), # If you lose the mission
		DillohMission4, # If you win the mission. Usually points to the next mission
		DillohMission3, # The current mission node.
		mission_desc) # Name that describes the mission in flight and in the mission computer.

	mission_desc="Dilloh_4:_Negotiate_with_confed"
	MakeCargoMission(priv, # Creates any type of mission
		DILLOH_SPRITE, # Campaign, sprite
		[InSystemCondition("Gemini/Pollux","Remus")], # Where fixer meets you to start the mission
		[InSystemCondition("Gemini/Tingerhoff","Bodensee")], # Where the mission ends.
		AddCredits(20000), # Script to be run as you click on the fixer. A common use is to AddCredits() for the previous mission.
		LoadMission(mission_desc,"directions_mission",(priv.name+"_mission",['Gemini/Sherwood', 'Gemini/Capella', 'Gemini/Nexus', 'Gemini/Tingerhoff'], 'Bodensee')), # Script to be run to start the mission (usually None if you don't have a script, but ambush is also common.) (having no destination will call significant unit.. oakham should be the only dockable significant in that system
		("Non-aggression-contract",1), # Mission arguments.
		priv.name+"_mission", # Script to be set on completion. -1=Failure, 0=Not Accepted, 1=Succeed, 2=In progress
		dillohspeech4, # Dictionary containing what the fixer says.
		None, # If you reject the mission twice. "None" means that he continues asking you forever until you accept
		CampaignEndNode(priv), # If you lose the mission
		DillohGoodinMission, # If you win the mission. Usually points to the next mission
		DillohMission4) # The current mission node.

	mission_desc="Dilloh_4b:_Bring_message_back"
	MakeCargoMission(priv, # Creates any type of mission
		GOODIN_SPRITE, # Campaign, sprite
		[InSystemCondition("Gemini/Tingerhoff","Bodensee")], # Where fixer meets you to start the mission
		[InSystemCondition("Gemini/Pollux","Remus")], # Where the mission ends.
		ClearFactionRecord('confed',1.0,PushRelation('confed')), # Script to be run as you click on the fixer. A common use is to AddCredits() for the previous mission.
		LoadMission(mission_desc,"ambush",(priv.name+"_mission",("Gemini/Tingerhoff",),0,'kilrathi_',4,'','',["You're spreading cloaking technology into the hands of the apes.","Prepare to die by our swords!"],['Gemini/Nexus', 'Gemini/Capella', 'Gemini/Sherwood', 'Gemini/Pollux'], 'Remus')), # Script to be run to start the mission (usually None if you don't have a script, but ambush is also common.)
		("Signed_contract",1), # Mission arguments.
		priv.name+"_mission", # Script to be set on completion. -1=Failure, 0=Not Accepted, 1=Succeed, 2=In progress
		dillohgoodinspeech, # Dictionary containing what the fixer says.
		None, # If you reject the mission twice. "None" means that he continues asking you forever until you accept
		CampaignEndNode(priv), # If you lose the mission
		DillohMission5, # If you win the mission. Usually points to the next mission
		DillohGoodinMission) # The current mission node.

	mission_desc="Dilloh_5:_Bring_Dilloh_to_Anapolis"
	MakeCargoMission(priv, # Creates a cargo mission
		DILLOH_SPRITE, # Campaign, sprite
		[InSystemCondition("Gemini/Pollux","Remus")], # Where fixer meets you to start the mission
		[InSystemCondition("Gemini/Perry","Anapolis")], # Where the mission ends. Usually the same as starting point for next fixer.
		AddCredits(5000), # Script to be run as you click on the fixer. A common use is to AddCredits() for the previous mission.
		LoadMission(mission_desc,'ambush',(priv.name+"_mission",('Gemini/Nexus'),25,'kilrathi_',3,'sartha','',[("We know you are transporting a cloak scientist."),("We are here to kill him, with you as a bonus, ape!")],['Gemini/Sherwood', 'Gemini/Capella', 'Gemini/Nexus', 'Gemini/Tingerhoff', 'Gemini/Perry'], 'Anapolis')), # Script to be run to start the mission (usually None if you don't have a script, but ambush is also common.)
		("Dilloh",1), # Mission arguments.
		priv.name+"_mission", # Script to be set on completion. -1=Failure, 0=Not Accepted, 1=Succeed, 2=In progress
		dillohspeech5, # Dictionary containing what the fixer says.
		None, # If you reject the mission twice. "None" means that he continues asking you forever until you accept
		CampaignEndNode(priv), # If you lose the mission
		DillohMission6, # If you win the mission. Usually points to the next mission
		DillohMission5) # The current mission node.

	mission_desc="Dilloh_6:_Display_of_firefighting"
	MakeMission(priv, # Creates a cargo mission
		DILLOH_SPRITE, # Campaign, sprite
		[InSystemCondition("Gemini/Perry","Anapolis")], # Where fixer meets you to start the mission
		[InSystemCondition("Gemini/Perry","Anapolis")], # Where the mission ends. Usually the same as starting point for next fixer.
		AddCredits(15000), # Script to be run as you click on the fixer. A common use is to AddCredits() for the previous mission.
		LaunchWingmen("confed__","fireblade",3), # Script to be run to start the mission (usually None if you don't have a script. Do NOT load an ambush mission here.)
		'bounty_leader',(0,0,0,False,6,'kilrathi_',(),priv.name+"_mission",'','grikath',False,'','grikath',["There's no freighters out there, but there's still some apes! Engage!"]), # Mission arguments.
		priv.name+"_mission", # Script to be set on completion. -1=Failure, 0=Not Accepted, 1=Succeed, 2=In progress
		dillohspeech6, # Dictionary containing what the fixer says.
		None, # If you reject the mission twice. "None" means that he continues asking you forever until you accept
		CampaignEndNode(priv), # If you lose the mission
		DillohFinish,
		DillohMission6, # The current mission node.
		mission_desc) # Name that describes the mission in flight and in the mission computer.

	DillohFinish.Init(priv,
		[],
		None,
		None,
		GoToSubnode(0),
		None,
		[CampaignClickNode().Init(priv,
			[InSystemCondition("Gemini/Perry","Anapolis")],
			dillohsuccess,
			DILLOH_SPRITE,
			TrueSubnode(AddCredits(50000,AddTechnology("fireblade"))),
			None,
			[CampaignEndNode(priv)])]) # YOU WIN!!!

	return priv #return the newly created campaign back.
