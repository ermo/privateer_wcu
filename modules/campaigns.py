import campaign_bonus
import camptroy
import dillohfb
import sligorsc
import zoolcamp
import galagoss
import hospital
import irene
import scottval
import avalon
import ebenezer
campaignsloaders=[lambda:LoadMainCampaign(),lambda:LoadRFCampaign(),lambda:LoadRFMurphyCampaign(),lambda:LoadRFGoodinCampaign(),lambda:LoadRFTaylaCampaign(),lambda:LoadRFLynchCampaign(),lambda:campaign_bonus.LoadBonusCampaign(),lambda:camptroy.LoadTroyCampaign(),lambda:dillohfb.LoadDillohCampaign(),lambda:sligorsc.LoadSligorCampaign(),lambda:zoolcamp.LoadZoolCampaign(),lambda:galagoss.LoadGosshawkCampaign(),lambda:hospital.LoadNateCampaign(),lambda:irene.LoadIreneCampaign(),lambda:scottval.LoadScottCampaign(),lambda:avalon.LoadAvalonCampaign(),lambda:ebenezer.LoadEbenezerCampaign()]
campaigns=[]

def loadAll(cockpit):
	for x in campaignsloaders:
		ret=x()
		if ret:
			campaigns.append(ret)

def getCampaigns():
	return campaigns

import campaign_lib
from campaign_lib import *


sandovalspeech={"intro":[("Sandoval","Welcome to New Detroit. You look like a man who's hungry for work.", "barspeech/campaign/sandoval1intro.wav"),
							("Burrows","Among other things. You hiring?"),
							("Sandoval","Indeed I am. A simple delivery of iron, strictly legit."),
							("Burrows","I've heard that song before, Mr?"),
							("Sandoval","Sandoval, Ernesto Sandoval."),
							("Burrows","Then I'll be your pilot."),
							("Sandoval","You'll be running the load of iron to the Liverpool refinery in Newcastle, which is just a short jump from here. No contraband, no hassles. Just dock at the station. My people will pick up the cargo. Afterwards, return here for your payment, 15000 credits. Interested?")],
				"reject1":[("Burrows","Sorry, I'm looking for a higher paying mission right now.", "barspeech/campaign/sandoval1reject1.wav"),
							("Sandoval","You fool, you have no idea! All right, fine. Take a hike, I've got my own problems.")],
				"reconsider":[("Burrows","I'm reconsidering your offer, Sandoval.", "barspeech/campaign/sandoval1reconsider.wav"),
							("Sandoval","A wise move. I can't understand why you walked away from such an easy job. I have something here that I want to show you."),
							("Burrows","What is it, some sort of sculpture?"),
							("Sandoval","It's an alien artifact. Extremely valuable. Soon I'll be selling it for a considerable sum. If you accept my mission I'll let you hold on to it as collateral. You'll run iron from here to the Liverpool refinery in Newcastle. Once there, dock and allow my men to retrieve the cargo. Return here with my artifact, and I'll pay you a 15000 fee, along with 5000 for the artifact's return. Do we have a deal?")],
				"reject2":[("Burrows","Maybe later, Sandoval.", "barspeech/campaign/sandoval1reject2.wav"),
							("Sandoval","I need to find someone right away, so don't take too long to make up your mind.")],
				"accept":[("Burrows","Sure, why not? I could use the credits. What about an advance?", "barspeech/campaign/sandoval1accept1.wav"),
				("Sandoval","Will this do?"),
				("Burrows","What is it, some sort of sculpture?"),
				("Sandoval","It is an alien artifact, extremely valuable. Soon I will be selling it for a considerable sum. In the meantime, I'll let you hold on to it as collateral."),
				("Burrows","In other words, it's hot, and you want to distance yourself from it."),
				("Sandoval","For a while, if you'll just hold on to it for me. Just for this run. I'll pay you a bonus of 5000 when you return. Fair enough?"),
				("Burrows","I suppose. Though I'm sure I'll wind up regretting this."),
				("Sandoval","Go with God, my suspicious friend. And hurry back.")],
		"accept2":[("Sandoval","Good. Keep this artifact in a safe place. I will have your ship loaded with iron immediately. Get moving.", "barspeech/campaign/sandoval1accept2.wav")],
				"reminder":[("Sandoval","What are you doing here? You should've been gone long ago!", "barspeech/campaign/sandoval1reminder.wav"),
							("Burrows","Some other business came up."),
							("Sandoval","This delay is risking us both!"),
							("Burrows","I thought this job was just a run of iron to the Liverpool refinery base."),
							("Sandoval","The artifact. Is it safe?"),
							("Burrows","Sure. Why wouldn't it be?"),
							("Sandoval","Just get it off this base."),
							("Burrows","What's the hurry?"),
							("Sandoval","You don't want to know. Trust me. Run the iron from here to the Liverpool refinery in Newcastle. Your ship has already been loaded. Deliver the iron, return here, and I'll pay you 15000 for your trouble, along with a 5000 bonus when you return my artifact."),
							("Burrows","All right, I'll get right on it. You've made your point."),
							("Sandoval","I hope so for both our sakes")],
				"failure":[("Sandoval","You failed to deliver the iron to Liverpool. I cannot imagine ever trusting you again. Keep the artifact...I hope they hunt you down and kill you for it. Goodbye")]
				}
taylafailure=[("Burrows","Okay, sweetheart. What's my next assignment?", "barspeech/campaign/taylafailure.wav"),
			("Tayla","Uh uh. You're a bad pony. I can't afford to bet on you anymore. You screwed up the last mission. I'm cutting my losses. You'll have to take your chances with InSys. I'm out of here."),
			("Burrows","But I need information on that artifact, Tayla!"),
			("Tayla","You should've thought of that before you choked up. Later.")]
tayla1={"intro":[("Tayla","Ah. You look just like your picture. Too bad.", "barspeech/campaign/tayla1intro.wav"),
				("Burrows","After a few drinks you'll change your mind, Miss...?"),
				("Tayla","Call me Tayla. I used to do business with Sandoval."),
				("Burrows","I'd rather talk about my face. What's wrong with it, anyway?"),
				("Tayla","Nothing, except the police have it plastered all over the holos. Sandoval is dead, and they want you for questioning. Tough break, but I'm here to offer you work now that you're... between jobs. I need you to make four special deliveries for me."),
				("Burrows","By special you mean risky and illegal."),
				("Tayla","And lucrative. The first run pays 10000 credits."),
				("Burrows","That's lucrative? Thanks, but I got my own leads to follow up."),
				("Tayla","Right, the artifact. You have it, but you don't know anything about it. I could fill you in... after you fly my missions. How about it, Captain?")],
		"reject1":[("Burrows","I think I'll check into this artifact business alone.", "barspeech/campaign/tayla1reject1.wav"),
				("Tayla","Bad choice. You're in danger as long as you hold onto that thing... and you're walking away from more money than you ever dreamed of!")],
		"reconsider":[("Tayla","Back, huh? I guessed you'd change your mind.", "barspeech/campaign/tayla1reconsider.wav"),
					("Burrows","That remains to be seen."),
					("Tayla","Look, it's a great deal. Your cargo will consist of nothing but plastics... completely legal. Supposedly you'll be running it to Newcastle, but actually... you'll divert to Oakham, a hidden pirate base, and dock. You won't have any trouble with the pirates because you work for me. Once there, leave your ship unattended and meet me in the bar there at Oakham for your pay. In exchange for the service, I'll pay you 10000 credits. And don't forget... I have information on the artifact, info I'll share... if you fly for me. So... is it a deal?")],
		"reject2":[("Tayla","If you don't want the job, just leave me alone!", "barspeech/campaign/tayla1reject2.wav")],
		"accept":[("Burrows","With the police after me, I could use the trip off-system...", "barspeech/campaign/tayla1accept1.wav"),
				("Tayla","Good, but you don't get paid until you finish."),
				("Burrows","Suits me, so long as you tell me about the artifact now."),
				("Tayla","After you're done. Now listen, the first mission is easy. Your cargo will be a legal load of plastics. Although your manifest will say you're running it to Newcastle, you'll deviate from your course along the way and deliver it to Oakham, a hidden pirate base where I have connections. While you work for me, the pirates will leave you alone. Count on it. Leave your ship unattended and I'll meet you there in the bar."),
				("Burrows","Just be sure no one kills you while I'm gone, Tayla. I've got an investment in you... and I mean to collect.")],
		"accept2":[("Burrows","Sure. Why not? I could use the credits.", "barspeech/campaign/tayla1accept2.wav")],
		"reminder":[("Tayla","Hey, I just spoke with my contact on Oakham. They told me you still haven't delivered the cargo!", "barspeech/campaign/tayla1reminder.wav"),
					("Burrows","Something came up, sweetheart. You know how it is."),
					("Tayla","Sure do. Unless you transport that load of plastic to Oakham , deviating from your flight path to Newcastle to throw off pursuit , you can forget about the 10000 credits!"),
					("Burrows","Okay, okay, no need to panic. I'll get to it. And why should I worry about being followed if my cargo's legit?"),
					("Tayla","Consider it a competency test. You know the rest...?"),
					("Burrows","Yeah. Once I arrive, I should leave my ship unattended, right?"),
					("Tayla","If you want to make a profit, yeah. And don't go shooting up any pirates there! You work for me, so they'll leave you alone... unless you get trigger-happy. Meet me in the bar at Oakham when you're done. And step on it!")],
		"failure":taylafailure
		}
tayla2={
	"intro":[("Tayla","What took you so long? Rough day at the office?", "barspeech/campaign/tayla2intro.wav"),
			("Burrows","Business before banter, Tayla. The money."),
			("Tayla","Relax. The first instalment is right here."),
			("Burrows","That's better. Now tell me about the artifact. Why would Sandoval just hand it over if it's so valuable?"),
			("Tayla","Maybe he got a sore neck from watching his back all the time. How's your neck feeling? Getting sore yet?"),
			("Burrows","No... but I don't intend to let you get behind me, Tayla."),
			("Tayla","Wrong, ace. I've never whacked anyone for profit. Now, your next job is to run a load of Brilliance to Hector mining base in Troy. The run pays 15000 credits, too much for such an easy job, if you ask me.")],
	"reject1":[("Burrows","You're pulling my chain. I'll learn about the artifact on my own.", "barspeech/campaign/tayla2reject1.wav"),
			("Tayla","You'd better reconsider, Captain. You'll need all the help you can get. Someone knows what that artifact is. And if it was worth killing Sandoval, then killing you will be no more to them than... overhead.")],
	"reconsider":[("Tayla","So... you want the mission after all?", "barspeech/campaign/tayla2reconsider.wav"),
				("Burrows","Let's just say I'm reassessing my options."),
				("Tayla","Smart move. You're taking a load of Brilliance to Hector mining base in Troy. Just hit Hector, leave your ship docked, and meet me back here in the bar when you're done. I'll pay you 15000 credits for the mission... and tell you a little more about your treasure. How about it?")],
	"reject2":[("Tayla","If you don't want the job, just leave me alone!", "barspeech/campaign/tayla2reject2.wav")],
	"accept":[("Burrows","I'll take your word for it. What kind of opposition am I looking at?", "barspeech/campaign/tayla2accept1.wav"),
			("Tayla","Minimal. Maybe a few militia patrols, nothing you can't handle."),
			("Burrows","Yeah? And what about all these pirates? What if they get greedy?"),
			("Tayla","While you work for me, no one'll hassle you. If you make it back, meet me back here in the bar for your pay."),
			("Burrows","When I get back, Tayla, you better have some answers.")],
	"accept2":[("Burrows","Sure. Why not? I could use the credits.", "barspeech/campaign/tayla2accept2.wav")],
	"reminder":[("Tayla","You haven't flown the mission yet? What's the problem?", "barspeech/campaign/tayla2reminder.wav"),
				("Burrows","I'm waiting for the mood to hit me."),
				("Tayla","Unless you fly that load of Brilliance to Hector mining base in Troy quick, the only thing that's gonna hit you is hard times."),
				("Burrows","You need to chill, Tayla. I know the routine. I hit Hector, leave the ship docked, let your goons go over it and remove what law enforcement officials refer to as the evidence. Then I head back here and link up with you in the bar to get my 15000."),
				("Tayla","Just make sure you complete the delivery. Soon.")],#militia hit
	"failure":taylafailure
	}
tayla3={"intro":[("Tayla","You took your sweet time, Captain.", "barspeech/campaign/tayla3intro.wav"),
		("Burrows","Better late than never. Now I want my money... and info on the artifact."),
		("Tayla","I won't say anything that will tip my hand prematurely... but I can tell you that Sandoval got it by killing its previous owner. Before that a spice merchant named Deiter obtained it from his own father. Death follows this thing. Feel lucky?"),
		("Burrows","Just give me my next mission, and let me worry about my health."),
		("Tayla","I'll pay you 20000 credits to make another delivery of Brilliance. I'm putting you on my main supply route to New Constantinople."),
		("Burrows","A promotion, huh? And what'll I be up against?"),
		("Tayla","Some Confed patrols, but I've paid some major bribes to make sure you're left alone."),
		("Burrows","Major bribes, huh? Great. I smell a major risk here."),
		("Tayla","You're taking a bigger risk keeping that artifact with so many willing to kill for it."),
		("Burrows","I'm taking a risk trusting you in the first place."),
		("Tayla","I've always paid you on time, so quit whining. Are you gonna fly my mission... or not?")],
		"accept":[("Burrows","I made an agreement with you and I'll honour it.", "barspeech/campaign/tayla3accept1.wav"),
		("Tayla","Good. You'll transfer the cargo from here to New Constantinople. Once you arrive, leave your ship unattended for an hour..."),
		("Burrows","...then get out. I know the drill, Tayla."),
		("Tayla","A hotshot pilot with brains. Wonders never cease. Hurry back. I'll be waiting right here with your pay.")],
	"accept2":[("Burrows","Sure.", "barspeech/campaign/tayla3accept2.wav")],
		"reject1":[("Burrows","Wealth sounds great, but I tell you what, sweetheart... I'm going to find it on my own. Later.", "barspeech/campaign/tayla3reject1.wav"),
			( "Tayla", "Stay alive without my help... if you can.")],
		"reject2":[("Tayla","If you don't want the job, just leave me alone!", "barspeech/campaign/tayla3reject2.wav")],
		"reconsider":[("Tayla","Hey, I really hope you've changed your mind about flying this mission. I need someone good to fly some Brilliance to New Constantinople, taking over my standard supply run from someone who... didn't work out. I'll pay you 20000 credits to make the run, dock and leave the ship unattended...", "barspeech/campaign/tayla3reconsider.wav"),
			("Burrows","...and meet you back here for my pay, along with some information, right?"),
			("Tayla","Yeah. I've spread a few bribes around InSys to pave your way... though if you hit some Confed patrols, watch out. So how about it?")],
		"reminder":[("Tayla","Please, tell me you've completed the delivery to New Constantinople.", "barspeech/campaign/tayla3reminder.wav"),
			("Burrows","Not yet. What's the hurry?"),
			("Tayla","Time is money. How much is how soon, get it?"),
			("Burrows","Got it. I'll be heading in there soon. Whether or not I get out depends on how substantial your bribes were. That's one heavily patrolled sector!"),
			("Tayla","I told you, InSys has been taken care of. Just run the Brilliance from here to New Constantinople... dock there, leave your ship, take a stroll... and then meet me here in Oakham for your 20000."),
			("Burrows","And more information on the artifact, Tayla. I'll uphold my end of the bargain. Make sure you do the same.")],
		"failure":taylafailure}
tayla4={"intro":[("Tayla","You look like Hell.", "barspeech/campaign/tayla4intro.wav"),
		("Burrows","Now I know what happens to charm school dropouts. Where's my money?"),
		("Tayla","Keep your shorts dry, will you? Here, take it."),
		("Burrows","I can't understand why a woman as attractive as you has to pay for the company of men in bars."),
		("Tayla","I see it as an investment... with a penalty for early withdrawal."),
		("Burrows","Well, since you're so quick with the answers, here's another question. If you know the artifact's value, why don't you want it for yourself?"),
		("Tayla","You'll have to kill a lot of people to hang onto it. And I'm no murderer. Anyway, I'll tell you all I know about that thing after you finish this last job."),
		("Burrows","Let me guess... I'm running a shipment of catnip to Kilrah."),
		("Tayla","Nope, I save the really lucrative jobs for myself. Actually you're running more Brilliance to New Constantinople. It pays 10000 credits."),
		("Burrows","To Hell with that! Those Confeds were all over me!"),
		("Tayla","Well, I've got an idea which will help prevent that this time out. But I'm sick of holding your hand while you whine. You want the job or not?")],
		"accept":[("Burrows","Okay, what's this great idea of yours?", "barspeech/campaign/tayla4accept1.wav"),
		("Tayla","I've gone over the schematics of your ship. I've located a space where we can install a secret compartment. It'll be completely undetectable and make smuggling much easier."),
		("Burrows","I'll believe it when I see it."),
		("Tayla","Just make the damned run. I promise you won't have any problems."),
		("Burrows","Famous last words."),
		("Tayla","Just handle your end, and report back here for your pay."),
		("Burrows","You never have to worry about that, Tayla.")],
		"reject1":[("Burrows","Sorry, Tayla. I got a feeling my luck is running thin. I'm out.", "barspeech/campaign/tayla4reject1.wav"),
		("Tayla","Are you kidding? You've almost completed your part of the deal! You back out now, and we're both screwed!")],
		"reject2":[("Burrows","No deal, Tayla, I'm out!", "barspeech/campaign/tayla4reject2.wav")],
		"reconsider":[("Burrows","Tell me a little bit more about this mission you're offering.", "barspeech/campaign/tayla4reconsider.wav"),
			("Tayla","We'll install a secret compartment in your vessel and pay you 10000 credits... if you'll run some Brilliance from here to New Constantinople. You know the routine by now, right?"),
			("Burrows","Yeah. Dock, leave the ship, meet you back here and try not to get vaporised. What could be easier?"),
			("Tayla","Exactly. So... is it a deal?")],
	"reminder":[("Tayla","I can't believe you haven't made the drop yet. You think I had that secret compartment installed in your ship just for kicks? Get on the ball, will you? I've had enough of your waffling!", "barspeech/campaign/tayla4reminder.wav"),
			("Burrows","Easy, Tayla. I'll run your drugs to New Constantinople pretty soon... I just hope that compartment is all it's cracked up to be."),
			("Tayla","Just make the run and come back here for your 10000. Is that so tough?"),
			("Burrows","Believe me, with all the patrols in that sector, it's not the docking so much as the ducking...")],
	"accept2":[("Burrows","Great! I'll have your ship modified and loaded right away. Good Luck!", "barspeech/campaign/tayla4accept2.wav")],
		"failure":taylafailure #Riordian attacks!
		}
tayla_final=[("Tayla","Here's your final payment, 10000 credits.", "barspeech/campaign/taylafinal.wav"),
("Burrows","Thanks, Tayla. That secret compartment made it easy."),
("Tayla","Glad to hear it. This is our final meeting, Captain."),
("Burrows","Hold on a minute. You still owe me info on that artifact."),
("Tayla","The person you need to talk to is Roman Lynch."),
("Burrows","You mean the mob boss on New Constantinople?"),
("Tayla","He may be a thug, but he's also an expert on exotic and valuable items. I set up a meeting with Lynch. He's expecting you in the bar on New Constantinople. I really don't know any more about that thing than I've already told you... but play your cards right with Lynch, you'll be a rich man.")]

lynchfailure=[("Burrows","Sorry I haven't been coming up with the goods, but I'll do better next time.", "barspeech/campaign/lynchfailure.wav"),
("Lynch","Regrettably, there shall be no next time. Your services are no longer required. Good day to you."),
("Burrows","What! You're cutting me off just because of one mess up? We had a deal! You owe me information on that artifact!"),
("Lynch","That deal was not based upon failure."),
("Miggs","Want me to explain it to him, Mr Lynch?"),
("Lynch","No, Miggs. He is incompetent, not stupid. Good day to you... and trouble me no more!")]

lynch1={"intro":[("Lynch","Ah, Captain. I've been expecting you. I am Roman Lynch.", "barspeech/campaign/lynch1intro.wav"),
		("Burrows","Mr Lynch, as you know, what we have to discuss is... confidential."),
		("Lynch","Oh, you may speak freely around my assistant Miggs. He is exceedingly loyal."),
		("Burrows","Okay. As Tayla probably told you, I need information on an artifact , what it is, its history and, most of all, its value."),
		("Lynch","Of course. I have examined the holo your associate Tayla provided me. I believe I could shed some light on this mystery... given the right motivation. For example, there is a certain pilot who has caused me much professional embarrassment. Could you take care of him for me, Captain?"),
		("Burrows","Ha! You must be joking. I'm no assassin."),
		("Miggs","You want I should take you outside the airlock and teach you how to suck vacuum?"),
		("Lynch","Gentlemen, please, let us remain professional. I only want you to find the man and deliver a personal message for me. Simply tell him how profoundly displeased and... disappointed I am with him. Do this, and I will pay you 10000 credits, as well as investigate this artifact of yours. Agreed?")],
		"accept":[("Burrows","Okay, what's this pilot's name?"),
		("Lynch","You'll find Captain Seelig in the Pentonville system. His ship is the Hooded Hawk. See that he gets my message.", "barspeech/campaign/lynch1accept1.wav"),
		("Burrows","And what about the artifact, Mr Lynch?"),
		("Lynch","Naturally I'll need to borrow it, so my experts can appraise it."),
		("Burrows","Naturally, you'll excuse me while I laugh. Now that we've had our fun, will a hologram do?"),
		("Lynch","It will not. The analysis will take longer, and be less thorough."),
		("Burrows","But I'm sure you'll do your best for someone you owe a favour."),
		("Lynch","Very well. This is my place. Come here when you're done for your pay.")],
		"reject1":[("Burrows","This sounds like an internal problem. Get one of your own people to do it.", "barspeech/campaign/lynch1reject1.wav"),
			("Lynch","I go to great lengths for my friends, Captain. But I am not a charity. If you wish to learn about this artifact, you'll have to talk to me... sooner or later.")],
		"reconsider":[("Lynch","Well, if it isn't our pilot. Have you reconsidered?", "barspeech/campaign/lynch1reconsider.wav"),
			("Burrows","I'm waiting to be convinced."),
			("Lynch","Your services are not indispensable to me... however, I'll humour you this time. I want you to fly to the Pentonville system. There you will locate a man named Seelig, captain of the Hooded Hawk. I wish you to tell him how profoundly... disappointed I am in him. For that service I will pay you 10000 credits, and provide you with information regarding the object once you return here. So... either accept my deal, or stop wasting my time.")],
		"reject2":[("Burrows","I still think you need to handle this one yourself, Mr Lynch.", "barspeech/campaign/lynch1reject2.wav")],
		"reminder":[("Lynch","Ah. How did Captain Seelig react to my chastisement?", "barspeech/campaign/lynch1reminder.wav"),
		("Burrows","Actually, I haven't taken him the message yet."),
		("Lynch","Indeed? I must admit, I'm surprised. I suppose you're not as curious regarding the artifact as I had thought."),
		("Burrows","You suppose wrong. I just got... delayed. Trust me... I'll scour the nav points in the Pentonville system, find the Hooded Hawk, and tell Captain Seelig just how disappointed you are with him."),
		("Lynch","I hope so. Unless you succeed, I fear I'll be quite incapable of helping you."),
		("Burrows","Or quite unwilling."),
		("Lynch","Either way, neither of us profits. Remember that.")],
		"accept2":[("Lynch","Be on your way then, Captian. Miggs and I await your... speedy return.", "barspeech/campaign/lynch1accept2.wav" )],
		"failure":lynchfailure
		}
lynch2={"intro":[("Lynch","Did you deliver my message to Captain Seelig?", "barspeech/campaign/lynch2intro.wav"),
		("Burrows","Yes. He attacked me."),
		("Lynch","Alas, who would've thought Captain Seelig would react in such paranoid fashion?"),
		("Burrows","I have a feeling that's just what you wanted. I don't like being manipulated, Lynch!"),
		("Lynch","Perhaps this payment, along with some information, will smooth your furrowed brow. Thus far, our search of records and databases has turned up nothing. On numerous worlds my people have been harassed, arrested, interrogated... all for asking questions about your artifact. Granting you this favour is costing me rather dearly. You will therefore need to make another effort to keep our relationship a happy one."),
		("Burrows","Another chump job, Lynch?"),
		("Miggs","Ever seen your lungs? Keep crackin' wise, I'll show them to ya... up-close, like."),
		("Burrows","Jeez, where do you get your dialogue, Thugs-R-Us?"),
		("Lynch","Enough, Miggs. Pilot, I need you to make a very important delivery. It will further finance the study of your artifact. I'll also pay you 15000 credits. Interested?")],
		"accept":[("Lynch","Good. I need you to rush a weapons shipment to planet Siva in Rikel system. It's already late. Merely dock, and my people will unload your ship. Leave immediately thereafter, and return here for your payment.", "barspeech/campaign/lynch2accept1.wav"),
		("Burrows","Do you have the weapons here?"),
		("Lynch","Of course not. I don't soil my hands with such... incriminating details. You will find them already loaded on your ship. Also, I must caution you regarding one... potential danger. One of my less scrupulous competitors, Salman Kroiz, may be out to stop the shipment. But I have every confidence that you will handle him... appropriately.")],
	"accept2":[("Lynch","I will load the weapons into your ship immediately. This is an urgent mission, please expedite.", "barspeech/campaign/lynch2accept2.wav")],
		"reject1":[("Burrows","You've told me nothing so far, Lynch. I'll take my search elsewhere.", "barspeech/campaign/lynch2reject1.wav"),
			("Lynch","You'll find it severely impeded. I have a monopoly on this sort of information. Especially since we both know you can't go to the authorities with this. Mark my words... you'll be back.")],
		"reconsider":[("Lynch","I do hope you've returned to accept the mission. Really, you should, you know. All you need do is transport my load of weapons to the Siva agricultural planet in Rikel. Afterwards, return here and I'll pay you 15000 credits. Interested?", "barspeech/campaign/lynch2reconsider.wav")],
		"reject2":[("Burrows","You still haven't told me anything, Lynch. I'll get my information elsewhere.", "barspeech/campaign/lynch2reject2.wav"),
			("Lynch","You may again mark my words... If you want information on the artifact... you'll be back.")],
		"reminder":[("Lynch","I understand from my contacts on Siva that you've not delivered those weapons yet. I did inform you that it was late already. What's the delay?", "barspeech/campaign/lynch2reminder.wav"),
			("Burrows","I do have other business to attend to, Lynch."),
			("Miggs","Other business? You want I should help him priority-wise, Mr Lynch?"),
			("Lynch","Not now, Miggs. Pilot, when you fly for me, mine is the only business that matters. However, I'll overlook this if you move immediately. Deliver the weapons to the agricultural planet Siva in Rikel. Afterwards, return here for your payment of 15000 credits."),
			("Burrows","Fine... but I'll want info on the artifact when I get back, Lynch."),
			("Lynch","Rest assured, you will have it.")],
		"failure":lynchfailure
		}
lynch3={"intro":[("Lynch","I understand you thwarted Mr Kroiz. Well done. Here's your payment and, as agreed, some additional information. Your find is of alien origin and, as such, virtually priceless. Which also means the Confederation will want to keep it from private hands. To keep your possession of it secret, I've incurred additional expenses...", "barspeech/campaign/lynch3intro.wav"),
		("Burrows","You want another favour, right?"),
		("Miggs","Mr Lynch did you a favour, pal. Better get grateful quick-like... while you can still walk."),
		("Burrows","I could always get crutches, Miggs... but there's no cure for ugliness."),
		("Lynch","I urge you to observe caution with Miggs. My control over him extends only so far. Actually, my request is personal. I'll pay you 30000 credits to take someone off world. Do this, and I'll continue to procure the information you seek.")],
		"accept":[("Burrows","Doesn't sound like much to ask. What's the catch?", "barspeech/campaign/lynch3accept1.wav"),
		("Lynch","My cousin Regis and I share certain business interests. Sadly, he's been subpoenaed in a murder trial. It would be best if he disappeared."),
		("Burrows","Uh-huh. Is he a witness... or a suspect?"),
		("Lynch","He is my cousin, which is enough for you. Regis enjoys spending time on the Romulus mining base in Castor system. I suggest you get him out of New Constantinople and take him there. After you've dropped Regis off, return here for your pay... and more information.")],
	"accept2":[("Lynch","Upon returning to your ship you will find Regis already aboard. After you've dropped Regis off, return here for your pay.", "barspeech/campaign/lynch3accept2.wav")],
		"reject1":[("Burrows","Sorry, Lynch, but we had a deal. I've lived up to it. You haven't.", "barspeech/campaign/lynch3reject1.wav"),
		("Lynch","I wouldn't be exaggerating if I said your artifact is worth millions of credits... credits you'll never see without my help.")],
		"reconsider":[("Lynch","Do us both a favour and accept this mission. My cousin Regis simply cannot appear at that murder trial. I wish him to disappear.", "barspeech/campaign/lynch3reconsider.wav"),
		("Burrows","I charge extra for magic tricks, Lynch."),
		("Lynch","Magic is not required, only guile and a certain amount of... discretion. I'll pay you 30000 credits to fly him to Romulus base in Castor system... 30000 payable once you return here. Agreed?")],
		"reject2":[("Burrows","Sorry, Lynch. I've got to follow up on some other leads.", "barspeech/campaign/lynch3reject2.wav")],
		"reminder":[("Lynch","My dear cousin Regis called. You have yet to deliver him to Romulus base in Castor. I did communicate the urgency of the mission, did I not?", "barspeech/campaign/lynch3reminder.wav"),
		("Burrows","Sure. He's the one facing the murder rap."),
		("Lynch","A subpoena in a murder trial. I'd advise you not to assume anything."),
		("Miggs","Yeah, it just makes an ass out of me."),
		("Burrows","If a little knowledge is a dangerous thing, Miggs has Kilrah licked. I'll get your cousin out of New Constantinople safely, Lynch. Just make sure you deliver the goods on the artifact when I return.")],
		"failure":lynchfailure
		}
lynch4={"intro":[("Lynch","I trust you took care of my dear cousin.", "barspeech/campaign/lynch4intro.wav"),
		("Burrows","InterSys was ready for us. But I got him to Romulus all right."),
		("Lynch","Excellent. Please accept this payment of 30000 credits, with my warmest thanks. But now, steel yourself for bad news. Smythe, a man in my employ, found vital information regarding the artifact at the Oxford Library. Unfortunately, Mr Smythe is currently trapped on a base in the Newcastle system. The authorities there, rife with corruption, have stopped me from... exerting my influence."),
		("Burrows","I see. What kind of information?"),
		("Lynch","Smythe has not communicated that, but I believe our best chance of identifying your find resides in the files at Oxford. Smythe has access to this information. I'll pay you 30000 credits to retrieve this man. It's in our mutual interest, after all. Deal?")],
		"accept":[("Lynch","Smythe is on Liverpool. A small refinery in the Newcastle system. He'll be waiting for you there, in the bar.", "barspeech/campaign/lynch4accept1.wav"),
		("Burrows","Look, why don't I just head for Oxford myself and locate the information?"),
		("Lynch","Smythe is a data retrieval expert. You'd never find what you need alone."),
		("Burrows","Okay, I'll get him... but I hate to run off without giving Miggs a kiss. Where is he?"),
		("Lynch","Miggs is currently eliminating a... labour difficulty. I'll convey your regards.")],
		"accept2":[("Lynch","Smythe is on Liverpool. A small refinery in the Newcastle system. He'll be waiting for you there, in the bar.", "barspeech/campaign/lynch4accept2.wav")],
		"reject1":[("Burrows","I think I've got enough out of you. Our business is done. I'm headed for Oxford to find the information I need.", "barspeech/campaign/lynch4reject1.wav"),
			("Lynch","Smythe is an information retrieval expert. You'll never find what you need alone... but I suppose you'll need to learn that the hard way. You'll be back.")],
		"reconsider":[("Burrows","I've been thinking... maybe you're right. Your man Smythe uncovered something important at Oxford... something it might take me months to locate on my own.", "barspeech/campaign/lynch4reminder.wav"),
			("Lynch","An optimistic estimate, I'm afraid. The Oxford stacks are voluminous. We'll both be better off if you rescue Smythe. I'm offering 30000 credits for his return here, payable on delivery. Interested?")],
		"reject2":[("Burrows","No thanks, I'm headed for Oxford to find the information myself.", "barspeech/campaign/lynch4reject2.wav"),
			("Lynch","You'll be back, Captain, you'll be back.")],
		"reminder":[("Lynch","I am truly dismayed at your haphazard attitude regarding our business. Unless you retrieve Smythe from the Newcastle system... our mutual search for information on the artifact is stymied.", "barspeech/campaign/lynch4reminder.wav"),
			("Burrows","We know he uncovered something at the Oxford library. Why not go there?"),
			("Lynch","Wasteful duplication of effort. Smythe knows what we want to know. Better to retrieve him than to attempt to duplicate his research."),
			("Burrows","Okay, Lynch. I'll get him off... Liverpool, was it?"),
			("Lynch","Yes, in Newcastle. And I would advise you to hurry. Return here afterwards with Smythe for your payment of 30000 credits.")],
		"failure":lynchfailure
		}
mastersonfailure=[("Burrows","So what's next? Evicting bookworms? Repossessing delinquent library cards?", "barspeech/campaign/mastersonfailure.wav"),
		("Masterson","How about retirement?"),
		("Burrows","What do you mean?"),
		("Masterson","Our deal is null and void. You failed a task I gave you. That's not the way to earn access to the Oxford Library, sir."),
		("Burrows","Look, I need that access. Just give me another chance."),
		("Masterson","Impossible, I'm afraid. Now kindly leave... or I'll have security assist you out.")] 

masterson1={"intro":[("Masterson","I'm sorry, but library use is restricted to students and teachers only. ", "barspeech/campaign/masterson1intro.wav"),
			("Burrows","Yeah? What makes you think I'm not enrolled at Oxford?"),
			("Masterson","Students don't generally conduct research while armed."),
			("Burrows","Okay, you got me there. I'm a privateer."),
			("Masterson","Sorry, access exceptions are only made for endowment sponsors."),
			("Burrows","Then how would I go about doing that? Making an endowment?"),
			("Masterson","If you have to ask, you can't afford it."),
			("Burrows","Okay, maybe we could work a trade. I could fly for the University... say, four runs at a reduced rate in exchange for access to your files, Mr...?"),
			("Masterson","...Masterson. Yes, your offer might substitute for an endowment... You could start with an escort mission which pays 10000 credits.")],
			"accept":[("Masterson","Good, now listen. We need you to escort someone to Oxford. You will find him in the Oxford system, in the vicinity of Nav 3. The man you are to escort here is named Hunter Toth.", "barspeech/campaign/masterson1accept1.wav"),
			("Burrows","Hunter Toth? He wrote that book, what was it...?"),
			("Masterson","Prometheus Unplugged. The Church of Man has marked him for death because of it. He's scheduled to give a commencement speech here... and he's already cashed the chit. Unfortunately, the Church of Man has vowed he will never reach Oxford."),
			("Burrows","That's one vow those freaks will have to break. I'll bring him. Count on it.")],
	"accept2":[("Masterson","Good, time is of the essence; Toth is in grave danger.", "barspeech/campaign/masterson1accept2.wav"),
			("Burrows","This Hunter Toth, he wrote that book, what was it...?"),
			("Masterson","Prometheus Unplugged. The Church of Man has marked him for death because of it. Unfortunately, the Church of Man has vowed he will never reach Oxford."),
			("Burrows","That's one vow those freaks will have to break. I'll bring him. Count on it.")],
			"reject1":[("Burrows","Forget it. What do I look like, a charity?", "barspeech/campaign/masterson1reject1.wav"),
			("Masterson","You're the one who brought this matter up. If you're not interested in working for Oxford, then don't waste my time.")],
			"reconsider":[("Masterson","Back again, eh? You must need library access rather badly.", "barspeech/campaign/masterson1reconsider.wav"),
			("Burrows","Let's just say I'm reconsidering. What are the mission details?"),
			("Masterson","Oxford will pay you 10000 credits to escort Hunter Toth here. Toth has agreed to deliver the commencement speech this year. You'll link up with him at Oxford system, Nav 3... and protect him from Church of Man fanatics who want to kill him. Return here for your payment and next mission. Have we got a deal?")],
			"reject2":[("Burrows","No thanks, I'm still not a charity worker.", "barspeech/campaign/masterson1reject2.wav"),
			("Masterson","The University cannot afford to pay more. If you're not interested in working for Oxford, then quit wasting my time.")],
			"reminder":[("Masterson","Where's Hunter Toth?", "barspeech/campaign/masterson1reminder.wav"),
			("Burrows","Still hanging around Nav 3 of the Oxford system, I guess. I haven't flown the mission yet."),
			("Masterson","Maybe I didn't make myself clear. Time is of the essence! Toth is scheduled to deliver the Oxford commencement speech in just a few days! You'll meet him at Nav 3 in the Oxford system... and escort him here, protecting him from Church of Man fanatics who want him dead."),
			("Burrows","All right, all right. I'll bring him in alive... or die trying."),
			("Masterson","Oh, that's a big comfort.")],
			"failure":mastersonfailure
			}
masterson2={"intro":[("Masterson","I and the Oxford Graduating Class thank you for delivering Mr Toth unharmed.", "barspeech/campaign/masterson2intro.wav"),
			("Burrows","Think of it as a tribute to free speech. What's your second mission?"),
			("Masterson","Some low-level data pirates have been troubling us. We would like you to intercept them, and end their activities. This mission pays 10000 credits upon completion. Can you do it?")],
			"accept":[("Burrows","Sounds easy enough. Where can I find these hackers?", "barspeech/campaign/masterson2accept1.wav"),
			("Masterson","They operate a ship that hides somewhere in the Oxford system. From their vessel they somehow tap into our database remotely. No one knows how. Information is copied from the Library and then our memory is deleted. Afterwards, they try to sell our own information back to us! More often than not, we lose it anyway. It goes to the highest bidder. We simply cannot afford to outbid the private sector."),
			("Burrows","Yeah, I can tell how strapped Oxford is for capital, ever since you started letting smugglers like me make endowments. Any other leads? That's not much to go on."),
			("Masterson","Only one. The name of the ship is The Black Rhombus. Return here for your payment and third assignment. Good luck, privateer.")],
	"accept2":[("Burrows","Excellent. I will have your third assignment ready for you when you return.", "barspeech/campaign/masterson2accept2.wav")],
			"reject1":[("Burrows","Forget it. I'm already tired of this deal, Mr Masterson.", "barspeech/campaign/masterson2reject1.wav"),
			("Masterson","I see. A pity you'll never discover whatever you came here to learn... Ah well. Higher education isn't for everyone.")],
			"reconsider":[("Masterson","Back so soon? Data pirates are tapping into the Oxford database, stealing information and then deleting it from our files! They operate out of a vessel called The Black Rhombus currently located somewhere in the Oxford system. Return here for your fee of 10000 credits after you've ended their piracy. Do we have a deal?", "barspeech/campaign/masterson2reconsider.wav")],
			"reject2":[("Burrows","Sorry. I've had enough higher education.", "barspeech/campaign/masterson2reject2.wav")],
			"reminder":[("Masterson","Were you able to locate the database pirates?", "barspeech/campaign/masterson2reminder.wav"),
			("Burrows","I haven't got around to looking for them just yet..."),
			("Masterson","What are you waiting for? They're stealing information from our library and then deleting it from our banks! If you want access to our files , those that are intact , you'd better get moving!"),
			("Burrows","Okay, don't blow your stack..."),
			("Masterson","The pirates are doing a good job of that already! Now, they're on a ship called The Black Rhombus. Don't come back for your 10000 credits until they're taken care of!")],
			"failure":mastersonfailure
			}

masterson3={"intro":[("Burrows","Okay, Masterson. Those pirates won't be hassling you again.", "barspeech/campaign/masterson3intro.wav"),
			("Masterson","That will be a welcome change. How did you manage...?"),
			("Burrows","Right now I'm more interested in getting into your stacks... nothing personal."),
			("Masterson","Perhaps if you told me what you're looking for I could find it for you. The fee for research is much lower than that required for private access."),
			("Burrows","I don't think so. This is private business."),
			("Masterson","Might there be a large sum of money involved?"),
			("Burrows","Might you be looking for disability payments?"),
			("Masterson","Really, you needn't be threatened that I've discovered your intent. People are always coming here to research one treasure or another. But enough of this. We have a shipment of rare and valuable books en route here. The ship bringing them in needs an escort. We'll pay you the usual 10000 credits upon your return...")],
			"accept":[("Burrows","Okay, where can I intercept the courier?", "barspeech/campaign/masterson3accept1.wav"),
			("Masterson","Vulcan's Forge is awaiting her escort at Nav 3 in the Oxford system."),
			("Burrows","Any particular reason it needs an escort?"),
			("Masterson","Several unscrupulous collectors have offered a... finder's fee for the books."),
			("Burrows","Don't worry. I'll bring them in... safe and sound.")],
	"accept2":[("Burrows","Don't worry, I'll bring them in. Safe and sound.", "barspeech/campaign/masterson3accept2.wav")],
			"reject1":[("Burrows","Sorry, pal. Books aren't exactly my speed.", "barspeech/campaign/masterson3reject1.wav"),
			("Masterson","No doubt. Still, this is the largest repository of information in the sector. You'll be back, sooner or later...")],
			"reconsider":[("Masterson","I hope you've changed your mind. I'm against the wall, so to speak. I need someone to escort Vulcan's Forge to Oxford. She's carrying a load of rare books here, books many collectors would kill to have. Vulcan's Forge is awaiting her escort at Nav 3, Oxford system. Rendezvous with her and bring her back here. After your successful return, meet me here for your usual payment of 10000 credits. This mission will count as your third instalment toward your endowment to Oxford, which will get you access to our files... sooner or later.", "barspeech/campaign/masterson3reconsider.wav"),
			("Burrows","Better make that sooner, Masterson."),
			("Masterson","That depends on you. Are you in?")],
			"reject2":[("Burrows","No, I'm out. Books aren't for me. I'll see you later, Masterson.", "barspeech/campaign/masterson3reject2.wav"),
			("Masterson","I'm sure you will.")],
			"reminder":[("Masterson","So... where are my books?", "barspeech/campaign/masterson3reminder.wav"),
			("Burrows","Sorry Masterson, I haven't been in the neighbourhood of Nav 3, Oxford lately."),
			("Masterson","Unbelievable! Vulcan's Forge has a cargo-hold full of priceless books... she's a sitting duck waiting for you to escort her here, and you're wasting time! If you want library access, you'd better do your job and return here with good news... unless you're no longer interested in that 10000."),
			("Burrows","Point taken. I'll get to Nav 3 ASAP... and I promise you, none of those book collectors will get to her."),
			("Masterson","They'd better not! Any one of those books is worth more than you make in a year!"),
			("Burrows","Give me the library clearance I need, and we'll see about that...")],
			"failure":mastersonfailure}
masterson_extraspeech=""
masterson4={"intro":[("Masterson","I don't have time to swap pleasantries. Here's your payment of 10000 credits for the last mission. We have an incoming freighter laden with materials about to be attacked by several fighters. Valuables as well as vital supplies are aboard. You'll probably find it somewhere near Nav 1, Oxford system. Rendezvous with the freighter and bring it back safely... and return here for library access, along with a final payment of 10000 credits.", "barspeech/campaign/masterson4intro.wav"),
			("Burrows","How long before they strike?"),
			("Masterson","They could arrive at any moment. Please, will you help?")],
			"accept":[("Burrows","Okay, I'll save your freighter. But I'd better get full access to the library... Hell, you'd better name an entire wing after me!", "barspeech/campaign/masterson4accept1.wav"),
			("Masterson","Stop stalling and save that freighter!"),
			("Burrows","Touchy, touchy...")],
	"accept2":[("Burrows","Okay, I'll save your freighter. But I'd better get full access to the library... heck, you better name an entire wing after me!", "barspeech/campaign/masterson4accept2.wav"),
			("Masterson","Stop stalling and save that freighter!"),
			("Burrows","Touchy, touchy...")],
			"reject1":[("Burrows","Shove it, pal. Consider this payback for all the flak you've given me.", "barspeech/campaign/masterson4reject1.wav"),
			("Masterson","Unless you take this mission, consider our agreement terminated. Whatever your angle is, you might as well forget about it paying off.")],
			"reconsider":[("Masterson","Look, our freighter is about to be attacked, and I don't have time to waste with you. That freighter is carrying vital supplies, and we can't afford to lose it. It's at Nav 1, Oxford. I told you, if you want 10000 credits and access to our files, you need to defend it! Your endowment will be complete as soon as you return here successfully. Will you help us, or not?", "barspeech/campaign/masterson4reconsider.wav")],
			"reject2":[("Burrows","Forget it, Masterson. This mission looks like a suicide run. I need the information, but it's only useful to me if I'm around to enjoy it.", "barspeech/campaign/masterson4reject2.wav")],
			"reminder":[("Masterson","Of all the... what are you doing here? Our freighter is being attacked even now! Unless you hurry up, vital supplies will be lost!", "barspeech/campaign/masterson4reminder.wav"),
			("Burrows","Well, I..."),
			("Masterson","What are you standing there for? Get to Nav 1 and protect our freighter... or kiss your precious access good-bye. NOW MOVE!")],
			"failure":mastersonfailure}
mastersonhelp=[("Masterson","The freighter is safe, thanks to you."),
			("Burrows","Skip the hearts and flowers. My library access...?"),
		("Masterson","Everything has been arranged. And here's your final payment of 10000 credits. Good luck with that personal business. I hope you find what you're looking for.")] 
monkhouseintro=[("Burrows","Dr Monkhouse, I presume.", "barspeech/campaign/monkhouse1intro.wav"),
		("Monkhouse","Yes, you do, greatly. I wish to be alone."),
		("Burrows","Sorry, Doc, but I didn't run the blockade just to be treated like a vacuum salesman. I need a favour. I understand you're an expert on alien... antiquities."),
		("Monkhouse","That I am, but my consulting price is currently transportation off this rock."),
		("Burrows","Say no more, climb into my ship and we're out of here."),
		("Monkhouse","Heavens no! Not while the blockade is in effect! I shall sit tight until that unfortunate situation is ended. Should you wish to facilitate that circumstance, head for Basra. From what I understand, the resistance is centred there."),
		("Burrows","Basra, huh? All right... I'll look into it."),
		("Monkhouse","You do that. I'll be right here, waiting.")]

murphyfailure=[("Burrows","What's the matter, Murphy? You look more sour than usual.", "barspeech/campaign/murphyfailure.wav"),
		("Murphy","You want it straight? Well here it is. I don't think much of your flying. You're sloppy. You fail to realise mission objectives. We can't afford to waste time with you. You're washed up here. Collect your things and pull out."),
		("Burrows","But we have the same goal. I have to get down to Palan."),
		("Murphy","Then you'll have to do it alone. Good-bye.")]
murphy1={"intro":[("Murphy","You here to sign up?", "barspeech/campaign/murphy1intro.wav"),
		("Burrows","Sign up for what, Miss...?"),
		("Murphy","'Miss' nothing. The name's Lynn Murphy. I go by Murphy."),
		("Burrows","Fine, Murphy. Look, all I want is to get down to Palan. I'm looking for... an old friend, and I can't get through."),
		("Murphy","Join the club. You get to cool your heels with the rest of us on Basra awhile. Bronte Corporation has thrown up a blockade around Palan. Tough luck... but you could turn a nice profit, if you're smart. There's two corporations in the Palan system, Rondell and Bronte. Bronte is responsible for the blockade. They want to block Rondell food exports, while kicking up their own to fill the void, stealing Rondell's market share. I'm organising the resistance for Rondell from this base. Hired resistance."),
		("Burrows","My reasons for wanting to get down to Palan are personal."),
		("Murphy","Sure, but you'll never break the blockade alone. Smarten up, flyboy."),
		("Burrows","Flyboy? I'm a privateer!"),
		("Murphy","Privateer, is it? Why not sign on? The money's good. This next mission, an intercept operation, pays 15000 credits. Interested?")],
		"accept":[("Burrows","Hey, if I'm gonna bang up against that blockade, might as well get paid for it.", "barspeech/campaign/murphy1accept1.wav"),
		("Murphy","Good, I got a mission right now. We've traced several jumps in-system. They're merc ships, coming to reinforce the Bronte blockade. I want you to intercept them at Nav 1 of the Palan system and prevent them from joining the main group... by any means necessary."),
		("Burrows","Funny, you don't look like the type to use euphemisms."),
		("Murphy","Just trying to spare you, ace. You look like the squeamish type to me."),
		("Burrows","Yeah? Guess you've never seen a real man up close. I could arrange it, if you like."),
		("Murphy","Sure. If one comes by, let me know. Just stop those reinforcements, and meet me back here afterwards... without the cheap come-ons, got it?"),
		("Burrows","Murphy... you're all heart.")],
		"accept2":[("Burrows","Hey, if I'm gonna bang up against that blockade, might as well get paid for it.", "barspeech/campaign/murphy1accept2.wav"),
		("Murphy", "Prevent those mercs from joining the main group by any means necessary." ),
		("Burrows","Funny, you don't look like the type to use euphemisms."),
		("Murphy","Just trying to spare you, ace. You look like the squeamish type to me."),
		("Burrows","Yeah? Guess you've never seen a real man up close. I could arrange it, if you like."),
		("Murphy","Sure. If one comes by, let me know. Just stop those reinforcements, and meet me back here afterwards... without the cheap come-ons, got it?"),
		("Burrows","Murphy... you're all heart.")],
		"reject1":[("Burrows","I'm not looking to get involved in any corporate war. I'll take my chances with the blockade alone.", "barspeech/campaign/murphy1reject1.wav"),
		("Murphy","Your loss, ace, I got no time to argue with you. It's your funeral.")],
		"reconsider":[("Murphy","Back again? If you're here to bust my chops some more...", "barspeech/campaign/murphy1reconsider.wav"),
		("Burrows","Chill, Murphy. I'm thinking of signing on after all."),
		("Murphy","Yeah? Well, we could use an extra hand. Bronte has hired mercs to reinforce their blockade of Palan. The merc ships have jumped in-system, and are set to rendezvous with Bronte forces. We'll pay you 15000 credits to intercept them at Nav 1 of the Palan system and prevent them from joining the main group... preferably by blowing them to pieces. Afterwards, return here for your pay and another assignment. For the last time, are you interested or not?")],
		"reject2":[("Burrows","I guess I'll still take my chances with the blockade alone.", "barspeech/campaign/murphy1reject2.wav"),
		("Murphy","If you don't want my missions, then leave me alone, got it?")],
		"reminder":[("Murphy","Didn't I give you a mission to fly, Mister?", "barspeech/campaign/murphy1reminder.wav"),
		("Burrows","Yeah, but I had business to tend to..."),
		("Murphy","Stow it. This is important! If you want this blockade broken, and want to get paid, you better listen up! Merc ships have jumped in-system to reinforce the Bronte blockade of Palan. Unless you intercept them at Nav 1 of the Palan system and prevent them from joining the main group, this blockade won't end any time soon."),
		("Burrows","Okay, okay... I'm on my way.")],
		"failure":murphyfailure}
murphy2={"intro":[("Burrows","Scratch one set of reinforcements, Lynn.", "barspeech/campaign/murphy2intro.wav"),
		("Murphy","Make it Murphy. Only my close friends call me Lynn."),
		("Burrows","And how do I go about getting close to you?"),
		("Murphy","I'm a sucker for love letters... posted from Kilrah."),
		("Burrows","Jeez, you must have a lot of company."),
		("Murphy","No. And I like it that way. Now listen up. We've received a tip that a large scout patrol is approaching our base. They're probably just looking for the first reinforcement wing... but if they come across this base, they'll destroy it. We're not equipped to deal with an assault.")],
		"accept":[("Burrows","I can handle that patrol, no sweat. Where do I find them?", "barspeech/campaign/murphy2accept1.wav"),
		("Murphy","They're currently sweeping the Palan system. Intercept and eliminate the reinforcements at Nav 1... assuming you can."),
		("Burrows","Like I said, don't sweat it. I'll handle things on my end. It's your end I'm concerned with."),
		("Murphy","Again with the cheap come-ons? How about a fat lip, Mister?"),
		("Burrows","Lighten up. I only meant for you to have the money when I get back. I like you, Murphy, but you ain't keeping me up nights."),
		("Murphy","At last, we have something in common.")],
	"accept2":[("Burrows","I can handle that patrol, no sweat. Where do I find them?", "barspeech/campaign/murphy2accept2.wav"),
		("Murphy","They're currently sweeping the Palan system. Intercept and eliminate them at Nav 1... assuming you can."),
		("Burrows","Like I said, don't sweat it. I'll handle things on my end. It's your end I'm concerned with."),
		("Murphy","Again with the cheap come-ons? How about a fat lip, Mister?"),
		("Burrows","Lighten up. I only meant for you to have the money when I get back. I like you, Murphy, but you ain't keeping me up nights."),
		("Murphy","At last, we have something in common.")],
		"reject1":[("Burrows","No can do. The downside's too steep. I think I'd do better against this blockade on my own.", "barspeech/campaign/murphy2reject1.wav"),
		("Murphy","I think you're kidding yourself. You'll never get down to Palan without help... but that's not my problem. Good luck. You'll need it.")],
		"reconsider":[("Murphy","You want me to beg you to take the blasted mission? Forget it! A large scout patrol may be headed toward our base... but I'll never be desperate enough to plead with someone like you.", "barspeech/campaign/murphy2reconsider.wav"),
		("Burrows","C'mon, Murphy. Can't a guy have second thoughts? I've got to get down to Palan. Seems like if you get blown to atoms, it doesn't improve my chances."),
		("Murphy","Logic from a spacer? That's a first... but you're right. This base won't survive an assault, and we could use your help. We'll pay you 10000 credits to intercept that patrol. That's my final offer.")],
		"reject2":[("Burrows","Still no can do, Murphy. The downside's getting steeper by the minute.", "barspeech/campaign/murphy2reject2.wav"),
		("Murphy","Then buzz off. I got a blockade to break through.")],
		"reminder":[("Murphy","Well, you may talk a good game... but I can't say I'm impressed with your performance so far.", "barspeech/campaign/murphy2reminder.wav"),
		("Burrows","Performance? We haven't even got to the good night kiss yet."),
		("Murphy","If you spent as much time flying as you do making lousy jokes, you'd have flown the mission by now. What's the hold-up? Scared? Or are you enjoying the rec facilities here on scenic Basra too much to be bothered?"),
		("Burrows","No problem. I just got tied up."),
		("Murphy","Look, either head for Nav 1 and intercept that patrol headed for our base, or blow off the 10000 credits and quit wasting my time.")],
		"failure":murphyfailure}
murphy3={"intro":[("Murphy","I heard you waxed the patrol. Not too bad, Ace.", "barspeech/campaign/murphy3intro.wav"),
		("Burrows","That's the closest thing to a compliment you've ever given me. Getting sentimental in your golden years, Murphy?"),
		("Murphy","If I came on to you in my golden years it wouldn't be sentiment... it'd be senility. Now listen up. Our attacks on Bronte's reinforcements have finally weakened the blockade. They're running low on fuel, food, patience, you name it. It's time to make the big push and break the blockade. If you'll throw in, I can provide a force of two militia Talons for your wing. We'll pay you 15000 credits when you return here. You in?")],
		"accept":[("Burrows","I can't speak for everyone, but... I like kicking a guy when he's down.", "barspeech/campaign/murphy3accept1.wav"),
		("Murphy","Then you'll start right away, before more reinforcements jump in-system. This'll be a tough one. If you make it through, pick up your friend and return here for your pay."),
		("Burrows","You worried about my pay... or that I might leave without saying goodbye?"),
		("Murphy","Believe me, if you had left without saying hello I'd be delighted."),
		("Burrows","You're one tough broad, Murphy."),
		("Murphy","Why... that's the nicest thing you've ever said to me.")],
	"accept2":[("Burrows","I can't speak for everyone, but... I like kicking a guy when he's down.", "barspeech/campaign/murphy3accept1.wav"),
		("Murphy","Then you'll start right away, before more reinforcements jump in-system. This'll be a tough one. If you make it through, pick up your friend and return here for your pay."),
		("Burrows","You worried about my pay... or that I might leave without saying goodbye?"),
		("Murphy","Believe me, if you had left without saying hello I'd be delighted."),
		("Burrows","You're one tough broad, Murphy."),
		("Murphy","Why... that's the nicest thing you've ever said to me.")],
		"reject1":[("Burrows","This is a really bad idea, Murphy. Bronte's net isn't as frayed as it seems. This is a suicide run. I want out.", "barspeech/campaign/murphy3reject1.wav"),
		("Murphy","This is the best chance we'll get, we can't hold off the reinforcements forever... but do whatever you want. No skin off my nose.")],
		"reconsider":[("Murphy","What's your problem? You're about as decisive as a politico.", "barspeech/campaign/murphy3reconsider.wav"),
		("Burrows","Just trying to check out all my options, Murphy."),
		("Murphy","Hey, you want to get down to Palan and hook up with your friend, you have no option but to fly this mission. We're going to try to break the blockade with you or without you... but this is your best chance to get to Palan, and make 15000 credits to boot. So... are you going to hook up with the two Talons we managed to dig up, head for Nav 4 and kick some butt... or kiss your friend, and your fee, good-bye?")],
		"reject2":[("Burrows","Actually I just came to kiss you goodbye, Murphy. I'm gonna make this run on my own.", "barspeech/campaign/murphy3reject2.wav"),
		("Murphy","Oh, you are a dreamer. You'll never make it to Palan on your own. Now beat it, before I have to throw you outta here myself.")],
		"reminder":[("Murphy","I don't know what your angle is, mister, but if we don't punch through that blockade now, we never will.", "barspeech/campaign/murphy3reminder.wav"),
		("Burrows","Yeah... I have been kind of dragging my heels."),
		("Murphy","You should be dragged by your heels. Look, if you want to pick up this friend of yours, now is the time. The blockade ships orbiting Palan at Nav 4 won't be getting any weaker. We've got to hit them now, before more reinforcements arrive. Two militia Talons are standing by to accompany you on the assault. Don't come back here until the mission is finished and you want your pay. I've wasted too much time with you as it is.")],
		"failure":murphyfailure
		}
murphyfinish=[("Burrows","Just like I promised, I've come back for my pay... and anything else you'd like to give me.", "barspeech/campaign/murphy3finalnomonkhouse.wav"),
	("Murphy","I never considered a swift kick in the butt an incentive, but have it your way."),
	("Burrows","Cute. Give me my money before I get all mushy on you."),
	("Murphy","Here it is. Did you find your friend?"),
	("Burrows","Not yet. I'll pick him up on the next run."),
	("Murphy","There won't be a next run, ace. Not flying for us, anyway. The blockade's broken, and hard as it may be for you to believe... we don't need you anymore."),
	("Burrows","Well, thanks for breaking it to me gently, sweetheart. You're an angel."),
	("Murphy","News is news. What do you want, tears? Fact is, the job's done. If you want your friend, go to Palan and pick him up. No skin off my nose, either way...")]
murphyfinishwithmonkhouse=[("Burrows","Just like I promised, I've come back for my pay... and anything else you'd like to give me.", "barspeech/campaign/murphy3final.wav"),
	("Murphy","I never considered a swift kick in the butt an incentive, but have it your way."),
	("Burrows","Cute. Give me my money before I get all mushy on you."),
	("Murphy","Here it is. Did you find your friend?"),
	("Burrows","Uh huh. He's waiting at the next table."),
	("Murphy","Then goodbye, and take care of yourself.")]
monkhouse1={"intro":[("Burrows","Ah, Dr Monkhouse. I'm glad to see you.", "barspeech/campaign/monkhouse2intro.wav" ),
			("Monkhouse","I wish I could say the same. I'm not receiving visitors right now, young man. I wish to be alone."),
			("Burrows","Sorry, Doc, but I didn't run the blockade to take no for an answer. Listen, I have this alien artifact, and I..."),
			("Monkhouse","Don't speak to me about extra-terrestrial artifacts! I'm sick of them! I nearly got killed here because of my work. You've heard of the Steltek? Well, suffice it to say, I recovered an interesting piece of Steltek manufacture... a piece which interested certain corrupt corporate interests who shall be nameless. All I need is a libel suit on top of everything else. Who are you?"),
			("Burrows","Just a curious privateer."),
			("Monkhouse","Well listen. I was kidnapped and brought to Palan by men who wanted my artifact... and then I was nearly killed in last month's bombing attacks. Thank God, my kidnappers were buried beneath the rubble of the interrogation compound."),
			("Burrows","And what happened to your artifact?"),
			("Monkhouse","Never you mind about my artifact. What do you want of me?"),
			("Burrows","I have an artifact of my own. I want you to tell me what it is."),
			("Monkhouse","I'd consider it... in exchange for transportation off world. If you'll fly me to Basra refinery base in the Palan system, I'll help you solve this puzzle."),
			("Burrows","Basra refinery base? It's not exactly vacation central. Why go there?"),
			("Monkhouse","It's the nearest base, and I detest space travel in cramped quarters. I'll charter a luxury liner back to civilisation later. I will pay you 5000 credits towards your expenses. Have we a bargain?")],
			"accept":[("Burrows","Okay, Doc. I'll get you off this rock and fly you to Basra. But once we hit Basra, you better prove you were worth the trouble.", "barspeech/campaign/monkhouse2accept1.wav"),
			("Monkhouse","Meet me in the bar on Basra for your payment, and your analysis. Most assuredly. If I can't tell you about your find... no one can.")],
			"accept2":[("Burrows","Okay, Doc. I'll get you off this rock and fly you to Basra. But once we hit Basra, you better prove you were worth the trouble.", "barspeech/campaign/monkhouse2accept2.wav"),
			("Monkhouse","Meet me in the bar on Basra for your payment, and your analysis. Most assuredly. If I can't tell you about your find... no one can.")],
			"reject1":[("Burrows","Sorry, Doc. I don't like those terms at all.", "barspeech/campaign/monkhouse2reject1.wav"),
			("Monkhouse","And yet you expect to employ my years of hard earned knowledge for nothing? No, young man. I don't like those terms either. Farewell.")],
			"reconsider":[("Monkhouse","See here, young man. I won't be trifled with. If you'll transport me off this wretched world and get me to the Basra refinery base, I'll pay you 5000 credits and help you identify your find. Have we a bargain?", "barspeech/campaign/monkhouse2reconsider.wav")],
			"reject2":[("Burrows","I want the information up front, Monkhouse.", "barspeech/campaign/monkhouse2reject2.wav"),
			("Monkhouse","I'm afraid that would leave me with little leverage in this situation. I have made my position clear. I will tell you about the artifact the moment I arrive in Basra. Come back when you are willing to accept my offer.")],
			"reminder":[("Monkhouse","I thought we had a deal, young man.", "barspeech/campaign/monkhouse2reminder.wav"),
			("Burrows","We do."),
			("Monkhouse","Well, in that case, I'd advise you to get me off this wretched planet immediately, and take me without further delay to Basra! My patience is wearing thin, and the longer we delay, the more it deteriorates! If you want me to help you identify your find, GET ME OUT OF HERE NOW!"),
			("Burrows","Yes, sir. Be on my ship in five minutes.")],
			"failure":[]
			}
monkhouseinfo=[("Monkhouse","That was truly an exciting ride. Thank you for getting me here in one piece. I've examined your artifact. A very interesting piece you have there, young man... especially since I have one almost like it. Ironically, it's the very piece that my kidnappers were interested in.", "barspeech/campaign/monkhousefinal.wav"),
		("Burrows","Then... you know what it is?"),
		("Monkhouse","Ah yes. You said you knew nothing of the Steltek. Well, long before man emerged on Earth, the Steltek ruled an empire that spanned the galaxy. Even then, they were more technologically advanced than we are now. By the time their empire crumbled, they were possessed of wonders beyond our comprehension."),
		("Burrows","Is that so? Well, if they were so tough, what happened to them?"),
		("Monkhouse","No one knows. Some say they perished in a civil war that lasted millennia... others believe they simply grew weary of their power, surrendered it... and even now enjoy a simple, tranquil existence at the heart of the galaxy."),
		("Burrows","Nice fairy tale, Doc. But what about the artifact?"),
		("Monkhouse","Here's my piece of it. Notice anything odd?"),
		("Burrows","The markings..."),
		("Monkhouse","Hold it up beside yours."),
		"",
		"",
		"",
		("Burrows","A map. Good heavens, it's a treasure map!"),
		("Monkhouse","Superficially. It also contains a complete set of the Steltek alphabet."),
		("Burrows","Who cares about that? What are we going to find at the spot indicated, Doc?"),
		("Monkhouse","Who knows? The real question is, where do we go from here?"),
		("Burrows","The sector on the map seems to be located on the edge of the frontier."),
		("Monkhouse","Bad luck indeed. That area is currently uncharted. Without the location of the sector's jump points, exploring the area will be nearly impossible."),
		("Burrows","Unless I enlist with the Exploratory Service in Rygannon. That way I could map the jump points, and get paid for it at the same time."),
		("Monkhouse","Always the privateer, eh? Care you nothing for the possibility of scientific advancement?"),
		("Burrows","You got it, Doc. Nothing. I'm in this for the profit."),
		("Monkhouse","Very well. I have no interest in baubles. You may keep my fragment, and whatever treasure you find... so long as I get to publish any scientific finds. Agreed?"),
		("Burrows","Sounds good to me."),
		("Monkhouse","Excellent. Before you go, I'll program your computer with the nav information from the map, as well as the Steltek alphabet. It may come in handy where you're going."),
		("Burrows","What? You think X marks the spot to a Steltek colony? You've been watching too many late night holos, Doc."),
		("Monkhouse","We shall see.")]

tarynfailure=[("Burrows","Look, you don't have to tell me. I know I screwed up.", "barspeech/campaign/crossfailure.wav"),
		("Cross","Yeah, you did. It hurts me to say this, because I like you, but I'm afraid you're fired. We need results. And I don't want to sit around this sector forever."),
		("Burrows","Hey, I'll try harder, I'll work faster..."),
		("Cross","Sorry, you had your chance and you blew it. I wish you luck. Good-bye.")]

taryn1={"intro":[("Burrows","Excuse me, I'm looking for Taryn Cross.", "barspeech/campaign/cross1intro.wav"),
		("Cross","You've found her. So... you gonna slit my throat, or just rob me?"),
		("Burrows","Don't let my clothes fool you. They're a little rough, but times have been hard... which leads me to the point. I'm looking for work..."),
		("Cross","...and you heard that the Exploratory Service takes anyone, is that it? That's a misconception, I'm afraid. Our work is hazardous, yes, but not all our employees sport scars and pirate hats. The job requires brains as well as blasters."),
		("Burrows","I'm a privateer. Believe me, I'm not looking for a handout, just a job. I have all the qualifications you're looking for... an eye for detail, a nose for trouble and a butt that's never been kicked."),
		("Cross","Suppose I'll have to check that out for myself... later. Okay. If you want the job, you're in, on a per mission basis. Right now I need someone for a potentially dangerous assignment. I'm in charge of charting maps for the sector. The ES has lost a number of ships in the Delta system... and through jump point Delta, which remains unexplored. Could be Kilrathi, a singularity or black magic. No one knows... but I'll pay you 10000 credits to find out.")],
		"accept":[("Cross","You'll leave Rygannon, travel to the Delta system and scout it through 4 nav points. The navigational info you'll need will be programmed into your nav computer. Basically, for charting purposes, you'll be flying a small loop, and standard nav points which make up the loop have been calculated. Simply hit all the nav points and return here safely, and we'll download what we need from your flight disc... and pay you, of course.", "barspeech/campaign/cross1accept1.wav"),
		("Burrows","Sounds pretty easy."),
		("Cross","Easy? We've lost three vessels so far."),
		("Burrows","Yeah, but did those pilots have scars or pirate hats?"),
		("Cross","Neither."),
		("Burrows","Then get ready to strike \"Here there be dragons\" from your map, Ms Cross."),
		("Cross","It'll be a pleasure. Good luck.")],
	"accept2":[("Cross","You'll leave Rygannon, travel to the Delta system and scout it through 4 nav points. The navigational info you'll need will be programmed into your nav computer. Basically, for charting purposes, you'll be flying a small loop, and standard nav points which make up the loop have been calculated. Simply hit all the nav points and return here safely, and we'll download what we need from your flight disc... and pay you, of course.", "barspeech/campaign/cross1accept2.wav"),
		("Burrows","Sounds pretty easy."),
		("Cross","Easy? We've lost three vessels so far."),
		("Burrows","Yeah, but did those pilots have scars or pirate hats?"),
		("Cross","Neither."),
		("Burrows","Then get ready to strike \"Here there be dragons\" from your map, Ms Cross."),
		("Cross","It'll be a pleasure. Good luck.")],
		"reject1":[("Burrows","Somehow the idea doesn't grab me. Got anything else?", "barspeech/campaign/cross1reject1.wav"),
		("Cross","Not at the moment."),
		("Burrows","Then I'll pass. Thanks anyway."),
		("Cross","Sorry it didn't work out. Good luck, anyway.")],
		"reconsider":[("Cross","I didn't think pirates were known for their waffling.", "barspeech/campaign/cross1reconsider.wav"),
		("Burrows","We're not, but we never jump into things without thinking them through... if we can."),
		("Cross","Look, I can't let you take too much longer to decide. I need someone to head out to Delta system and chart it, following the pre-programmed nav points which comprise the mapping loop. We've lost three ships attempting to do just that, and I'll pay 10000 credits to the man who can bring back the cartographical info we need. How about it? Yes or no?")],
		"reject2":[("Burrows","Got anything else?", "barspeech/campaign/cross1reject2.wav"),
		("Cross","Not currently."),
		("Burrows","Then I'll try later. Thanks again.")],
		"reminder":[("Cross","Just as I suspected... all talk and no action. You disappoint me. You should have left Rygannon and charted the nav points in Delta system by now.", "barspeech/campaign/cross1reminder.wav"),
		("Burrows","I'll get around to it sooner or later."),
		("Cross","Make it sooner. I may be desperate for someone to fly this... but I can't afford to wait forever. ")],
		"failure":tarynfailure}
taryn2={"intro":[("Cross","Well, are the dragons slain?", "barspeech/campaign/cross2intro.wav"),
		("Burrows","Wipe the dragons from your charts, and replace them with pirates. Dead pirates, anyway. The area was swarming with the little buggers... but I did a little exterminating before completing my mapping run."),
		("Cross","That's good to know. If I don't get this sector mapped real soon, the brass at HQ will have my rear."),
		("Burrows","Lucky brass. Any way I can beat them to it?"),
		("Cross","Hmmm... maybe we'll discuss that after this next mission. This time you'll enter a completely unexplored region. I need you to launch from Rygannon, pass through Delta to a new jump point which you will use to jump to the uncharted system we've designated Beta. All you have to do is hit all the nav points in your computer. I'll update the chart using your flight disc and pay you 10000 credits when you return...")],
		"accept":[("Burrows","Like I told you before, I need the work.", "barspeech/campaign/cross2accept1.wav"),
		("Cross","Don't worry. You're not going into a known hazard area."),
		("Burrows","Yeah, but it's the unknown hazards that scare me. Still, I'll do my best and meet you back here when I'm done."),
		("Cross","Good. By the way, there's one more thing I need you to do on this run. One of my men, Captain Garrovick, made the same run you're making. He never came back, so one of your objectives is to find him if you can."),
		("Burrows","I thought this wasn't a known hazard area."),
		("Cross","We don't know if anything hazardous happened to Garrovick... but keep your eyes peeled just the same, okay?")],
		"accept2":[("Burrows","Like I told you before, I need the work.", "barspeech/campaign/cross2accept2.wav"),
		("Cross","Don't worry. You're not going into a known hazard area."),
		("Burrows","Yeah, but it's the unknown hazards that scare me. Still, I'll do my best and meet you back here when I'm done."),
		("Cross","Good. By the way, there's one more thing I need you to do on this run. One of my men, Captain Garrovick, made the same run you're making. He never came back, so one of your objectives is to find him if you can."),
		("Burrows","I thought this wasn't a known hazard area."),
		("Cross","We don't know if anything hazardous happened to Garrovick... but keep your eyes peeled just the same, okay?")],
		"reject1":[("Burrows","Sounds kind of boring. I think I'll bow out.", "barspeech/campaign/cross2reject1.wav"),
		("Cross","Too bad. I think this one would've been a lot easier... but I guess you have your reasons...")],
		"reconsider":[("Cross","Why are you hesitating about taking this mission? It's not difficult. You'll launch from Rygannon, pass through Delta to a new jump point which you'll use to jump to the uncharted system we've designated Beta. Then all you have to do is hit all the nav points in your computer. I'll update the chart using your flight disc and pay you 10000 credits for your charts. That's my offer. Sound good to you?", "barspeech/campaign/cross2reconsider.wav")],
		"reject2":[("Cross","I'll be here if you need the work.", "barspeech/campaign/cross2reject2.wav")],
		"reminder":[("Cross","Finished your mapping run of Beta system already?", "barspeech/campaign/cross2reminder.wav"),
		("Burrows","Haven't left yet, actually."),
		("Cross","Look, this is easy money. If you don't want it... I'll be happy to find someone who does!"),
		("Burrows","Like I told you, I need the money."),
		("Cross","Then take jump point Delta to Beta system, follow your mapping spiral, try to locate Captain Garrovick and report back here for your 10000. And please hurry. I have deadlines, you know.")],
		"failure":tarynfailure
		}
taryn3={"intro":[("Cross","Finished your mapping loop, privateer?", "barspeech/campaign/cross3intro.wav"),
		("Burrows","Yeah, the information's on my flight disc. And I found Garrovick. You didn't tell me he was a raving lunatic, Taryn."),
		("Cross","Oh, Garrovick isn't crazy, he's one of our best pilots! Thank goodness, you brought him back!"),
		("Burrows","Uh, well... actually, I didn't."),
		("Cross","What?!"),
		("Burrows","Garrovick was out of his mind, Taryn. He fired on me for no reason. Whatever attacked his ship must've been so frightening it drove him mad. That's what bothers me. I can't believe the pirates did all this."),
		("Cross","Which means there's a new player in the sector."),
		("Burrows","One tough enough to end the game. So... where do we go from here?"),
		("Cross","Keep exploring. What else can we do? I have maps to prepare. I'll pay you 10000 credits to make another mapping run... ")],
		"accept":[("Burrows","Ah, why not? Some say life is hell and death an escape, others say heaven awaits us in the world beyond... but either way, I need a new pair of shoes.", "barspeech/campaign/cross3accept1.wav"),
		("Cross","Then listen. You'll leave Rygannon, pass through Beta system, and use the jump point there to reach the uncharted Gamma system. Fly the loop pattern in your nav comp by hitting each nav point in sequence, complete the mapping spiral through Gamma and hurry back here to collect your pay.")],
	"accept2":[("Burrows","Ah, why not? Some say life is hell and death an escape, others say heaven awaits us in the world beyond... but either way, I need a new pair of shoes.", "barspeech/campaign/cross3accept2.wav")],
		"reject1":[("Burrows","What, with Death Incarnate sucking around out there? No way.", "barspeech/campaign/cross3reject1.wav"),
		("Cross","I'm disappointed... but I can't say I blame you. Good luck and... good-bye.")],
		"reconsider":[("Cross","Thinking twice before bailing out? Smart boy. This is easy money if ever there was such a thing. All you need to do is pilot through the Beta system and use the jump point there, which should take you to the uncharted Gamma system. Fly the loop pattern in your nav comp by hitting each nav point in sequence, complete the mapping spiral through Gamma and hurry back here to collect your 10000 credits.", "barspeech/campaign/cross3reconsider.wav"),
		("Burrows","Sounds easy enough... so why are unmentionable portions of my body spontaneously puckering?"),
		("Cross","Don't let the disappearances bother you. Just focus on the mission at hand, okay?")],
		"reject2":[("Burrows","Not until I find out what's out there.", "barspeech/campaign/cross3reject2.wav"),
		("Cross","I still can't say I blame you. Good luck.")],
		"reminder":[("Cross","Back already, eh? Did you turn your flight disc over to Cartography?", "barspeech/campaign/cross3reminder.wav"),
		("Burrows","To tell the truth, I haven't left yet."),
		("Cross","Look, I know it's dangerous out there, but if you can't take the heat..."),
		("Burrows","Hey, no sweat. I'm not afraid. Things come up, you know?"),
		("Cross","All I know is, the ES brass are breathing down my neck. They're interested in the sector, and they're pressuring me to finish up. Listen, pilot through the Beta system and use the jump point there, which should take you to the uncharted Gamma system. Fly the loop pattern in your nav comp by hitting each nav point in sequence, complete the mapping spiral through Gamma and hurry back here to collect your 10000.")],
		"failure":tarynfailure
		}
taryn4={"intro":[("Cross","Did you complete the run?", "barspeech/campaign/cross4intro.wav"),
		("Burrows","Yeah... no thanks to the Kilrathi."),
		("Cross","Kilrathi? What were they doing there?"),
		("Burrows","They were flying an inverted V, the usual formation for a broad sector sweep."),
		("Cross","But what could they be searching for, out here in the middle of nowhere?"),
		("Burrows","You tell me. Why is the Confed interested in mapping this sector, anyway?"),
		("Cross","I don't know. The top brass makes those decisions, I only implement them. If you're suggesting there's some kind of hidden agenda here..."),
		("Burrows","All I'm saying is, if the Confed is out here looking for something, it makes sense that the Kilrathi would share their interest. Anyway, they're the ones who've been trashing your ships all along."),
		("Cross","Makes sense... I guess. Up for another mapping run? It pays the usual 10000 credits...")],
		"accept":[("Cross","This time you'll map a newly-discovered system, designated Delta Prime for it's transpacial proximity to Delta system.", "barspeech/campaign/cross4accept1.wav"),
		("Burrows","Transpacial, eh? So I'll be doing a little jumping to get there."),
		("Cross","Right. You'll need to fly through Gamma to the jump point there, jump to Delta Prime and hit the nav point we've programmed into your computer. Afterwards, report back here for your pay. If it goes well, this will be the last run in this sector. Good luck.")],
	"accept2":[("Cross","If it goes well, this will be our last run for this sector. Good luck.", "barspeech/campaign/cross4accept2.wav")], 
		"reject1":[("Burrows","If I'd wanted to tangle with Kilrathi, I'd have enlisted. Forget it.", "barspeech/campaign/cross4reject1.wav"),
		("Cross","Too bad. Another run, and we'd have finished with this sector...")],
		"reconsider":[("Cross","You've changed your mind?", "barspeech/campaign/cross4reconsider.wav"),
		("Burrows","I am considering rethinking my decision."),
		("Cross","Talk about fear of commitment... Look. You need to fly through Gamma to the jump point there, jump to Delta Prime and hit the nav point we've programmed into your computer. Afterwards, report back here for your payment of 10000 credits. Agreed?")],
		"reject2":[("Burrows","I'd better quit while I'm ahead here, Taryn.", "barspeech/campaign/cross4reject2.wav"),
		("Cross","Your call. Someone will come along and finish this job. So long.")],
		"reminder":[("Cross","Blast it, am I expecting too much asking you to complete your mission in a timely manner? I can see it in your eyes. You haven't flown it yet, have you?", "barspeech/campaign/cross4reminder.wav"),
		("Burrows","Quit nosing around in my eyes, Taryn. I promise, your mission is now on top of my list of things to do."),
		("Cross","Yeah? Then get to it! I want to see Delta Prime charted in my lifetime! Manoeuvre through Gamma to the jump point located there, jump to Delta Prime and hit the nav point we've programmed in your computer. Just one more mapping run, and we've completed our chart of this sector. Just fly your programmed course, and return when you're finished."),
		("Burrows","You don't have to remind me. I'm negligent, not stupid...")],
		"failure":tarynfailure
		}
taryninfo=[("Cross","Well? How did it go?", "barspeech/campaign/crossfinal.wav"),
	("Burrows","Pulled it off, naturally. What else did you expect?"),
	("Cross","No offence intended. I suppose you want to be paid for pushing back the frontier for all mankind?"),
	("Burrows","Not to be crass... but yeah."),
	("Cross","Here it is. Last payday. Don't drink it all at once."),
	("Burrows","Yeah... well, I guess that wraps up my stint in the ES. Taryn, it's been fun."),
	("Cross","Too much fun can kill you."),
	("Burrows","Yeah... that's why I'm heading out before it becomes a joy. Take care."),
	("Cross","You too. ")]
goodinfailure = [("Goodin","You've got some nerve coming back here!", "barspeech/campaign/terrelfailure.wav"),
		("Burrows","Hey, I was a sitting duck for you clowns, the least I expect is an apology."),
		("Goodin","For what? Allowing the drone to annihilate our strike force?"),
		("Burrows","Sweetheart, Commodore Reismann had an entire fleet. I had a gun. Gee, I wonder who screwed the pooch on that one?"),
		("Goodin","As far as Terrell is concerned, the puppies are gonna look just like you! And unless you want to be thrown into the brig, you better hit the lanes before he sees you!"),
		("Burrows","I see. Thanks for reminding me why I hate sleeping with the military."),
		("Goodin","Yeah? Well on your way out, don't look for any money on the dresser, pal. It wasn't that good.")]
goodin={"intro":[("Goodin","I'm Captain Goodin, attache to Admiral Terrell. We've been expecting you.", "barspeech/campaign/goodin1intro.wav"),
		("Burrows","And yet no cake? I'm crushed. Excuse my flippancy, but it's not every day I have the honour of being arrested."),
		("Goodin","You're not under arrest. Though we have all the evidence we need. What does the word smuggler mean to you?"),
		("Burrows","It's an antonym for plausible deniability. Sorry, Cap. I won't say another word without my lawyer."),
		("Goodin","Relax. I'm only here to extend an... invitation. You'll proceed to Perry Naval Base, where the Admiral will interview you personally."),
		("Burrows","Regarding...?"),
		("Goodin","Playing dumb, huh? Have it your way, then. We've traced a series of disappearing and destroyed ships to your movements. Looks like wherever you go, disaster follows. Tell me, are the Kilrathi paying you to test their secret weapon, or do you merely keep the plunder?"),
		("Burrows","I don't know what you're talking about, Cap."),
		("Goodin","Well, you'll have plenty of time to think about it, en route to Perry."),
		("Burrows","And if I don't want to go?"),
		("Goodin","You don't have to. As I said, you're not under arrest. But something out there has the hots for you. Something nasty. And if you really don't know what it is - if you're as much in the dark as we are - maybe we can help each other out. How about it?")],
		"accept":[("Burrows","I'll hear the Admiral out, Goodin. But I don't like sleeping with the military.", "barspeech/campaign/goodin1accept1.wav"),
		("Goodin","You don't have to kiss us, just grit your teeth and close your eyes. Better get a move on. You never know what's out there waiting for you...")],
	"accept2":[("Burrows","I'll hear the Admiral out, Goodin. But I don't like sleeping with the military.", "barspeech/campaign/goodin1accept2.wav"),
		("Goodin","You don't have to kiss us, just grit your teeth and close your eyes. Better get a move on. You never know what's out there waiting for you...")],
		"reject1":[("Burrows","Sorry, but working with you military types makes me nervous. I'd rather tackle a monster than a bureaucracy.", "barspeech/campaign/goodin1reject1.wav"),
		("Goodin","Red tape or blood, same colour either way. No skin off my nose. I'll be here if you change your mind.")],
		"reconsider":[("Goodin","Really, you'd be smart to head to Perry Naval Base at max speed. The Admiral wants your help in destroying that thing, whatever it is, and if you've got a brain in your head, you'll co-operate. Will you meet with him at Perry or not?", "barspeech/campaign/goodin1reconsider.wav")],
		"reject2":[("Burrows","Again, I'd rather deal with a monster than the military.", "barspeech/campaign/goodin1reject2.wav"),
		("Goodin","Have it your way. I'll be here if you change your mind.")],
		"reminder":[("Goodin","Look, I know you hate co-operating with 'authority', but Admiral Terrell is waiting for you at Perry Naval Base. Are you heading out, or not?", "barspeech/campaign/goodin1reminder.wav"),
		("Burrows","Yeah, I guess I might as well get it over with...")],
		"failure":["Having to hitch a ride from a patrolling broadsword is not my idea of a good time. You should consider yourself a fool and an enemy of confed. I've already earmarked your files--good luck getting out of system."]
		}
terrellfailure=[("Terrell","I'm disappointed, son. I thought I could count on you to deliver, but I guess that I was wrong. It goes to show that you can never trust someone without a uniform to do the duty of a soldier")]

terrell={"intro":[("Terrell","We don't have a lot of time, privateer, so let's cut the niceties. I'm Admiral Terrell, and the Confederation needs your help.", "barspeech/campaign/terrel1intro.wav"),
		("Burrows","Goodin accuses me of being a kitty collaborator, and now you want my help?"),
		("Terrell","Yes, well, Goodin has always been a little overzealous in executing her orders. We know you're not responsible for the destruction of our fleet... at least not directly."),
		("Burrows","Then what exactly do you want from me?"),
		("Terrell","For quite a while we've suspected the Kilrathi of having a secret weapon. There could be no other explanation for the havoc being wreaked upon our forces. This was confirmed recently when, using the path of destruction as a baseline, we drew a correlation between that course and your flight path. That correlation approaches unity."),
		("Burrows","You mean the thing that's following me around is a Kilrathi secret weapon?"),
		("Terrell","Yes. For some odd reason, the thing has locked on to you. Maybe it's a flaw in the targeting algorithms. Who knows? The point is, wherever you go, it shows up eventually... and that's why we need your help."),
		("Burrows","Are we talking bait here, Admiral? I've been jumping like crazy, trying to keep ahead of this thing... and now you want me to stand still?"),
		("Terrell","It's not like I'm asking you to slit your wrists. Commodore Reismann has assembled an entire fleet! Even as we speak, they stand ready to destroy the Kilrathi marauder. All they need is for you to lure it into the ambush."),
		("Burrows","An entire fleet, huh? So why doesn't that make me feel better?"),
		("Terrell","I could force you to do this, but I won't. The way I see it, you can either co-operate, and let the fleet blast it to Kingdom Come... or you can keep running the rest of your life. To sweeten the deal, we'll throw in 30000. So... what'll it be? ")],
		"accept":[("Burrows","Running has never been my style, Admiral. Deal me in.", "barspeech/campaign/terrel1accept1.wav"),
		("Terrell","Excellent. This should be the easiest mission you've ever flown. Simply fly to the ambush point at Blockade Point Tango, Nav 1. That's far enough away to minimise civilian casualties. Once there all you have to do is kick back and wait. We'll do the rest."),
		("Burrows","I hope so, Admiral. I surely do hope so.")],
		"accept2":[("Burrows","Even though the though of being your sitting duck doesn't thrill me, running has never been my style, Admiral. Deal me in.", "barspeech/campaign/terrel1accept1.wav"),
		("Terrell","Excellent. This should be the easiest mission you've ever flown. Simply fly to the ambush point at Blockade Point Tango, Nav 1. That's far enough away to minimise civilian casualties. Once there all you have to do is kick back and wait. We'll do the rest."),
		("Burrows","I hope so, Admiral. I surely do hope so.")],
		"reject1":[("Burrows","I've done all right so far, Admiral. Frankly, the thought of being your sitting duck doesn't thrill me. I'll take my chances on my own.", "barspeech/campaign/terrel1reject1.wav"),
		("Terrell","As I said, I won't force you to do this... but you're making a bad mistake... and I hope you live long enough to realise it.")],
		"reconsider":[("Terrell","What're you doing here? Thought you'd be gone by now. Gone as in dead.", "barspeech/campaign/terrel1reconsider.wav"),
		("Burrows","I'm not that anxious to hit space again. I'm thinking your offer over."),
		("Terrell","Then think fast. I was about to order the fleet massed at Blockade Point Tango to disperse. No sense in giving an ambush if nobody's coming."),
		("Burrows","You really expect me to lure this... whatever it is... to Tango Point... serving as your decoy?"),
		("Terrell","Sooner or later you'll have to face that thing. This way you can do it on your own terms... with an armed fleet as chaperone. It's the best shot you've got. And we'll pay you 30000 besides. Will you do it?")],
		"reject2":[("Terrell","As I said, I won't force you to do this... but I still think you're making a bad mistake. Now if you would leave me alone, I have a decision to make.", "barspeech/campaign/terrel1reject2.wav")],
		"reminder":[("Terrell","What are you doing here?", "barspeech/campaign/terrel1reminder.wav"),
			("Burrows","What's the matter? Make you nervous having your decoy sitting around the base?"),
			("Terrell","Frankly, yes. We don't want to lure the blasted thing to Perry! Head out to Blockade Point Tango, Nav 1, pronto! They can't hold the ambush without you, you know! ")],
		"failure":terrellfailure
		}

steltekhelptext=[("You're not Kilrathi, are you?",True,"campaign/Steltek.wav"),
		("Alien craft. Communication needed."),
		("Uh? okay. I'm listening.",True),
		("Alien craft. Information required. We are Steltek. You have technology belonging to us. You will tell us where you got technology. Now."),
		("Do you know something about the thing we're ambushing?",True),
		("Understood. Steltek drone keys off Steltek technology on your ship. Will pursue you until you are destroyed."),
		("That death machine is one of yours?",True),
		("Regrettable. When retreated from galaxy, tried to eliminate all Steltek technology to bar developing races from finding our relics, bringing upon themselves the ruin we wrought. However, were too pervasive. Pockets of technology, weapons, drones, remain. We eliminate these pockets when possible. Again, query: where did you get technology?"),
		("You want to remove it?",True),
		("Again, query: where did you get technology?"),
		("That information'll cost you.",True),
		("Cost? Barter, economics?"),
		("How about a trade?",True),
		("We could energise weapon to destroy drone, but dispersal of Steltek technology, in opposition to Steltek policy."),
		("We deal, or I reveal the ship's location to more Humans.",True),
		("Not good."),
		("Have we got a deal?",True),
		("Agreed. Will attach power booster to your weapon now. Booster will provide a limited number of shots to destroy drone. Agreed?"),
		("I guess we have a deal.",True),
		(),
		("Power booster installed, prepared for jump to derelict.")]

terrellsuccess=[("Terrell","Congratulations. That was some amazing flying. You took out that drone like a real pro. Ever consider a career in the military?", "barspeech/campaign/terrelfinal.wav"),
		("Burrows","Yeah, once, but the fever broke and I got better."),
		("Terrell","You're an insubordinate smart-ass... and one of the best pilots I've ever seen. Just say the word, and an officer's commission is yours."),
		("Burrows","Appreciate it, but I'm not cut out for the military. I'm a privateer. There's a fortune waiting for me out there somewhere... and all I've gotta do is smuggle, steal and kill a lot of people to get it."),
		("Terrell","All right, but you're going to be awarded the Confederation Medal of Freedom... whether you like it or not. Understand?"),
		("Burrows","Hey, far be it for me to screw up a photo op. I'll take it."),
		("Terrell","Okay. I'm sure you're headed for trouble, and I'm sure you probably deserve it... but I wish you good luck anyway. And if you ever change your mind about serving..."),
		("Burrows","I'll have my head examined. Take care, Admiral.")]

#Broken mission
#def LoadTest():
#	CROSS_SPRITE = ("taryn.spr", "Talk_To_Taryn_Cross")#,"bases/heads/cross.spr")
#	GOODIN_SPRITE = ("goodin.spr", "Talk_To_Goodin","bases/heads/goodin.spr")
#	SANDOVAL_SPRITE  = ("sandoval.spr","Talk_To_Sandoval","bases/heads/sandoval.spr") #sprite file for the fixer
#	priv=Campaign("kiddie")
#
#	mission_desc="Robot:_Assassination"
#	priv.Init(MakeMission(priv,
#				CROSS_SPRITE,
#				[InSystemCondition("Gemini/Tingerhoff","Munchen")],
#				[InSystemCondition("Gemini/Midgard","Heimdel")],
#				AddCredits(13000),
#				Cutscene('Automated Robotic Message','PoliticianCutscene.spr',(0.582,-0.3),(3.104,1.2416),'Message from insurgency',[("","A Few Hours Later..."),("Robot","This is an automated message..."),("Robot","Members of my organization are displeased with the latest turn of politics."),("Robot","Later today there will be a vote on a new bill called the LOYALTY act."),("Robot","If this bill passes, it will give police forces a mandate to hold anyone suspected of interacting with one of several organizations indefinitely."),("Robot","While the bill expires in 90 days, people arrested in that duration may be held without trial at the discression of the Gemini state senate for up to 40 years."),("Robot","You are our only hope for stopping the bill. With a current 50-50 tie in the senate, our Governor, a man from the Landreich with a hunger for power will be the man to select whether this bill passes."),("Robot","Hence we offer a reward for the 'removal' of one of the senators, specificially 40,000 credits for the failure to deliver your senator to New Constantinople"),("Robot","You are the last hope in securing freedom for the Gemini sector. Meet us for your pay in the Midgard system."),("Robot","I will purge my memory and initiate self destruct...now")],'refinery.m3u','refinery.m3u').MakeEnqueue(),
#				"escort_mission",("confed",0,0,0,1500,0,0,0,("Gemini/New_Detroit","Gemini/New_Constantinople"),priv.name+"_mission",'','stiletto'),
#				priv.name+"_mission",
#				goodin,
#				None,
#				CampaignEndNode(priv),CampaignEndNode(priv)), # If you win the mission. Usually points to the next mission
#		mission_desc # Name that describes the mission in flight and in the mission computer.
#		)
#	return priv

def LoadMainCampaign():
	SANDOVAL_SPRITE  = ("sandoval.spr","Talk_To_Sandoval","bases/heads/sandoval.spr") #sprite file for the fixer
	ARTIFACT1_SPRITE = "artifact1.spr"
	ARTIFACT2_SPRITE = "artifact2.spr"
	ARTIFACT_POSITION= ( 0, 0) #(0.582, -0.2716)
	ARTIFACT_SIZE    = (3.2, 2.0) #(3.104, 2.4832)
	SandovalMission1 = CampaignClickNode() # Initialize each node
	TAYLA_ND_SPRITE     = ("tayla.spr","Talk_To_Tayla","bases/heads/taylanewdetroit.spr")
	TAYLA_SPRITE     = ("tayla.spr","Talk_To_Tayla","bases/heads/taylapirate.spr") #sprite file for the fixer
	TaylaMission1    = CampaignClickNode() # Initialize each node
	SandovalFinish   = TaylaMission1
	TaylaMission2    = CampaignClickNode() # Initialize each node
	TaylaMission3    = CampaignClickNode() # Initialize each node
	TaylaMission4    = CampaignClickNode() # Initialize each node
	TaylaFinish      = CampaignClickNode() # Talks to you, then proceeds to Lynch missions!
	
	MIGGS_SPRITE     = "miggs.spr" # miggs is a special case...
	MIGGS_POSITION   = (-0.8143125, -0.4845886363) # (-0.80625, -0.357421875) Miggs static #(-0.7820625, -0.3783)
	MIGGS_WIDTH_HEIGHT = (.2,.9)
	MIGGS_LABEL      = "Talk_To_Miggs"
	MIGGS_SCRIPT     = "#\nimport Base\nimport VS\nBase.Message('You don\\'t wanna talk to me cus I don\\'t wanna talk to you, and whoever makes me do what I don\\'t want, gets hurt, painwise')\nVS.StopAllSounds()\nVS.playSound('barspeech/campaign/miggs.ogg',(0,0,0),(0,0,0))"
	LYNCH_SPRITE     = ("lynch.spr","Talk_To_Lynch","bases/heads/lynch.spr") #sprite file for the fixer
	LynchMission1    = CampaignNode() # Initialize each node
	LynchMission2    = CampaignNode() # Initialize each node
	LynchMission3    = CampaignNode() # Initialize each node
	LynchMission4    = CampaignClickNode() # Initialize each node
	
	LynchFinish      = CampaignNode()
	MastersonMission1= CampaignClickNode() # Initialize each node
	MastersonMission2= CampaignClickNode() # Initialize each node
	MastersonMission3= CampaignClickNode() # Initialize each node
	MastersonMission4= CampaignClickNode() # Initialize each node
	MastersonFinish  = CampaignNode()

	MONKHOUSE_SPRITE = ("monkhouse.spr", "Talk_To_Monkhouse","bases/heads/monkhousebasra.spr")
	MONKHOUSE_PALAN_SPRITE = ("monkhouse.spr", "Talk_To_Monkhouse","bases/heads/monkhousepalan.spr")
	MURPHY_SPRITE    = ("murphy.spr", "Talk_To_Murphy","bases/heads/murphy.spr")
	MonkhouseIntro   = CampaignNode()
	MurphyMission1   = CampaignClickNode() # Initialize each node
	MurphyMission2   = CampaignClickNode() # Initialize each node
	MurphyMission3   = CampaignClickNode() # Initialize each node
	MurphyFinish     = CampaignClickNode()

	MonkhouseMission1= CampaignClickNode()
	MonkhouseFinish  = CampaignClickNode()
	
	CROSS_SPRITE     = ("taryn.spr", "Talk_To_Taryn_Cross","bases/heads/cross.spr")
	CrossMission1    = CampaignClickNode() # Initialize each node
	CrossMission2    = CampaignClickNode() # Initialize each node
	CrossMission3    = CampaignClickNode() # Initialize each node
	CrossMission4    = CampaignClickNode() # Initialize each node
	CrossFinish      = CampaignClickNode() # Initialize each node

	GOODIN_SPRITE    = ("goodin.spr", "Talk_To_Goodin","bases/heads/goodin.spr")
	GoodinMission    = CampaignClickNode() # Initialize each node
	TERRELL_SPRITE   = ("terrell.spr", "Talk_To_Admiral_Terrell")
	TerrellMission   = CampaignClickNode() # Initialize each node
	TerrellFinish    = CampaignNode() # Initialize each node
	
	priv=Campaign("privateer_campaign") # Name of the save game variable for the entire campaign. Can't contain spaces
	priv.Init(SandovalMission1) # the first node.
	
	mission_desc="Sandoval:_Transport_iron"
	MakeCargoMission(priv, # Creates a cargo mission
		SANDOVAL_SPRITE, # Campaign, sprite
		[InSystemCondition("Gemini/New_Detroit","New_Detroit")], # Where fixer meets you to start the mission
		[InSystemCondition("Gemini/Newcastle","Liverpool")], # Where the mission ends. Usually the same as starting point for next fixer.
		None, # Script to be run as you click on the fixer. A common use is to AddCredits() for the previous mission.
		AddCargo('Artifact',1,True,SetSaveVariable('terrell_no_entry',1.0,AddRemovingSprite("artifact_1", ARTIFACT1_SPRITE, ARTIFACT_POSITION, ARTIFACT_SIZE, "Put_Away_the_Artifact",LoadMission(mission_desc,"directions_mission",(priv.name+"_mission",['Gemini/New_Constantinople', 'Gemini/Newcastle'], 'Liverpool'))))), 
		# Script to be run to start the mission (usually None if you don't have a script, but ambush is also common.)
		("Iron",10), # Mission arguments.
		#[['Gemini/New_Constantinople', 'Gemini/Newcastle'], 'Liverpool'], # directions
		priv.name+"_mission", # Script to be set on completion. -1=Failure, 0=Not Accepted, 1=Succeed, 2=In progress
		sandovalspeech, # Dictionary containing what the fixer says.
		None, # If you reject the mission twice. "None" means that he continues asking you forever until you accept
		CampaignEndNode(priv), # If you lose the mission
		SandovalFinish, # If you win the mission. Usually points to the next mission
		SandovalMission1) # The current mission node.
	
	mission_desc="Tayla_1:_Transport_to_Oakham"
	MakeCargoMission(priv, # Creates a cargo mission
		TAYLA_ND_SPRITE, # Campaign, sprite
		[InSystemCondition("Gemini/New_Detroit","New_Detroit")], # Where fixer meets you to start the mission
		[InSystemCondition("Gemini/Pentonville","Oakham")], # Where the mission ends. Usually the same as starting point for next fixer.
		ClearFactionRecord('pirates',1.0,PushRelation('pirates')), # Script to be run as you click on the fixer. A common use is to AddCredits() for the previous mission.
		LoadMission(mission_desc,"directions_mission",(priv.name+"_mission",['Gemini/XXN-1927', 'Gemini/119ce', 'Gemini/Pentonville'], 'Oakham')), # Script to be run to start the mission (usually None if you don't have a script, but ambush is also common.) (having no destination will call significant unit.. oakham should be the only dockable significant in that system
		("Plastics",10), # Mission arguments.
		priv.name+"_mission", # Script to be set on completion. -1=Failure, 0=Not Accepted, 1=Succeed, 2=In progress
		tayla1, # Dictionary containing what the fixer says.
		None, # If you reject the mission twice. "None" means that he continues asking you forever until you accept
		CampaignEndNode(priv), # If you lose the mission
		TaylaMission2, # If you win the mission. Usually points to the next mission
		TaylaMission1) # The current mission node.
	
	mission_desc="Tayla_2:_Smuggling_to_Troy"
	MakeCargoMission(priv, # Creates a cargo mission
		TAYLA_SPRITE, # Campaign, sprite
		[InSystemCondition("Gemini/Pentonville","Oakham")], # Where fixer meets you to start the mission
		[InSystemCondition("Gemini/Pentonville","Oakham")], # Where the mission ends. Usually the same as starting point for next fixer.
		AddCredits(10000), # Script to be run as you click on the fixer. A common use is to AddCredits() for the previous mission.
		LoadMission(mission_desc,"ambush",(priv.name+"_mission",("Gemini/Troy",),10,'militia_',3,'','System_guard',[("Filthy little Brilliance runner, you're busted!",False,"campaign/Brilliance.wav")],['Gemini/119ce', 'Gemini/Junction', 'Gemini/Penders_Star', 'Gemini/Troy'], 'Hector')), # Script to be run to start the mission (usually None if you don't have a script, but ambush is also common.)
		("Brilliance",25), # Mission arguments.
		priv.name+"_mission", # Script to be set on completion. -1=Failure, 0=Not Accepted, 1=Succeed, 2=In progress
		tayla2, # Dictionary containing what the fixer says.
		None, # If you reject the mission twice. "None" means that he continues asking you forever until you accept
		CampaignEndNode(priv), # If you lose the mission
		TaylaMission3, # If you win the mission. Usually points to the next mission
		TaylaMission2) # The current mission node.
	
	mission_desc="Tayla_3:_Smuggling_to_New-Constantinople"
	MakeCargoMission(priv, # Creates a cargo mission
		TAYLA_SPRITE, # Campaign, sprite
		[InSystemCondition("Gemini/Pentonville","Oakham")], # Where fixer meets you to start the mission
		[InSystemCondition("Gemini/Pentonville","Oakham")], # Where the mission ends. Usually the same as starting point for next fixer.
		AddCredits(15000), # Script to be run as you click on the fixer. A common use is to AddCredits() for the previous mission.
		LoadMission(mission_desc,"ambush",(priv.name+"_mission",("Gemini/XXN-1927"),10,'confed_',2,'','Sector_guard',[("Filthy little brilliance runner! You're busted!",False,"campaign/Brilliance.wav")],['Gemini/119ce', 'Gemini/XXN-1927', 'Gemini/New_Constantinople'], 'New_constantinople')), # Script to be run to start the mission (usually None if you don't have a script, but ambush is also common.)
		("Brilliance",25), # Mission arguments.
		priv.name+"_mission", # Script to be set on completion. -1=Failure, 0=Not Accepted, 1=Succeed, 2=In progress
		tayla3, # Dictionary containing what the fixer says.
		None, # If you reject the mission twice. "None" means that he continues asking you forever until you accept
		CampaignEndNode(priv), # If you lose the mission
		TaylaMission4, # If you win the mission. Usually points to the next mission
		TaylaMission3) # The current mission node.
	
	mission_desc="Tayla_4:_Hidden_smuggling_to_New-Constantinople"
	MakeCargoMission(priv, # Creates a cargo mission
		TAYLA_SPRITE, # Campaign, sprite
		[InSystemCondition("Gemini/Pentonville","Oakham")], # Where fixer meets you to start the mission
		[InSystemCondition("Gemini/Pentonville","Oakham")], # Where the mission ends. Usually the same as starting point for next fixer.
		AddCredits(20000), # Script to be run as you click on the fixer. A common use is to AddCredits() for the previous mission.
		LoadMission(mission_desc,"ambush",(priv.name+"_mission",("Gemini/Pentonville"),20,['riordian','pirates_'],[1,2],['centurion.blank','talon'],["William_Riordian","Riordian's_pal"],
			[("#bb4400Where do you think you're going?",False,"campaign/Riordian.wav"),
			("#996600About my business. And you?",True),
			("#996600You don't recognise me, do you?"),
			("#bb4400Hold on, Mister. I think it's high time we were introduced, don't you?"),
			("#bb4400No. I'm picky about my friends.",True),
			("#996600Come on, you steal a man's business, you ought to at least know his name."),
			("#996600If you care that much, go ahead.",True),
			("#888800My name is William Riordian."),
			("#996600Okay. May I be of service?",True),
			("#dd2200You take over my route, fly for Tayla, and then have the gall to insult me! There's not enough work for two privateers. I'll teach you to steal my business!"),
			("#dd2200I'm pretty good at that already.",True),
			("#ff0000You're a dead man."),
			("#ff0000I'll show Tayla what a real man can do!")], ['Gemini/119ce', 'Gemini/XXN-1927', 'Gemini/New_Constantinople'], 'New_Constantinople')),
		("Hidden_Brilliance",25), # Mission arguments.
		priv.name+"_mission", # Script to be set on completion. -1=Failure, 0=Not Accepted, 1=Succeed, 2=In progress
		tayla4, # Dictionary containing what the fixer says.
		None, # If you reject the mission twice. "None" means that he continues asking you forever until you accept
		CampaignEndNode(priv), # If you lose the mission
		TaylaFinish, # If you win the mission. Usually points to the next mission
		TaylaMission4) # The current mission node.
	
	TaylaFinish.Init(priv,
		[InSystemCondition("Gemini/Pentonville","Oakham")],
		tayla_final,
		TAYLA_SPRITE,
		GoToSubnode(0,AddCredits(10000,AddTechnology("pirates",PopRelation('pirates')))),
		None,
		[LynchMission1])
	
	mission_desc="Lynch_1:_Deliver_message_to_Captain_Seelig"
	LynchMission1.Init(
		priv, [InSystemCondition("Gemini/New_Constantinople","New_constantinople")], [], LYNCH_SPRITE, GoToSubnode(0,AddPythonSprite("miggs",MIGGS_SPRITE,MIGGS_POSITION,MIGGS_WIDTH_HEIGHT,MIGGS_LABEL,MIGGS_SCRIPT)), None, [
		MakeMission(priv, # Creates any type of mission
		LYNCH_SPRITE, # Campaign, sprite
		[InSystemCondition("Gemini/New_Constantinople","New_constantinople")], # Where fixer meets you to start the mission
		[InSystemCondition("Gemini/New_Constantinople","New_constantinople")], # Where the mission ends.
		None, # Adds Miggs' sprite. This is a special case.
		None, # Script to be run to start the mission (usually None if you don't have a script. Do NOT load an ambush mission here.)
		'ambush',(priv.name+"_mission",("Gemini/Pentonville",),0,['seelig','pirates_'],[1,2],['talon','talon.blank'],["Captain_Seelig","Seelig's_goon"],
			[("#996600I'm looking for a Captain Seelig.",True,"campaign/Seelig.wav"),
			("#669900Nice ship, Captain. How about a little tour?"),
			("#996600Sorry, but we have other business right now.",True),
			("#996600Okay, you got my attention. What do you want?"),
			("#dd2200Roman Lynch is very disappointed in you.",True),
			("#bb4400He is, is he? Want to hear our response?"),
			("#996600Yes",True),
			("#bb4400Well, here it comes"),
			("#ff0000How's that for a message, errand boy?")],('Gemini/XXN-1927', 'Gemini/119ce', 'Gemini/Pentonville'),'Jump_To_119CE'), # Mission arguments.
		priv.name+"_mission", # Script to be set on completion. -1=Failure, 0=Not Accepted, 1=Succeed, 2=In progress
		lynch1, # Dictionary containing what the fixer says.
		None, # If you reject the mission twice. "None" means that he continues asking you forever until you accept
		CampaignEndNode(priv), # If you lose the mission
		LynchMission2, # If you win the mission. Usually points to the next mission
		None, # The current mission node.
		mission_desc) # Name that describes the mission in flight and in the mission computer.
		])
	
	mission_desc="Lynch_2:_Transport_weapons"
	LynchMission2.Init(
		priv, [InSystemCondition("Gemini/New_Constantinople","New_constantinople")], [], LYNCH_SPRITE, GoToSubnode(0,AddPythonSprite("miggs",MIGGS_SPRITE,MIGGS_POSITION,MIGGS_WIDTH_HEIGHT,MIGGS_LABEL,MIGGS_SCRIPT)), None, [
		MakeCargoMission(priv, # Creates a cargo mission
		LYNCH_SPRITE, # Campaign, sprite
		[InSystemCondition("Gemini/New_Constantinople","New_constantinople")], # Where fixer meets you to start the mission
		[InSystemCondition("Gemini/Rikel","agricultural")], # Where the mission ends. Usually the same as starting point for next fixer.
		AddCredits(10000), # Script to be run as you click on the fixer. A common use is to AddCredits() for the previous mission.
		LoadMission(mission_desc,"ambush",(priv.name+"_mission",("Gemini/Rikel"),0,['kroiz','hunter_'],[1,2],['demon','demon.blank'],['Salman_Kroiz',"Kroiz's_associate"],
			[("I say, would you kindly identify yourself?",False,"campaign/Kroiz1.wav"),
			("I've never been that kind to strangers.",True),
			("I am Salman Kroiz, Privateer Extraordinaire. Terribly sorry to interrupt your flight, but it seems as if we're a bit at odds, here."),
			("You represent one of Lynch's rivals?",True),
			("I'm to prevent you from delivering those weapons. Since we both cannot fulfil our contracts, it seems we'll need to settle this ourselves. Would you consider dumping your cargo?"),
			("Nope.",True),
			("Alas, we'll have to settle this by violent means."),
			(),
			("So sorry, but I'm afraid I cannot let you pass. Now my operatives and I will end your career and bolster our resumes in the process. Cheers!"),
			("Oh, this is most distasteful, I must say.")],['Gemini/New_Detroit', 'Gemini/Rikel'], 'Siva')),
		("Weapons",10), # Mission arguments.
		priv.name+"_mission", # Script to be set on completion. -1=Failure, 0=Not Accepted, 1=Succeed, 2=In progress
		lynch2, # Dictionary containing what the fixer says.
		None, # If you reject the mission twice. "None" means that he continues asking you forever until you accept
		CampaignEndNode(priv), # If you lose the mission
		LynchMission3) # If you win the mission. Usually points to the next mission
		])
	
	mission_desc="Lynch_3:_Smuggle_Regis"
	LynchMission3.Init(
		priv, [InSystemCondition("Gemini/New_Constantinople","New_constantinople")], [], LYNCH_SPRITE, GoToSubnode(0,AddPythonSprite("miggs",MIGGS_SPRITE,MIGGS_POSITION,MIGGS_WIDTH_HEIGHT,MIGGS_LABEL,MIGGS_SCRIPT)), None, [
		MakeCargoMission(priv, # Creates a cargo mission
		LYNCH_SPRITE, # Campaign, sprite
		[InSystemCondition("Gemini/New_Constantinople","New_constantinople")], # Where fixer meets you to start the mission
		[InSystemCondition("Gemini/Castor","Romulus")], # Where the mission ends. Usually the same as starting point for next fixer.
		AddCredits(15000), # Script to be run as you click on the fixer. A common use is to AddCredits() for the previous mission.
		LoadMission(mission_desc,"ambush",(priv.name+"_mission",("Gemini/Castor"),0,'confed_',5,'stiletto','Executioner',
			[("We know you are transporting a known felon. Prepare to die, criminal scum!",False,"campaign/FelonM.wav"),
			("A life sentence doesn't look so bad now, eh Regis?")],['Gemini/Junction', 'Gemini/Castor'], 'Romulus')),
		("Lynch's_cousin_Regis",1), # Mission arguments.
		priv.name+"_mission", # Script to be set on completion. -1=Failure, 0=Not Accepted, 1=Succeed, 2=In progress
		lynch3, # Dictionary containing what the fixer says.
		None, # If you reject the mission twice. "None" means that he continues asking you forever until you accept
		CampaignEndNode(priv), # If you lose the mission
		LynchMission4) # If you win the mission. Usually points to the next mission
		])
	
	#################### FIXME: Mission 3: Should be Regis. Escaped Political Prisoners was as close as I can get to this.
	
	mission_desc="Lynch_4:_Meet_\"Smythe\""
	MakeVariableMission(priv, # Creates any type of mission
		LYNCH_SPRITE, # Campaign, sprite
		[InSystemCondition("Gemini/New_Constantinople","New_constantinople")], # Where fixer meets you to start the mission
		[InSystemCondition("Gemini/Oxford","Oxford")], # Where the mission ends.
		AddCredits(30000), # Money money money moneymoneymoneymoney $$$$$$ !!!!
		LoadMission(mission_desc,'ambush',(priv.name+"_mission",('Gemini/Newcastle'),0,['miggs','pirates_'],[1,4],['orion','talon.blank'],['Miggs','Henchman'],
			[("Hey, bright boy, guess who's in deep trouble? Mr Lynch wants that artifact. I'm gonna count to ten. Then I start shootin'. One, two, uh... Forget this! Start shootin' boys!",False,"campaign/Miggs.wav"),
			("#996600Miggs, is that you?",True),
			("Heh, heh! Wiseguy thinks he's winnin'.",False),
			(),
			("Oh... wrong button...")],['Gemini/Newcastle'],'Jump_To_New_Constantinople')), # script to be run.
		priv.name+"_mission", # Script to be set on completion. -1=Failure, 0=Not Accepted, 1=Succeed, 2=In progress
		lynch4, # Dictionary containing what the fixer says.
		None, # If you reject the mission twice. "None" means that he continues asking you forever until you accept
		CampaignEndNode(priv), # If you lose the mission
		LynchFinish, # If you win the mission. Usually points to the next mission
		LynchMission4) # The current mission node.
	
	LynchFinish.Init(priv,
		[],
		[],
		None,
		GoToSubnode(0,SetSaveVariable('access_to_library',2.000000)),
		None,
		[MastersonMission1])
	
	mission_desc="Masterson_1:_Escort_Hunter_Toth"
	MakeMission(priv, # Creates any type of mission
		None, # Campaign, sprite
		[InSystemCondition("Gemini/Oxford","Oxford")], # Where fixer meets you to start the mission
		[InSystemCondition("Gemini/Oxford","oxford")], # Where the mission ends.
		None, # Script to add your credits
		None, # Script to be run to start the mission (usually None if you don't have a script. Do NOT load an ambush mission here.)
		'escort_local',('retro_',0,2,1,3000,0,True,'toth',(),priv.name+"_mission","Critic_of_Prometheus_Unplugged",'talon.blank','Hunter_Toth', 'drayman',[("Hunter Toth! You are hereby sentenced to death for your heresy. The execution should commence now.",False,"campaign/ExecutionF.wav")]), # Mission arguments.
		priv.name+"_mission", # Script to be set on completion. -1=Failure, 0=Not Accepted, 1=Succeed, 2=In progress
		masterson1, # Dictionary containing what the fixer says.
		None, # If you reject the mission twice. "None" means that he continues asking you forever until you accept
		CampaignEndNode(priv), # If you lose the mission
		MastersonMission2, # If you win the mission. Usually points to the next mission
		MastersonMission1, # The current mission node.
		mission_desc # Name that describes the mission in flight and in the mission computer.
		)
	
	mission_desc="Masterson_2:_Destroy_hackers"
	MakeMission(priv, # Creates any type of mission
		None, # Campaign, sprite
		[InSystemCondition("Gemini/Oxford","Oxford")], # Where fixer meets you to start the mission
		[InSystemCondition("Gemini/Oxford","oxford")], # Where the mission ends.
		AddCredits(10000,AdjustRelation('pirates','privateer',-2)), # Script to add your credits
		None, # Script to be run to start the mission (usually None if you don't have a script. Do NOT load an ambush mission here.)
		'bounty_leader',(0,0,0,False,4,'pirates_',(),priv.name+"_mission",'Black_Rhombus','galaxy.blank',False,'Hacker','talon.blank',[("Oxford has no right to hoard data! Access is ours!",False,"campaign/SlicerM.wav"),"Knowledge belongs to the galaxy, you #ff999ffascist!"],["tungsten","tungsten_hull"]), # Mission arguments.
		priv.name+"_mission", # Script to be set on completion. -1=Failure, 0=Not Accepted, 1=Succeed, 2=In progress
		masterson2, # Dictionary containing what the fixer says.
		None, # If you reject the mission twice. "None" means that he continues asking you forever until you accept
		CampaignEndNode(priv), # If you lose the mission
		MastersonMission3, # If you win the mission. Usually points to the next mission
		MastersonMission2, # The current mission node.
		mission_desc # Name that describes the mission in flight and in the mission computer.
		)

	############## FIXME: Mission 2: Black Rhombus (Galaxy) is defended by 7 Talons, not 7 Galaxies. ###############

	mission_desc="Masterson_3:_Escort_freighter"
	MakeMission(priv, # Creates any type of mission
		None, # Campaign, sprite
		[InSystemCondition("Gemini/Oxford","Oxford")], # Where fixer meets you to start the mission
		[InSystemCondition("Gemini/Oxford","oxford")], # Where the mission ends.
		AddCredits(10000,AdjustRelation('pirates','privateer',2)), # Script to add your credits
		None, # Script to be run to start the mission (usually None if you don't have a script. Do NOT load an ambush mission here.)
		'escort_local',('hunter_',0,2,2,3000,0,True,'merchant__',(),priv.name+"_mission","Book_thief",'demon',"Vulcan's_Forge",'drayman',[("Those books go in my hold or up in flames.",False,"campaign/BooksM.wav")]), # Mission arguments.
		priv.name+"_mission", # Script to be set on completion. -1=Failure, 0=Not Accepted, 1=Succeed, 2=In progress
		masterson3, # Dictionary containing what the fixer says.
		None, # If you reject the mission twice. "None" means that he continues asking you forever until you accept
		CampaignEndNode(priv), # If you lose the mission
		MastersonMission4, # If you win the mission. Usually points to the next mission
		MastersonMission3, # The current mission node.
		mission_desc # Name that describes the mission in flight and in the mission computer.
		)

	mission_desc="Masterson_4:_Save_freighter"
	MakeMission(priv, # Creates any type of mission
		None, # Campaign, sprite
		[InSystemCondition("Gemini/Oxford","Oxford")], # Where fixer meets you to start the mission
		[InSystemCondition("Gemini/Oxford","oxford")], # Where the mission ends.
		AddCredits(10000), # Script to add your credits
		None, # Script to be run to start the mission (usually None if you don't have a script. Do NOT load an ambush mission here.)
		'escort_local',('pirates_',0,3,1,3000,0,True,'merchant__',(),priv.name+"_mission",'Raider','talon.blank','Supply_freighter','drayman'), # Mission arguments.
		priv.name+"_mission", # Script to be set on completion. -1=Failure, 0=Not Accepted, 1=Succeed, 2=In progress
		masterson4, # Dictionary containing what the fixer says.
		None, # If you reject the mission twice. "None" means that he continues asking you forever until you accept
		CampaignEndNode(priv), # If you lose the mission
		MastersonFinish, # If you win the mission. Usually points to the next mission
		MastersonMission4, # The current mission node.
		mission_desc # Name that describes the mission in flight and in the mission computer.
		)

	MastersonFinish.Init(priv,
		[InSystemCondition("Gemini/Oxford","Oxford")],
		mastersonhelp,
		None,
		GoToSubnode(0,AdjustRelation('hunter','privateer',-1.25,SetSaveVariable('access_to_library',1.000000,AddCredits(10000,AddTechnology("merchant"))))),
		None,
		[MonkhouseIntro])

	MonkhouseIntro.Init(priv,
		[],
		[],
		None,
		TrueSubnode(),
		None,
		[CampaignClickNode().Init(priv,
			[InSystemCondition("Gemini/Palan","Palan")],
			monkhouseintro,
			MONKHOUSE_PALAN_SPRITE,
			TrueSubnode(),
			MonkhouseIntro,
			[]),
		MurphyMission1])

	mission_desc="Murphy_1:_Stop_blockade_reinforcements"
	MakeMission(priv, # Creates any type of mission
		MURPHY_SPRITE, # Campaign, sprite
		[InSystemCondition("Gemini/Palan","Basra")], # Where fixer meets you to start the mission
		[InSystemCondition("Gemini/Palan","Basra")], # Where the mission ends.
		None, # Script to add your credits
		None, # Script to be run to start the mission (usually None if you don't have a script. Do NOT load an ambush mission here.)
		'defend',('hunter_',0,3,5000,123456.789,0,False,True,'merchant',(),priv.name+"_mission",'Blockader','demon','Palan',1), # Mission arguments.
		priv.name+"_mission", # Script to be set on completion. -1=Failure, 0=Not Accepted, 1=Succeed, 2=In progress
		murphy1, # Dictionary containing what the fixer says.
		None, # If you reject the mission twice. "None" means that he continues asking you forever until you accept
		CampaignEndNode(priv), # If you lose the mission
		MurphyMission2, # If you win the mission. Usually points to the next mission
		MurphyMission1, # The current mission node.
		mission_desc # Name that describes the mission in flight and in the mission computer.
		)

	mission_desc="Murphy_2:_Intercept_patrol"
	MakeMission(priv, # Creates any type of mission
		MURPHY_SPRITE, # Campaign, sprite
		[InSystemCondition("Gemini/Palan","Basra")], # Where fixer meets you to start the mission
		[InSystemCondition("Gemini/Palan","Basra")], # Where the mission ends.
		AddCredits(15000), # Script to add your credits
		None, # Script to be run to start the mission (usually None if you don't have a script. Do NOT load an ambush mission here.)
		'defend',('hunter_',0,2,5000,123456.789,0,False,True,'merchant',(),priv.name+"_mission",'Blockader','centurion.blank','Palan',3), # Mission arguments.
		priv.name+"_mission", # Script to be set on completion. -1=Failure, 0=Not Accepted, 1=Succeed, 2=In progress
		murphy2, # Dictionary containing what the fixer says.
		None, # If you reject the mission twice. "None" means that he continues asking you forever until you accept
		CampaignEndNode(priv), # If you lose the mission
		MurphyMission3, # If you win the mission. Usually points to the next mission
		MurphyMission2, # The current mission node.
		mission_desc # Name that describes the mission in flight and in the mission computer.
		)

	############# FIXME: Mission 2: "Upon reaching Nav one you are greeted by an inital wave of 3 Demons. These are soon backed up by 4 Centurions."

	mission_desc="Murphy_3:_Break_the_blockade"
	MakeMission(priv, # Creates any type of mission
		MURPHY_SPRITE, # Campaign, sprite
		[InSystemCondition("Gemini/Palan","Basra")], # Where fixer meets you to start the mission
		[InSystemCondition("Gemini/Palan","Basra")], # Where the mission ends.
		AddCredits(10000), # Script to add your credits
		LaunchWingmen("militia__","talon.blank",2), # Script to be run to start the mission (usually None if you don't have a script. Do NOT load an ambush mission here.)
		'defend',('hunter_',0,5,5000,123456.789,0,False,True,'merchant',(),priv.name+"_mission",'Blockader','demon','Palan',0), # Mission arguments.
		priv.name+"_mission", # Script to be set on completion. -1=Failure, 0=Not Accepted, 1=Succeed, 2=In progress
		murphy3, # Dictionary containing what the fixer says.
		None, # If you reject the mission twice. "None" means that he continues asking you forever until you accept
		CampaignEndNode(priv), # If you lose the mission
		MurphyFinish, # If you win the mission. Usually points to the next mission
		MurphyMission3, # The current mission node.
		mission_desc # Name that describes the mission in flight and in the mission computer.
		)

	MurphyFinish.Init(priv,
		[InSystemCondition("Gemini/Palan","Basra")],
		murphyfinish,
		MURPHY_SPRITE,
		GoToSubnode(0,ChangeSystemOwner("Gemini/Palan","merchant",AddCredits(15000))),
		None,
		[MonkhouseMission1])
	
	mission_desc="Monkhouse:_Relocate_Mission"
	MakeCargoMission(priv, # Creates a cargo mission
		MONKHOUSE_PALAN_SPRITE, # Campaign, sprite
		[InSystemCondition("Gemini/Palan","Palan")], # Where fixer meets you to start the mission
		[InSystemCondition("Gemini/Palan","Basra")], # Where the mission ends. Usually the same as starting point for next fixer.
		None, # Script to be run as you click on the fixer. A common use is to AddCredits() for the previous mission.
		LoadMission(mission_desc,'ambush',(priv.name+"_mission",('Gemini/Palan'),25,'kilrathi_',3,'dralthi','Kilrathi_kidnapper',[("Apeling, you are entirely in our power.",False,"campaign/MonkhouseWanted.wav"),"You will surrender him to us immediately or be destroyed","Monkhouse, surrender and be spared"],['Gemini/Palan'], 'Basra')), # Script to be run to start the mission (usually None if you don't have a script, but ambush is also common.)
		("Dr_Monkhouse",1), # Mission arguments.
		priv.name+"_mission", # Script to be set on completion. -1=Failure, 0=Not Accepted, 1=Succeed, 2=In progress
		monkhouse1, # Dictionary containing what the fixer says.
		None, # If you reject the mission twice. "None" means that he continues asking you forever until you accept
		CampaignEndNode(priv), # If you lose the mission
		MonkhouseFinish, # If you win the mission. Usually points to the next mission
		MonkhouseMission1) # The current mission node.

	MonkhouseFinish.Init(priv,
		[InSystemCondition("Gemini/Palan","Basra")],
		monkhouseinfo,
		MONKHOUSE_SPRITE,
		GoToSubnode(0,AddRemovingSprite("artifact_2", ARTIFACT2_SPRITE, ARTIFACT_POSITION, ARTIFACT_SIZE, "Put_Away_the_Artifact", AddCargo('Artifact',1,True,AddCredits(5000,AddTechnology("hunter"))))),
		None,
		[CrossMission1])
	
	mission_desc="Taryn_1:_Explore_Delta"
	MakeVariableMission(priv, # Creates any type of mission
		CROSS_SPRITE, # Campaign, sprite
		[InSystemCondition("Gemini/Rygannon","Rygannon")], # Where fixer meets you to start the mission
		[InSystemCondition("Gemini/Rygannon","Rygannon")], # Where the mission ends.
		None, # Add your moneys
		LoadMission(mission_desc,'patrol_enemies',(1,3,10,0,('Gemini/Delta',),priv.name+"_mission",2,4,0.7,0.0,'pirates_',True, "Delta_bandit", {"addall":["nav"],"add":["Nav_2"]}), LoadMission(mission_desc,'ambush',(priv.name+"_mission",('Gemini/Delta',),0,'pirates_',3,'talon.blank','Delta_bandit',[("Shoulda stuck to your charts: it's dangerous out here!",False,"campaign/ChartsM.wav")], ['Gemini/Delta'], 'Gemini/Delta'))), # script to be run.
		priv.name+"_mission", # Script to be set on completion. -1=Failure, 0=Not Accepted, 1=Succeed, 2=In progress
		taryn1, # Dictionary containing what the fixer says.
		None, # If you reject the mission twice. "None" means that he continues asking you forever until you accept
		CampaignEndNode(priv), # If you lose the mission
		CrossMission2, # If you win the mission. Usually points to the next mission
		CrossMission1) # The current mission node.

	mission_desc="Taryn_2:_Explore_Beta"
	MakeVariableMission(priv, # Creates any type of mission
		CROSS_SPRITE, # Campaign, sprite
		[InSystemCondition("Gemini/Rygannon","Rygannon")], # Where fixer meets you to start the mission
		[InSystemCondition("Gemini/Rygannon","Rygannon")], # Where the mission ends.
		AddCredits(10000), # Add your moneys
		LoadMission(mission_desc,'patrol_enemies',(2,3,10,0,['Gemini/Delta', 'Gemini/Beta'],priv.name+"_mission",2,3,0.5,0.0,'retro_',True, "Raving_lunatic", {"addall":["nav"]}), LoadMission(mission_desc,'ambush',(priv.name+"_mission",('Gemini/Beta',),0,'garrovick',1,'centurion.blank','Garrovick',[
			("#669900Unidentified vessel, request status.",True,"campaign/Garrovick.wav"),
			("#bb4400Damn you! Keep back!", False),
			("#996600No... #ff999FNO!", False),
			("#996600Is that any way to greet your saviour?",True),
			("#dd2200Stay away! You hear me? #ff999ABACK OFF!", False),
			("#669900I mean you no harm.",True),
			("#669900Do you require assistance?",True),
			("#ff0000All right... you asked for it!", False),
			("#ff0000Vicious bastard! Murderer! I'll show you!", False)], ['Gemini/Delta', 'Gemini/Beta'], 'Gemini/Beta'))), # script to be run.
		priv.name+"_mission", # Script to be set on completion. -1=Failure, 0=Not Accepted, 1=Succeed, 2=In progress
		taryn2, # Dictionary containing what the fixer says.
		None, # If you reject the mission twice. "None" means that he continues asking you forever until you accept
		CampaignEndNode(priv), # If you lose the mission
		CrossMission3, # If you win the mission. Usually points to the next mission
		CrossMission2) # The current mission node.

#FIXME: it would be sweet to make it possible to tractor ejected Garrovick as a bonus objective.

	mission_desc="Taryn_3:_Explore_Gamma"
	MakeVariableMission(priv, # Creates any type of mission
		CROSS_SPRITE, # Campaign, sprite
		[InSystemCondition("Gemini/Rygannon","Rygannon")], # Where fixer meets you to start the mission
		[InSystemCondition("Gemini/Rygannon","Rygannon")], # Where the mission ends.
		AddCredits(10000), # Add your moneys
		LoadMission(mission_desc,'patrol_enemies',(3,3,10,0,['Gemini/Delta', 'Gemini/Beta', 'Gemini/Gamma'],priv.name+"_mission",3,4,0.8,0.0,'kilrathi_',True, "Kilrathi_scout", {"addall":["nav"]}), LoadMission(mission_desc,'ambush',(priv.name+"_mission",('Gemini/Gamma',),0,'kilrathi_',6,'dralthi','Scout_party',[], ['Gemini/Delta', 'Gemini/Beta', 'Gemini/Gamma'], 'Gemini/Gamma'))),
		priv.name+"_mission", # Script to be set on completion. -1=Failure, 0=Not Accepted, 1=Succeed, 2=In progress
		taryn3, # Dictionary containing what the fixer says.
		None, # If you reject the mission twice. "None" means that he continues asking you forever until you accept
		CampaignEndNode(priv), # If you lose the mission
		CrossMission4, # If you win the mission. Usually points to the next mission
		CrossMission3) # The current mission node.

	######## FIXME: Mission 3: "At Nav 2, you'll find an initial force of 4 Dralthi, followed by 3 Gothri, and then another 3 Dralthi. This is on top of random pirate and Kilrathi forces at other Nav points."

	mission_desc="Taryn_4:_Explore_Delta_Prime"
	MakeVariableMission(priv, # Creates any type of mission
		CROSS_SPRITE, # Campaign, sprite
		[InSystemCondition("Gemini/Rygannon","Rygannon")], # Where fixer meets you to start the mission
		[InSystemCondition("Gemini/Rygannon","Rygannon")], # Where the mission ends.
		AddCredits(10000,AdjustRelation('unknown','privateer',-2,SetSaveVariable('privateer_drone_active',1.000000))), # Add your moneys
		LoadMission(mission_desc,"directions_mission",(priv.name+"_mission",['Gemini/Delta', 'Gemini/Beta', 'Gemini/Gamma', 'Gemini/Delta_Prime'], "Jump_To_Gamma")), # script to be run.
		priv.name+"_mission", # Script to be set on completion. -1=Failure, 0=Not Accepted, 1=Succeed, 2=In progress
		taryn4, # Dictionary containing what the fixer says.
		None, # If you reject the mission twice. "None" means that he continues asking you forever until you accept
		CampaignEndNode(priv), # If you lose the mission
		CrossFinish, # If you win the mission. Usually points to the next mission
		CrossMission4) # The current mission node.
	
	CrossFinish.Init(priv,
		[InSystemCondition("Gemini/Rygannon","Rygannon")],
		taryninfo,
		CROSS_SPRITE,
		GoToSubnode(0,AddCredits(10000,AddTechnology("militia"))),
		None,
		[GoodinMission])

	mission_desc="Terrell:_Ambush_drone"
	MakeCargoMission(priv, # Creates a cargo mission
		GOODIN_SPRITE, # Campaign, sprite
		[NotCondition(InSystemCondition("Gemini/Rygannon")),InSystemCondition(None,"mining_base")], # Where fixer meets you to start the mission
		[InSystemCondition("Gemini/Perry","Perry")], # Where the mission ends. Usually the same as starting point for next fixer.
		SetSaveVariable('terrell_no_entry',2.0), # Script to be run as you click on the fixer. A common use is to AddCredits() for the previous mission.za
		LoadMission(mission_desc,"ambush",(priv.name+"_mission",("Gemini/Tingerhoff"),5,'retro_',4,'talon','Retro_enforcer',
			[("Sinner! Ready thyself for righteous retribution! We know you possess high-level alien devices, machines of damnable intent! For adding to the technological burden of mankind, the Church Of Man condemns you! In the moments left to you, repent!",False,"campaign/TechnologyF.wav"),
			("I'll slow roast your guts!",True)],['Gemini/Perry'], 'Perry_Naval_Base')),
		("Goodins_orders",1), # Mission arguments.
		priv.name+"_mission", # Script to be set on completion. -1=Failure, 0=Not Accepted, 1=Succeed, 2=In progress
		goodin, # Dictionary containing what the fixer says.
		None, # If you reject the mission twice. "None" means that he continues asking you forever until you accept
		CampaignEndNode(priv), # If you lose the mission
		TerrellMission, # If you win the mission. Usually points to the next mission
		GoodinMission) # The current mission node.

	mission_desc="Steltek:_Destroy_drone"
	MakeMission(priv,
		None, # Campaign, sprite
		[InSystemCondition("Gemini/Perry","Perry")], # Where fixer meets you to start the mission
		[InSystemCondition("Gemini/Perry","Perry")], # Where the mission ends.
		None, # Add your moneys
		None, # script to be run.
		'defend_drone',('steltek_fighter','steltek','Gemini/Nitir','drone','unknown',10,'confed__',('Gemini/Nitir','Gemini/Blockade_Point_Tango'),priv.name+"_mission", steltekhelptext), # Mission arguments.
		priv.name+"_mission", 
		terrell, # Dictionary containing what the fixer says.
		None, # If you reject the mission twice. "None" means that he continues asking you forever until you accept
		CampaignEndNode(priv), # If you lose the mission
		TerrellFinish, # If you win the mission. Usually points to the next mission
		TerrellMission, # The current mission node.
		mission_desc # Name that describes the mission in flight and in the mission computer.
		)

	TerrellFinish.Init(priv,
		[],
		None,
		None,
		GoToSubnode(0,Cutscene('Final Cutscene','OutroCutscene.spr',(0,0),(2,1.24),'Steltek Captures Drone',['                                     ','                                                       ','                                                 ','  Meanwhile....','                                                       '],'end.m3u','perry.m3u')),
		None,
		[CampaignClickNode().Init(priv,
			[InSystemCondition("Gemini/Perry","Perry")],
			terrellsuccess,
			None,
			TrueSubnode(AddCredits(30000,AddTechnology("confed"))),
			None,
			[CampaignEndNode(priv)])]) # YOU WIN!!!

	return priv #return the newly created campaign back.

class StealGun(InSystemCondition):
	def __init__(self,guntype,system,shipname):
		InSystemCondition.__init__(self,system,shipname)
		self.guntype=guntype
		self.stoleit=False
	def __call__(self):
		import VS
		print "CHECKING INSYSTEM COND"
		if (InSystemCondition.__call__(self)):
			print "CHECKING GUN"
			if (VS.getPlayer().removeWeapon(self.guntype,0,True)!=-1):
				import universe
				universe.addTechLevel("tech",False)
				#add sprite!
				import quest
				quest.removeQuest(VS.getCurrentPlayer(),"removed_"+self.guntype,1)
				print "REMOVED GUN"
				self.stoleit=True
				return True
			else:
				print "CANNOT REMOVE GUN"
		import quest
		if (quest.checkSaveValue(VS.getCurrentPlayer(),"removed_"+self.guntype,1)):
			return True
		return False


def LoadRFMurphyCampaign():
	MURPHY_SPRITE = ("murphy.spr", "Talk_To_Murphy","bases/heads/murphy.spr")
	rf=Campaign("rf_murphy_campaign")
	MurphyMission1=CampaignClickNode()
	MurphyMission2=CampaignClickNode()
	MurphyMission3=CampaignClickNode()
	MurphyMission4=CampaignClickNode()
	murphy1 = {'failure': murphyfailure, 'intro': [('Murphy', 'Hey, Privateer!'), ('Burrows', 'Long time no see, Lynn.'), ('Murphy', 'Murphy to you. You want a job?'), ('Burrows', "Let's hear what you've got."), ('Murphy', "Pirate activity in 44-P-1M has had several major corporations worried for a long time. But now the Retros are showing up too, and the interested parties want to act before it's too late. Your job is to patrol 44-P-1M and destroy all pirate and Retro craft encountered. Come back here afterwards. After I take my cut of the proceeds, you'll get 10000."), ('Burrows', 'Just how big is your cut?'), ('Murphy', "That's not your concern. 10000 for an easy patrol. How about it?")], 'reconsider': [('Murphy', "Back again... That didn't take long."), ('Burrows', 'I may accept your insignificant little mission, Murphy, but first I want some courtesy and some details.'), ('Murphy', 'All right. Go to 44-P-1M. Patrol the system, destroying all pirates and Retros. Return here afterwards for 10000.')], 'reject1': [('Burrows', 'No thanks.'), ('Murphy', 'Your loss, ace.')], 'reject2': [('Burrows', 'Courtesy and details both lacking. Forget it.')], 'reminder': [('Murphy', "What's the deal... You still haven't done the mission."), ('Burrows', 'I may be reconsidering. Give me the details again.'), ('Murphy', 'All right. Go to 44-P-1M. Patrol the system, destroying all pirates and Retros. Return here afterwards for 10000.')], 'accept': [('Burrows', 'Sounds good to me.'), ('Murphy', 'Good. Enjoy the cruise.')]}
	murphy2 = {'failure': murphyfailure, 'intro': [('Murphy', "Good work. It's always nice to see a patrol mission get done right."), ('Burrows', 'That was a piece of cake, Murphy. You have anything a little more challenging?'), ('Murphy', 'Plenty. How about a blockade busting mission?'), ('Burrows', 'Tell me more.'), ('Murphy', "The Corcoran Corporation runs the biggest operation on the Liverpool refinery. It's in the Newcastle system. Recently, an unknown band has blockaded Liverpool. Ore and construction equipment are in very short supply. Corcoran wants a blockade-runner to deliver a shipment of ore and construction supplies."), ('Burrows', 'How bad is the blockade?'), ('Murphy', "Nothing you can't handle, I'm sure. I'll give you 20000 for the mission.")], 'reconsider': [('Murphy', 'Liverpool is in bad shape, they need those supplies.'), ('Burrows', "We'll see. Give me the details again."), ('Murphy', 'Deliver ore and construction cargo to Liverpool in Newcastle. Return here afterwards for 20000.')], 'reject1': [('Murphy', 'Cold feet, huh... I understand.')], 'reject2': [('Murphy', "No deal, huh... When the ship dealers start running out of spare parts, don't come crying to me.")], 'reminder': [('Murphy', "Corcoran Corporation's screaming about their supplies. What's going on?"), ('Burrows', 'I had some business to attend to. Tell me about the mission again.'), ('Murphy', 'Deliver ore and construction cargo to Liverpool in Newcastle. Return here afterwards for 20000.')], 'accept': [('Burrows', 'Liverpool, here I come.')]}
	murphy3 = {'failure': murphyfailure, 'intro': [('Murphy', "The Corcoran Corporation is pleased with your work. Now they've got enough supplies to finish their next major order. I hope the mission wasn't too hard on you."), ('Burrows', "You'll have to come up with more than that to scare me."), ('Murphy', "I think I can, as a matter of fact. There's another, tougher Retro patrol around New Detroit. They're laying siege to the base, trying to keep out consumer goods. The Retros aren't about to make New Detroit submit, but they are scaring away most merchants and driving consumer prices way up."), ('Burrows', "And that's where I come in."), ('Murphy', "Right. You're to deliver a cargo of generic and luxury foods. The pay is, believe it or not, 30000."), ('Burrows', '30000 for a food run... Wow.')], 'reconsider': [('Murphy', 'Changed your mind?'), ('Burrows', "Maybe. Let's hear the mission again."), ('Murphy', 'Deliver generic and luxury foods through a Retro blockade to New Detroit. Return here afterwards for 30000.')], 'reject1': [('Murphy', 'Not ready for the big leagues, ace?')], 'reject2': [('Murphy', 'The Retro threat is only going to get worse.')], 'reminder': [('Murphy', "You don't get any money until you deliver the food."), ('Burrows', "I understand. Let's hear the deal again."), ('Murphy', 'Deliver generic and luxury foods through a Retro ambush to New Detroit. Return here afterwards for 30000.')], 'accept': [('Burrows', "You know I wouldn't pass up a deal like that.")]}
	murphy4 = {'failure': murphyfailure, 'intro': [('Burrows', "Well, the food's delivered, but you and I both know it's just a drop in the bucket."), ('Murphy', 'I thought you were just in it for the money.'), ('Burrows', 'Yeah, I guess I mostly am. Speaking of which, any more jobs?'), ('Murphy', "Yes. I've got one more I'm willing to give you. It's a tough one."), ('Burrows', 'Go on.'), ('Murphy', "Pirate and Retro activity is wreaking havoc on the Metsor system. Several major corporations, who wish to remain anonymous, have offered big bucks to whoever clears out the system. I won their contract, and I'm offering you 50000 to do the job. Destroy all pirates and Retros in the Metsor system. Return here afterwards.")], 'reconsider': [('Burrows', 'Has anyone else taken the mission yet?'), ('Murphy', "It's still yours, if you want it. Want the details again?"), ('Burrows', 'Yeah.'), ('Murphy', 'Destroy all pirate and Retro vessels in the Metsor system. Return here afterwards for 50000. Simple, but not easy.')], 'reject1': [('Murphy', '50000, ace. See where else you can get a deal like that.')], 'reject2': [('Burrows', "Not right now. I'll keep it in mind, though.")], 'reminder': [('Murphy', "You can't accept a job like this and then forget about it. Powerful corporations hire powerful bounty hunters."), ('Burrows', "I'll take my chances. Tell me the story again."), ('Murphy', 'Destroy all pirate and Retro vessels in the Metsor system. Return here afterwards for 50000.')], 'accept': [('Burrows', "50000. I can't believe a skinflint like you would cough up that much cash. But I'll be happy to relieve you of it.")]}

	rf.Init(MurphyMission1)

	mission_desc="Murphy_1:_Patrol"
	MakeMission(rf,
		MURPHY_SPRITE,
		[InSystemCondition("Gemini/New_Constantinople","Edom"),SaveVariableCondition("gun_stolen",1.0)],
		[InSystemCondition("Gemini/New_Constantinople","Edom")],
		None,
		None,
		'patrol',(0,8,50,0,('Gemini/44-p-im',),rf.name+"_mission"),
		rf.name+"_mission",
		murphy1,
		None,
		CampaignEndNode(rf),
		MurphyMission2,
		MurphyMission1, # The current mission node.
		mission_desc # Name that describes the mission in flight and in the mission computer.
		)

	mission_desc="Murphy_2:_Blockade_runner"
	MakeCargoMission(rf,
			MURPHY_SPRITE,
			[InSystemCondition("Gemini/New_Constantinople","Edom")],
			[InSystemCondition("Gemini/Newcastle","Liverpool")],
			AddCredits(10000),
			LoadMission(mission_desc,"ambush",(rf.name+"_mission",("Gemini/Newcastle",),0,'hunter_',8,'demon','',['Privateer, do not attempt to run the blockade.','We will shoot you if you attempt to engage us in this system. Retreat now!'],['Gemini/Newcastle'], 'Liverpool')), # Script to be run to start the mission (usually None if you don't have a script, but ambush is also common.) (having no destination will call significant unit.. oakham should be the only dockable significant in that system)
			("Ore_Supplies",10),
			rf.name+"_mission",
			murphy2,
			None,
			CampaignEndNode(rf),
			MurphyMission3,
			MurphyMission2)

	mission_desc="Murphy_3:_Break_siege"
	MakeCargoMission(rf,
			MURPHY_SPRITE,
			[InSystemCondition("Gemini/New_Constantinople","Edom")],
			[InSystemCondition("Gemini/New_Detroit","New_Detroit")],
			AddCredits(20000),
			LoadMission(mission_desc,"ambush",(rf.name+"_mission",("Gemini/New_Detroit",),0,'retro_',8,'talon.blank','',['Heathen! Do not attempt to deliver your goods to the industrialized world below.','Leave now or God will have no mercy on your soul.','Your death is at hand'],['Gemini/New_Detroit'], 'New_Detroit')), # Script to be run to start the mission (usually None if you don't have a script, but ambush is also common.) (having no destination will call significant unit.. oakham should be the only dockable significant in that system)
			("Luxury_Food",30),
			rf.name+"_mission",
			murphy3,
			None,
			CampaignEndNode(rf),
			MurphyMission4,
			MurphyMission3)

	mission_desc="Murphy_4:_Clean_sweep"
	MakeMission(rf,
		MURPHY_SPRITE,
		[InSystemCondition("Gemini/New_Constantinople","Edom")],
		[InSystemCondition("Gemini/New_Constantinople","Edom")],
		AddCredits(30000),
		None,
		'cleansweep',(0,8,50,0,('Gemini/Newcastle','Gemini/Metsor',),rf.name+"_mission",1,2,.9,0,['unknown','retro_','pirates_'],1,1),#FIXME needs testing!
		rf.name+"_mission",
		murphy4,
		None,
		CampaignEndNode(rf),
		CampaignClickNode().Init(rf,
					[InSystemCondition("Gemini/New_Constantinople","Edom")],
					[("Murphy","That's all the work I have for you right now. I do have a standing offer, though. There's this guy named Menesch. You may hear about him in your travels. I've heard the Confederation is offering a big bounty on him. If you ever get around to collecting it, come back here and I'll supplement the bounty by 20000. That guy's been a thorn in my side for a long time. Anyway, thanks again. See you."),("Burrows","Menesch, huh? I'll remember that.")],
					MURPHY_SPRITE,
					GoToSubnode(0,IncSaveVariable('rf_recs',AddCredits(50000))),
					None,
					[CampaignClickNode().Init(rf,
						[InSystemCondition("Gemini/New_Constantinople","Edom"),SaveVariableCondition("menesch_dead",1)],
						[("Murphy","Good to see you again. Here's the 20000 I promised you. Don't spend it all in one place."),("Burrows","Thanks."),("Murphy","By the way, I've heard the Confeds are also offering a bounty. You might want to go to Perry and see what's up. I'll see you around.")],
						MURPHY_SPRITE,
						GoToSubnode(0),
						None,
						[CampaignEndNode(rf)])]),
		MurphyMission4, # The current mission node.
		mission_desc # Name that describes the mission in flight and in the mission computer.
		)
	return rf

INFORMANT_SPRITE=("informant.spr","Talk_To_Informant")
def MakeDrakePirateNode(rf,creds,contingency=None):
	IDIOT_SPRITE=("informant.spr","Talk_To_Faithful")
	WinRF=CampaignClickNode()
	WinInformant=CampaignClickNode()
	SelectWinningNode=CampaignNode()
	WinRF.Init(rf,
		[InSystemCondition("Gemini/Perry","Perry"),SaveVariableCondition("jones_dead",1.0)],
		[("Terrell","Brilliant work. Gemini and the Confederation owe you another debt. It's too bad so few people know about your heroic actions. If they did, you'd be the most popular man in Gemini."),("Burrows","Flattery will get you nowhere, Admiral. I'm not going to join the Navy. End of story."),("Terrell","Maybe not, but who knows what the future will bring? Anyway, I assume you've been paid?"),("Burrows","Yes I have, and I think I'm going to take a holiday."),("Terrell","Good. You certainly deserve it. Goodbye, son. You have my eternal respect and gratitude.")],
		None,
		TrueSubnode(AddCredits(creds,ChangeSystemOwner("Gemini/Eden","unknown"))),
		None,
		[CampaignEndNode(rf)])
	WinInformant.Init(rf,
		[InSystemCondition("Gemini/Capella","Drake"),SaveVariableCondition("jones_dead",1.0)],
		[("Informant","Greetings. I thank you for your service. But I must also warn you that I am once again your mortal enemy. I am a man of my word, and will carry out my promise. All plans and copies of the Steltek gun will be destroyed. In return, you must refrain from revealing the location of Eden to the Confederation."),("Burrows","The Confederation would pay a lot for that information. What's to stop me?"),("Informant","Only the threat of vengeance. And your conscience, if you have one. Our acquaintance has been brief, and we will not meet again. Farewell, infidel.")],
		INFORMANT_SPRITE,
		GoToSubnode(0),
		None,
		[WinRF])
	JonesBountyMissionNode = CampaignNode()
	mission_desc = "Kill_Mordecai_Jones"
	return CampaignClickNode().Init(rf,
				[InSystemCondition("Gemini/Capella","Drake")],
				[("Burrows","You were looking for me?"),("Informant","Yes, I'm glad you've come. Normally, I'd consider a privateer like you far too risky to confide in. But your recent destruction of Kahl and Menesch gives me faith in your trustworthiness. My clothing belies my true calling. I am a member of the Church of Man."),("Burrows","Go on."),("Informant","I am one of Mordecai Jones' elite counsellors. I, like all my brethren, have sworn to accomplish the destruction of all technology. And I believe that our ends justify the means we use. What do you think?"),("Burrows","Sorry, but I think you guys are nuts."),("Informant","So I expected. But our interests may coincide for a little while. Let me tell you the story of Mordecai Jones. He was an unknown when he joined the Church of Man five years ago. He started as a ship technician, but by virtue of his astounding eloquence and technical skill, he quickly attained a position of leadership. Within a year, he commanded a church battalion. Within three years, he was an Elite Guard Commander. He was soon in a position equal to my own. When his holiness Father Benengeli, the previous church leader, died a year ago, it was revealed that he had appointed Mordecai Jones as his successor. Jones' leadership brought the church a stunning string of victories. He provided us with new Kilrathi ships and stronger arms. And, of course, our new secret weapon. I believe it is known to you."),("Burrows","My gun?"),("Informant","Yes. The Steltek super-weapon. Church engineers have already learned how to duplicate it. The copies have been used experimentally. Mass production is imminent. I don't believe your Confederation can withstand such a powerful force."),("Burrows","That's for sure. But I thought you were disgruntled. This whole situation seems perfect for you."),("Informant","Oh, it is. The average churchman's dreams seem about to be realised. But my high rank gives me access to some closely guarded secrets. Six months ago, I accidentally came upon some transmissions from Jones to Governor Menesch. They mentioned 'The Ulterior Motive'. A plan I had never heard of. My suspicions were aroused. Further research revealed the nature of this plan. In summary, it led to Jones' domination of Gemini, and gave Menesch a great deal of power and wealth. When the entire region was secure, Jones would dismantle the Church of Man. He planned to use churchmen as a police force. No ultimate destruction of technology. Only megalomania. It's an old story. Somehow, though, I'm surprised that it's worked again."),("Burrows","That's some pretty wild stuff."),("Informant","It is. I have taken a leave of absence from my church duties, hoping to find some means of stopping Jones. Time is short. But I think you can save us. I have a plan."),("Burrows","Save you? So that you can wipe out the Confederation anyway? No thanks. I like my electric razors and my holo-vids."),("Informant","I understand your concern. So I'll offer you a deal. If you succeed in destroying Jones, I give you my word that we will destroy all copies of the Steltek gun. Additionally, your name will be removed from the church hit list."),("Burrows","Pretty crazy. Your word is all I have."),("Informant","That is true. Of course, during the mission you will discover our headquarters. If you wish, you can inform the Confederation and they can eventually destroy it. We will be forced to relocate. Very costly and disruptive. But it's worth it to me."),("Burrows","Why me? Why not take this to the Confederation?"),("Informant","A large fleet would be detected too far in advance. The jump tunnel could be blocked. There is no other pilot in Gemini with your reputation for success. I'm afraid you are my only hope."),("Burrows","What are the details of the mission?"),("Informant","You are to fly to the Valhalla system. There is a secret jump tunnel there."),("Burrows","'Secret'? How does that work?"),("Informant","We have contacts at the Exploratory Services. They have removed it from official records. Do not worry. I will enter the co-ordinates into your ship's navigation system. After locating the tunnel, you must jump to a new system called Eden. There you will find Jones and members of his elite guard. You must destroy them all. Return here afterwards.")],
				INFORMANT_SPRITE,
				GoToSubnode(0),
				contingency,
				[JonesBountyMissionNode.Init(rf,[],[],None,TrueSubnode(),None,
					[SelectWinningNode.Init(rf,
							[SaveVariableCondition("jones_dead",1.0)],
							[],
							None,
							TrueSubnode(),
							None,
							[WinRF,
								WinInformant,
								CampaignClickNode().Init(rf,
									[InSystemCondition("Gemini/Eden")],
									["Alas! Woe to us all! Our leader has been stricken down! His mighty temple, destroyed. You have survived and returned for initiation, but in vain. The light shines in the temple no longer.",("Burrows","Darn. Guess I'd better be going, then"),"The tears of the faithful will flood the land. A new, dark age has risen for the Church of Man. Will we survive? I do not know"],
									None,
									GoToSubnode(0),
									SelectWinningNode,
									[CampaignNode().Init(rf,[],[],None,TrueSubnode(),
										WinInformant,
										[WinInformant,WinRF])]
								)]),
					CampaignClickNode().Init(rf,
						[InSystemCondition("Gemini/Eden"),NotCondition(SaveVariableCondition("jones_dead",1.0))],
						["Greetings, convert! Welcome to the bliss of Eden. There is no suffering here. Your clothing is strange. You have just arrived, yes? You may be initiated in the temple.",("Burrows","I see. Thank you."),"Ah, soon the glory of the Church of Man will spread throughout the stars. Soon our great leader will vanquish the infidels and bring us peace.",("Burrows","Um, may I ask a question about our great leader?"),"Of course, of course!",("Burrows","Where is he? I was, er, supposed to fly with him, but I have been left behind."),"He flies directly towards our beautiful grey moon. Perhaps you should do the same. Alas that your initiation will be postponed.",("Burrows","Yeah, alas."),"Farewell. I must return to my meditation."],
						IDIOT_SPRITE,
						TrueSubnode(LoadMission(mission_desc,"bounty_leader",(0,0,0,0,6,"retro_",(),"jones_dead",'',"centurion.blank",0,"","salthi",[("#ff4400Trespasser! You fly in sacred space!",False,"campaign/Jones.wav"),"The Church of Man is mighty!","We will not tolerate the transgressions, of those serving a false god!","Soon, all of Gemini will be wiped clean, with our Righteous Fire!","#ff4400Fool! My elite guards cannot be defeated!"],[("steltek_gun",0),("steltek_gun",1),("steltek_gun",2),("steltek_gun",3),"isometal","plasteel_hull"],True))),
						JonesBountyMissionNode,[JonesBountyMissionNode])])])
						
def LoadRFLynchCampaign():
	rf=Campaign("rf_lynch_campaign")
	LYNCH_SPRITE = ("lynch.spr","Talk_To_Lynch","bases/heads/lynch.spr") #sprite file for the fixer
	LynchSeed = CampaignClickNode()
	rf.Init(LynchSeed)
	KilledHim=CampaignChoiceNode()
	KillOrPay=CampaignClickNode()
	HaveCreditsClear=CampaignChoiceNode()
	LynchSeed.Init(rf,
		[NotCondition(SaveVariableCondition("menesch_dead",1)),
			InSystemCondition("Gemini/Pyrenees","Basque"),
#			OrCondition(SaveVariableCondition("rf_recs",2), #no longer necessary
#				OrCondition(
#					SaveVariableCondition("rf_recs",3),
#					SaveVariableCondition("rf_recs",4))),
			],
		[("Lynch","It's always a pleasure to see old acquaintances."),
			("Burrows","You're a mean man, Lynch."),
			("Lynch","Yes I am. I hope your encounter with Miggs was not too disturbing. I see from your success that you are a man to be taken seriously."),
			("Burrows","Quite."),
			("Lynch","You know, I believe there's some work you could do for me. There's this fellow called Governor Menesch. Perhaps you've heard of him. Recently, he's been cutting deep into my business. He's been supplying the Retros with ships, weapons, and other goods. My profits have fallen accordingly. I would like you to kill him."),
			("Burrows","You're nuts, Lynch. Go stick your head in a pig."),
			("Lynch","Wait a second. I can offer you more than money. I don't know what your current status with the various Gemini groups is, but since you're a rough-and-tumble privateer, I bet it's not too pretty. Pirates troubling you? Get caught with contraband too many times?"),
			("Burrows","What are you getting at, ugly boy?"),
			("Lynch","If you destroy Menesch, I'll take care of wiping all your records. Militia, Confed, pirates, merchants, and bounty hunters. They'll all become your outer-space pals again. How can you refuse?"),
			("Burrows","If I wanted to help you, where would I find Menesch?"),
			("Lynch","That information I do not have. He's operating out of the Clarke quadrant. That's about all I know. If and when you get him, come back here. We'll talk. Of course, you should feel free to come back sooner. I'll be happy to clear your record at any time for the nominal fee of 200000.")],
		LYNCH_SPRITE,
		TrueSubnode(),
		None,
		[KillOrPay.Init(rf,
				[InSystemCondition("Gemini/Pyrenees","Basque")],
				[],
				LYNCH_SPRITE,
				TrueSubnode(),
				None,
				[KilledHim.Init(rf,
					[SaveVariableCondition("menesch_dead",1),InSystemCondition("Gemini/Pyrenees","Basque"),NotCondition(SaveVariableCondition("rf_lynch_used_freebie",1.0))],
					[("Lynch","Congratulations. You have killed Menesch, as I asked. It may surprise you, but I am going to live up to my word. At your command, I will wipe your records. The Militia, Confeds, pirates, merchants, and bounty hunters. They will all forget about your transgressions.")],
					LYNCH_SPRITE,
					KillOrPay,
					[((NO_SPRITE,"Refuse_Offer"),CampaignNode().Init(rf,
						[],
						[("Lynch","As you wish. If you should change your mind, my offer stands.")],
						LYNCH_SPRITE,
						GoToSubnode(0),
						KilledHim,
						[KilledHim])),
					((YES_SPRITE,"Accept_Offer"),CampaignNode().Init(rf,
						[],
						[("Lynch","As you wish. Note that I am willing to clear your records at any time. If you should be in need of a clean slate again in the future, come back here. I'll do the job for 200000.")],
						LYNCH_SPRITE,
						GoToSubnode(0,SetSaveVariable("rf_lynch_used_freebie",1.0,ClearRecord())),
						KillOrPay,
						[KillOrPay]))]),
				HaveCreditsClear.Init(rf,
					[InSystemCondition("Gemini/Pyrenees","Basque"),HaveCredits(200000)],
					[("Lynch","Hello again. I have an offer for you. Thanks to my connections with various Gemini data management gurus, I have gained access to a great deal of heavily protected information. Some of it relates to you. Are you still having trouble with Confeds? Militia? Any of the Gemini sector organisations?"),("Burrows","Maybe."),("Lynch","Then consider my offer. For 200000 I will clear your records. All Gemini groups will forget about your hostile behaviour. You will be surrounded by friends again. Sweet offer, isn't it? Bear in mind, if you ever manage to bump off my arch-rival, Governor Menesch, come back here and I'll happily wipe your record for free.")],
					LYNCH_SPRITE,
					KillOrPay,
					[((NO_SPRITE,"Refuse_Offer"),CampaignNode().Init(rf,
						[],
						[("Burrows","Not a chance, Lynch. Too much money, and besides I still don't trust you."),("Lynch","As you wish. If you should change your mind, my offer stands.")],
						LYNCH_SPRITE,
						TrueSubnode(),
						KillOrPay,
						[KillOrPay])),
					((YES_SPRITE,"Accept_Offer"),CampaignNode().Init(rf,
						[],
						[("Lynch","As you wish. Note that I am willing to clear your records at any time. If you should be in need of a clean slate again in the future, come back here. I'll do the job for 200000.")],
						LYNCH_SPRITE,
						TrueSubnode(RemoveCredits(200000,ClearRecord())),
						KillOrPay,
						[KillOrPay]))]),
				CampaignNode().Init(rf,
						[InSystemCondition("Gemini/Pyrenees","Basque"),NotCondition(HaveCredits(200000))],
						[("Lynch","Hello again. I have an offer for you. For 200000 I will clear your record with various Gemini groups including the Militia, Confeds, pirates, merchants, and bounty hunters. They will all forget about your hostile behaviour. You will be surrounded by friends again. Unfortunately, however, you don't have 200000. Come back when you're richer."),("Burrows","You're a weeny, Lynch.")],
						LYNCH_SPRITE,
						GoToSubnode(0),
						KillOrPay,
						[KillOrPay])])])
	return rf

def LoadRFGoodinCampaign():
	GOODIN_SPRITE = ("goodin.spr", "Talk_To_Goodin","bases/heads/goodin.spr")
	rf=Campaign("rf_goodin_campaign")
	GoodinMission1=CampaignClickNode()
	GoodinMission2=CampaignClickNode()
	GoodinMission3=CampaignClickNode()
	GoodinMission4=CampaignClickNode()
	GoodinMission5=CampaignClickNode()
	TerrellMission=CampaignClickNode()
	goodin1 = {'failure': goodinfailure, 'intro': [('Goodin', "Wow. It's been quite a while."), ('Burrows', 'Yes it has. How are you, Captain Goodin?'), ('Goodin', "The navy's been treating me pretty good. In fact, I think I stand a good chance at promotion next month. How's the privateer business?"), ('Burrows', 'I was taking an extended break, but it got cut short. Someone ripped off my Steltek gun.'), ('Goodin', 'Sounds like a serious blow. Do you know who?'), ('Burrows', "Not yet. That's what I'm aiming to find out."), ('Goodin', "Well, I'm afraid I don't have any info about stolen guns."), ('Burrows', "I know. I'm actually looking for work. I understand you guys have been giving a lot of contracts to privateers lately."), ('Goodin', "That's certainly true. With our forces spread so thin, we need all the help we can get. As a matter of fact, I do have a mission for you. Kilrathi activity has increased steadily in the last year. Many of our border bases are having a tough time of it. Nitir, an agriculture base in the Nitir system, is currently being harassed by the Kilrathi. Fly there and defend it from a Kilrathi attack. Then return here for 10000. Not much, but it should be pretty smooth sailing.")], 'reconsider': [('Goodin', "You're back. Want the mission?"), ('Burrows', 'What is it again?'), ('Goodin', 'Fly to Nitir, an agriculture base in the Nitir system. Defend it from a Kilrathi attack. Then return here for 10000.')], 'reject1': [('Burrows', 'No dice.'), ('Goodin', 'Whatever you say. We sure could use you, though.')], 'reject2': [('Burrows', 'No dice.')], 'reminder': [('Goodin', "You haven't finished the mission."), ('Burrows', 'What is it again?'), ('Goodin', 'Fly to Nitir, an agriculture base in the Nitir system. Defend it from a Kilrathi attack. Then return here for 10000.')], 'accept': [('Burrows', 'Okay.'), ('Goodin', 'See you soon.')]}
	goodin2 = {'failure': goodinfailure, 'intro': [('Burrows', "Well, that's that. The furballs didn't stand much chance."), ('Goodin', 'Good work. You interested in further missions?'), ('Burrows', 'Possibly.'), ('Goodin', 'I need you to fly to Charon in the Hyades system. Defend it from a Kilrathi attack. Then return here for 10000.'), ('Burrows', 'How can you afford to be so cheap with such a shortage of ships?'), ('Goodin', 'Believe me, there are plenty of hungry privateers out there.'), ('Burrows', "But they're not as good as me."), ('Goodin', 'Take it or leave it.')], 'reconsider': [('Goodin', "You're back. Want the mission?"), ('Burrows', 'What is it again?'), ('Goodin', 'Fly to Charon in the Hyades system. Defend it from a Kilrathi attack. Then return here for 10000.')], 'reject1': [('Burrows', "I'll leave it.")], 'reject2': [('Burrows', 'No dice.')], 'reminder': [('Goodin', "You haven't finished the mission."), ('Burrows', 'What is it again?'), ('Goodin', 'Fly to Charon in the Hyades system. Defend it from a Kilrathi attack. Then return here for 10000.')], 'accept': [('Burrows', "I'll take it.")]}
	goodin3 = {'failure': goodinfailure, 'intro': [('Goodin', 'Once again, good work.'), ('Burrows', 'Naturally. I presume you have some more missions?'), ('Goodin', "Certainly. We've managed to take the heat off a couple of bases, so now we can concentrate on reducing the Kilrathi presence in Confed space. Patrol the New Caledonia system. Patrol all nav points and destroy all Kilrathi vessels you encounter. Return here afterwards. The pay is 10000 again.")], 'reconsider': [('Goodin', "You're back. Want the mission?"), ('Burrows', 'What is it again?'), ('Goodin', 'Patrol the New Caledonia system. Destroy all Kilrathi vessels. Then return here for 10000.')], 'reject1': [('Burrows', 'Nope.')], 'reject2': [('Burrows', 'No dice.')], 'reminder': [('Goodin', "You haven't finished the mission."), ('Burrows', 'What is it again?'), ('Goodin', 'Patrol the New Caledonia system. Destroy all Kilrathi vessels. Then return here for 10000.')], 'accept': [('Burrows', 'Okay.')]}
	goodin4 = {'failure': goodinfailure, 'intro': [('Goodin', "Excellent. You really stuck it to them. You've been doing the Confederation a great service."), ('Burrows', "You know me. I'm all heart."), ('Goodin', "I've got one more mission for you. It's the toughest one we've got right now. We need to continue fighting the Kilrathi presence in Confed space. Fly to the Regallis system. Patrol all nav points. Destroy all Kilrathi vessels. Then return here for 10000.")], 'reconsider': [('Goodin', "You're back. Want the mission?"), ('Burrows', 'What is it again?'), ('Goodin', 'Patrol the Regallis system. Destroy all Kilrathi vessels. Then return here for 10000.')], 'reject1': [('Burrows', 'No thanks.'), ('Goodin', 'Chickening out, huh... Too bad.')], 'reject2': [('Burrows', 'No dice.')], 'reminder': [('Goodin', "You haven't finished the mission."), ('Burrows', 'What is it again?'), ('Goodin', 'Patrol the Regallis system. Destroy all Kilrathi vessels. Then return here for 10000.')], 'accept': [('Burrows', 'Sounds straightforward. See you soon.')]}
	goodin5={'failure': goodinfailure, 'intro': [('Goodin', 'Good day. I hope you remember me.'), ('Burrows', 'Of course, Captain Goodin.'), ('Goodin', "I'm very glad to see that Menesch is dead. You beat out a lot of other top-notch bounty hunters. I'm transferring the Confederation's 40000 bounty to your account."), ('Burrows', 'Good deal.'), ('Goodin', "I'd like to get right to business. As you know, the Confederation has spread its forces very thin in Gemini. Our fight against the Retros has greatly weakened our lines on the Kilrathi front, and the war there has become purely defensive."), ('Burrows', 'And you need all the help you can get.'), ('Goodin', "I'm afraid so. Incidentally, please remember that this conversation is strictly confidential."), ('Burrows', "I'll keep that in mind."), ('Goodin', "We are currently trying to secure the Blockade systems, and drive back Kilrathi intrusions there. We want your help at Blockade Point Alpha. I'm offering you 20000 to fly to Nav 1 there, and rendezvous with our Commodore Uhler. He will give you further instructions.")], 'reconsider': [('Goodin', 'Ah. Have you reconsidered?'), ('Burrows', "Maybe. Let's hear the story again."), ('Goodin', "We're trying to secure Blockade Point Alpha against further Kilrathi aggression. We want your help at Blockade Point Alpha. Fly to Nav 1 there and meet with Commodore Uhler. Follow his instructions, then return here for 20000.")], 'reject1': [('Goodin', 'I see. Remember, the instability in Gemini threatens everyone, including you.')], 'reject2': [('Goodin', 'I wish there was something I could say to change your mind.')], 'reminder': [('Goodin', "The Commodore's orders have not been carried out. The Kilrathi threat at Blockade Point Alpha remains. Let me remind you of your duties. Fly to Nav 1 at Blockade Point Alpha and meet with Commodore Uhler. Follow his instructions, then return here for 20000.")], 'accept': [('Goodin', 'Good. Embark as soon as you can.')]}
	terrell = {'failure': terrellfailure, 'intro': [('Terrell', 'Good day, privateer. I trust you remember me?'), ('Burrows', 'Naturally.'), ('Terrell', "I've been impressed by your recent efforts to help the Confederation. Captain Goodin's reports to me have been most positive. As I'm sure you have learned, the Retros have got out of hand. Their recent surge in activity is attributable to one Mordecai Jones. Stopping the threat means eliminating Jones. Unfortunately, we have very little information about his current location. Intelligence analysis indicates that he's operating from the Fariss quadrant. But that's all we know. Therefore, we'll begin a thorough search of Fariss. We'll comb each system until we find him."), ('Burrows', 'So how do I fit in?'), ('Terrell', "As you know, we've got nearly all our forces mobilised already. They're split between the Kilrathi and the Retros. We can only spare a handful of ships for the search. But a handful is not enough. Using Confederation ships alone, the search would take years. We need volunteers to beef up our search teams. That's how you fit in."), ('Burrows', 'What are you offering?'), ('Terrell', 'We need you to patrol Death, Pestilence, and War. You get 20000.'), ('Burrows', "That's an awful lot of space to cover in one flight."), ('Terrell', 'I know. You should fuel up at Macabee in Nexus before starting.')], 'reconsider': [('Terrell', 'Good to see you again. We need you badly. Let me describe my offer again. You are to patrol Death, Pestilence and War. I recommend you fuel up at Macabee in Nexus first. Return here afterwards. The pay is 20000.')], 'reject1': [('Terrell', "That's too bad. Our effort depends on you. Please reconsider.")], 'reject2': [('Terrell', 'I see. Then our cause is all but lost.')], 'reminder': [('Terrell', "What are you doing here... Your mission's not complete."), ('Burrows', 'I may be reconsidering. What are the details again?'), ('Terrell', 'You are to patrol Death, Pestilence and War. I recommend you fuel up at Macabee in Nexus first. Return here afterwards. The pay is 20000.')], 'accept': [('Terrell', "Good. Return here when you're done. We'll analyse your data and see if there's any place to attack.")]}

	rf.Init(CampaignNode().Init(rf,
					[InSystemCondition("Gemini/Perry","Perry"),SaveVariableCondition("gun_stolen",1.0)],
					[],
					GOODIN_SPRITE,
					TrueBackwardsSubnode(),
					None,
					[GoodinMission1,GoodinMission5]))

	mission_desc="Goodin_1:_Defend_Nitir"
	MakeMission(rf,
		GOODIN_SPRITE,
		[InSystemCondition("Gemini/Perry","Perry")],
		[InSystemCondition("Gemini/Perry","Perry")],
		None,
		None,
		'defend',('kilrathi_',0,2,5000,10000,0,False,False,'confed',('Gemini/Nitir',),rf.name+"_mission",'','gothri','',1),
		rf.name+"_mission",
		goodin1,
		None,
		CampaignEndNode(rf),
		GoodinMission2,
		GoodinMission1, # The current mission node.
		mission_desc # Name that describes the mission in flight and in the mission computer.
		)

	mission_desc="Goodin_2:_Defend_Charon"
	MakeMission(rf,
		GOODIN_SPRITE,
		[InSystemCondition("Gemini/Perry","Perry")],
		[InSystemCondition("Gemini/Perry","Perry")],
		AddCredits(10000),
		None,
		'defend',('kilrathi_',0,2,5000,10000,0,False,True,'confed',('Gemini/Surtur','Gemini/Blockade_Point_Charlie','Gemini/Hyades'),rf.name+"_mission",'','gothri','',1),
		rf.name+"_mission",
		goodin2,
		None,
		CampaignEndNode(rf),
		GoodinMission3,
		GoodinMission2, # The current mission node.
		mission_desc # Name that describes the mission in flight and in the mission computer.
		)

	mission_desc="Goodin_3:_Clean_Sweep"
	MakeMission(rf,
		GOODIN_SPRITE,
		[InSystemCondition("Gemini/Perry","Perry")],
		[InSystemCondition("Gemini/Perry","Perry")],
		AddCredits(10000),
		None,
		'cleansweep',(0,8,1500,0,('Gemini/Tingerhoff','Gemini/Nexus','Gemini/Capella','Gemini/Crab-12','Gemini/New_Caledonia'),rf.name+"_mission",1,2,.5,.125,"kilrathi_",0,0),
		rf.name+"_mission",
		goodin3,
		None,
		CampaignEndNode(rf),
		GoodinMission4,
		GoodinMission3, # The current mission node.
		mission_desc # Name that describes the mission in flight and in the mission computer.
		)

	mission_desc="Goodin_4:_Clean_Sweep"
	MakeMission(rf,
		GOODIN_SPRITE,
		[InSystemCondition("Gemini/Perry","Perry")],
		[InSystemCondition("Gemini/Perry","Perry")],
		AddCredits(10000),
		None,
		'cleansweep',(0,8,1500,0,('Gemini/Tingerhoff','Gemini/Nexus','Gemini/Capella','Gemini/Sherwood','Gemini/Regallis'),rf.name+"_mission",1,2,.5,.125,["unknown","kilrathi_"],1,0),
		rf.name+"_mission",
		goodin4,
		None,
		CampaignEndNode(rf),
		CampaignClickNode().Init(rf,
					[InSystemCondition("Gemini/Perry","Perry")],
					[("Burrows","Well, Regallis is free from the furball menace."),("Goodin","I've been informed. Excellent work. I don't have any more missions for you, but I do have a tip. The Confederation has posted a bounty for the death of Governor Menesch. You may have heard of him. He's done a lot of illegal dealing with the Kilrathi. If you ever come across him, destroy him. Come back here when you do, and I'll see you get the 40000 bounty."),("Burrows","Good deal.")],
					GOODIN_SPRITE,
					GoToSubnode(0,IncSaveVariable('rf_recs',AddCredits(10000))),
					None,
					[GoodinMission5]),
		GoodinMission4, # The current mission node.
		mission_desc # Name that describes the mission in flight and in the mission computer.
		)

	mission_desc="Goodin_5:_Assist_Commodore_Uhler"
	MakeMission(rf,
		GOODIN_SPRITE,
		[InSystemCondition("Gemini/Perry","Perry"),SaveVariableCondition("menesch_dead",1)],
		[InSystemCondition("Gemini/Perry","Perry")],
		AddCredits(40000,SetSaveVariable('terrell_no_entry',2.0)),
		None,
		"cleansweep_escort",(0,6,1500,0,('Gemini/Ragnarok','Gemini/Blockade_Point_Alpha'),rf.name+"_mission",3,5,.5,.2,"kilrathi_",0,1,"confed__",[("Did someone mention Cats for dinner?",True,"campaign/Uhler1.wav"),("#00ff00Uhler: Good, our support has arrived. Listen up, there are Kilrathi en route."),("#00ff00Uhler: We'll proceed to Nav 5 and seal off the jump tunnel."),("#00ff00Uhler: We need your help to cover our flank. Clear the other three Nav points of all Kilrathi."),("#00ff00Uhler: And rendezvous with us at Nav 5. Patrol, move out.")],5,[("Hey, is catnip illegal on Kilrah?",True),("Kahl: This is Kahl, Commander of the Sixth Fleet. No doubt you've come in contact with the Kilrathi's latest weapon? Your Retros make it so easy for us. We provide a few ships, and watch death spread like an epidemic! Amusing, no? Apes killing hairy apes.",False,"campaign/Kahl.wav"),("Kahl: A pity you've wandered so far from your tree, Ape.",False),("You are no entirely at my mercy.",False),("Surrender or die, insufferable Earth-Monkey!",False)]),
		rf.name+"_mission",
		goodin5,
		None,
		CampaignEndNode(rf),
		CampaignClickNode().Init(rf,
					[InSystemCondition("Gemini/Perry","Perry")],
					[("Goodin","Good work. I'm frankly surprised you obeyed orders so well."),("Burrows","Cash helps put me in my place."),("Goodin","Admiral Terrell is impressed as well. In fact, he wants to see you right away. He's waiting for you in his office across the main concourse.","Burrows","I wonder what he wants this time."),("Goodin","I have no idea, so it must be pretty confidential. Good luck.")],
					GOODIN_SPRITE,
					GoToSubnode(0,AddCredits(20000)),
					None,
					[TerrellMission]),
		GoodinMission5, # The current mission node.
		mission_desc # Name that describes the mission in flight and in the mission computer.
		)
	ChoiceDrakeTerrell=CampaignNode()

	mission_desc="Terrel:_Search_for_retros"
	MakeMission(rf,
		None,
		[InSystemCondition("Gemini/Perry","Perry")],
		[SaveVariableCondition("rf_patrol_war",1.0),SaveVariableCondition("rf_patrol_death",1.0)],
		None,
		None,
		"tripatrol",(0,4,1650,2048,('Gemini/Tingerhoff','Gemini/Nexus','Gemini/Capella','Gemini/Famine','Gemini/Death','Gemini/Pestilence'),rf.name+"_mission",2,3,.66,0,["retro_","pirates_"],0,1,["[Static]",("#bb4400Hope you're not looking for trouble.",True),("#996600Pirate: Hey hot-shot, my employer wants to see you. He's waiting for you at Drake base, in the Capella system. He can't wait for long?",False,"campaign/Invitation.wav"),("#bb4400Who would employ you?",True),("#996600Pirate: I just get paid to deliver the message. I'm much more interested in your cargo. Fat cargo holds are hard to come by these days. Say, maybe you're carrying something good for me. Eh, sailor boy?"),("#bb4400Back off, I've got nothing for you!",True),("#996600Pirate: Well, we'll meet again. My manners end when you land on Drake. We'll see if you ever get to Drake!")]),
		rf.name+"_mission",
		terrell,
		None,
		CampaignEndNode(rf),
		ChoiceDrakeTerrell.Init(rf,
			[],
			[],
			None,
			TrueSubnode(),
			None,
			[MakeDrakePirateNode(rf,100000,ChoiceDrakeTerrell),CampaignClickNode().Init(rf,
				[InSystemCondition("Gemini/Perry","Perry"),SaveVariableCondition("rf_patrol_war",1.0),SaveVariableCondition("rf_patrol_death",1.0)],
				[("Terrell","Good work. Your data is complete. I'm afraid that there was no evidence of any bases in the systems you patrolled. You're not alone. All patrols so far have turned up nothing. All except the Epsilon group, which hasn't returned yet. They were sent to patrol 17-AR, J-900, Telar, and Valhalla. We've lost contact with them. I'm sending additional ships to look for them. Anyway, I want to thank you for your help, and to inform you that I'll pay you 80000 if you can somehow get rid of Jones. That's all. Goodbye.")],
				None,
				GoToSubnode(0,AddCredits(20000)),
				ChoiceDrakeTerrell,
				[MakeDrakePirateNode(rf,80000)])]),
		TerrellMission, # The current mission node.
		mission_desc # Name that describes the mission in flight and in the mission computer.
		)
	return rf

def LoadRFTaylaCampaign():
	TAYLA_SPRITE = ("tayla.spr","Talk_To_Tayla","bases/heads/taylapirate.spr") #sprite file for the fixer
	rf=Campaign("rf_tayla_campaign")
	TaylaMission1=CampaignClickNode()
	TaylaMission2=CampaignClickNode()
	TaylaMission3=CampaignClickNode()
	TaylaMission4=CampaignClickNode()
	TaylaMissionFinal=CampaignClickNode()
	tayla1 = {'failure': taylafailure, 'intro': [('Burrows', 'Hello, Tayla.'), ('Tayla', "Wow. I never expected to see you again. What's new?"), ('Burrows', 'The usual. Boy meets gun, boy blows up drone, boy loses gun, you know the story.'), ('Tayla', 'I heard. Say, you interested in some dirty work?'), ('Burrows', 'Probably.'), ('Tayla', "I could use you to deliver some personal cargo for me. I need it to go to Tuck in Sherwood. No contraband, and I'll make sure the pirates stay off your back. The job pays 10000. I'll meet you at Tuck. How about it?")], 'reconsider': [('Tayla', "I knew you'd come back."), ('Burrows', "Let's hear the specs again."), ('Tayla', "Here it is. You deliver some personal cargo for me to Tuck in Sherwood. There's no contraband, and I'll keep the pirates on your side. You get 10000, and I'll be at Tuck to greet you.")], 'reject1': [('Tayla', "Not good enough for you, huh... I know you. You'll change your tune.")], 'reject2': [('Tayla', 'Whatever you say.')], 'reminder': [('Tayla', "I see you still haven't delivered my goods to Tuck."), ('Burrows', 'I had some stuff to take care of. What was the plan again?'), ('Tayla', "Let me refresh your memory. Deliver some personal cargo for me to Tuck in Sherwood. There's no contraband, and I'll keep the pirates on your side. The pay is 10000. I'll be at Tuck to greet you. Once and for all, are you going to do it or not?")], 'accept': [('Tayla', 'Great. See you there.')]}
	tayla2 = {'failure': taylafailure, 'intro': [('Tayla', 'Congratulations, you finally made it.'), ('Burrows', "Yeah, yeah. Say, just what was that 'personal stuff, anyway?"), ('Tayla', "None of your business, naturally. And speaking of business, I've got a load of Brilliance for you to smuggle."), ('Burrows', "Great. There's nothing like running a gauntlet of self-righteous Confeds. Where's the Brilliance going?"), ('Tayla', 'A mining base in Prasepe called Saratov. It should be a piece of cake, if you can avoid contraband searches. Come back here for payment.'), ('Burrows', "What's the wages?"), ('Tayla', '20000. Deal?')], 'reconsider': [('Burrows', "Tayla, I've thought about your offer. Tell me the details again."), ('Tayla', "Take a load of Brilliance to Saratov base in Prasepe. Come back here and get 20000. It's that simple.")], 'reject1': [('Burrows', 'Sorry. Not my style.')], 'reject2': [('Tayla', 'Whatever.')], 'reminder': [('Tayla', "The boys on Saratov say they haven't got their Brilliance yet. What's the deal... Just bring the Brilliance to Saratov, and you get 20000. Are you going to do it?")], 'accept': [('Tayla', 'Good luck. See you soon.')]}
	tayla3 = {'failure': taylafailure, 'intro': [('Tayla', "You're back. Good work. I've got another Brilliance run for you, if you're interested."), ('Burrows', 'Tell me the payoff first.'), ('Tayla', '30000.'), ('Burrows', 'Go on.'), ('Tayla', 'Fly to Junction and deliver the stuff to Speke. Come back here for payment.'), ('Burrows', "Why aren't you giving any of these missions to your normal pirate pals?"), ('Tayla', "I think some of them are nervous about the increased Retro activity. Plus you've proven yourself more reliable."), ('Burrows', "I'm glad you've finally noticed."), ('Tayla', 'What do you say?')], 'reconsider': [('Tayla', 'Back so soon?'), ('Burrows', "Yeah, back so soon. Let's hear the deal again."), ('Tayla', 'Okay. For 30000, you deliver a cargo of Brilliance to Speke in Junction. Return here afterwards.')], 'reject1': [('Tayla', 'Seems strange to back out now, ace.')], 'reject2': [('Burrows', "Nope. Still don't want it.")], 'reminder': [('Tayla', "They haven't got the Brilliance yet. What's going on?"), ('Burrows', 'Yeah, I know. Sorry. I got side-tracked. Let me hear the scoop again.'), ('Tayla', "I don't know why, but I'll give you another chance. Take the load of Brilliance to Speke in Junction. That's it. The job pays 30000.")], 'accept': [('Tayla', 'Good luck.')]}
	tayla4 = {'failure': taylafailure, 'intro': [('Tayla', 'Excellent work. That last run made a lot of important people happy.'), ('Burrows', 'Swell. Then it was all worth while.'), ('Tayla', "I do have another run, if you're interested."), ('Burrows', 'Let me guess. Brilliance.'), ('Tayla', "Correct. Bring it to Basque base in the Pyrenees system. Pyrenees is quite a trip from here, and you'll be compensated accordingly: 40000. Come back here afterwards.")], 'reconsider': [('Burrows', 'Tell me about the mission again.'), ('Tayla', 'Okay. For 40000, you deliver a cargo of Brilliance to Basque in Pyrenees.')], 'reject1': [('Tayla', 'Too bad. 40000 would buy a lot of spare missiles, you know.')], 'reject2': [('Burrows', "Nope. Still don't want it.")], 'reminder': [('Tayla', "I hope you're not going to ask for payment, since you haven't made the delivery yet."), ('Burrows', 'Sorry. Are you still offering?'), ('Tayla', 'Yes, but only because of your past success. You are to take the Brilliance to Basque in Pyrenees for 40000. Decide carefully. Do you want the job?')], 'accept': [('Tayla', 'Good.')]}
	taylafinal=[("Tayla","Great job. You've made my friends on Basque very happy. Well, that's all the work I have for you. Be advised, though, I've got several contacts who are interested in your exploits. I'll make sure to put in a good word for you."),("Burrows","Great. Thanks.")]
	rf.Init(TaylaMission1)

	mission_desc="Tayla_1:_Deliver_personal_cargo"
	MakeCargoMission(rf,
			TAYLA_SPRITE,
			[InSystemCondition("Gemini/Pentonville","Oakham"),SaveVariableCondition("gun_stolen",1.0)],#where you get mission
			[InSystemCondition("Gemini/Sherwood","Tuck's")],#where mission ends
			ClearFactionRecord('pirates',1.0,PushRelation('pirates')),#Scriopt to be run after fixer clicks
			LoadMission(mission_desc,"directions_mission",(rf.name+"_mission",['Gemini/119ce', 'Gemini/Junction','Gemini/Nexus','Gemini/Capella','Gemini/Sherwood'],"Tuck's")), # Script to be run to start the mission (usually None if you don't have a script, but ambush is also common.) (having no destination will call significant unit.. oakham should be the only dockable significant in that system)
			("Tayla's_Personal_Goods",10),
			rf.name+"_mission",
			tayla1,#FIXME dictionary of speech
			None,
			CampaignEndNode(rf),
			TaylaMission2,
			TaylaMission1)

	mission_desc="Tayla_2:_Smuggle_to_Saratov"
	MakeCargoMission(rf,
			TAYLA_SPRITE,
			[InSystemCondition("Gemini/Sherwood","Tuck's")],#where you get mission
			[InSystemCondition("Gemini/Prasepe","Saratov")],#where you get mission
			AddCredits(10000),
			LoadMission(mission_desc,"ambush",(rf.name+"_mission",("Gemini/New_Caledonia",),0,'militia_',3,'talon','',['Filthy Little Brilliance Runner',"You're busted! The run stops here"],['Gemini/New_Caledonia', 'Gemini/Prasepe'], "Saratov")),
			("Brilliance",10),
			rf.name+"_mission",
			tayla2,
			None,
			CampaignEndNode(rf),
			TaylaMission3,
			TaylaMission2)

	mission_desc="Tayla_3:_Smuggle_to_Speke"
	MakeCargoMission(rf,
			TAYLA_SPRITE,
			[InSystemCondition("Gemini/Sherwood","Tuck's")],#where you get mission
			[InSystemCondition("Gemini/Junction","Speke")],#where you get mission
			AddCredits(20000),
			LoadMission(mission_desc,"ambush",(rf.name+"_mission",("Gemini/Capella","Gemini/Junction"),0,'militia_',4,'talon','',['Filthy Little Brilliance Runner',"You're busted! The run stops here"],['Gemini/Capella', 'Gemini/Nexus',"Gemini/Junction"], "Speke")),
			("Brilliance",20),
			rf.name+"_mission",
			tayla3,
			None,
			CampaignEndNode(rf),
			TaylaMission4,
			TaylaMission3)

	mission_desc="Tayla_4:_Smuggle_to_Basque"
	MakeCargoMission(rf,
			TAYLA_SPRITE,
			[InSystemCondition("Gemini/Sherwood","Tuck's")],#where you get mission
			[InSystemCondition("Gemini/Pyrenees","Basque")],#where you get mission
			AddCredits(30000),
			LoadMission(mission_desc,"ambush",(rf.name+"_mission",("Gemini/Regallis",),0,'militia_',4,'talon','',['Filthy Little Brilliance Runner',"You're busted! The run stops here"],['Gemini/Regallis', 'Gemini/Freyja',"Gemini/Pyrenees"], "Basque")),
			("Brilliance",25),
			rf.name+"_mission",
			tayla4,
			None,
			CampaignEndNode(rf),
			CampaignClickNode().Init(rf,
						[InSystemCondition("Gemini/Sherwood","Tuck's")],
						[("Tayla","Great job. You've made my friends on Basque very happy. Well, that's all the work I have for you. Be advised, though, I've got several contacts who are interested in your exploits. I'll make sure to put in a good word for you."),("Burrows","Great. Thanks.")],
						TAYLA_SPRITE,
						GoToSubnode(0,IncSaveVariable('rf_recs',AddCredits(40000,PopRelation('pirates')))),
						None,
						[CampaignEndNode(rf)]),
			TaylaMission4)
	return rf

def LoadRFCampaign():
	TAYLA_SPRITE = ("tayla.spr","Talk_To_Tayla","bases/heads/taylapirate.spr") #sprite file for the fixer
	MONTE_NEWDET_SPRITE = ("monte0.spr","Talk_To_Monte","bases/heads/montenewdetroit.spr") #sprite file for the fixer
	MONTE_MINING_SPRITE = ("monte1.spr","Talk_To_Monte","bases/heads/monte/monte.spr") #sprite file for the fixer
	INFORMANT_SPRITE = ("informant.spr","Talk_To_Informant","bases/heads/informant.spr")
	LYNCH_SPRITE = ("lynch.spr","Talk_To_Lynch","bases/heads/lynch.spr") #sprite file for the fixer
	MURPHY_SPRITE = ("murphy.spr", "Talk_To_Murphy","bases/heads/murphy.spr")
	rf=Campaign("rf_campaign")
	Theft=CampaignNode()
	MastersonMission1= CampaignClickNode()
	MastersonMission2= CampaignClickNode()
	MastersonMission3= CampaignClickNode()
	MastersonMission4= CampaignClickNode()
	MastersonMission5= CampaignClickNode()
	MastersonIntro=CampaignClickNode()
	MonteMission1 = CampaignClickNode()
	MonteMission2 = CampaignClickNode()
	MonteMission3 = CampaignClickNode()
	MonteMission4 = CampaignClickNode()
	montefailure=[("Monte","You could have done Gemini a great service. Too bad.")]
	monte1 = {'failure': montefailure, 'intro': [('Monte', 'Greetings. You must be that privateer.'), ('Burrows', "That's right. I was sent to see you by Masterson."), ('Monte', 'I know.'), ('Burrows', 'Just who are you?'), ('Monte', 'Call me Monte. The details of my identity do not concern you. I have information that you may find quite valuable, but I must request a few favours in exchange.'), ('Burrows', 'You want me to fly missions for you.'), ('Monte', 'Certainly. Some will be difficult, but I have faith in your abilities.'), ('Burrows', "Let's talk money. How much for the first job?"), ('Monte', "No money, I'm afraid. I'm a rather poor man."), ('Burrows', "I sympathise, but I can't afford to do charity work. Sorry."), ('Monte', 'Hold on, my friend. The information in my possession is more important than you realise. For example, I have been able to obtain a list of the Retros, most wanted enemies. It names the ten individuals who pose the greatest threat to the Retros, growing empire. Your name is on that list. The danger to your life becomes ever more serious. Your survival depends on the defeat of the Retros.'), ('Burrows', "Well, I'll hear you out. What's the first job?"), ('Monte', 'Quite simple. I desire safe transport to New Detroit. If you take me there, our discussions can proceed.')], 'reconsider': [('Monte', "I hope you've reconsidered. I would like safe transport to New Detroit. Take me there, and our discussions can proceed.")], 'reject1': [('Monte', 'Time is running out. Please reconsider.')], 'reject2': [('Monte', 'Remember, the Retros are not asleep.')], 'reminder': [('Monte', 'This is not New Detroit. Please take me there.')], 'accept': [('Monte', "Excellent. I'm ready to go.")]}
	monte2 = {'failure': montefailure, 'intro': [('Monte', 'Thank you for the transportation.'), ('Burrows', 'No problem. Tell me what you know.'), ('Monte', 'Patience. I receive my information slowly. Besides, it would be unwise to divulge all my knowledge immediately.'), ('Burrows', "I'm starting to wonder just how much you do know, pal."), ('Monte', "Let me try to pacify you. I know that the Retros have recently been united. This unity has given them the strength to begin their conquest. It has all been possible because of a strong new Retro leader, as you may have discovered. Probably no more than ten people in Gemini, including the Retros themselves, know the identity of this new leader. I am one of those ten. The leader's name is Mordecai Jones."), ('Burrows', "I don't care about his name. What do you know about him?"), ('Monte', 'Not much, admittedly. He is some sort of scientist or engineer. He became a Retro only recently. His organisation of the Retros has been astounding. I have never heard of any organisation going from disarray to power in such a short time.'), ('Burrows', "Yeah, I think he's swell, too. The question is, where is he?"), ('Monte', 'I do not know. But I may be able to find out soon.'), ('Burrows', 'How soon?'), ('Monte', 'Patience. First, you must fly another mission.'), ('Burrows', "I guess I'm at your mercy."), ('Monte', 'I want you to go to Drake in the Capella system. You will meet a man there. Follow his instructions. That is all.')], 'reconsider': [('Monte', 'You have returned. Will you accept my mission... I want you to fly to Drake in the Capella system, and carry out the instructions of the person you will meet there.')], 'reject1': [('Monte', 'I see. Then I can give you no further information.')], 'reject2': [('Burrows', 'I tire of your ramblings. Farewell.')], 'reminder': [('Monte', 'I have not heard from my associate. Apparently you have not completed his task.'), ('Burrows', 'Yeah, I guess not. Who was that again?'), ('Monte', 'He is on the Drake base in Capella. He will give you further instructions.')], 'accept': [('Monte', 'Good luck.')]}
	monte3 = {'failure': montefailure, 'intro': [('Monte', 'Excellent. You have made the delivery as requested. Now I will give you what little additional information I have. I was hoping to find out where Mordecai Jones resides. Unfortunately, I have not been given that information. I do know, however, that he has a secret base in Gemini. Inevitably, it is well guarded by the Retros.'), ('Burrows', "That's not much to go on, Monte."), ('Monte', "No, it isn't. I apologise. If I knew more, I would tell you."), ('Burrows', "If that's it, I guess I'll be going."), ('Monte', 'I do have one more request of you. I will pay this time.'), ('Burrows', 'And how much?'), ('Monte', "5000. It's not much, but it's all I have. I too am on the Retros, most wanted list. I'm not sure why. They may have found out about my information dealing. In any case, I need to travel to the Nexus system, but I have learned that a group of Retros awaits me there. I would like you to destroy those Retros. They should be waiting to surprise me at Nav 4."), ('Burrows', '5000 is not much money.'), ('Monte', 'There is more. I am about to receive additional information that will interest you. If you return here after completing the mission, I will give it to you. That is surely worth something.')], 'reconsider': [('Burrows', "I've reconsidered."), ('Monte', 'I see. Let me describe the mission again. Fly to Nav 4 in the Nexus system. Destroy the Retros you will find there. Return here afterwards for 5000 and additional information.')], 'reject1': [('Burrows', 'Your track record is too poor. Forget it.')], 'reject2': [('Burrows', "Sorry, Monte, I'm not interested.")], 'reminder': [('Monte', 'You have not completed my mission. I cannot help you until you help me.'), ('Burrows', 'Right. Where were the Retros again?'), ('Monte', 'They await me at Nav 4 in the Nexus system. I will give you 5000 and some useful information.')], 'accept': [('Burrows', "All right. I'll do it."), ('Monte', 'Wonderful. I await your safe return.')]}
	monte4 = {'failure': montefailure, 'intro': [('Monte', 'Fine work. I will be able to return to Nexus soon.'), ('Burrows', "Let's hear the information. What else do you know about Jones?"), ('Monte', "Nothing, I'm afraid. The knowledge I referred to earlier is not about Jones. It is about someone else you may have heard of, Governor Menesch."), ('Burrows', 'That name sounds familiar.'), ('Monte', "The man is a menace. Years ago, Menesch was governor of a base in a more populated system. As his influence grew, so did his lust for money. He had used his connections to sell Confederation ships, mostly Talons, to outlaw groups such as the pirates and the Retros. It's been years since his administration collapsed, and now, he's come out of hiding to do business in Gemini. It seems more than coincidence that your gun should disappear with Menesch around. I wouldn't put anything past him. If he can stoop to becoming the Retros main supplier, I wouldn't be surprised if he had connections with the Kilrathi."), ('Burrows', 'Sounds like true slime to me.'), ('Monte', "I'll give you this tip. If you want to get to Mordecai Jones, the first step is to destroy his supply line. Eliminate Menesch, and we'll see how the Retros get their weapons."), ('Burrows', 'I can only kill him if I can find him.'), ('Monte', "The best I can do is steer you in the right direction, if you're interested."), ('Burrows', 'Are you offering a bounty?'), ('Monte', 'No. If you complete the mission, I will return to Nexus and go into hiding. I understand, however, that there may be others in Gemini offering to pay a bounty. If I was a fighting man I would try to collect the bounties myself, but, do what you will with the information. The choice and risk are yours.')], 'reconsider': [('Monte', "Have you thought it over... Do you wish to accept... The mission is to kill Governor Menesch. I know he is currently in operation somewhere near the Troy system. If you don't find him in Troy, he's bound to be hiding out in one of the neighbouring systems. Of course, I can offer no reward, but others in Gemini are offering bounties. What do you say?")], 'reject1': [('Monte', 'I see. I will await your reconsideration.')], 'reject2': [('Burrows', "Not a chance, Monte. Ship maintenance isn't free, you know.")], 'reminder': [('Monte', "Menesch lives. Did you forget his location... I will repeat it. He is currently in operation somewhere near the Troy system. If you don't find him in Troy, he's bound to be hiding out in one of the neighbouring systems. Your mission is to destroy him.")], 'accept': [('Monte', "Unfortunately, I don't know his exact location, but I can tell you he is currently in operation somewhere near the Troy system. If you don't find him in Troy, he's bound to be hiding out in one of the neighbouring systems. I believe that if you patrol all those systems, you will be able to find him. I do not know how well he defends himself. Good luck, this may be our last meeting.")]}
	
	Monte=CampaignClickNode()
	masterson1 = {'failure': mastersonfailure, 'intro': [('Burrows', "Hello, Masterson. I've come looking for a little help."), ('Masterson', 'Great, we can use all the help we can get these days.'), ('Burrows', "You misunderstood. I'm looking for information that'll help me find my gun."), ('Masterson', "I heard news. I thought that gun was dangerous in your hands, but... Perhaps we can trade services. I have a friend who considers himself an expert on every fringe organisation in Gemini. He has his ear open to all underground activity, but, he's leery of meeting new people. Somewhat paranoid. I can't blame him. He's pretty unpopular from exposing certain groups. But, if you could help me out I would consider introducing you."), ('Burrows', "Meeting your friend doesn't sound too exciting, but I can check my own leads with your money. I hope you're not expecting charity work."), ('Masterson', "Well we are an academic institution, and rather needy at the moment. The constant threat from the Retros has us worried. We are disassembling the Oxford library. With the Retros on the rise, having all our knowledge in one place has become dangerous. We've become too big of a target. And with the Confederation occupied with the Kilrathi, we're virtually unprotected. I need you to deliver part of our rare books collection to a safer place, Base Edom in New Constantinople. The job pays 10000. Return here afterwards. How about it?")], 'reconsider': [('Masterson', "I had a hunch you'd return."), ('Burrows', 'Swell. Tell me about the mission again.'), ('Masterson', "You're to deliver a load of rare books to Base Edom in New Constantinople. Your reward will be 10000 credits.")], 'reject1': [('Masterson', "I know it's not many credits, but I'm offering extended employment, and the chance to meet an invaluable contact. We're desperate, but you would be crazy to pass up this opportunity. You'll be back.")], 'reject2': [('Masterson', "If you want to meet my contact, you'll have to fly my missions.")], 'reminder': [('Masterson', "I see you still haven't delivered my rare books. Why is that?"), ('Burrows', "Not your concern, Masterson. Let's hear the details again."), ('Masterson', "All right, then. You're to deliver a load of rare books to Base Edom in New Constantinople. It's that simple. Your reward will be 10000 credits.")], 'accept': [('Masterson', "Hurry back for more work, and I'll see about locating my friend.")]}
	masterson2 = {'failure': mastersonfailure, 'intro': [('Masterson', "Good to see you back. We've been needing your help."), ('Burrows', "Yeah, well, I didn't realise how dangerous research had become."), ('Masterson', 'The Retros are always at our throats trying to stop it, and the pirates trying to get to it. Which, of course, could mean money for you. We need someone to patrol Oxford.'), ('Burrows', "Well, I suppose I could take easy money from you. Don't you have less skilled help for your simple chores?"), ('Masterson', "The militia reinforcements are weeks late. They're in high demand these days. We need you to patrol each nav point, and eliminate any threats, fanatical or opportunistic. Come back here for payment."), ('Burrows', 'I could use the target practice, but not for free, of course.'), ('Masterson', 'I can offer the usual 10000.')], 'reconsider': [('Burrows', "Okay, Masterson, I've reconsidered. Tell me the details again."), ('Masterson', 'Patrol the nav points in Oxford. Destroy all Retro and pirate threats, and return for your 10000.')], 'reject1': [('Burrows', 'Sorry. Not my style.')], 'reject2': [('Masterson', "You must not value my opinion of your dependability. I'm sure my friend would not approve.")], 'reminder': [('Masterson', "Oxford Security reports increased activity in the system. Obviously, you've not held up your end of the deal."), ('Burrows', 'Could be temporary amnesia. What was I supposed to do?'), ('Masterson', 'Simply Patrol all nav points of Oxford system, and return for 10000. Deal?')], 'accept': [('Masterson', 'Good luck. See you soon')]}
	masterson3 = {'failure': mastersonfailure, 'intro': [('Burrows', "Hello, Masterson. I'm back."), ('Masterson', 'Great.'), ('Burrows', "What's next?"), ('Masterson', 'I need you to deliver part of our rare books collection to Burton in Junction. The job pays 10000. Return here afterwards. How about it?')], 'reconsider': [('Masterson', "I knew you'd come back."), ('Burrows', "Let's hear the specs again."), ('Masterson', 'Here it is. You deliver some books for me to Burton in Junction. You get 10000, and return here.')], 'reject1': [('Masterson', "I know you. You'll change your tune.")], 'reject2': [('Masterson', 'Whatever you say.')], 'reminder': [('Masterson', "I see you still haven't delivered books to Burton."), ('Burrows', 'I had a memory lapse. What was the plan again?'), ('Masterson', "Let me refresh your memory. Deliver rare books to Burton in Junction. The pay is 10000. I'll see you back here. Once and for all, are you going to do it or not?")], 'accept': [('Masterson', "Hurry back for more work and I'll see about locating my friend.")]}
	masterson4 = {'failure': mastersonfailure, 'intro': [('Masterson', "I don't have time to swap pleasantries. We have a freighter making the jump to Saxtogue from Nav 1, Oxford system. We're making a series of transports of library support machinery. We believe they could be in some danger from Retro attacks. Escort the freighter and make sure it jumps out safely and return here for your payment, along with more work."), ('Burrows', 'How long before they strike?'), ('Masterson', 'They could arrive at any moment. Please help. Surely, 10000 credits still interests you.')], 'reconsider': [('Masterson', 'Look, we need a freighter escort. Our freighters are sitting ducks without protection. The freighter is making the jump to Saxtogue at Nav 1, Oxford. I told you, if you want 10000 credits and an introduction to my friend, you need to defend it! Will you help us, or not?')], 'reject1': [('Burrows', "Shove off, pal. Consider this payback for all the flak you've given me."), ('Masterson', 'Unless you take this mission, consider our agreement terminated.')], 'reject2': [('Burrows', "Forget it, Masterson. This mission looks like a suicide run. I need the information, but it's only useful to me if I'm around to enjoy it.")], 'reminder': [('Masterson', "Of all the, what are you doing here... Our freighters are being attacked even now! Unless you hurry up, we won't get sufficient equipment for the reconstruction."), ('Burrows', 'Well, I...'), ('Masterson', 'What are you standing there for... Launch and escort our freighter to the jump point at Nav 1, or kiss your precious information good-bye. Please decide. Are you going to do it or not?')], 'accept': [('Burrows', "Okay, I'll save your equipment. But I'd better get a full letter of recommendation to your friend."), ('Masterson', "We'll see about that.")]}
	masterson5 = {'failure': mastersonfailure, 'intro': [('Burrows', "Hello, Masterson. I'm back."), ('Masterson', 'Great.'), ('Burrows', "What's next?"), ('Masterson', 'I need you to deliver our Twentieth Century Artwork collection to Perry Naval Base in Perry. The job pays 10000. Return here afterwards. How about it?')], 'reconsider': [('Masterson', "I knew you'd come back."), ('Burrows', "Let's hear the specs again."), ('Masterson', 'Here it is. You deliver artwork to Perry Naval Base in Perry. You get 10000, and return here.')], 'reject1': [('Masterson', "I know you. You'll change your tune.")], 'reject2': [('Masterson', 'Whatever you say.')], 'reminder': [('Masterson', "I see you still haven't delivered the artwork to Perry Naval Base."), ('Burrows', 'I had a memory lapse. What was the plan again?'), ('Masterson', "Let me refresh your memory. Deliver artwork to Perry Naval Base in Perry. The pay is 10000. I'll be see you back here. Once and for all, are you going to do it or not?")], 'accept': [('Masterson', "Great, I'll see about locating my friend.")]}

	informant1={"intro":[("Burrows","I represent Monte."),("Informant","Ah, good. My instructions are simple. Take these encrypted documents and deliver them to Monte. Simple enough?")],
		"accept":[("Burrows","Yes."),("Informant","Good. Make haste.")],
		"reject1":("Burrows","No"),
		"reject2":("Burrows","No I will not."),
		"reconsider":[("Informant","We cannot delay. Either take these encrypted documents and deliver them to Monte or get out of here. Simple enough?")],
		"reminder":[("Informant","You have not delievered the documents to Monte on New Detroit. Make haste!")],
		"failure":[("Informant","You are unworthy of my trust!")]}
	rf.Init(Theft)
	Theft.Init(rf,
		[StealGun("BoostedSteltek","Gemini/XXN-1927","Jolson")],
		['They stole my gun, my beautiful Steltek gun...'],
		None,
		GoToSubnode(0,Cutscene('Security','RighteousFireCutscene.spr',(0.582,-0.3),(3.104,1.2416),'They stole my gun',[
			("Location","Jolson Pleasure Base...                                   ","barspeech/campaign/rfintro.ogg"),
#			("One year later..."),
			("                                                                                                            "),
			("Robot","Attention please.                                                      "),
			("Burrows","Huh?                           "),
			("Robot","Base Command has instructed me to notify you of a recent theft.                                                      "),
			("Burrows","Theft? What are you talking about?                           "),
			("Robot","Unknown persons have tampered with a spaceship registered under your name. Analysis indicates that one cannon has been dismounted and taken. The ship is otherwise undamaged.                                                                                                                                          "),
			("Burrows","Which gun? Do you know which gun?                           "),
			("Robot","Your most recent docking record indicates that the stolen cannon is of an unregistered type.                                                      "),
			("Burrows","They stole my Steltek gun? I don't believe it.                           "),
			("Robot","A report is available at the Base Command offices.                           "),
			("Burrows","Listen, metal man, I don't think you understand me. That gun represents blood, sweat, and money! It's irreplaceable! And you bozos let somebody walk off with it? This is outrageous! I paid my docking fee for actual security, not some bunch of tin idiots! I ought to blow you to bits right here. In fact?                                                                                                                                                                                      "),
			("Robot","Desist.                           "),
			("Burrows","Then again, who am I to tell you how to do your job.                           "),
			("Robot","To file a security complaint, please begin by completing the appropriate forms. A Base Command representative will be able to help you. Have a pleasurable stay on Jolson.                                                      "),
			("Burrows","They stole my gun. My beautiful Steltek gun.")],"openrf.m3u","pleasure.m3u",SetSaveVariable('access_to_library',2.0000,SetSaveVariable('terrell_no_entry',1.0,SetSaveVariable('gun_stolen',1.0,AdjustRelation('retro','privateer',-2)))))),
		None,
		[MastersonMission1])

	mission_desc="Masterson_1:_Deliver_books_to_Edom"
	MakeCargoMission(rf,
			None,
			[InSystemCondition("Gemini/Oxford")],#where you get mission
			[InSystemCondition("Gemini/New_Constantinople","Edom")],#where mission ends
			None,#Scriopt to be run after fixer clicks
			LoadMission(mission_desc,"directions_mission",(rf.name+"_mission",['Gemini/XXN-1927', 'Gemini/New_Constantinople'], 'Edom')), # Script to be run to start the mission (usually None if you don't have a script, but ambush is also common.) (having no destination will call significant unit.. oakham should be the only dockable significant in that system)
			("Research",10),
			rf.name+"_mission",
			masterson1,#FIXME dictionary of speech
			None,
			CampaignEndNode(rf),
			MastersonMission2,
			MastersonMission1)

	mission_desc="Masterson_2:_Clean_sweep_of_Oxford"
	MakeMission(rf,
		None,
		[InSystemCondition("Gemini/Oxford","Oxford")],
		[InSystemCondition("Gemini/Oxford","Oxford")],
		AddCredits(10000),
		None,
		'cleansweep',(0,7,1490,0,(),rf.name+"_mission",2,4,.9,0,['retro_','pirates_'],1,1),
		rf.name+"_mission",
		masterson2,
		None,
		CampaignEndNode(rf),
		MastersonMission3,
		MastersonMission2, # The current mission node.
		mission_desc # Name that describes the mission in flight and in the mission computer.
		)

	mission_desc="Masterson_3:_Deliver_books_to_Burton"
	MakeCargoMission(rf,
			None,
			[InSystemCondition("Gemini/Oxford")],#where you get mission
			[InSystemCondition("Gemini/Junction","Burton")],#where mission ends
			AddCredits(10000),#Scriopt to be run after fixer clicks
			LoadMission(mission_desc,"directions_mission",(rf.name+"_mission",['Gemini/XXN-1927', 'Gemini/119ce','Gemini/Junction'], 'Burton')), # Script to be run to start the mission (usually None if you don't have a script, but ambush is also common.) (having no destination will call significant unit.. oakham should be the only dockable significant in that system)
			("Rare_Books",10),
			rf.name+"_mission",
			masterson3,#FIXME dictionary of speech
			None,
			CampaignEndNode(rf),
			MastersonMission4,
			MastersonMission3)

	mission_desc="Masterson_4:_Escort_freighter"
	MakeMission(rf,
		None,
		[InSystemCondition("Gemini/Oxford","Oxford")],
		[InSystemCondition("Gemini/Oxford","Oxford")],
		AddCredits(10000),
		None,
		'escort_local',('retro_',0,3,1,3000,0,False,'merchant__',(),rf.name+"_mission",'','talon.blank','','drayman',[('Drayman: Welcome volunteer. You will escort us to Nav 1. Do not abandon us until we have jumped.',False,'campaign/Oxford.wav'),"Drayman: I won't feel safe until we've jumped.",'Drayman: Hey, keep the freaks away, all right?','Drayman: I just want to make it alive.']),
		rf.name+"_mission",
		masterson4,
		None,
		CampaignEndNode(rf),
		MastersonMission5,
		MastersonMission4, # The current mission node.
		mission_desc # Name that describes the mission in flight and in the mission computer.
		)

	mission_desc="Masterson_5:_Deliver_artwork_to_Perry"
	MakeCargoMission(rf,
			None,
			[InSystemCondition("Gemini/Oxford")],#where you get mission
			[InSystemCondition("Gemini/Perry","Perry")],#where mission ends
			AddCredits(10000),#Scriopt to be run after fixer clicks
			LoadMission(mission_desc,"ambush",(rf.name+"_mission",("Gemini/Perry",),0,'unknown',3,'salthi.particle','',['...','...'],['Gemini/XXN-1927', 'Gemini/New_Detroit','Gemini/Perry'], 'Perry')), # Script to be run to start the mission (usually None if you don't have a script, but ambush is also common.) (having no destination will call significant unit.. oakham should be the only dockable significant in that system)
			("Artwork",10),
			rf.name+"_mission",
			masterson5,#FIXME dictionary of speech
			None,
			CampaignEndNode(rf),
			MastersonIntro,
			MastersonMission5)

	MastersonIntro.Init(rf,
			[InSystemCondition("Gemini/Oxford")],
			[("Masterson","Well, with your help Oxford base has transferred most of its valuables offworld, and until the Retro threat abates, we will remain an empty shell. Now the business about my contact? I'm afraid my friend is a little wary about meeting you. However, if you were able to provide reliable services to a few other employers around Gemini, then I could pass on more than just my own recommendation. Perhaps then we could talk further."),("Burrows","Sounds like you're changing the terms of our agreement. I didn't intend to do this much work."),("Masterson","Hold on. I'm not setting the conditions anymore. I'm just making a suggestion on how to alleviate his paranoia. You had best take my advice and find a few employers around Gemini. Then we can continue our business."),("Burrows","You drive a hard bargain, Masterson.")],
			None,
			GoToSubnodeIfTrue(DisplayTextIfTrueScript([("Masterson","Well, with your help Oxford base has transferred most of its valuables offworld, and until the Retro threat abates, we will remain an empty shell. Now the business about my contact? I have very good news. Multiple sources around Gemini report that you provide reliable services. So, my hitherto secret contact is now willing to meet with you. His name is Monte. You will find him on Macabee base in the Nexus system. Good luck. I hope he provides you with useful information."),("Burrows","Thanks, Masterson.")],SaveVariableGreaterScript("rf_recs",1,AddCredits(10000))),1,0),
			None,
			[CampaignClickNode().Init(rf,
						[InSystemCondition("Gemini/Oxford"),
						OrCondition(SaveVariableCondition("rf_recs",2),
							OrCondition(
								SaveVariableCondition("rf_recs",3),
								SaveVariableCondition("rf_recs",4))),],
						[("Masterson","I have very good news. Multiple sources around Gemini report that you provide reliable services. So, my hitherto secret contact is now willing to meet with you. His name is Monte. You will find him on Macabee base in the Nexus system. Good luck. I hope he provides you with useful information."),("Burrows","Thanks, Masterson.")],
						None,
						GoToSubnode(0),
						None,
						[MonteMission1]),
			MonteMission1])

	mission_desc1="Monte_1:_Relocate_to_New-Detroit"
	mission_desc2="Monte_2:_Go_to_Drake"
	mission_desc3="Informant:_Deliver_documents"
	MakeCargoMission(rf,
			MONTE_MINING_SPRITE,
			[InSystemCondition('Gemini/Nexus',"Macabee")],
			[InSystemCondition('Gemini/New_Detroit',"New_Detroit")],
			None,
			LoadMission(mission_desc1,"ambush",(rf.name+"_mission",("Gemini/New_Detroit"),0,'unknown',3,'salthi.particle','',['...','...'],('Gemini/Tingerhoff','Gemini/Perry','Gemini/New_Detroit'),"New_Detroit")),
			("Monte",1),
			rf.name+"_mission",
			monte1,
			None,
			CampaignEndNode(rf),
			CampaignClickNode().Init(rf,
#Fixme: directions_mission to Drake
						[InSystemCondition('Gemini/New_Detroit')],
						monte2['intro']+monte2['accept'],
						MONTE_NEWDET_SPRITE,
						GoToSubnode(0),
						None,
						[MakeCargoMission(rf,
								INFORMANT_SPRITE,
								[InSystemCondition('Gemini/Capella','Drake')],
								[InSystemCondition('Gemini/New_Detroit','New_Detroit')],
								None,
								LoadMission(mission_desc3,"ambush",(rf.name+"_mission",("Gemini/Nexus",),0,'unknown',3,'salthi.particle','',["...","...","..."],['Gemini/Nexus', 'Gemini/Tingerhoff','Gemini/Perry','Gemini/New_Detroit'], "New_Detroit")),
								("Documents",1),
								rf.name+"_mission",
								informant1,
								None,
								CampaignEndNode(rf),
								MonteMission3)]),
			MonteMission1)

	mission_desc="Monte_3:_Defeat_ambush"
	MakeMission(rf,
		MONTE_NEWDET_SPRITE,
		[InSystemCondition('Gemini/New_Detroit')],
		[InSystemCondition('Gemini/New_Detroit')],
		None,
		None,
#Fixme: should be ambush
		'defend',('retro_',0,10,5000,123456.789,0,False,False,'hunter__',('Gemini/Perry','Gemini/Tingerhoff','Gemini/Nexus'),rf.name+"_mission",'','talon.blank','',0),
		rf.name+"_mission",
		monte3,
		None,
		CampaignEndNode(rf),
		MonteMission4,
		MonteMission3, # The current mission node.
		mission_desc # Name that describes the mission in flight and in the mission computer.
		)

	mission_desc="Kill Governor Menesch"
	MakeMission(rf,
		MONTE_NEWDET_SPRITE,
		[InSystemCondition('Gemini/New_Detroit')],
		[],
		AddCredits(5000,AdjustRelation('unknown','privateer',-2)),
		None,
		'bounty_leader',(0,#minsys
			0,#maxsys
			0,#creds
			True,#run away
			6,#num escorts
			'unknown',#faction
			('Gemini/New_Constantinople','Gemini/Junction','Gemini/Penders_Star','Gemini/Troy'),
			"menesch_dead",#vartoset
			'',#fgname
			'centurion.blank',#Type of ship
			0,#displayLocation
			'',
			'salthi.particle',
			[("#996600Menesch? Looks like I'm gonna be rich",True,"campaign/Menesch1.wav"),
				("#bb4400Menesch: Not so quickly, aren't you looking for something? Aren't you the unfortunate privateer who lost his gun?"),
				("#996600Where's the gun, then I'll kill you.",True),
				("#bb4400Menesch: Kill? Another fine privateer like yourself. That gun was one of my great enterprising endeavours. With trading leverage that good, even the Cats will deal.",False),
				("#996600You gave the gun to the Kilrathi?",True),
				("#bb4400No, even I would not give a Cat sharper claws. Mordecai Jones was so fond of it. And the kilrathi... so afraid the Confeds would get it. So, we made a deal."),
				("#bb4400Jones wants the gun on every Retro ship. Something about a spiritual cleansing tool. I really must be jumping out now. I'll leave you to your death."),
				("#996600Are you ready for a fight?",True),
				("#bb4400Menesch: Ironic, isn't it? I place a bounty on your head, and here you are trying to collect one on me."),
				("#996600I don't need a green gun to kill you!",True),
				("#bb4400Menesch: Out of my space, second class citizen!",True)],[("steltek_gun",0),("steltek_gun",1),("steltek_gun",2),("steltek_gun",3),"tungsten","plasteel_hull"]),
		"menesch_dead",
		monte4,
		None,
		CampaignEndNode(rf),
		CampaignClickNode().Init(rf,
			[InSystemCondition("Gemini/New_Detroit")],
			[("Monte","Well done. Menesch is dead. I'm afraid I have to go now, but I wanted to thank you. You have done the Gemini sector an invaluable service. Goodbye.")],
			MONTE_NEWDET_SPRITE,
			GoToSubnode(0),
			None,
			[CampaignClickNode().Init(rf,
				[InSystemCondition("Gemini/Oxford")],
				["The library is closed for good. Now, go Away or I shall taunt you a second time, matey."],
				None,
				TrueSubnode(),
				None,
				[CampaignClickNode().Init(rf,
					[InSystemCondition("Gemini/Oxford")],
					["The library is closed for good. Now, go Away or I shall taunt you another time, matey."],
					None,
					TrueSubnode(),
					None,
					[CampaignEndNode(rf)])])]),
		MonteMission4, # The current mission node.
		mission_desc # Name that describes the mission in flight and in the mission computer.
		)

	return rf
