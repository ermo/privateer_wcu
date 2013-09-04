
from campaign_lib import *
#Syrai
#Caleigh
#Kaydence
#Demetria
#Destinee

#Destinee
#Kyree
#Zayne
#Soren
#Tre
#Syed
#Malakai
FIXME={"intro":"Welcome To Intro.","reminder":"Reminder! Reminder!","accept":"I boldy accept","accept2":"After some debate, I accept","reject1":"I reject your claim","reject2":"I wholeheartedly reject","reconsider":"Hmm can I hear more?","failure":"You have failed me for the last time!"}
DESTINEE_SPRITE=("militia.spr","Talk_To_Destinee","bases/heads/destinee.spr")
DEMETRIA_SPRITE=("demetria.spr","Talk_To_Demetria","bases/heads/demetria.spr")
DEMETRIA_SPRITE_SMALL=("demetria_2.spr","Talk_To_Demetria","bases/heads/demetria.spr")
KAYDENCE_SPRITE=("confed.spr","Talk_To_Kaydence","bases/heads/kaydence.spr")
KAYDENCE_SPRITE_NOHEAD=("confed.spr","Talk_To_Kaydence")
SYRAI_SPRITE=("pirate.spr","Talk_To_Syrai","bases/heads/syrai.spr")
SOREN_SPRITE=("merchant.spr","Talk_To_Soren","bases/heads/soren.spr")
DestineeFailure = [("Burrows","I'm not sure I'm cutout to be a cop.","barspeech/campaigns/bonus/destineefail.ogg"),("Destinee","I knew you were all hot air."),("Burrows","Well I may be hot air, but I'm certainly not hot coffee and doughnuts."),("Destinee","Well you failed me...and that means no pay and no work. I'll probably be seeing you in the backseat of my crate in the not too distant future Mr."),("Burrows","If you can catch me... otherwise I'll see you at the doughnut shop someday, Mrs Destinee"),("Destinee","Fat chance, Mr... I don't do doughnuts.")]
destinee1speech={"intro":[("Destinee","Good evening, hunter.","barspeech/campaigns/bonus/destinee1intro.ogg"),
            ("Burrows","Good evening to you.... may I have your name?"),
            ("Destinee","Destinee, Destinee Caleigh. And yours?"),
            ("Burrows","I don't give my name to...strangers.  What can I do for you?"),
            ("Destinee","Actually I represent the Quadrant police. We need some help in investigating some problems we've had with outlaws."),
            ("Burrows","Outlaws, eh? I think I know a thing or two about that"),
            ("Destinee","From the looks of it... I'd figure that you knew more about being an outlaw than about catching one."),
            ("Burrows","Being is believing, sweetheart. Now I think I can catch your bandits, if you've got the cash..."),
            ("Destinee","Well I've got authorization from the High Command to give up to 24,000 per mission; however for our first outing..."),
            ("Burrows","You mean *my* first mission."),
            ("Destinee","Well I wanted to make sure you wouldn't come crying back to mommy for help."),
            ("Burrows","Cute, but you're not old enough to be my wife much less my mother... But I do make exceptions for cuties like..."),
            ("Destinee","Can it, cousin...Now the job goes like this: We've had reports of pirates in the 17-AR system, harrassment of police, outright disappearences of merchants, the rumors abound. We need you to ensure that the 17-AR system is clean enough so that if it were your balding head, I could see myself in it."),
            ("Burrows","Now that's unfair; hair I've got aplenty"),
            ("Destinee","But apparently not the brains underneath remember to ask me how much it's worth to me. The mission pays 15 K. Interested?")],
        "accept":[("Burrows","Sure thing, sweetheart. Keep the food warm for me.","barspeech/campaigns/bonus/destinee1accept.ogg"),("Destinee","I don't do the 'kitchen', now get cooking")],
        "reject1":[("Burrows","Thanks for the invitation to a hot date, but I've got my own dinner plans tonight. Maybe later","barspeech/campaigns/bonus/destinee1reject1.ogg")],
        "reconsider":[("Destinee","Looks like someone got ditched at dinner","barspeech/campaigns/bonus/destinee1reconsider.ogg"),("Burrows","No the dinner was fantastic, and now I'm hungry for dessert"),("Destinee","Cute, now how does Pirate Soufflet sound? I need you to patrol the 17-AR system and eliminate all pirate activity. The pay is 15,000. How about it?")],
        "reminder":[("Burrows","About that hot date...","barspeech/campaigns/bonus/destinee1reminder.ogg"),("Destinee","Remember it was at your house and you were cookin--cookin pirates that is.  I need you to eliminate all pirates at the 17-AR system."),("Burorws","Right...pirate stew... and you've got dessert covered"),("Destinee","Doughnuts for you, Mr Pig, now get enforcin'--Law enforcing")],
        "reject2":[("Burrows","Sorry sweetheart, maybe I'm the pirate you should be lookin for.","barspeech/campaigns/bonus/destinee1reject2.ogg"),("Destinee","I'll keep that in mind, Mr..."),("Burrows","I only give my name to those who write me my check. Later.")],
        "failure":DestineeFailure,}


destinee2speech={"intro":[("Destinee","So I've got a doughnut saved up for you... you finish dinner yet?","barspeech/campaigns/bonus/destinee1intro.ogg"),("Burrows","The pirates are as good as cooked"),("Destinee","Now does that mean they all ran away when they saw your guns blazing, or that you booked as soon as you were cooked"),("Burrows","Now I may be all talk, but that's only if you ignore the fact that I also don't balk.  I've waxed your pirates"),("Destinee","Wonders never cease to amaze me...he not only cooks...he cleans, and waxes too!  Here's your cash."),("Burrows","Excellent, now what sort of work do you have in stock for me"),("Destinee", "Stock is exactly the problem. You see our militia forces in the New Caldeonia system are wearing out of their weapon stockpiles. They need ammo and missiles delivered at top speed."),("Burrows","And you wanted to hire me because of my 'explosive' personality"),("Destinee","You're more right than you think, Mr.  Take the cache of weapons I give you from here and deliver them to the Glasgow base in New Caledonia, then meet me back here on Munchen."),("Burrows","This is going to cost you 20k... I don't like running flammables"),("Destinee","10K is all you get for this mission, but I can guarantee you some interesting work when you return. Interested?")],
        "accept":[("Burrows","I'll do it for 15K.","barspeech/campaigns/bonus/destinee2accept.ogg"),("Destinee","I can tell when I have a man on his knees, and you want to do this job more than I want to give it.  My original price holds, 10K... I'll meet you back here when you finish")],
        "reject1":[("Burrows","I'll do it for 18K.","barspeech/campaigns/bonus/destinee2reject1.ogg"),("Destinee","I know you'd do it for less...and you want me more than I want you mister.  I'll see you when you decide that 10,000 is enough"),("Burrows","Ok I don't think you'll find someone else without my explosive personality to deliver weapons past those bandits")],
        "reject2":[("Burrows","No Ma'am! I'll do it for 18K, no less","barspeech/campaigns/bonus/destinee2reject2.ogg"),("Destinee","You're a tough sell.  I guess I'll be seeing you... perhaps in the back of my crate someday"),("Burrows","probably more likely I'll be seeing you in the back of some doughnut shop..."),("Desitnee","With an attitude like that I'll probably be more likely to find you in a poor house.")],
        "reconsider":[("Burrows","Let me hear your best offer again...","barspeech/campaigns/bonus/destinee2reconsider.ogg"),("Destinee","I need you to run some weapons to resupply our police forces in the New Caledonia system at the Glasgow base there.  This run pays 10,000 because that's what the chief thinks it's worth.  You with me or against me.")],
        "reminder":[("Burrows","So, uhh...where do I go again?","barspeech/campaigns/bonus/destinee2remidner.ogg"),("Destinee","You're delivering our little weapons to our friends on Glasow in the New Caldeonia base."),("Burrows","Right, and you're going to pay me 15,000 credits"),("Destinee","10,000 for deliver, and another 5,000 if you nuke that pirate base"),("Burrows","That was never in the plan!"),("Destinee","Exactly. 10,000 it is then...see you back here shortly")],
        "failure":DestineeFailure}

destinee3speech={"intro":[("Burrows","I'm back...what sort of report were you hoping for?","barspeech/campaigns/bonus/destinee3intro.ogg"),("Destinee","An in depth report of pirate activity near or in Telar...what do you have for me"),("Burrows","Well I wouldn't want to tip my hand before I got the cash... money then banter."),("Destinee","Actually I can just as well hire the next guy who comes over here to find out more about the Telar...so I'll leave it up to you... as soon as you tell me I've got the money for you--it's in my checkbook right now.")],
        "reject1":[("Burrows","Excellent.  Now I hope you're not disappointed to find out that Telar's not your place.  You're really better off looking in 17-AR or one of the surrounding systems.  I think you're hot on the wrong lead.","barspeech/campaigns/bonus/destinee3reject1.ogg"),("Destinee","Why do you say that.  Are you sure you conducted a careful search.  I have a hunch you're wrong on this one, flyboy."),("Burrows give me the money and I'll feed you my scanning logs--the sector's got nothing to do with bandits...the little business I saw going on was legitimate."),("Destinee","Well consider our deal off.  I don't think you even bothered with your end of the bargain. Keep the original 12K...that's the last of the money you'll see in a long time.  Bye...I liked you better when I thought you were competent.")],
        "accept":[("Burrows","Excellent. Well I'll tell you what I've found out. I established contact with a pirate named Syrai. She apparently runs an Ultimate shipping operation.  They run Ultimate to the Pleasure planet in Junction system, and she wants me to cover her next run. So should I do it?","barspeech/campaigns/bonus/destinee3accept.ogg"),("Destinee","Inter-quadrant smugglers, eh?  I think these are bigger fish than we thought.  Now don't take it that we want to fry 'em just yet. We have to get some evidence.  I want you to accept the mission, then dump the goods in J900 on the way"),("Burrows","I take it you have a revised pardon signed by the local judge just in case... I don't want..."),("Destinee","One step ahead of you.  You know the game... get the cargo...dump it in J900 before the local authorities arrive.  Once you've ditched the cargo, meet me on the Victoria agricultural base.  I'll probably be back from New Constantinople capital with a Warrant."),("Burrows","Later sweetheart"),("Destinee","Bye BOFH.")]}

destinee4speech={"intro":[("Burrows","When I talked to the pirates before my run, they told me that I was supposed to pick up F&O for them after I dropped the brilliance...well that's kind of moot now."),("Destinee","F&O? That a new drug?","barspeech/campaigns/bonus/destinee4intro.ogg"),("Burrows","Naw, you know... pilot speak for Food and Oxygen"),("Destinee","What do you think that means?"),("Burrows","I'd bet they have a shipment coming in right now. If you're going to lay siege to the base, that's the first place to start... their supplies"),("Destinee","I was more thinking of running in guns blazing, but there is something to be said about cutting off their supplies.  Any idea where you can find that transport?"),("Burrows","Depends on your price... What kind of money are we talking?"),("Destinee","I can't afford much more than 11,000 credits right now.  Is that ok?"),],
        "accept":[("Burrows","that's cutting it close, but I figure I can earn my privateer wings this way --Government sponsored piracy-- sounds dandy.","barspeech/campaigns/bonus/destinee4accept.ogg"),("Destinee","Remember anything you pick up and bring back to me is evidence"),("Burrows","Don't worry, sweetie, I'll polish it off...I can polish--"),("Destinee","Enough of your pathetic quips. If you can get that transport, 11K...either way, meet me at Munchen in Tingerhoff for your final mission. I promise that one will reward you more gratuitously."),("Burrows","My senses are tingling with anticipation.")],
        "reject1":[("Burrows","Not enough cash...unless you throw something else in on the side...like","barspeech/campaigns/bonus/destinee4reject1.ogg"),("Destinee","11K Take it or leave it this is your mission idea...the only rewards between you and me will reside squarely in your imagination.")],
        "reconsider":[("Destinee","I'm still offering 11K for the mission... Go to Telar, stop the supply shipment. You in?","barspeech/campaigns/bonus/destinee4reconsider.ogg")],
        "reject2":[("Burrows","This is my mission...I'll only do it if I choose to, at my price...and right now that's higher than 11K","barspeech/campaigns/bonus/destinee4reject2.ogg"),("Destinee","Not much of a mission if you can't budget it, is it?")],
        "reminder":[("Destinee","So I take it you've nailed that transport before it arrived... so why are you here in Burton rather than in Munchen.","barspeech/campaigns/bonus/destinee4reminder.ogg"),("Burrows","Because I haven't found that freighter yet. It must have taken those pirates a fair chunk of time to even realize I'd pilfered the Ultimate."),("Destinee","They may not have their frieghter, but you're probably numero uno on their hit list. You'd better get a move on --why waste a good opportunity to make enemies deeper enemies?"),("Burrows","That sounds familiar..."),],
        "failure":[("Destinee","I knew you weren't man enough to finish the job.","barspeech/campaigns/bonus/destinee4failure.ogg"),("Burrows","I can finish anything you desire","Can it buddy. You let that transport through. And from the manifest we downloaded from ComNet, it had more that just W&F, you monster. It was full of a number of weapons of mass destruction. I'm going to call this operation off. We can't afford to keep screwing up like this.")]}
destineegloat=[("Destinee","So you turned coats and you weren't able to stop us.  Well this is a state owned base now.  You might as well just slink off into a corner and die","barspeech/campaigns/bonus/destineegloat.ogg"),("Burrows","Hey not so fast sister. What about putting the accomodations of this first class *government* facility to use.  Care to meet me before dinner"),("Destinee","I'm not a pirate and I'm certainly not a traitor; nor do I respect either.  You can go dine with someone who's got a hat and a patch rather than a life.")]

destinee3text=[("Destinee","Good work, you've helped to reinforce our police craft. Now they should better be able to cover the area between Telar and Junction.","barspeech/campaigns/bonus/destinee3text.ogg"),("Burrows","So do I get my complimentary badge, or my free doughnuts."),("Destinee","You get something even better: a reason not to sport that badge"),("Burrows","You want me out of your hair?"),("Destinee","Well yes and no. We want you to do some under cover work"),("Burrows","So out of your hair--and under your covers-I get it!"),("Destinee","I'm going to ignore that. We have a hunch which mining base is responsible for this illegal activity, and we need you to play pirate for a bit and get us some evidence so we can get a court order."),("Burrows","So you want me to run some illegal cargo so I can get caught red handed. Sorry baby, but I don't place my butt on the grill and give you a lighter"),("Destinee","What if it means 30K"),("Burrows","I want half in advance and a pardon, signed by the judge."),("Destinee","You mean this pardon here...Now for the first mission I don't need you to run the cargo...just make a deal with the pirates and sniff it out...I'll pay you a third in advance and another third when you return with the first bit of info. Then I'll need you to run cargo for me. Deal?")]
destinee3accept=[("Burrows","Ok you have me interested. You will note that I'll do it for 12K upfront, no less, and I'll find that pirate base and try to strike a deal with 'em...then I'll come back here before running their drugs.","barspeech/campaigns/bonus/destinee3agree.ogg"),("Destinee","You got it...According to our triangulation, the base should be somewhere in the Telar system"),("Burrows","I'll see you back here... have some martinis and my second round o' cash ready.")]
destinee3reject=[("Burrows","Hey this pardon only covers my crime if the cargo isn't in the hold when the cops catch me, or I'm still in Telar. Sounds fishy.","barspeech/campaigns/bonus/destinee3decline.ogg"),("Destinee","Clearly we can't let you run with it and take our 12K..."),("Burrows","Sorry, lady I think I'm going to try my luck doing something...more legitimate"),("Destinee","Like _running_ that cargo"),("Burrows","You wish, more like getting the hell out of this quadrant."),("Destinee","So this is good bye... can't say I'll miss you."),("Burrows","Later, pumpkin.")]


destinee5speech={"intro":[("Burrows","That transport got vaporized before it could call for help much less deliver its goods.","barspeech/campaigns/bonus/destinee5intro.ogg"),("Destinee","My report looks kind of different: You let the transport get passed you, and then you managed to get lucky and nail it before it docked to the base."),("Burrows","I remember it was better than that last night..."),("Destinee","Records indicate you actually did the attack this morning"),("Burrows","Way to burst  my bubble, Destinee. Anyhow my pay?"),("Destinee","Already credited to you.  And your next mission is simple: Escort our modified Paradigm class troop transport to the base... oversee its capture...and meet me on the base."),("Burrows","A date, eh? Fair enough... but I'm not doing this for any less than 25K"),("Destinee","Don't worry I've got your 20K saved up right here... I need to eat too!"),("Burrows","You mean you take 20%?!"),("Destinee","Hey, what can I say, I'm a flyboy magnet..and I get the job done. So will you?")],
        "accept":[("Burrows","Can't say I've ever met a fixer as honest as you.  Fair enough--I'll do the run, in exchange for your money...and a date on that base--you're buying dinner","barspeech/campaigns/bonus/destinee5accept.ogg"),("Destinee","Wow I've tamed you already...too bad this is going to be our last date."),("Burrows","Turning me down already? You haven't even seen me go after those pirates"),("Destinee","Don't worry, a gir's got friends"),("Burrows","So now you're trying to hook me up with your ugly friends--I get it!"),("Destinee","Don't be so overconfident...I just mean I know some people who can get you work"),("Burrows","Ok I'll run your mission. Later")],
        "reject1":[("Burrows","I'll do it for 25. Lady you get a salary as well. I have to work on a per-meal basis.","barspeech/campaigns/bonus/destinee5reject1.ogg"),("Destinee","If you want another meal with me you'll be back.")],
        "reconsider":[("Burrows","So what are the odds of me completing this mission successfully","barspeech/campaigns/bonus/destinee5reconsider.ogg"),("Destinee","Well you're going to be both outnumbered and outgunned, since that heavy transport will not be sporting many turrets. I won't lie to you, it'll take an ace to crack that base")],
        "reject2":[("Burrows","Sounds like a suicide run. I think I'll take my chances playing russian roulette.  Want to join me","barspeech/campaigns/bonus/destinee5reject2.ogg"),("Destinee","Sorry pal. You don't make good company unless you're I'm the one who's dead. See you.")],
        "reminder":[("Destinee","That paradigm is on its way! You've got to hurry to catch it.  Don't botch this one, Privateer. It's critical that transport get through and wrest that base.","barspeech/campaigns/bonus/destinee5reminder.ogg"),("Burrows","I'm hurrying, I'm hurrying")],
        "failure":DestineeFailure}
destineefinal=[("Destinee","I'm impressed. You handled those pirates like a pro.","barspeech/campaigns/bonus/destineefinal.ogg"),("Burrows","To borrow a line from an old friend: what can I say, I'm a professional"),("Destinee","Well I'm glad those pirates are out of my hair. And I think you deserve a little in."),("Burrows","While I could make any number of interesting wisecracks I think I'm going to let you speak now"),("Destinee","Well I know a girl who works out of Anapolis in the Perry system. Confed hotshot, lookin to hire.  I'm sure you could make...an impression"),("Burrows","I don't like flying with military types"),("Destinee","You won't need to sign up...this will be on a per job basis. Anyhow if you're interested just fly over to that refinery in Perry, and I'm sure she'll accept a meeting. Don't count on anything more than a few missions though."),("Burrows","Don't worry, I don't sleep with the military. Good bye Destinee...it's been...almost a pleasure")]


destinee6speech={"intro":[("Destinee","Charming to see you again, captain"),("Burrows","I didn't know I earned a rank"),("Destinee","Well captain of your ship. I hear you got along with Kaydence quite well."),("Burrows","Unlike you, she doesn't have much of a personality, so naturally she was easy to please"),("Destinee","I take it you like my personality a bit better?"),("Burrows","Don't get jealous, Destinee, I don't sleep with the military...but I might consider a cop"),("Destinee","Well I wouldn't consider you, so you can kiss those dreams goodbye. However I do have a job for you, if you'll stop hanging that head of yours."),("Burrows","I'm listening!"),("Destinee","I've gotten some insider information about a pirate base in the otherwise uninhabited KM-252 system. I want you to nail the pirates there so that I can send in a troop transport and take those pirates out."),("Burrows","And the reward is..."),("Destinee","A kiss...."),("Burrows","I'm on it"),("Destinee","on the cheek."),("Burrows","Well in that case... what other reward is there"),("Destinee","How does 15K sound?")],
    "accept":[("Burrows","Right on missus...15 K and a kiss"),("Destinee","Kiss only starts with K, Captain... it doesn't end with it.  Move along.")],
    "reject1":[("Burrows","Maybe if you included a kiss"),("Destinee","I'd only consider it...")],
    "reconsider":[("Burrows","Well I'm thinking about that clean sweep mission... what's the offer again?"),("Destinee","15K for eliminating all the pirates in KM-252. Interested?")],
    "reject2":[("Burrows","I think I'd rather sit it out than stir up a hornet's nest of pirates"),("Destinee","Suit yourself... note I said suit, not un...")],
    "reminder":[("Destinee","Have you eliminated the bees from my pirates nest yet?"),("Burrows","I was rather thinking of giving you a good-bye kiss."),("Destinee","How about you go out to KM-252 and eliminate the pirates instead, deal?")],
    "failure":[("Destinee","Looks like you weren't man enough to face up to those pirates. Well I'm sorry, but that means you're not man enough for me, either"),("Burrows","Don't I at least get to say goodbye?")],}
        
destinee7speech={"intro":[("Destinee","Fantastic captain. Let me hear your report?"),("Burrows","Since it seems to excite you so much, sure. I was able to eliminate whatever the pirates threw at me. How's that?"),("Destinee","Fantastic. Almost worth a kiss.... but maybe if you finish the next thing at hand"),("Burrows","Which is escorting in that troop transport I presume"),("Destinee","And you presume correctly.  You are to be the knight in shining armor and guide these troops past the dragon and into the pirate base."),("Burrows","And the pirates are going to have fire-breath"),("Destinee","Maybe, but probably they will just swarm you with their numbers"),("Burrows","What's the reward you got for me, aside from that kiss you promised"),("Destinee","20000 and a peck")],
        "accept":[("Burrows","That's definitely worth it. I'll go for it")],
        "reject1":[("Burrows","I'm not sure I can handle those pirates in my crate. Maybe I'll wait until I repair")],
        "reconsider":[("Destinee","Man enough to assault those pirates in KM-252? It's a whole 20,000 credits.")],
        "reject2":[("Burrows","I think I'm going to sit this one out.")],
        "reminder":[("Destinee","So, has my hero pilot eliminated those awful pirates."),("Burrows","No your hero pilot just got tired and took a nap. I'll get on it though."),("Destinee","Timing is critical here. Go there. I'll make sure you're happy when you return...")],
        "failure":[("Destinee","I can't believe you let that transport get sacked! This is outrageous. I though there was one man I could trust, and now he does this to me? Well goodbye pilot. Don't even talk to me again. You're not worth the weight of my breath in bronze")],}
destineefinal2=[("Destinee","                                            "),("Burrows","That was the...... I'm speechless"),("Destinee","Maybe we can walk together through the sunset...Munchen is a beautiful place."),("Burrows","I hope you mean the one on Earth...I could fly you there sometime you know...it's not too many jumps away."),("Destinee","What a dream...what a dream...and like all good things, dreams have to come to an end..."),("Burrows","I guess you're right... you're a cop...I'm a cowboy... we really can't be on the same side too long."),("Destinee","Well keep your nose clean in my sector..and maybe you can come back, and maybe I can take you up on that offer to get out of this sector, if only for a little while. So long, captain. And as long as you're willing, you're always welcome.")]



syrai1speech={"intro":[("Syrai","You look...new."), ("Burrows", "Looking around here, I hope that's a complement."), ("Syrai", "Cute. I haven't got time to look for someone better than you. Need some easy cred?"), ("Burrows", "I could be persuaded."), ("Syrai", "You'd have to be a complete moron to screw up THIS one, you know?"), ("Burrows", "Much like your usual clientele?"), ("Syrai", " At least you're mildly perceptive, but I think even someone from Sector Security would've noticed. Let's get down to business. A low-down traitorous dog has been sticking his nose into everyone's business all over Telar."), ("Burrows", "Well, you -are- pirates."), ("Syrai", "There's even honor among Thieves. The clinch is that he's decided he's going to tip off the Feds with the dirt he's uncovered! He may have already told them about our Ultimate shipping operation that supplies Speke..."), ("Burrows", "And it's hard to find good help these days. I've heard it all, get to the point."), ("Syrai", "Yeah, yeah. He's no big deal, but he'll be flying an Orion. His name is Otrief Jenkins. If you can encourage him to become an inert vapor, I'll pay you 14,000 credits.")],
"accept":[("Burrows", "I'll do it. It might be a good idea not to piss off the Feds while I'm gone."), ("Syrai", "Perhaps you could use that amazing wit of yours to bore him to death. It'd work just as well as far as I care.")],
"reject1":[("Burrows", "I'm not sure. You want me to vape someone for becoming an informant, plus there's Fed involvement?"), ("Syrai", "Look, it's just one guy. Even for what we do, some people are just worse than others. A lot of us are just trying to survive. Someone selling out all of the secrets to the Feds just means that everyone is in jeopardy, and not just 'those dirty pirates'.")],
"reconsider": [("Burrows", "You could be right. Even this is a community..."), ("Syrai", "You'll just be ridding the world of another piece of scum, the kind that sticks his knife in your back out of boredom, rather than hunger."), ("Burrows", "Hunger...?"), ("Syrai", "Oh, come on, like you've never seen that happen...")],
"reject2": [("Burrows", "Sorry, no."), ("Syrai", "Well, then I'll just have to kill you for what you know."), ("Burrows", "You think you can?"), ("Syrai", "Actually, I don't care enough. It was a joke. Get out of here, let me know if you see any Greenies looking for work.")],
"reminder": [("Syrai", "Back so soon? Look, all you have to do is find Jenkins in this system, and make sure he's out of our way. That's all. It's simple. You want to get paid, right?")],
"failure": [("Burrows", "Things didn't go so smoothly."), ("Syrai", "No kidding. You royally screwed that one up. At least I can get someone else to do it, but get out of here, will you? You just wasted everyone's time.")],
"reminder":[("Syrai", "What are you doing back here? You go and find Jenkins in this system. He'll be flying an Orion. This should be easy.")]}

syrai2speech={"intro":[("Syrai", "Here's your cash! You took care of Jenkins well enough."), ("Burrows", "It wasn't a problem. Small fish...sometimes you should expect a shark to come along."), ("Syrai", "Don't mistake me for being impressed."), ("Burrows", "Right. Anything else?"), ("Syrai", "Your being back in one piece aside, I have something else that needs to get done. Your timing just makes it convenient."), ("Burrows", "Perhaps you'd like me to wash and dry some kittens on a..."), ("Syrai", "No. I have a shipment of Ultimate headed for the Junction system. Speke is low on supplies, my shipment is more important."), ("Burrows", "'No bleeding hearts allowed', I take it?"), ("Syrai", "It's just business. I need you to meet with me on the planet. Once the shipment is safely under my care, I'll transfer 20,000 creds to your account.")],
"accept":[("Burrows", "Consider it done."), ("Syrai","Great. And do get off this rock soon. We're nearly out of food, and our oxygen supply is quite limited."),("Burrows","Really? how'd that happen?"),("Syrai","The militia has nailed a couple of our cargo transports already and we're really hurtin.'  In fact, if we don't get resupplied in a day we're going to have to stop feeding people and start recycling old air...and you know just how long that lasts."),("Burrows","Egads, that sounds like some bad planning--perhaps I could make a profit off this somehow"),("Syrai", "Remember what you said before about the Feds. Consider this your warning to tread lightly and..."), ("Burrows", "Carry a BIG stick."), ("Syrai", "Just go...")],
"reject1": [("Burrows", "Murder, drug trafficking...why don't I just drop a signal beacon for the feds while I'm at it?"), ("Syrai", "It's money, and you're going to have to dirty your hands sometime to get ahead in this universe.")],
"reconsider": [("Burrows", "My hands already are dirty, I suppose."), ("Syrai", "Hey, don't worry about it. That guy was a piece of trash, and it's not as if I'm asking you to blow the station up. Just deliver a few drugs. It's no sweat.")],
"reject2": [("Burrows", "It doesn't look like I can do your drug run."), ("Syrai", "Well, if you can't do a simple delivery like this, I wonder how far you'll really get. If you're too straight-and-narrow, you'll always find something that your associates will ask, you won't do. Maybe it'll get you killed someday. Go on, I can get someone else. People like drugs, and money. What a shock.")],
"failure": [("Burrows", "Things didn't go so smoothly."), ("Syrai", "No kidding. You royally screwed that one up. At least I can get someone else to do it, but get out of here, will you? You just wasted everyone's time.")],
"reminder": [("Syrai", "Back? Just get to Speke in Junction and deliver the Ultimate. You're wasting time.")]}
    
syrai3speech={"intro": [("Syrai", "It's amazing. You can actually follow simple instructions."), ("Burrows", "Also something that's rare around here?"), ("Syrai", "That would appear to be the case, yes. I have something else for you. I'd give this to someone else, but not many new people come through here. It's quite simple, routine."), ("Burrows", "It couldn't be nearly as simple as if you hadn't made that so clear."), ("Syrai", "...right. But still. All you have to do is take some foodstuff and other basic supplies back to the pirate base in Telar. It's only worth 10,000 credits, but I'm sure you won't find anything else this simple, or easy."), ("Burrows", "Oh, plus it wouldn't involve you, my dear friend Syrai."), ("Syrai", "...you're really pushing my patience, Hotshot.")],
"accept": [("Burrows", "It's just fun to see you squirm. Fine, I'll do it."), ("Syrai", "Just...make sure that point defenses don't 'malfunction' when you land.")],
"reject1": [("Burrows", "A simple foodstuff run for 10,000? Do you take me for a fool?"), ("You don't really want me to answer that, do you? I promise. It's on the up and up.")],
"reconsider": [("Burrows", "I suppose it couldn't hurt, could it? Then again, maybe you laced it with something that'll explode when I take off..."), ("Syrai", "As tempting as that is for how you push my buttons, I need the shipment to get through.")],
"reject2": [("Burrows", "It sounds too good to be true. I'll have to pass."), ("Syrai", "I can't believe you. It's just beyond me. It's simple, it's easy, it's legitimate. A delivery that couldn't possibly get you in any trouble, and you turn me down. I swear. People are getting crazier, and it's not just the pirates that frequent this place..."), ("Burrows", "Don't be so sure...")],
"failure": [("Burrows", "Things didn't go so smoothly."), ("Syrai", "No kidding. You royally screwed that one up. At least I can get someone else to do it, but get out of here, will you? You just wasted everyone's time.")],
"reminder": [("Syrai", "Don't waste any more time. Get the supplies back to the pirate base in Telar. There shouldn't be any problems on the way. It's just basic supplies.")]}
    
syrai4speech={"intro": [("Burrows", "I thought you said it was clean, on the up and up..."), ("Syrai", "I swear, Burrows, I had no idea that there were weapons stashed in there. You can rest assured that the people responsible will get what they deserve."), ("Burrows", "I'm sure. If I didn't know better, Syrai, I'd say you were 'unreliable'."), ("Syrai", "So we've had a few problems...but none bigger than this one. Look, just after you came in, the Feds started to swoop in for a raid. We've got a Paradigm incoming, heading right for us. It's just your luck, but noone else around right now has either the skill or equipment."), ("Burrows", "Terrific. I suppose you also want me to wear a special hat and..."), ("Syrai", "Look, I'm sorry. I don't have time for your sarcasm. Yes or no?")],
"accept": [("Syrai", "You're really saving us, all of us. I'll hook you up with a good friend of mine once the dust settles, at least if you make it. Otherwise I suppose it won't really matter. You do this, you've earned not just my respect, but that of everyone on this base. Go get 'em..."), ("Burrows", "You almost made me feel warm and fuzzy.")],
"reject1": [("Burrows", "You want me to get in a direct confrontation with the Feds to save a bunch of pirates?"), ("Syrai", "These 'pirates' also have families to support. Not everyone is a reckless, ruthless scumbag. We don't have TIME for this. You're either in, or you're out.")],
"failure": [("Burrows", "Things didn't go so smoothly."), ("Syrai", "No kidding. You royally screwed that one up. At least I can get someone else to do it, but get out of here, will you? You just wasted everyone's time.")],
"reconsider": [("Burrows", "I'm still thinking about it."), ("Syrai", "If you don't do this, you'll be responsible for what happens to everyone here, including children. Can you live with that? This is more important than petty squabbles.")],
"reject2": [("Burrows", "I'm sorry, I'm not risking my hide for for a base full of pirates."), ("Syrai", "What should I have expected? You're just a mercenary...not merely a mercenary but a coward. What happens here is on YOUR conscience! Get out of my sight.")],
"reminder":[("Syrai", "Get OUT there. We've got a Paradigm closing in on the base. If you stick around here, you'll just wind up dead, or worse.")]}

syrai5speech={"intro": [("Burrows", "Well, it certainly LOOKS as if you're not dead..."), ("Syrai", "Save the gloating. You really saved our asses. I mean it. You good, good enough to've earned the interest of one of my friends. I'll vouch for you, but I can't help you anymore."), ("Burrows", "Well, well...it almost sounds as if you're going to miss me, Syrai."), ("Syrai", "Don't be silly...well, I'm not much for farewells. I keep my promises, though. Will you go?")],
"accept": [("Burrows", "Sure, I'm not going to turn down an opportunity like this."), ("Syrai", "Good. His name is Soren. I've taken the liberty of having a container with an encrypted data pod loaded onto your ship. Take it and go to the Midgard system. He's on the planet Heimdel and will arrange to meet you there."), ("Burrows", "How did you know I'd accept?"), ("Syrai", "Call it a hunch. You don't have to thank me, just don't waste any time. He doesn't like to be kept waiting. He's a hard person to get in association with. Don't make me look bad, you got it? Now shoo."), ("Burrows", "You're going to miss me, but I won't let you down."), ("Syrai", "Punk...")],
"reject1": [("Burrows", "I'm sorry, I don't think I can..."), ("Syrai", "What? Are you a lot more stupid than I thought? This is a good opportunity, and a reward for your work, for getting the feds off of our backs.")],
"reconsider": [("Burrows", "Why? Does it matter who I go and talk to?"), ("Syrai", "Yes, actually. We're going to try to lay low for a while, but if you care about your career, you'll go and work for my friend.")],
"reject2": [("Burrows", "Sorry, I think after all of this, I can't go associate with the friend of a pirate like you."), ("Syrai", "That's beyond stupidity. I wonder how you managed to do all of that with the brain the size of a pea. I don't think I want to know. Just get out of my sight..."), ("Burrows", "You'll feel sorry once I'm gone."), ("Syrai", "Don't play that...I gave you a golden opportunity. One few get. You slammed the door shut.")],
"failure": [("Burrows", "Things didn't go so smoothly."), ("Syrai", "No kidding. You royally screwed that one up. I won't entrust you to deliver that information securely if it's now in someone else's hands. This is outrageous! Goodbye!")],
"reminder": [("Syrai", "Just take the data pod to Soren on the planet Heimdel in the Midgard system. He'll give you more information. This is goodbye, Hotshot.")]}



kaydence1speech={"intro":[("Kaydence","Good day to you, sir. I've been expecting you"),("Burrows","The pleasure is entirely my. You're..."),("Kaydence","Kaydence's the name. Destinee has told me all about you"),("Burrows","All?"),("Kaydence","More than you probably want me to know, plus the files the military has on hand"),("Burrows","So this is it? Am I under arrest?"),("Kaydence","Nice joke, actually you're under hire. We've actually lost a patrol near Blockade Point Alpha, and we've received a distress beacon. Every pilot is valuable to us, so we'd like you to go pick him up for us in case the Kilrathi decide to do some target practice, or worse, pick him up and enslave him"),("Kaydence","The reward is 11500 So are you in?")],
        "accept":[("Burrows","So I get to play Prince Charming. Who's the princess I get to rescue."),("Kaydence","Dvell Skovikon, a great pilot, and the best lifter on this side of Clarke. Looks like you two would make a lovely pair."),("Burrows","Cute, so I rescue burly guy and you get to kiss him."),("Kaydence","Or maybe you, Mr Charming. Now get a move on")],
        "reminder":[("Kaydence","Is Prince Charming trying to swoop down and sweep up women who don't need a-rescuin', because our prince(ess) out there needs you...Now"),("Burrows","Don't worry, I'll bring him in."),("Kaydence","Good, because a botched rescue means our charming hero sleeps on the couch"),("Burrows","As opposed to...")],
        "reject1":[("Burrows","Not enough credits. I'd do it for double"),("Kaydence","I've got my budget, you've got yours. I'm sure there are a dozen pilots out there who'd try this pro-bono"),("Burrows","I doubt that. Those kind of pilots are the ones who get left out there in the first place")],
        "reconsider":[("Kaydence","So, you couldn't find any other work?"),("Burrows","Lets just say this idea of rescuing a pilot against all odds has begun to strike me as glamorous."),("Kaydence","Yes...you too can be a Prince Charming, sweeping, sun at your back, flying through a hail of furball fire..."),("Burrows","This isn't a holovid, darling.  A hail of furball fire is instant death!  Let me think about this..."),("Kaydence","There really should only be 1 or 2 ships in the immediate area. Just sneak in, nab the pilot, then get out of there. Then I give you 11500.")],
        "reject2":[("Burrows","Rescuing an idiot who got himself shot up doesn't strike me as very appealing. 'Welcome to the military, we'll rescue your sorry butt as soon as you bail' You know, lady, if I bail I stay out there, and the only Prince Charming who comes looking for me is the one lookin to sell me into slavery for half of my weight in Tungsten")],
        "failure":[("Burrows","Well it looks like Prince Charming bugged out after the Kats got to your friend."),("Kaydence","That's a shame. If you had hurried out there a bit faster maybe he'd be extolling your piloting skill.  Well it looks like you're out of work pal. No contract, no money.")]}

kaydence2speech={"intro":[("Kaydence","Excellent work!  Mr Skovikon was complimenting your flying style when I met him on the runway."),("Burrows","Well I don't like to disappoint any eager princesses. Now do I get that kiss?"),("Kaydence","He got the kiss, but you get some cash."),("Burrows","Cash! I like the sound of that."),("Kaydence","Then you'll like the sound of this: Blockade Point Alpha still is populated with a half-dozen or so cats.  We need you to toast them by whatever means necessary"),("Burrows","So a cleansweep? What's this worth to you?"),("Kaydence","A grand total of 13000 credits"),("Burrows","If you call that grand I wonder what a pathetic sum would be?"),("Kaydence","It's all I got for this sort of work. Take it or leave it.")],
        "accept":[("Burrows","What the heck. This might not even cover my wingman expenses, but I think I can manage.")],
        "reject1":[("Burrows","Not enough cash. That will cost me some serious damage and I need more to cover my wingmen expenses"),("Kaydence","Suit yourself. I can dedicate some military vessels instead if necessary")],
        "reconsider":[("Burrows","Maybe I'll do the job after all, what are the details?"),("Kaydence","I'll need you to clear the Kilrathi in Blockade Point Alpha. The reward is 13000; are you in?")],
        "reminder":[("Kaydence","So have you managed to successfully nail those cats"),("Burrows","Not yet...been busy with 'other' things"),("Kaydence","Not funny--this is a military sector not a pleasure planet."),("Burrows","Don't get jealous, honey. Just did a couple of jobs in the meantime."),("Kaydence","Well I need you to immediately clear out the Blockade Point Alpha sector for a reward of 13000 credits. Hurry!")],
        "reject2":[("Burrows","I don't think so. I thought you'd have made a better offer by now"),("Kaydence","Take it or leave it")],
        "failure":[("Kaydence","You failed to take on those cats. I can't let you continue to work for me.  Consider our work relationship off"),("Burrows","What about any other sort of--"),("Kaydence","Goodbye")]}
kaydence3speech={"intro":[("Kaydence","Perfect. I knew I could count on you"),("Burrows","What can I say? I'm a professional!"),("Kaydence","Professional in flying, maybe, professional in banter, not really.  But I have a job that needs some nice flying tricks"),("Burrows","What kind of tricks"),("Kaydence","Specifically the 'Don't let someone famous get killed' tricks. If you do, there might be some consequences that go well beyond me not paying you.  He will become your responsibility"),("Burrows","That sounds more like babysitting than anything glamorous. Who is this prick"),("Kaydence","Well be a bit careful with what you say. This man is someone important, that's all I can say until you agree with me.  However I can tell you in advance that this mission is well worth your while, raking in 18,000 credits.")],
        "accept":[("Burrows","I'm up for a challenge...who am I looking to escort? Admiral Terrell? Prince Thrakhath?"),("Kaydence","Nothing so glamorous. Just a local politician from the Gemini state senate."),("Burrows","Why is it worth so much to you"),("Kaydence","Well first of all, if our Senator doesn't make it, you're the one who gets the blame.  Secondly there have been a number of threats to his life--"),("Burrows","Anyone in my hold need not worry about threats, Kaydence--and that includes you."),("Kaydence","Kind offer, but let me tell you about reason number three: the senator is not a good pilot"),("Burrows","Pilot? I thought I'd be responsible for taking this person in my hold...now I have to escort a bad pilot--Oy veh!"),("Kaydence","Well you'll be escorting the senator's personal Stiletto to the sector capitol in New Constantinople. I'm sure you'll be able to make those two jumps without incident"),("Burrows","Count on it. Later")],
        "reject1":[("Burrows","I think I need to know more about this person I'm escorting.  Is he dangerous? Is she wanted?"),("Kaydence","I'm afraid you're just going to have to look into yourself for those answers. I can't give them. All I want is for you to make a guarantee that this person will arrive safely to a location 2 systems away, no matter who it is, no matter if you like that person or not. Agreed?"),("Burrows","Let me think about it...")],
        "reconsider":[("Burrows","Ok I see where you're coming from. I'm pretty certain I can take this puppy to the dog house, if you get my meaning. Why would I want to put my neck on the line for some chump change"),("Kaydence","This might be your opportunity to make some very...interesting...contacts who could give you some even more profitable missions. You in?")],
        "reject2":[("Burrows","No I think I'm going to sit this one out until you can guarantee my safety no matter about what happens to the puppy I'm supposed to walk.")],
        "reminder":[("Kaydence","So have you escorted our Senator. I hear the senate's about to convene and the Senator already launched!"),("Burrows","I'm sorry, but I haven't gotten around to it.  A stiletto's a fast ship and I'm sure this won't cause any harm"),("Kaydence","Hurry up. Remember a lost senator equates to your lost freedom")]}
kaydence4speech={"intro":[("Kaydence","Fantastic. I'm sure the senator is grateful to be able to vote today. Did you encounter much resistance?"),("Burrows","For all that money you were paying me I thought there would be a gang of retros, or at least a furfight. But in all honesty this was the easiest money I've ever earned. If the senator was only a pilot instead of a bandit-repellant."),("Kaydence","I'll take kindly and not pass that comment along.  Anyhow we've been having some trouble from an unknown threat. We don't know their strength or numbers, but they seem to be flying military craft."),("Burrows","Most importantly what's the money like, and where do I start"),("Kaydence","The first mission pays 15K, and it starts in Blockade Point Alpha. Many corporate and military vessels have been eliminated by this threat.  I want you to destroy them first.")],
        "accept":[("Burrows","Count on it!")],
        "reject1":[("Burrows","I don't think I like the idea of going against an unknown threat. What if I don't make it?")],
        "reminder":[("Burrows","So where is this unknown threat of yours again?"),("Kaydence","You want to eliminate all unknown units in the Blockade Point Alpha system before they eliminate any more of our ships. The reward is 15000 credits. Please do hurry.")],
        "reconsider":[("Burrows","So what are the details again and the reward?"),("Kaydence","You're to go to Blockade Point Alpha, where we've lost a number of ships...We need you to eliminate them: the pay is 15000 credits.")],
        "reject2":[("Burrows","Actually I think I need to upgrade my ship before I take them to task. I'll be back with a souped up ship and in need of some more credits")],
        "failure":[("Kaydence","I can't believe you those terrorists get away"),("Burrows","Sorry, sweetheart. They just were too fast in those death darts"),("Kaydence","Those death darts are the same stilettos the military flies. Now get used to it.  I won't be seeing you doing any more work for me.  See you later")]}


kaydence5speech={"intro":[("Those guys didn't put up much of a fight in those death darts"),("Kaydence","Hey those were military stilettos, nothing to be sneezed at!"),("Burrows","And I wonder just how they got them. Anyhow it wasn't a very wise choice. So what do you want me to do next"), ("Kaydence","From your scanners and recent intelligence, these attackers call themselves the AWACS--Armed Workers against Coporate Slavery.  While none of us like the way these big corporations have been bullying people around, we have a war to fight...and that means putting these dogs down."),("Burrows","Crushing the little guy, eh?"),("Kaydence","More like making sure these terrorists don't crush us...but yes"),("Kaydence","I want you to go to the Auriga system and eliminate the terrorists there. The reward is 16K credits")],
        "accept":[("Burrows","Not a problem: I'm on it. I'll nail them all in Auriga")],
        "reminder":[("Burrows","So where are these terrorists"),("Kaydence","You want to eliminate all AWACS units in the Auriga system before they cause us any havoc here. The reward is 16000 credits. Please do hurry, we have some marines just waiting to get into that system.")],
        "reject1":[("Burrows","I'm not sure this one is worth my while. For 16K I can do something quite a lot nicer than smashing the little guy."),("Kaydence","Well they aren't your ordinary little guys. They are dangerous terrorists causing havoc."),("Burrows","I'll think about it. Then again where are these guys located. Maybe I could just drop 'em a line"),("Kaydence","Give 'em a foot and they'll blow off your leg. They're godless freaks."),("Burrows","Unlike the retros... anyhow I'll think about it")],
        "reconsider":[("Burrows","Ya these armed workers sound pretty dangerous, but not dangerous enough that I can't put them in their place."),("Kaydence","Good. The reward is 16000, I take it you're in?")],
        "reject2":[("Burrows","That doesn't sound too safe right now. I think I'll let it cool off."),("Kaydence","They may not stay just in that one sector if you let them 'cool off' You better reconsider and help me out here.")],
        "failure":[("Burrows","I couldn't manage them. There were too many"),("Kaydence","I'm sorry to hear that, but we needed those terrorists dead. You'll have to do better than that to work for me. I'm sorry")]}

kaydence7speech={"intro":[("Kaydence","Looks like we have another load of key arrests.  I need you to escort a prison transport out of this system. It should be a cake walk since this is the military base of the sector, but I'm paying 10000 credits for a safe escort. Are you in?")],
        "accept":[("Burrows","Sure I'm game. Where do I meet this transport?"),("Kaydence it should be waiting for you as you launch.  Just make sure it gets to the jump point. We've got some military escorts to take it from there.  Meet me back here for your pay")],
        "reject1":[("Burrows","I've got better things to do than babysit a bunch of criminals"),("Kaydence","Processing these criminals is the key to finding out where the leaders of the AWACS movement are. It's not as petty as you may think")],
        "reconsider":[("Burrows","I'm thinking that maybe you're right. Maybe this mission is important. How much is it worth to you"),("Kaydence","It's 15000 credits for a successful escort. Are you in?")],
        "reject2":[("Burrows","I don't really like doing prison duty. I'll talk to you later")],
        "reminder":[("Kaydence","Are those prisoners in safe hands?"),("Burrows","Safe? You're calling me safe? Err I think they're in space somewhere"),("Kaydence","Get a move on.We have reason to suspect there may be attacks on them soon."),("Burrows","All right, all right I'll go babysitting")],
        "failure":[("Kaydence","I can't believe you let the attackers get to that transprot. Are you in cohorts with them"),("Burrows","And I can't believe these rebels would attack their own ship"),("Kaydence","That's where you're wrong. I think it wasn't the AWACS group, but someone more sinister even. Anyhow I can't let you work for me any more.  It's completely out of our bounds to start letting prisoners die before they even get to trial.")]}
kaydence6speech={"intro":[("Kaydence","I see you've been successful. I'm glad to see it. I just got word from one of our marine ships that he was able to land on Elysia and they've already located some key prisoners.  They need to undergo a lengthy trial in the capitol in New Constantinople."),("Burrows","And that's where I come in, I take it?"),("Kaydence","Indeed those are all the details I can give you at this moment, but I'll assure you the reward will be 18000 credits, not half bad for the work I'm going to give you. Interested?")],
        "accept":[("Burrows","Sure, why not. You've been good to me...before"),("Kaydence","I need you to escort a drayman full of prisoners over to New Constantinople.  We have word that there are insurgents just waiting to attack in Newcastle, so please avoid that and go along the main populated route through New Detroit.  That way you can guarantee the troop transports survival. Godspeed and good luck!")],
        "reject1":[("Burrows","I think I'll need to think this one over. There is a lot of hubbub about these recent arrests of protesters, some of whom aren't even dangerous")],
        "reconsider":[("Burrows","Well I'm back.  I think I've justified the moral grounds on which to take this mission. Remind me of the fiscal grounds again?"),("Kaydence","The mission is a clean escort. It will pay a whopping 18,000 credits, which should be good enough to keep you eating. That good enough for you?")],
        "reject2":[("Burrows","Anything is good enough for me, baby, except this mission. I think I'm gonna take a hike for now.")],
        "reminder":[("Burrows","Where am I going with that transport again?"),("Kaydence","You're supposed to go to New Constantinople, stopping nowhere and going through New Detroit on the way. Take no detours or you may well end up eating it. There are lots of rebels out there."),("Burrows","I thought you called these folks terrorists, not rebels. Where'd that come from"),("Kaydence","Just get moving. We don't have any time to lose")]}

kaydence8speech={"intro":[("Kaydence","These latest arrests have really put a spear through the terroist operations in this sector.  I have to admit it's your doing that really helped bring it home.  I heard of a number of rescue attempts on these transports and it's a good thing the prisoners made it all in one piece.  There are a few scattered angry members around. They seem to be in the Ragnarok system for now.  I believe there is also an encroachment of Kilrathi there too, so if you could head over there and eliminate them that would be worth a fat 13000 to us. You in?")],
        "accept":[("Burrows","Cats and chickens, eh? It's on!")],
        "reject1":[("Burrows","I'm not sure I like the sound of angry Kats and angry workers. I think I'll sit this one out."),("Kaydence","I can promise you some nice work after your done. Please consider it")],
        "reconsider":[("Burrows","Ok what are the odds an what is the mission again?"),("Kaydence","I want you to patrol Ragnarok and eliminate all Kats and terrorists for a wad of cash that should make you grin.  You in?")],
        "reject2":[("Burrows","I'm out actually. Maybe later, Kaydence")],
        "reminder":[("Kaydence","So are the Kats dead? How were the terrorists. Did they give you any troube"),("Burrows","Actually I'm not done eliminating them yet. I'll be back when I do.  You wanted Ragnarok clean, right"),("Kaydence","Ya... did your brain get cleaned or something?")],
        "failure":[("Kaydence","I'm sorry but our contract is over. I'll see you far in the future perhaps."),("Burrows","Bye sweetie")]}
kaydence9speech={"intro":[("Kaydence","Well I'm glad you got rid of the enemies of the state in Ragnarok. Now we can push our border back out to Blockade Point Alpha again."),("Burrows","No worries. All in a days work, Madame"),("Kaydence","A privateer with manners. Wonder will never cease to amaze me.  Anyhow Your next assignment is a bit more important. We suspect that one of the new corporations that has risen to power based on the recent political events is exploiting this power to make secret deliveries to our enemies, Kilrathi included.  There is reason to believe a critical shipment to the Tr'Pakh system is happening today, and you must stop it. The reward is 20K. Are you game?")],
        "accept":[("Burrows","Sounds important, and I wouldn't want to dissapoint you, sweetie. I'm on the job"), ("Kaydence","And you've got flair to. Good luck to you, sir")],
        "reject1":[("Burrows","Well it sounds like they're just deliverin a bit of Catnip to Kilrah. Maybe I should dabble in a bit of that myself."),("Kaydence","Funny, but this is serious. They could be giving these guys new weapons that are only currently available to the Confederation. Please reconsider.")],
        "reconsider":[("Burrows","Alas I guess I'm back to consider taking out your Fur(ball)-trading merchant. What's your best Offer?"),("Kaydence","I'm offering 20 grand for the destruction of one merchant in the TrPakh system. Are we agreed?")],
        "reject2":[("Burrows","I think I'll stay on this side of the border, sweetheart. Those cats have claws")],
        "reminder":[("Burrows","So where is this kilrathi system these fools are trading to?"),("Kaydence","It's in the Tr'Pakh system. You need to eliminate the merchant there who's been doing business with the furballs."),("Burrows","Consider it done!")],
        "failure":[("Burrows","Well I'm sorry I failed you."),("Kaydence","Such treasure to be sought and you couldn't handle it. Well I can't say I envy you, but don't show your face here again. It's not welcome")]}
kaydencefinal=[("Burrows","I can now claim success. I've vanquished our enemy. And he had the logo of Transsector Plus."),("Kaydence","I can't believe he'd be so stupid to include the logo of his company on the ship. However I can imagine that we'll be able to follow that chain of evidence back to the indiviudal responsible. In the meantime I'm going to hand you over to my good associate and friend Destinee."),("Burrows","Good It's been too long since we met. I wonder how she's doing?"),("Kaydence","Well that insystem policing job has left her with a lot of success, and I hear she has another big pirate base to fry a little closer than last time.  I take it you'll be seeing her in Munchen"),("Burrows","Don't get jealous, Kaydence, but I have a date with Destinee, and I don't intend to be late")]


soren1speech={"intro":[("Soren","Good day, my name is not known to you, but you can call me Soren."),("Burrows","Why hello there Soren. I was referred to you by--"),("Soren","You may discard the pleasantries; I'm a man of business, not banter.  I need you to take care of a mark for me. It's nearby in the Ragnarok system.  The pay is 25,000 credits.  I will need you to perform some further services for me after that one. Interested?")],
        "accept":[("Burrows","Agreed, can I have some more specifics?"),("Soren","Our target is a Drayman transport. They will signal for help. Destroy them."),("Burrows","Ok and you say this is in the Ragnarok system? I'm on it.")],
        "reject1":[("Burrows","I'll need some more details before I go out on a limb for this one"),("Soren","That price requires no details")],
        "reconsider":[("Burrows","I'm reconsidering our deal. Give me some details about the bounty"),("Soren","Bounty is such a hard word...shall we say 'permanent relocation'.  The mark is in Ragnarok system. It is likely to be lightly defended")],
        "reject2":[("Burrows","I'll need some information on the opposition I'll be looking at."),("Soren","I'm sorry but I don't divulge this information lightly. Good day")],
        "reminder":[("Soren","Good to see you back. What's the status of your mission."),("Burrows","As of yet incomplete"),("Soren","Unacceptible I require you to finish it immediately or your compensation goes unpaid"),("Burrows","Touchy, touchy.  Lets just say that a crafty killer takes his time.  Don't worry when I'm good and ready I'll take care of your transport in Ragnarok")],
        "failure":[("Soren","Your clumsiness is unacceptible. Your contract's done.")]}
soren2speech={"intro":[("Soren","For the final mission in our contract I have a somewhat special assignment"),("Burrows","Let me guess, another cargo run"),("Soren","Why yes, but not to our--or rather your--ordinary customers."),("Burrows","I can't believe you deal with those Retros",),("Soren","You presume too quickly, privateer. Retros aren't interested in our goods, but various other species are."),("Burrows","I didn't know we dealt with aliens"),("Soren","We don't, but you do, for a large sum of money.  It's a simple delivery. They want a plant, we have the plant. It pays 60,000 credits--plus some perks."),("Burrows","Is Confed onto this"),("Soren","There's a chance they'll be able to scan for the cargo in question.  If so, I'm sure you'll be able to explain"),("Burrows","I have a feeling this mission isn't going to be a cakewalk."),("Soren","That's why I'm paying someone I know can get the job done, and keep quiet about it.  I think you'll have a much better reason when you complete it for me.  Are you interested?")],
    "accept":[("Burrows","I've always dreamt of running catnip to Kilrah. I guess this is my chance to score big time. Where is the location of the secret Kilrathi base?"),("Soren","I'm sure you will find the dropoff point in the Tr_Pakh system.  I'm also convinced that 60,000 won't be your only reward in this matter.  But I will leave that bit to you.  Come back here for your 60,000 and contract termination.")],
    "reject1":[("Burrows","I'm not so sure this mission fits my profile of a lucrative cargo run. It sounds more like suicide, or delivering honey to the Bee's nest"),("Soren","Trust me, these bees are in need of honey. And I believe you can make quite a sum giving it to them"),("Burrows","If they don't sting me first.  I'll pass")],
    "reconsider":[("Burrows","I'm reconsidering your offer. 60K is a lot of cash to be given.  Could I claim half upfront"),("Soren","I'm sure the reward is adequate to be paid at the end. I've always given my bill on time, and I'm sure you can clear your side. Is this reasonable?")],
    "reject2":[("Burrows","Actually I don't deal with the enemy, and quite frankly I'm not sure you don't fit that bill quite nicely"),("Soren","But luckily you don't know who I am or where I work. So if you refuse, I'm sure I'll be able to fulfill this contract myself.")],
    "reminder":[("Soren","The clients haven't received your shipment and they are starting to get irritable. I need you to deliver the cargo immediately or you risk getting any reward at all. Remember 60,000 for delivering the cargo to Tr_Pakh!")],
    "failure":[("Soren","You greedy privateer took the cargo and the loot for yourself and failed to deliver your bargain. If you check the news nets I'm sure you'll find a rather hefty bounty added to your head.  Have a nice flight mister. I'm sure it wont' be very far.  Remember that the cats want you dead as much as confed does. And your crimes are publically viewable.  Good day to you, sir")],}
demetria1speech={"intro":[("Demetria","Thank you so much for rescuing our organisation, comrade.  I hereby grant you honorable admission into the AWACS, Armed Workers Against Corporate Slavery"),("Burrows","Why thank you, but I'm not sure that would look too good on my resume as privateer-for-hire"),("Demetria","Perhaps, but I'm still thrilled that you've decided to help us out, and I'm offering you the reward we talked about"),("Burrows","I'm still surprised when people keep their word in this dangerous galaxy.  So is there any other service you need performed?"),("Demetria","Oh yes, we need you to help escort another one of the transports that managed to successfully revolt in to Auriga. There are apparently some attackers, but they aren't confed as you might expect but instead they are corporate-paid hunters who've been given orders to dog and destroy the transport before the authorities recapture it. I hope you get to them first. We will offer you 10,000 credits for the defense of the prisoner transport. Are you in?")],
        "accept":[("Burrows","Sounds like easy pickings. Any word as to the number of them"),("Demetria","Thanks to the evasive maneuvers the drayman went through, she managed to each hunter into a long stream--since they work alone, they are more than happy to clean up after each other. It seems as if you probably won't be facing many at a given time, but they are coming fast and furious."),("Burrows","Fantastic, sounds like a cakewalk")],
        "reject1":[("Burrows","I think I've had enough trouble avoiding the authorities myself. I think I'm going to lie low for a little bit"),("Destinee","These aren't the authorities, they are just hunters like yourself trying to make a killing at the behest of the corporations...")],
        "reconsider":[("Burrows","I'm rethinking that mission you've assigned me to. It sounds too easy to pass up. What's the reward for saving that transport again?"),("Demetria","I'll pay 10,000 for bringing in that transport alive. Are you with us, comrade?")],
        "reject2":[("Burrows","I think I should stick to my instincts for now.  I'll let you know if I manage to change my mind")],
        "reminder":[("Demetria","Are my comrades alive and well? Have you rescued the poor workers?"),("Burrows","My ship is still powering up on the pad. I'll snap to it.")],
        "failure":[("Demetria","I can't believe you let our people down. There were important leaders of our movement on that ship. I'm not sure we will be able to continue putting resistance to the corporate dogs out there.  I will let you know if I have further work for you, but for now, comrade, I think it's best if we parted ways"),("Burrows","Shame, I always wanted my own hammer and sickle trophy")],}
demetria5speech={"intro":[("Demetria","Comrade! You're back! I am most pleased to report that we have gained a large enough foothold in the Gemini sector to be able to negotiate with Confed with leverage. The end of the revolution is at hand, and the lives of workers across the Confederation will be able to improve.  However there is still one last thorn in our side. One Soren Malakai has been in charge of much of the massive resistance we faced at each turn. His personal defense contracting corporation has become weaker due to our success and internal outcry within the Confederation.  However we have information that he may be dealing with common foes of a greater level. We are worried that he is working with Kilrathi in the Tr'Pakh system.  We don't know exactly where he is, but since he is on the move, personally making deals, we think this is an excellent time to get our mark.  Can you do this for 9000 credits?")],
    "reject1":[("Burrows","I'm sorry, I'm not sure I can do it. Dealing with humans is bad enough, but sometimes those cats seem to have eyes on the back of their heads."),("Demetria","This is our one chance to find him outside the corporate defense walls of his personal fortress. Please reconsider")],
    "accept":[("Burrows","On my word will Soren Malakai, that evil double crossing corporate whore, will die. A toast to the revolution will be made with his blood."),("Demetria","Fierce words, but my you are interesting when you are angry.")],
    "reconsider":[("Burrows","Hitting that Soren might be fun. It would be good to get one of the serious bad guys behind these operations. What's the reward again?"),("Demetria","My bank is almost drained, and the AWACS is transferring to a more uniform system of currency, so I only have 9000 credits of discressionary funds left.")],
    "reject2":[("Burrows","Not enough cash for me right now. Find someoen else.")],
    "reminder":[("Demetria","Have you found Soren in the Tr'Pakh System?"),("Burrows","He's managed to elude me thus far. I'll let you know when I do")],
    "failure":[("Demetria","Your failure was dissapointing. I'm not sure if we will ever be able to purge that rat! Alas you have helped us through so much. We clearly will search for you again if the plight of the people ever needs someone as fierce yet kind as yourself.")],}

demetriafinal=[("Burrows","That rat had a whole wing of Kilrathi at his side. I have no idea how much damage he probably ended up doing to humanity as a whole."),("Demetria","We probably will never know the extent of his malice, but one thing is sure, this portion of Gemini is better in the hands of the people than in the hands of an autocratic government like that of the Confed.  We are already reorganizing ourselves such that each person has a voice in politics, yet no large group can crush a smaller one. We have drafted a constitution and a bill of rights that is much more expanded than the one that Confed has been whittling away at for all these years.  And all of this is thanks to your excellent skill and piloting work combined with the strength and resolve of the people who lived, died and sacrificed for change.  Together we can overcome. Together we can become the best, for the state is there to help the weak, educate the illiterate, and heal the wounded, not to enforce the power of the few. To this end we will fight, to this end we will struggle, to this end we will die. And so it is with the ISO, the Interstellar Socialist Organization."),("Burrows","It was wonderful to work with such a lady as yourself. Powerful yet beautiful. You are one of a kind, Demetria, one of a kind. I hope to see you again in the near future"),("Demetria","And so do I, so do we, and so does every man, woman and child that is a member of the Party")]

def OptionalTalkingHead(sprite):
    return "#\nimport Base\nimport campaign_lib\nif campaign_lib.doTalkingHeads():\n\tcampaign_lib.AddConversationStoppingSprite('Talking',"+repr(sprite)+",(.582,-.2716),(3.104,2.4832),'Return_To_Bar').__call__(Base.GetCurRoom(),None)\n"




def IntroCutscene():
#   return None#delete this line for intro cutscene with talons
    return Cutscene('Pirate_Encounter','IntroCutscene.spr',(0.582,0),(3.104,1.2416),'Intro_Cutscene',[("","                                                                                                 ","barspeech/campaign/intro.ogg"),"                                                                                      ","                                                                                 ","                                                                   ","                                                  ","                                                                                   ","                                                                                                ","                                                                                           ","                                                                                           ","                                                                                         ","                                                                ","                                                 ","                                                                                    ","                                                                                                             ","                                                                            ","                                                                                ","                                                                                ","                                                                                ","                                                                                ","                                                                                ","                                                                                ","                                                                                ","                                                                                ","                                                                                ","                                                                                ","                                                                                ","                                                                                ","                                                                                ","                                                                                "],"intro.m3u","mining_base.m3u").MakeEnqueue()

sorenseed=7
synseed=28
def syn(word):
    global synseed
    synseed+=23
    syndict={"see":["observe","found that","heard","informed myself that","garner"],"adequately":["acceptibly","sloppily","slowly","unattentively"],"assignment":["job","mission","run","contract"],"delivered":["transported to","taken to","moved","hauled"],"opposition":["attacks","engagements","attempts to stop you","action"],"I don't exist":["There is no Soren","Soren is a figment of your active imagination","You aren't employed by anyone","These actions are yours alone"],"people":["folks","dudes","men","members"],"lucrative":["profitable","important","dangeous","illegal"]}
    if word in syndict:
        tmp = syndict[word]+[word]
        return tmp[synseed%len(tmp)]
    return word
def getDialog(agg,carg):
    if agg=="militia" or agg=="confed":
        return ["We know you are carying "+carg+" contraband on your ship with the intent of servicing our enemies.  Dump it now or be destroyed!","You are hereby under arrest under confed contraband law 2630 paragraph 24 subparagraph 3"]
    elif agg=="AWACS":
        return ["Comrade, you are doing the work of one of the largest shadow coporations in the Gemini sector.","You are the enemy of all workers and those who respect our rights.","The armed workers against corporate slavery have denoted you a threat and an enemy for the destruction you have wrought on those innocents who were arrested."]
    else:
        return ["You better dump your "+carg+" or you can as good as bite the dust, buddy"]
def SorenCargoMission(priv,destsys,destbase,cargo,aggressor,lastreward=0,NextMission=None,specialspeech=None):
    global sorenseed
    sorenseed+=5
    where=destsys[-1].find("/")
    sys = destsys[-1][where+1:]
    if (NextMission==None):
        NextMission=CampaignEndNode(priv)
    sorenspeech ={"intro":[("Soren","I "+syn("see")+" you completed your last run "+syn("adequately")+". I have another "+syn("assignment")+" for you."),("Burrows","Excellent. I'm sure I can handle it. What are the details"),("Soren","I need some cargo "+syn("delivered")+" to "+sys+". There might be "+syn("opposition")+" from members of the "+aggressor.capitalize()+" as you approach your destination. Be wary...and as far as your potential captors are concerned "+syn("I don't exist")+".")],
        "accept":[("Burrows","Consider it done."),("Soren","I will take you at your word, but I will not pay you until you return The cargo is of type "+cargo+"")],
        "reject2":[("Burrows","It sounds too dangerous, and it could hurt my credit rating, especially with the "+syn("people")+ " from "+aggressor.capitalize()+"."),("Soren","I see. I will note that when selecting you for more..."+syn("lucrative")+" "+syn("assignment")+"s.")],
        "reject1":[("Burrows","I find it inconvenient at this time"),("Soren","Then I will find someone else. Good day")],
        "reconsider":[("Burrows","I've made time available to perform services with you again."),("Soren","Are you feelin' lucky?")],
        "reminder":[("Soren","My sources say that you have failed to deliver the cargo.  Do so at once or you risk your pay and your neck.  You must deliver "+cargo+" to the "+destbase+" in "+sys+". Go now!")],
        "failure":[("Soren","You have failed to deliver the cargo. My sources say you lost it on the way.  I have placed a bounty on your head. Go now lest I need to pay.  I prefer to see a man run his entire life in fear than wastefully killed. But I cannot excuse your arrogance.")],}
    if specialspeech:
        sorenspeech=specialspeech
    return MakeCargoMission(priv,
        SOREN_SPRITE,
        [InSystemCondition("Gemini/Midgard","Heimdel")],
        [InSystemCondition(destsys[-1],destbase)],
        AddCredits(lastreward),
        LoadMission('ambush','ambush',(priv.name+"_mission",(destsys[-2],),0,aggressor,sorenseed%7+1,'','',getDialog(aggressor,cargo),destsys,destbase,False)),
        (cargo,30),
        priv.name+"_mission",
        sorenspeech,
        None,
        CampaignEndNode(priv),
        NextMission)
demetriaNames=["Phil Tokris","Gov. Ishtan","Ross Atog","Fen Abil","Pol Fovkos","Stalin Abdeg","Itan Folker","Rasper Kennigan","Fohl Tygar","Ishtan Harkin","Redo Wahilis"]
def RandomRevolutionMission (priv,sys,base,aggressor,lastreward,demetriaseed,count,FailureMission,NextMission):
    if (count<=0):
        return NextMission
    demetriaseed=demetriaseed*1637
    demetriaseed=demetriaseed+19
    max=141
    dmm=demetriaseed%max;
    lastreward1=3000.+1000.*dmm%2+2000.*dmm%3+3000.*dmm%5;
    global demetriaNames    
    genericreject=[("Burrows","I'm not sure I'm strong enough to hold the revolution by myself."),("Demetria","You don't have to be. We are helping on the ground. Just consider helping us maintain space superiority")]
    genericreject2=[("Burrows","I can't continue killing innocent "+aggressor.capitalize()+" units just because you are sick of your boss. This revolution should stop. I can't help defend it any more"),("Demetria","It is sad when someone is so blind to the torture and assualt that the corporations keep suffocating our citizens with. You should join us now."),("Burrows","Not this time honey. Maybe in bed")]
    genericreconsider=[("Burrows","I'm considering your offer. I would love to assist the revolution once more in its grand quest to eliminate these large oppressors"),("Demetria","Thank Trotsky you're back. We need you to fly. Will you do it?")],
    genericfailure=[("Burrows","I'm sorry I failed you!"),("Demetria","There is no sorry for us here. Your failure caused some major damage to both morale and our strategic position. Even now we've lost more than a third of what we gained in the past week. And I'm afraid it's not going to stop there.  There will be other battles to fight...other systems to take over.  The revolution seems to be wilting before our eyes."),("Burrows","Shame, shame")]

    NRM = RandomRevolutionMission(priv,sys,base,aggressor,lastreward1,demetriaseed,count-1,FailureMission,NextMission)

    if (demetriaseed%max<30):
        teststr =aggressor.capitalize()
        demetriaspeech={"intro":[("Demetria","Excellent, comrade. Your work will ignite this revolution with the corpses of the corporate masters. However, there are a number of new "+teststr+" patrols in this system. In order to hold our system, we need to maintain space superiority at all costs. Please conduct a patrol of the system. We have 8000 credits for you when you have eliminated all enemies in this system.  I can offer a party member as an escort on your wing")],
            "reject1":genericreject,
            "reconsider":genericreconsider,
            "reject2":genericreject2,
            "accept":[("Burrows","This should be trivial for a worker like myself."),("Demetria","Do not be too confident. The "+teststr+" forces are more clever than you give them credit for.  Money and profit can make almost anyone clever.  But I need you to use their greed to their disadvantage.  Show them what a revolution does to the enemy of the people!"),("Burrows","And so I will, lovely. So I will")],
            "reminder":[("Demetria","I need you to patrol the system and eliminate all "+teststr+" hostiles so we can maintain space superiority. Can you do it?"),("Burrows","Not a worry, m'lady. Consider it done")],
            "failure":genericfailure}
            
        return MakeMission(priv,
                DEMETRIA_SPRITE,
                [InSystemCondition(sys,base)],
                [InSystemCondition(sys,base)],
                AddCredits(lastreward),
                LaunchWingmen("AWACS","stiletto",1),
                'cleansweep',(0,6,1200,0,(),priv.name+'_mission',1,demetriaseed%4,.4,.2,aggressor,1,1),
                priv.name+"_mission",
                demetriaspeech,
                None,
                FailureMission,
                NRM)
    elif (demetriaseed%max<60):
        findhim = demetriaseed%2
        located="We have located your target's position and have uploaded it into your computer."
        if findhim:
            located="We do not yet know where your target is. He is most probably in this system somewhere, so your best bet is to set your scanners to search for "+aggressor.capitalize()+" starships."

        demetriaspeech={"intro":[("Demetria","Ideal, comrade. You are worthy of the metal of Trotsky: forward with the revolution! Our recent successes had drawn a number of interesting personalities into this sector.  Specifically one "+demetriaNames[demetriaseed%len(demetriaNames)]+" has been responsible for hunting down a large number of revolutionaries. It seems as if our enemies have employed him specifically to halt the revolution in this sector. "+located+"We need you to destroy him first. We offer a mere 5000 for this effort, but the reward is the revolution! ")],
            "reject1":genericreject,
            "reconsider":genericreconsider,
            "reject2":genericreject2,
            "accept":[("Burrows","And for the revolution I will slay this man. He has no right to keep killing our comrades, nor any right to suppress the ardent workers! Viva La Revolution!"),("Demetria","Spoken like a revolutionary. I love you!")],
            "reminder":[("Demetria","Have you been able to locate "+demetriaNames[demetriaseed%len(demetriaNames)]+" yet?"),("Burrows","I have made it my mission, but he still eludes me.")],
            "failure":genericfailure}

        return MakeMission(priv,
            DEMETRIA_SPRITE,
            [InSystemCondition(sys,base)],
            [InSystemCondition(sys,base)],
            AddCredits(lastreward),
            None,
            'bounty_leader',(0,0,0,0,demetriaseed%5,aggressor,(),priv.name+"_mission",'','',findhim,'','',getDemetriaDialog(aggressor,2),['tungsten','tungsten_hull']),
            priv.name+"_mission",
            demetriaspeech,
            None,
            FailureMission,
            NRM)
    elif (demetriaseed%max<90):
        demetriaspeech={"intro":[("Demetria","By Marx your success has caused a bursts of joy and enthusiasm on the surface. We've controlled over 66% of the planet, and we are reorganizing its very infrastructure to accomodate each worker, giving every man his fair share of the work, and fair share of the reward. All of us are equal! However there are some problems in space: we have encountered resistance from the "+aggressor.capitalize()+" starships. They are assaulting one of our assets in this system. I am offering 6000 for its defense in addition to two wingmen. Can you do this for the revolution? I know my details are vague, but we will give you a chip with further instructions.")],
            "reject1":genericreject,
            "reconsider":genericreconsider,
            "reject2":genericreject2,
            "accept":[("Burrows","I can destroy whatever the "+aggressor.capitalize()+" can throw at me. Fear not for your revolution, for I will defend it to my last breath!"),("Demetria","I fear not when you do this for the love of the people, for the love of our freedom.")],
            "reminder":[("Demetria","Have you protected our assets in this system?"),("Burrows","I'm still preparing for this battle. It's not certain what kind of offense I will face, so I'm still tweaking my starship and refueling. I will report when I have cleaned our foe.")],
            "failure":genericfailure}
        return MakeMission(priv,
            DEMETRIA_SPRITE,
            [InSystemCondition(sys,base)],
            [InSystemCondition(sys,base)],
            AddCredits(lastreward),
            LaunchWingmen("AWACS","stiletto",2), # Script to be run to start the mission
            'defend',(aggressor,0,demetriaseed%2+2,1500,999999999,0,demetriaseed%5>3,demetriaseed%5>2,'AWACS',(),priv.name+"_mission",'','','',int((demetriaseed%3)/2),getDemetriaDialog(aggressor,2)),
            priv.name+"_mission",   
            demetriaspeech,
            None,
            FailureMission,
            NRM)
    else:
        demetriaspeech={"intro":[("Demetria","And the man of the people has successfully destroyed those capitalist pigs before in the name of the revolution. My you are a hero worthy of song and tale. We have identified the possibility of new "+aggressor.capitalize()+" patrols in this system. We need you to ascertain the strength of any enemy forces in this system. We have 4000 credits for this scanning run. Can you assist us?")],
            "reject1":genericreject,
            "reconsider":genericreconsider,
            "reject2":genericreject2,
            "accept":[("Burrows","If I can't scan this system, then your revolution has bigger problems than the "+aggressor.capitalize()),("Demetria","Oh I hope not, comrade, I would not want to see a hero like you get hurt"),("Burrows","You need fear not, I will perform my duty for the revoltion--or die trying")],
            "reminder":[("Demetria","You need to patrol the system so we can ascertain our space superiority. Can you do it?"),("Burrows","Not a worry, m'lady. Consider it done. For Lenin!"),("Demetria","May Trotsky smile upon this day.")],
            "failure":genericfailure}
        return MakeMission(priv,
            DEMETRIA_SPRITE,
            [InSystemCondition(sys,base)],
            [InSystemCondition(sys,base)],
            AddCredits(lastreward),
            None,
            'patrol',(0,10,50,0,(),priv.name+"_mission"),
            priv.name+"_mission",
            demetriaspeech,
            None,
            FailureMission,
            NRM)

def getDemetriaDialog(aggressor,typ):
    if (typ==0):
        return [("We know you are supplying known rebels with weapons of mass destruction. You are hereby ordered to stand down for arrest or be destroyed",False,"campaign/demetria0.ogg")]
    elif (typ==1):
        return [("The stiletto in your group is a known fugutive, saboteur and AWACS party member.",False,"campaign/demetria1.ogg"),"Surrender him to us at once or be destroyed."]
    else:
        return [("The AWACS cannot fight a revolution when it doesn't have the support of the people.",False,"campaign/demetria2.ogg"),"We know you will fail. You already cannot withstand our assaults.  The AWACS group will be crushed from within."]


def SimpleInvertPrequisites(pre):
    ret = []
    for i in pre:
        ret+=[NotCondition(i)]
    while len(ret)>1:
        ret= [OrCondition(ret[0],ret[1])]+ret[2:]
    return ret
    
def DemetriaRevolutionMissionPreq(priv,demetriaseed,path,base,aggressor,lastreward,FailureMission,NextMission,introspeechMoveon,introspeechHalt,prequisites):
    iprequisites=SimpleInvertPrequisites(prequisites)
    return CampaignNode().Init(priv,
            [],
            None,
            DEMETRIA_SPRITE,
            TrueSubnode(),
            None,
            [DemetriaRevolutionMission(priv,demetriaseed,path,base,aggressor,lastreward,FailureMission,NextMission,introspeechMoveon,prequisites),
            CampaignClickNode().Init(priv,
                [InSystemCondition(path[0])]+iprequisites,
                introspeechHalt,
                DEMETRIA_SPRITE,
                GoToSubnode(0,AddCredits(lastreward)),
                None,
                [DemetriaRevolutionMission(priv,demetriaseed,path,base,aggressor,0,FailureMission,NextMission,[])])])

def DemetriaLoseRevolution(priv,path):
    return DemetriaRevolutionMission(priv,
            123409,
            path,
            "N1912-1",
            "militia",
            0,
            CampaignEndNode(priv),
            DemetriaRevolutionMission(priv,
                191422,
                ["Gemini/DN-N1912","Gemini/Hinds_Variable_N"],
                "Oresville",
                "confed",
                2000,
                CampaignEndNode(priv),
                DemetriaRevolutionMission(priv,
                    912411,
                    ["Gemini/Hinds_Variable_N","Gemini/Aldebran"],
                    "Matahari",
                    "confed",
                    10000,
                    CampaignEndNode(priv),
                    CampaignClickNode().Init(priv,
                        [],
                        [("Demetria","The revolution has now ended. The people are happy with their newfound power and even now they are rebuilding the mess that confed made of the Potter quadrant. It is too bad that we could not capture the hearts of the rest of Gemini, or for that matter the rest of the confederation. But we will endure--and serve as a reminder to the confederation that Corporate slavery--will NOT stand--ever. And we will fight for the rights of the workers! It is an everlasting struggle, but your services are no longer needed-- politics will bring the changes we need now--politics and a stroke of luck and ingenuity. So long Comrade, you have made a noble effort.")],
                        DEMETRIA_SPRITE,
                        GoToSubnode(0,AddCredits(9000)),
                        None,
                        [CampaignEndNode(priv)]))),
            [("Demetria","Your failure has cost this revolution greatly. I'm afraid we will have to  pull out of this sector--it's a shame.  But we can safely withdraw to the DN-N1912 system. There are rumors about that this system has the seeds of revolution. Perhaps we can regain the power of the revolution! Perhaps we can succeed after all."),("Burrows","I haven't come all this way for nothing, have I"),("Demetria","The power of the revolution, of the people, of Marx and Lenin--that power is in you... you must fight--we might fight for what is right--for our Party, for the People's Party!")])


def DemetriaRevolutionMission(priv,demetriaseed,path,base,aggressor,lastreward,FailureMission,NextMission,introspeech=[("Demetria","Congratulations, comrade; you've supported yet another revolution by the Workers and against the oppressive corporations! The sector is finally secure and we are reinforcing against potential attacks by the various white armies. We are again in your debt, and have managed to collect 10,000 credits to reward you for your excellent marksmanship and courage in this struggle.")],prequisites=[]):
    sys = path[-1]
    nicesys = sys[sys.find("/")+1:]
    demetriaspeech1={"intro":introspeech+[("Demetria","The spirit of the revolution is growing and taking root in "+nicesys+", and we have no time to lose. I need you to ship some weapons to the workers there.  I will meet you on the planet, getting there through other means."),("Burrows","Anything for you, sweetheart."),("Demetria","The revolution needs your courage, your justice, to help our people resist oppression!")],
        "accept":[("Burrows","I will do my bit for this revolution. And delivering some illegal cargo for a beautiful girl like you is hardly a punishment, more of a pleasure. I'll see you on the other side, gal."),("Demetria","May the revolution guide you!")],
        "reject1":[("Burrows","Delivering weapons to the middle of enemy territory where there's a revolution in progress does not sound like the safest proposition. Do you have any tips on what sort of opposition I'll be facing?"),("Demetria","It looks like there could be a few "+aggressor.capitalize()+" fighters waiting on the way, but I think you can handle it."),("Burrows","I'm not sure I can manage it at the moment, let me consider")],
        "reconsider":[("Burrows","I think that I can handle the odds. Where would I taking these weapons? And more importantly what would I be paid?"),("Demetria","You would be paid a sum total of 8000 credits for assisting the revolution by delivering weapons to "+nicesys+". Will this suffice?")],
        "failure":[("Demetria","You corporate whore! You failed the revolution and dumped the cargo for profit. You have no place among the true revolutionaries. So long, and may our paths never cross except at the end of a blade.")],
        "reject2":[("Burrows","Sorry, sweetheart. I take higher paying customers"),("Demetria","The revolution is not about money, it is about freeing the workers from oppression, about turning our society into a welfare state rather than a state which breaks the backs of the workers at the behest of the corporate influence in New Constantinople"),("Burrows","Politics are just an excuse to make a lot of money...now excuse me.")],
        "reminder":[("Burrows","Where was I supposed to go with that cargo?"),("Demetria","You need to deliver the weapons to "+nicesys+" before the revolution dies down or is wiped out. Hurry!"),("Burrows","Anything for a lady like you.")]}
    demetriaspeech2={"intro":[("Demetria","Thank Lenin you got here so quickly, comrade!  It's getting red in the streets, the people are out, yelling for revolution, for change."),("Burrows","Great, both revolution and communism washing down the streets.  Well as long as I can make a pretty penny..."),("Demetria","We shall see, we're running somewhat low on cash at the moment, and even though the revolution is successful, I can only manage to pay you 4000 credits for your next assignment. Specifically we have a Party leader flying in a stiletto on his way here.  We believe that he will be able to coordinate the revolution and allow us to gain control of the ground, so we can use the local space force to assist with attaining space superiority in this system.  I need you to make sure that his stiletto arrives here safely. He will dock to the planet, and we will redeploy the stiletto for further space combat. Can you help us?")],
        "reject1":[("Burrows","What sort of opposition are we looking at for only 4000 credits?"),("Demetria","There are a number of patrols of 2 "+aggressor+" starships flying around this system. There's no telling how many will find you before you make it here at 1400 kps."),("Burrows","I'll have to consider this one. Can you find someone else to help?"),("Demetria","No, you're our main hope here.")],
        "reconsider":[("Burrows","I'm your only hope, eh? I like the sound of that. So you're offering me 4000 credits to escort a fully armed stiletto?"),("Demetria","The man is a great revolutionary, but he is not a particularly excellent pilot. Please help watch his back.")],
        "reject2":[("Burrows","I think I've spilled enough blood to almost pee red. I'm not sure I'm going to help you cause even more damage for chump change. You may be cute, but not that cute."),("Demetria","We need your help. I know that our revolutionary cannot make it past the blockade without you...")],
        "failure":[("Burrows","Well I couldn't help bring him back. There were too many of them."),("Demetria","I'm afraid our cause is lost here.  Already the corporations have hired numerous bounty hunters to fill the streets and kill anyone wearing red. People are becoming desperate and many have decided to go into hiding.  I'll see you...around. Perhaps there will be new revolutions to fight.  Perhaps there will be new workers to assist. In fact...")],
        "accept":[("Burrows","I'm your man. I will bring in your hero, in exchange you'll give me 4000 and hopefully some more lucrative work upon my return. We have a revolution to begin, and I don't want to be late."),("Demetria","It is now that we can fight! It is now that we can finally end the millenia of oppression! You must prevail... we must...prevail!")],
        "reminder":[("Demetria","Have you protected our hero?"),("Burrows","I'm still fueling up, don't worry I'll meet him at the jump point"),("Demetria","It is imperative that you move quickly. I'm not sure how long the moment for this planet will last. We need to exploit it, or we will be forever exploited by the likes of the Confederation")],}
    return MakeCargoMission(priv,
        DEMETRIA_SPRITE,
        [InSystemCondition(path[0])]+prequisites,   
        [InSystemCondition(sys,base)],
        AddCredits(lastreward,ChangeSystemOwner(path[0],"AWACS")),
        LoadMission('ambush','ambush',(priv.name+"_mission",(path[-2],),0,aggressor,demetriaseed%7+1,'','',getDemetriaDialog(aggressor,0),path,base,False)),
        ('Weapons',30),
        priv.name+"_mission",
        demetriaspeech1,
        None,
        CampaignEndNode(priv),
        MakeMission(priv,
            DEMETRIA_SPRITE,
            [InSystemCondition(sys,base)],
            [InSystemCondition(sys,base)],
            AddCredits(8000),
            None,
            'escort_local',(aggressor,0,2,demetriaseed%3,1500,0,True,'AWACS',(),priv.name+"_mission",'','','','stiletto',getDemetriaDialog(aggressor,1)),
            priv.name+"_mission",
            demetriaspeech2,
            None,
            FailureMission,
            RandomRevolutionMission (priv,sys,base,aggressor,4000,demetriaseed*13+7,3,FailureMission,NextMission)))
def LoadBonusCampaign():
    
    priv=Campaign("freetrader_campaign")
    MilitiaOrPirate=CampaignNode()
    SyraiMission2NoDump=CampaignClickNode()
    SyraiMission2Dump=CampaignClickNode()
    SyraiMission3=CampaignClickNode()
    SyraiMission4=CampaignClickNode()
    SyraiMission5=CampaignClickNode()
    DestineeMission3 =CampaignClickNode()
    DestineeMission4 =CampaignClickNode()
    DestineeMission6 =CampaignClickNode()
    SorenMission1= CampaignClickNode()
    KaydenceMission1=CampaignClickNode()
    KaydenceMission7=CampaignClickNode()
    DemetriaMission1=CampaignClickNode()
    DemetriaMission5=CampaignClickNode()
    #FOR USE LATER AddPythonSprite("Corporate_Affiliate","blackclear.spr",(0.5875, 0),(.7,1),'Talk_To_Corporate_Affiliate',"#\nimport Base\nimport VS\nBase.Message('comment')\nVS.StopAllSounds()\nVS.playSound('barspeech/campaign/bartender_counteroffer.ogg',(0,0,0),(0,0,0))\n"+OptionalTalkingHead("bases/heads/refinery.spr"),AddPythonSprite("demetria",DEMETRIA_SPRITE_SMALL[0],DEMETRIA_SMALL_POSITION,(.18,.54),DEMETRIA_SPRITE_SMALL[1],"#\nimport Base\nimport VS\nBase.Message('comment')\nVS.StopAllSounds()\nVS.playSound('barspeech/campaign/demetria_counteroffer.ogg',(0,0,0),(0,0,0))\n"+OptionalTalkingHead(DEMETRIA_SPRITE_SMALL[2]))),
    #DEMETRIA_SMALL_POSITION=(0.034, -0.138125, 0.1758125, 0.5385)
    DEMETRIA_SMALL_POSITION=(-.88, -0.048125, 0.1758125, 0.5385)
    priv.Init(CampaignNode().Init(priv,[],None,None,GoToSubnode(0,IntroCutscene()),None,[MakeMission(priv,
            DESTINEE_SPRITE,
            [InSystemCondition("Gemini/Tingerhoff","Munchen")],
            [InSystemCondition("Gemini/Tingerhoff","Munchen")],
            None,
            None,
            'cleansweep',(0,8,1500,0,('Gemini/Nexus','Gemini/Capella','Gemini/Crab-12','Gemini/New_Caledonia','Gemini/17-ar'),priv.name+"_mission",1,3,.4,0,'pirates',True,False),
            priv.name+"_mission",
            destinee1speech,
            None,
            CampaignEndNode(priv),
            MakeCargoMission(priv,
                DESTINEE_SPRITE,
                [InSystemCondition("Gemini/Tingerhoff","Munchen")],
                [InSystemCondition("Gemini/New_Caledonia","Glasgow")],
                AddCredits(15000),
                LoadMission('ambush',
                    'ambush',
                    (priv.name+"_mission",
                        ("Gemini/Telar","Gemini/Crab-12","Gemini/Sherwood"),
                        0,
                        'pirates',
                        4,
                        '',
                        '',
                        [("We know you're trying to deliver those weapons to the militia in the neighborhood.",False,"campaign/destinee1.wav"),("Your weapons run stops here. We own this space, pal! You're nothing.",False),("Unless you give up your ship, you're toast!",False),("Not a chance, pal",True)],
                        ['Gemini/Nexus','Gemini/Capella','Gemini/Crab-12','Gemini/New_Caledonia'],
                        'Glasgow',
                        False)),
                ("Weapons",40),
                priv.name+"_mission",
                destinee2speech,
                None,
                CampaignEndNode(priv),
                CampaignClickNode().Init(priv,
                        [InSystemCondition("Gemini/Tingerhoff","Munchen")],
                        destinee3text,
                        DESTINEE_SPRITE,
                        GoToSubnode(0,AddCredits(10000)),
                        None,
                        [CampaignChoiceNode().Init(priv,
                                [InSystemCondition("Gemini/Tingerhoff","Munchen")],
                                destinee3text,
                                DESTINEE_SPRITE,
                                None,
                                [(
                                    (NO_SPRITE,"Refuse_Undercover_Mission"),
                                    CampaignNode().Init(priv,
                                        [InSystemCondition("Gemini/Tingerhoff","Munchen")],
                                        destinee3reject,
                                        DESTINEE_SPRITE,
                                        GoToSubnode(0),
                                        None,
                                        [SyraiMission2NoDump])),
                                    ((YES_SPRITE,"Accept_Undercover_Mission"),
                                        CampaignNode().Init(priv,
                                            [InSystemCondition("Gemini/Tingerhoff","Munchen")],
                                            destinee3accept,
                                            DESTINEE_SPRITE,
                                            GoToSubnode(0,AddCredits(12000)),
                                            None,
                                            [MakeMission(priv,
                                                SYRAI_SPRITE,
                                                [InSystemCondition("Gemini/Telar","Megiddo")],
                                                [],
                                                None,
                                                None,
                                                'bounty_leader',(0,0,0,1,0,'pirates',(),priv.name+"_mission",'','orion',0,'',('talon','hunter'),[("For your betrayal, I hereby demand your surrender.",True,"campaign/syrai1.wav"),("Not a chance pal. Who's ever heard of honor among thieves anyway!",False),("Stand down or be destroyed!",True),("Not a chance you'll catch me pal, I haven't sold my secrets to be flying the crate you are.",False)],["isometal","tungsten_hull",("plasma_gun",0),("plasma_gun",1),"medium_turret_rear_plasma","mult_speed_enhancer"]),
                                                priv.name+"_mission",
                                                syrai1speech,
                                                None,
                                                DestineeMission4,
                                                MilitiaOrPirate)]))])])))]))
    
    MilitiaOrPirate.Init(priv,
                [],
                None,
                None,
                TrueSubnode(),
                None,
                [DestineeMission3,CampaignClickNode().Init(priv,
                                    [InSystemCondition("Gemini/Telar","Megiddo")],
                                    [("Syrai","Hey there, did you nail our guy?"),("Burrows","You got it. He's been reduced to his component atoms"),("Syrai","Excellent. Unfortunately I have bad news for you. I don't have the cash on hand."),("Burrows","Give it to me or I'll kill you where you stand"),("Syrai","Temper temper! I didn't think you'd nail him this fast.  Take a little breather and I'll get the money to you. Pirates keep their word: pirate honor. I'll get you that money. Count on it. Oh and here's 200 creds for your docking fee and your trouble.")],
                                    SYRAI_SPRITE,
                                    GoToSubnode(0,AddCredits(200)),
                                    MilitiaOrPirate,
                                    [MilitiaOrPirate]
                                    )])
    DestineeMission3.Init(priv,
            [InSystemCondition("Gemini/Tingerhoff","Munchen")],
            destinee3speech["intro"],
            DESTINEE_SPRITE,
            GoToSubnode(0),
            MilitiaOrPirate,
            [CampaignChoiceNode().Init(priv,
                [InSystemCondition("Gemini/Tingerhoff","Munchen")],
                destinee3speech["intro"],
                DESTINEE_SPRITE,
                None,
                [((NO_SPRITE,"Refuse_To_Give_Information"),CampaignNode().Init(priv,
                    [],
                    destinee3speech["reject1"],
                    DESTINEE_SPRITE,
                    GoToSubnode(0),
                    None,[SyraiMission2NoDump])),
                ((YES_SPRITE,"Offer_Information_On_Telar_Pirates"),CampaignNode().Init(priv,
                    [],
                    destinee3speech["accept"],
                    DESTINEE_SPRITE,
                    GoToSubnode(0,AddCredits(12000)),
                    None,
                    [SyraiMission2Dump]))])])
    
    MakeCargoMission(priv,
            SYRAI_SPRITE,
            [InSystemCondition("Gemini/Telar","Megiddo")],
            [InSystemCondition("Gemini/Junction","Speke")],
            AddCredits(14000),
            LoadMission("ambush","ambush",(priv.name+"_mission",("Gemini/J900","Gemini/Junction","Gemini/Rikel","Gemini/17-ar"),0,'militia',4,'','',[("We knew you'd double cross us. We were fixing to catch you Ultimate runners lickity split.",False,"campaign/syrai2nodump.wav"),("Dump your cargo and we'll get the judge to give you a good plea bargain!",False)],['Gemini/J900', 'Gemini/Junction'], 'Speke')),
            ("Ultimate",40),
            priv.name+"_mission",
            syrai2speech,
            DestineeMission3,
            CampaignEndNode(priv),#losing is death here
            SyraiMission3,
            SyraiMission2NoDump)

    MakeNoFailureCargoMission(priv,
            SYRAI_SPRITE,
            [InSystemCondition("Gemini/Telar","Megiddo")],
            [InSystemCondition("Gemini/Junction")],#don't specify so you can meet on Victoria
            AddCredits(14000),
            LoadMission("ambush_scan","ambush_scan",(priv.name+"_mission",("Gemini/J900","Gemini/Junction","Gemini/Rikel","Gemini/17-ar"),10,'militia',8,'','',[("We knew you'd double cross us. We were fixing to catch you Ultimate runners lickity split.",False,"campaign/syrai2nodump.wav"),("Dump your cargo and we'll get the judge to give you a good plea bargain!",False)],['Gemini/J900', 'Gemini/Junction'], 'Speke',True,'Ultimate',[("Thank you for helping us track this down.",False,"campaign/syrai2dump.wav"),("With any luck we'll be able to use the imprints on this to get an authoration to shut down the pirates in Telar.",False),("Destinee will meet you personally on Victoria",False)])),
            ("Ultimate",40),
            priv.name+"_mission",
            syrai2speech,
            None,
            DestineeMission4,#losing means you dumped cargo
            SyraiMission3,
            SyraiMission2Dump)
    MakeCargoMission(priv,
            SYRAI_SPRITE,
            [InSystemCondition("Gemini/Junction","Speke")],
            [InSystemCondition("Gemini/Telar","Megiddo")],
            AddCredits(20000),
            LoadMission("ambush","ambush",(priv.name+"_mission",("Gemini/Telar",),0,'militia',4,'','',[("You are hereby under arrest for collaborating with and assisting Telar based pirates.",False,"campaign/syrai3.wav"),("Surrender or be destroyed. We know you are responsible for recent drug runs, and we intend to prosecute.",False)],['Gemini/J900', 'Gemini/Telar'], 'Megiddo',False)),
            ("Food",40),
            priv.name+"_mission",
            syrai3speech,
            None,
            CampaignEndNode(priv),
            SyraiMission4,
            SyraiMission3);
    MakeMission(priv,
        SYRAI_SPRITE,
        [InSystemCondition("Gemini/Telar","Megiddo")],
        [InSystemCondition("Gemini/Telar","Megiddo")],
        AddCredits(10000,AdjustRelation('militia','privateer',-1.2)),
        None,
        'bounty_troop',(0,0,0,0,6,'militia',(),priv.name+"_mission",'','troop_transport',0,'','gladius',[('By order of the Militia High Command, All pirate affiliated craft must stand down.',False,'cmapaign/syrai4a.wav'),'You are to surrender your base at once!','Any starship not powered down will be considered in volation of Confederate Law.',('This is Syrai, reporting from the Telar outpost; somehow the troop transport has made it past your net.',True),('All friendly craft withdraw from the edge of space and assist the mother base',True)],[],30),
        priv.name+"_mission",
        syrai4speech,
        None,
        CampaignClickNode().Init(priv,
                    [InSystemCondition("Gemini/Telar","Megiddo"),HasUndocked()],
                    destineegloat,
                    DESTINEE_SPRITE,
                    GoToSubnode(0,ChangeShipOwners("pirates","militia",ChangeSystemOwner("Gemini/Telar","confed"))),
                    None,[CampaignEndNode(priv)]),
        SyraiMission5,
        SyraiMission4);
    MakeCargoMission(priv,
            SYRAI_SPRITE,
            [InSystemCondition("Gemini/Telar","Megiddo")],
            [InSystemCondition("Gemini/Midgard","Heimdel")],
            None,
            LoadMission("ambush","ambush",(priv.name+"_mission",("Gemini/New_Detroit","Gemini/44-p-im","Gemini/Newcastle"),0,('AWACS','AWACS'),[1,2],('stiletto','stiletto'),'',[("We Know you have information about and perhaps leading to one Soren Malakai.",False,"campaign/syrai5.wav"),"We've put a contract out for him and his contributors.","Unless you surrender yourself and cargo to us, we will be forced to destroy you","Eject and be spared"],['Gemini/J900','Gemini/Junction','Gemini/New_Constantinople','Gemini/New_Detroit','Gemini/Perry','Gemini/Midgard'],'Anapolis',False)),
            ("Information_Pod",1),
            priv.name+"_mission",
            syrai5speech,
            None,
            CampaignEndNode(priv),
            SorenMission1,
            SyraiMission5)
    MakeMission(priv,
        DESTINEE_SPRITE,
        [InSystemCondition("Gemini/Junction","Victoria")],
        [InSystemCondition("Gemini/Tingerhoff","Munchen")],
        AddCredits(6000),
        None,
        'bounty_troop',(0,0,0,0,6,'pirates',("Gemini/Junction","Gemini/J900","Gemini/Telar"),priv.name+"_mission",'','drayman',0,'','talon',[("You won't find that transport here!",False,"campaign/destinee3.wav"),"She's nearly safe in our docking port.","And to get there you have to go through us."],[],30),
        priv.name+"_mission",
        destinee4speech,
        None,
        CampaignEndNode(priv),
        MakeMission(priv,
            DESTINEE_SPRITE,
            [InSystemCondition("Gemini/Tingerhoff","Munchen")],
            [],
            AddCredits(11000),
            None,
            'escort_local',('pirates',0,4,2,3000,0,True,'militia',('Gemini/Nexus','Gemini/Junction','Gemini/J900','Gemini/Telar'),priv.name+"_mission",'','talon.blank','','paradigm',[('By order of the Militia High Command, All pirate affiliated craft must stand down.',True,'cmapaign/syrai4.wav'),'You are to surrender your base at once!','Any starship not powered down will be considered in volation of Confederate Law.',("This is Syrai: I can't believe you double crossed me.  Pirates across the galaxy will hear of this!",False),]),
            priv.name+"_mission",
            destinee5speech,
            None,
            CampaignEndNode(priv),
            CampaignClickNode().Init(priv,
                    [InSystemCondition("Gemini/Telar","Megiddo")],
                    destineefinal,
                    DESTINEE_SPRITE,
                    GoToSubnode(0,ChangeShipOwners("pirates","militia",ChangeSystemOwner("Gemini/Telar","confed",AddCredits(20000)))),
                    None,[KaydenceMission1])),
        DestineeMission4)

    MakeMission(priv,
        KAYDENCE_SPRITE,
        [InSystemCondition("Gemini/Perry","Anapolis")],
        [InSystemCondition("Gemini/Perry","Anapolis")],
        None,
        None,
        'rescue',(0,0,'confed',2,'kilrathi','',("Gemini/Ragnarok","Gemini/Blockade_Point_Alpha"),priv.name+"_mission"),
        priv.name+"_mission",
        kaydence1speech,
        None,
        CampaignEndNode(priv),
        MakeMission(priv,
            KAYDENCE_SPRITE,
            [InSystemCondition("Gemini/Perry","Anapolis")],
            [InSystemCondition("Gemini/Perry","Anapolis")],
            AddCredits(11500),
            None,
            "cleansweep",(0,8,1500,0,("Gemini/Ragnarok","Gemini/Blockade_Point_Alpha"),priv.name+"_mission",2,4,.5,0,"kilrathi",False,True),
            priv.name+"_mission",
            kaydence2speech,
            None,
            CampaignEndNode(priv),
            MakeNoFailureMission(priv,  
                KAYDENCE_SPRITE_NOHEAD,
                [InSystemCondition("Gemini/Perry","Anapolis")],
                [],
                AddCredits(13000),
                EnqueueMoreText(kaydence3speech["accept"],Cutscene('Automated Robotic Message','PoliticianCutscene.spr',(0.582,-0.3),(3.104,1.2416),'Message from insurgency: Kill Senator To Collect 40,000 at Elysia base in Auriga',[("","A Few Hours Later...           ","campaign/politician.wav"),("Robot","This is an automated message..."),("Robot","Members of my organization are displeased with the latest turn of politics."),("Robot","Later today there will be a vote on a new bill called the WAR-TIME-SUPPORT act."),("Robot","If this bill passes, it will give police forces a mandate to arrest protestors or strikers as saboteurs and punish them as such."),("Robot","It requires war-time support for merely a few interstellar coporation by the Gemini sector."),("Robot","You are our only hope for stopping the bill. With a current 50-50 tie in the senate, our Governor, a man from the Landreich with a hunger for power will be the man to select whether this bill passes."),("Robot","Hence we offer a reward for the 'removal' of one of the senators, specificially 40,000 credits for the failure to deliver your senator to New Constantinople"),("Robot","If this law passes we lose our right to organize in the face of increasingly greedy and ruthless corporations that dominate the frontier. The choice is yours..."),("Robot","Your reward will be available in the bar at the Elysia base in Auriga."),("Robot","I will purge my memory and initiate self destruct...now")],'awacs.m3u','refinery.m3u')),
                "escort_mission",("confed",0,0,0,1500,0,0,0,("Gemini/New_Detroit","Gemini/New_Constantinople"),priv.name+"_mission",'','stiletto'),
                priv.name+"_mission",
                kaydence3speech,
                None,
                DemetriaMission1,
                MakeMission(priv,
                    KAYDENCE_SPRITE,
                    [InSystemCondition("Gemini/Perry","Anapolis")],
                    [],
                    AddCredits(18000),
                    None,
                    "defend",('AWACS',0,4,5000,123456.789,0,False,True,'confed',('Gemini/Ragnarok','Gemini/Blockade_Point_Alpha'),priv.name+"_mission",'','stiletto','',4,[("You confed shills don't understand what's happening.",False,"campaign/kaydence4.wav"),"The WAR-TIME-SUPPORT act allows people to be arrested and held for organizing against greedy coporations, even if they have done so in the recent past.","Our very brothers and daughters are being taken from their homes at this very minute","We must unite...","We must come together to stop the government from taking what few liberties are left.","And you will not stand in our way!"]),
                    priv.name+"_mission",
                    kaydence4speech,
                    None,
                    CampaignEndNode(priv),
                    MakeMission(priv,
        KAYDENCE_SPRITE,
        [InSystemCondition("Gemini/Perry","Anapolis")],#[InSystemCondition("Gemini/Ragnarok","Mjolnar")],
        [InSystemCondition("Gemini/Perry","Anapolis")],
        AddCredits(15000),
        None,
        "defend",('AWACS',0,5,5000,123456.789,0,False,True,'confed',('Gemini/Newcastle','Gemini/Auriga',),priv.name+"_mission",'','stiletto','',1,[("We are the new front for revolution. If it does not happen now, then the tyrrany of Corporations will continue to suffocate the very people who keep them alive",False,"campaign/kaydence5.ogg"),"You cannot stop our assault on the corporate fascists of this sector!"]),
        priv.name+"_mission",
        kaydence5speech,
        None,
        CampaignEndNode(priv),
        MakeNoFailureMission(priv,
            KAYDENCE_SPRITE,
            [InSystemCondition("Gemini/Perry","Anapolis")],
            [InSystemCondition("Gemini/Perry","Anapolis")],
            AddCredits(16000),
            AddPythonSprite("Corporate_Affiliate","blackclear.spr",(0.5875, 0),(.7,1),'Talk_To_Corporate_Affiliate',"#\nimport Base\nimport VS\nBase.Message('Now I know that confed officer over there made you a pleasing deal to bring that transport in so the people can have their trial. But I know someone in Midgard who would pay double the price she offers to see that ship destroyed--no questions asked.  Remember if the prisoners fail to make it, you get 32 Gs by stopping at Midgard. Its your choice.')\nVS.StopAllSounds()\nVS.playSound('barspeech/campaign/bartender_counteroffer.ogg',(0,0,0),(0,0,0))\n"+OptionalTalkingHead("bases/heads/refinery.spr"),AddPythonSprite("demetria",DEMETRIA_SPRITE_SMALL[0],DEMETRIA_SMALL_POSITION,(.18,.54),DEMETRIA_SPRITE_SMALL[1],"#\nimport Base\nimport VS\nBase.Message('Kind sir, I know you have the skills and whereabouts to return our leaders to us. Allow me to inroduce myself. I am Demetria, one of the last leaders of AWACS, Workers against corporate slavery.  We need to stop these arrests, and to do so we need to organize. Our very leaders are on that transport you are supposed to escort. If you can make sure that transport makes it into the Newcastle system I can provide some help to get it all the way to Auriga where we can meet and discuss further ventures that you might find profitable! Remember just deviate from New Detroit and go to Newcastle instead.')\nVS.StopAllSounds()\nVS.playSound('barspeech/campaign/demetria_counteroffer.ogg',(0,0,0),(0,0,0))\n"+OptionalTalkingHead(DEMETRIA_SPRITE_SMALL[2]))),
            "wrong_escort",('confed',4,1000,100,0,("Gemini/New_Detroit","Gemini/New_Constantinople"),priv.name+"_mission",'','drayman',('Gemini/Newcastle',),('AWACS',),('',),('stiletto',),([('Thank you for delivering our people back to us. Now we can plan this revolution!',True,"campaign/kaydence6.ogg"),('We are grateful for your cooperation',True),('Meet us at the bar on the agricultural world in Auriga.',True)],),'awacs_escort'),
            priv.name+"_mission",
            kaydence6speech,
            None,
            CampaignNode().Init(priv,[],None,None,TrueSubnode(),None,[CampaignNode().Init(priv,[SaveVariableCondition('awacs_escort',0)],None,None,GoToSubnode(0,AddCredits(-20000)),None,[DemetriaMission1]),CampaignNode().Init(priv,[SaveVariableCondition('awacs_escort',-1)],None,None,GoToSubnode(0,AddCredits(35000)),None,[SorenMission1])]),
            KaydenceMission7)
        )))),KaydenceMission1)


    MakeMission(priv,
        KAYDENCE_SPRITE,
        [InSystemCondition("Gemini/Perry","Anapolis")],
        [InSystemCondition("Gemini/Perry","Anapolis")],
        AddCredits(18000),
        None,
        "escort_local",('hunter',0,2,2,3000,0,False,'confed',(),priv.name+"_mission",'','demon.blank','','drayman',[("We've been paid to decimate that drayman and nothing is getting in our way",False,"campaign/kaydence7.ogg"),("Stand down by the order of Confed High Command!",True),"Stand down and we may spare you, escorts. You are at our mercy, now"]),
        priv.name+"_mission",
        kaydence7speech,
        None,
        CampaignEndNode(priv),
        MakeMission(priv,
            KAYDENCE_SPRITE,
            [InSystemCondition("Gemini/Perry","Anapolis")],
            [InSystemCondition("Gemini/Perry","Anapolis")],
            AddCredits(10000),
            None,
            "cleansweep",(0,10,1500,0,("Gemini/Ragnarok",),priv.name+"_mission",1,4,.6,.5,['AWACS','kilrathi'],1,1),
            priv.name+"_mission",
            kaydence8speech,
            None,
            CampaignEndNode(priv),
            MakeMission(priv,
                KAYDENCE_SPRITE,
                [InSystemCondition("Gemini/Perry","Anapolis")],
                [InSystemCondition("Gemini/Perry","Anapolis")],
                AddCredits(13000),
                None,
                "bounty_leader",(0,0,0,0,8,'unknown',('Gemini/Ragnarok','Gemini/Blockade_Point_Alpha','Gemini/Tr_Pakh'),priv.name+"_mission",'','drayman',0,'',('gothri','kilrathi'),[("Human, dare not trespass this deep into Kilrathi space.  You will find things here you just do not want to see",False,"campaign/kaydence8.ogg"),("Rawwwrr retreat or be destroyed! Stay away from the asteroid field!"),("Do not attack the human vessel. It is under our protection. You are violating the law of Sivar!")],[("fusion_gun",0),("fusion_gun",1,1)]),
                priv.name+"_mission",
                kaydence9speech,
                None,
                CampaignEndNode(priv),
                CampaignClickNode().Init(priv,
                        [InSystemCondition("Gemini/Perry","Anapolis")],
                        kaydencefinal,
                        KAYDENCE_SPRITE,
                        GoToSubnode(0,AddCredits(20000)),
                        None,
                        [DestineeMission6]))),
                        
        KaydenceMission7)
    MakeMission(priv,
        DESTINEE_SPRITE,
        [InSystemCondition("Gemini/Tingerhoff","Munchen")],
        [InSystemCondition("Gemini/Tingerhoff","Munchen")],
        None,
        None,
        "cleansweep",(0,8,1500,0,("Gemini/Nexus","Gemini/KM-252"),priv.name+"_mission",3,6,.8,0,'pirates',1,0),
        priv.name+"_mission",
        destinee6speech,
        None,
        CampaignEndNode(priv),
        MakeMission(priv,
            DESTINEE_SPRITE,
            [InSystemCondition("Gemini/Tingerhoff","Munchen")],
            [InSystemCondition("Gemini/Tingerhoff","Munchen")],
            AddCredits(15000),
            None,
            'escort_local',('pirates',0,6,2,3000,0,True,'militia',('Gemini/Nexus','Gemini/KM-252'),priv.name+"_mission",'','talon.blank','','paradigm',[('By order of the Militia High Command, All pirate affiliated craft must stand down.',True,'cmapaign/destinee6.ogg'),'You are to surrender your base at once!','Any starship not powered down will be considered in volation of Confederate Law.',]),
            priv.name+"_mission",
            destinee7speech,
            None,
            CampaignEndNode(priv),
            CampaignClickNode().Init(priv,
                [InSystemCondition("Gemini/Tingerhoff","Munchen")],
                destineefinal2,
                DESTINEE_SPRITE,
                GoToSubnode(0,ChangeSystemOwner("Gemini/KM-252","confed",AddCredits(20000))),
                None,
                [CampaignEndNode(priv)])),
        DestineeMission6)
    MakeMission(priv,
        SOREN_SPRITE,
        [InSystemCondition("Gemini/Midgard","Heimdel")],
        [InSystemCondition("Gemini/Midgard","Heimdel")],
        None,
        None,
        'bounty_leader',(0,0,0,1,3,'confed',('Gemini/Perry','Gemini/Ragnarok'),priv.name+"_mission",'','drayman',0,'',('stiletto','confed'),[("This is a civilian prisoner transport. We have women and children on-board. Discharge your weapons immediately!",False,"campaign/soren1.ogg"),("Your death is my gain, buddy",True),("Desist on order of the Gemini Confed High Command and the Gemini Senate",False),("Not a chance, pal. Prepare to go to hell.",True),("Mayday mayday we are under attack by a civilian ident 0xb4df00d. All Confederate craft please assist!",False)],["isometal_hull",("plasma_gun",0),("plasma_gun",1)]),
        priv.name+"_mission",
        soren1speech,
        None,
        CampaignEndNode(priv),
        SorenCargoMission(priv,("Gemini/Rikel","Gemini/New_Detroit","Gemini/XXN-1927","Gemini/Oxford"),"Oxford","Plastics","AWACS",25000,SorenCargoMission(priv,("Gemini/Rikel","Gemini/44-p-im","Gemini/New_Constantinople"),"New_Constantinople","Ultimate","confed",9000,SorenCargoMission(priv,("Gemini/Perry","Gemini/Tingerhoff","Gemini/Nexus","Gemini/KM-252"),"Smallville","Weapons","militia",16000,SorenCargoMission(priv,("Gemini/Perry","Gemini/Nitir","Gemini/Blockade_Point_Tango","Gemini/Lisacc"),"Lisacc","Weapons","pirates",16000,SorenCargoMission(priv,("Gemini/Rikel","Gemini/New_Detroit","Gemini/Perry","Gemini/Ragnarok","Gemini/Blockade_Point_Alpha","Gemini/Tr_Pakh"),"Large_Asteroid","Catnip","confed",12400,
        CampaignNode().Init(priv,[],None,None,GoToSubnode(0,AddTechnology("kilrathi")),None,[CampaignClickNode().Init(priv,[InSystemCondition("Gemini/Midgard","Heimdel")],[("Soren","I think our Kilrathi allies were pleased at the small run.  Your success has meant a lot to the success of my corporation, and we will not forget your efforts.  Clearly our business interests have coincided until now, so while I will pay you now, this will be our last encounter for a while.  Hopefully our corporation will continue to assist its customers, within and outside of Gemini.  A wise man said that not only peace is good for business, but war is also good for business. And it is by this philosophy that I have worked with you to make so many credits together.  Good bye."),("Burrows","I never suspected you were such dirty operators. I can only guess as to the source of this grime you've had me do.  But as always money talks, and that 60,000 credits is sure to smooth my furrowed brow.  Remember I'll always do business with you for the right price."),("Soren","Something we...count on out here.  You can only trust a man--or being with a large enough pocketbook. We share more philosophy than you might care to know, Privateer. And it is with this thought that I leave you be.")],SOREN_SPRITE,GoToSubnode(0,AddCredits(60000)),None,[CampaignEndNode(priv)])]),soren2speech))))),
        SorenMission1)

    MakeMission(priv,
        DEMETRIA_SPRITE,
        [InSystemCondition("Gemini/Shangri_La","Erewhon")],
        [InSystemCondition("Gemini/Shangri_La","Erewhon")],
        AddCredits(10000),
        None,
        'bounty_leader',(0,0,0,1,6,'hunter',('Gemini/Newcastle','Gemini/Perry','Gemini/Ragnarok','Gemini/Blockade_Point_Alpha','Gemini/Tr_Pakh'),priv.name+"_mission",'','galaxy',0,'','gothri',[("Ha! Commander. Thought you could outwit me after all these years.",False,"campaign/demetria5.ogg"),"Didn't think I'd deal with the Cats, eh? Well I did. and Look where it got me. I've got a large escort right now, and plenty of cash in the bank that I've been using to crush your little revolutionaries.","Confed may be on the verge of turning a leaf with respect to the AWACS group, but I can sow a little more trouble for your people.","You see I'm all about money, and my virtual monopoly with confed would just have bolstered that.","Now it looks like what's left of the Gemini state senate may undo the WAR-TIME-SUPPORT","So that's why I've been talking to my feline brothers here. Now if you'll excuse me, I've got a jump to make."],[("isometal",0),("tungsten_hull",0),("fusion_gun",0),("fusion_gun",1),("medium_turret_plasma",0,0),("medium_turret_plasma",1,1),("ecm_package_3",0),("reactor_level_5_galaxy",0)]),
        priv.name+"_mission",
        demetria5speech,
        None,
        CampaignEndNode(priv),
        CampaignClickNode().Init(priv,
            [InSystemCondition("Gemini/Shangri_La","Erewhon")],
            demetriafinal,
            DEMETRIA_SPRITE,
            GoToSubnode(0,AddCredits(9000)),
            None,
            [CampaignEndNode(priv)]),
        DemetriaMission5)
    MakeMission(priv,
        DEMETRIA_SPRITE,
        [InSystemCondition("Gemini/Auriga","Elysia")],
        [InSystemCondition("Gemini/Auriga","Elysia")],
        AddCredits(40000),#20,000 case takes away 20000 credits first
        ChangeSystemOwner("Gemini/Auriga","AWACS"),
        'escort_local',('hunter',0,1,6,3000,0,True,'AWACS',(),priv.name+"_mission",'','demon.blank','','drayman',[("Prisoner transport. You are hereby under arrest. If you do not comply you will be destroyed!",False,"campaign/demetria1.ogg"),("Stand down. This is the AWACS personell transport. We owe nothing to Confed and will not surrender to you goons. You don't work for the Star Confederacy in the same way I don't.",True),("You've been paid off  by those corporate fascists!",True)]),
        priv.name+"_mission",
        demetria1speech,
        None,
        CampaignEndNode(priv),
        DemetriaRevolutionMission(priv,
                31339,
                ["Gemini/Auriga","Gemini/Newcastle","Gemini/New_Constantinople","Gemini/New_Detroit","Gemini/ND-57"],
                "New_Reno",
                "hunter",
                10000,
                DemetriaLoseRevolution(priv,["Gemini/ND-57","Gemini/New_Detroit","Gemini/New_Constantinople","Gemini/Newcastle","Gemini/Aldebran","Gemini/Hinds_Variable_N","Gemini/DN-N1912"],),
                DemetriaRevolutionMissionPreq(priv,
                            73313,
                            ["Gemini/ND-57","Gemini/New_Detroit"],
                            "New_Detroit",
                            "confed",
                            10000,
                            DemetriaLoseRevolution(priv,["Gemini/New_Detroit","Gemini/New_Constantinople","Gemini/Newcastle","Gemini/Aldebran","Gemini/Hinds_Variable_N","Gemini/DN-N1912"]),
                            DemetriaRevolutionMission(priv,
                                13243,
                                ["Gemini/New_Detroit","Gemini/Saxtogue"],
                                "Olympus",
                                "militia",
                                15000,
                                CampaignEndNode(priv),
                                DemetriaRevolutionMission(priv,
                                    16382,
                                    ["Gemini/Saxtogue","Gemini/Oxford","Gemini/Shangri_La"],
                                    "Erewhon",
                                    "hunter",
                                    10000,
                                    CampaignEndNode(priv),
                                    DemetriaMission5)),
                            [("Demetria","Your work thus far has been fantastic, comrade. By Lenin, the entire Potter quadrant is falling into the hands of the people.  The power of the government is beginning to ebb.  Now we need to strike a blow into the heart, mind, and machine of Confed: we need to take down New Detroit.  The people there are overworked, tired, and angry at the lunacy of the confederation, and it is up to us to plant the seed of revolution! Are you with us?")],
                            [("Demetria","Excellent! You have succeeded! Our resources are currently depleated, but since we have a number of systems in the hands of the Party, I'm certain that we will be able to plant the seed of revolution amongs new, unhappy workers on new planets. Come back in the future, and there will be red, the communism, the revolution, and the people!")],[SaveVariableCondition("menesch_dead",1)])),
                                
                        
        DemetriaMission1)

    return priv
