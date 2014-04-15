from __future__ import division

""" Ship upgrade test campaign.

    By default, the fixer is in Gemini/Troy on the Achilles mining base.

    Talking to the fixer will launch a defend mission with a single
    waypoint (Hector by default), at which a single Confed AI controlled
    ship (the type of which is configured below) will initiate an attack.

    * The first mission will have an opponent classified as 'Rabble'.
    * The second mission will have an opponent classified as 'Average'.
    * The third mission will have an opponent classified as 'Experienced'.
    * The fourth and final mission will have an opponent classified 'Hardcore'.

    The fixer can be reset at any time by twice rejecting the mission she
    offers.

    Upon beating all the missions, the fixer will reset as well.
"""

import VS
#import campaign_lib
import debug
import quest
from campaign_lib import *

# Difficulty tiers
# ================
#
# Rabble := [0; 2/9[
# Average := [2/9; 6/9[
# Experienced := [6/9; 8/9[
# Hardcore := [8/9; 9/9]

difficulty_ = 0  # will be incremented at some point. Range is [0/9; 9/9]

system_ = "Gemini/Troy"
base_ = "Achilles"
waypoint_ = "Helen"
opponent_ =  "talon"  # corresponds to the 'Average' ship

rabble_speech = {
            "intro":[("ES Associate", "Ready to test the upgrade routine on some rabble?")],
            "reject1":[("Burrows", "Not right now."),
                ("ES Associate", "OK.  Come see me again if you change your mind.")],
            "reconsider":[("Burrows", "What was the mission again?"),
                ("ES Associate", "Ready to test the upgrade routine on some rabble?")],
            "reject2":[("Burrows", "This is not working out for me.  Sorry"),
                ("ES Associate", "OK.  Let's start over, then.")],
            "accept":[("Burrows", "Let's do it."),
                ("ES Associate", "I've uploaded the mission details to your nav computer.  Good luck.")],
            "accept2":[("Burrows", "I've reconsidered.  Let's do it."),
                ("ES Associate", "Sure thing.  I've uploaded the details to your nav computer.  Good luck.")],
            "reminder":[("ES Associate", "The mission details have already been uploaded to your nav computer.  Good luck.")],
            "failure":[("ES Associate", "You failed to mop up the rabble?  Let's start over.")]
            }
average_speech = {
            "intro":[("ES Associate", "Ready to test the upgrade routine on an average opponent?")],
            "reject1":[("Burrows", "Not right now."),
                ("ES Associate", "OK.  Come see me again if you change your mind.")],
            "reconsider":[("Burrows", "What was the mission again?"),
                ("ES Associate", "Ready to test the upgrade routine on an average opponent?")],
            "reject2":[("Burrows", "This is not working out for me.  Sorry"),
                ("ES Associate", "OK.  Let's start over, then.")],
            "accept":[("Burrows", "Let's do it."),
                ("ES Associate", "I've uploaded the mission details to your nav computer.  Good luck.")],
            "accept2":[("Burrows", "I've reconsidered.  Let's do it."),
                ("ES Associate", "Sure thing.  I've uploaded the details to your nav computer.  Good luck.")],
            "reminder":[("ES Associate", "The mission details have already been uploaded to your nav computer.  Good luck.")],
            "failure":[("ES Associate", "You failed to beat an average opponent?  Let's start over.")]
            }
experienced_speech = {
            "intro":[("ES Associate", "Ready to test the upgrade routine on an experienced opponent?")],
            "reject1":[("Burrows", "Not right now."),
                ("ES Associate", "OK.  Come see me again if you change your mind.")],
            "reconsider":[("Burrows", "What was the mission again?"),
                ("ES Associate", "Ready to test the upgrade routine on an experienced opponent?")],
            "reject2":[("Burrows", "This is not working out for me.  Sorry"),
                ("ES Associate", "OK.  Let's start over, then.")],
            "accept":[("Burrows", "Let's do it."),
                ("ES Associate", "I've uploaded the mission details to your nav computer.  Good luck.")],
            "accept2":[("Burrows", "I've reconsidered.  Let's do it."),
                ("ES Associate", "Sure thing.  I've uploaded the details to your nav computer.  Good luck.")],
            "reminder":[("ES Associate", "The mission details have already been uploaded to your nav computer.  Good luck.")],
            "failure":[("ES Associate", "You failed to beat an experienced opponent?  Let's start over.")]
            }
hardcore_speech = {
            "intro":[("ES Associate", "Ready to test the upgrade routine on a hardcore opponent?")],
            "reject1":[("Burrows", "Not right now."),
                ("ES Associate", "OK.  Come see me again if you change your mind.")],
            "reconsider":[("Burrows", "What was the mission again?"),
                ("ES Associate", "Ready to test the upgrade routine on a hardcore opponent?")],
            "reject2":[("Burrows", "This is not working out for me.  Sorry"),
                ("ES Associate", "OK.  Let's start over, then.")],
            "accept":[("Burrows", "Let's do it."),
                ("ES Associate", "I've uploaded the mission details to your nav computer.  Good luck.")],
            "accept2":[("Burrows", "I've reconsidered.  Let's do it."),
                ("ES Associate", "Sure thing.  I've uploaded the details to your nav computer.  Good luck.")],
            "reminder":[("ES Associate", "The mission details have already been uploaded to your nav computer.  Good luck.")],
            "failure":[("ES Associate", "You failed to beat a hardcore opponent?  Let's start over.")]
            }

def load_ship_upgrade_test_campaign():
    debug.debug("Entering load_ship_upgrade_testpriv() ...")
    global system_
    global base_
    global waypoint_
    global opponent_

    ES_ASSOCIATE_SPRITE = ("goodin.spr", "Talk to ES Associate", "bases/heads/goodin.spr")
    rabble_mission = CampaignClickNode()
    average_mission = CampaignClickNode()
    experienced_mission = CampaignClickNode()
    hardcore_mission = CampaignClickNode()

    priv = Campaign("ship_upgrade_test_campaign")
    priv.Init(rabble_mission)

    mission_desc = "rabble_mission:_test_ship_upgrade_routine_on_rabble"
    debug.debug("Calling MakeMission()")
    MakeMission(priv,  # campaign
        ES_ASSOCIATE_SPRITE,  # sprite (fixer)
        [InSystemCondition(system_, base_)],  # conditiontobegin -- where the mission starts
        [InSystemCondition(system_, base_)],  # conditiontoend -- where the mission ends
        AddCredits(1000000),  # scriptonclick -- add credits; this is a cheat mission
        None,  # Script to be run to start the mission
        'defend',  # missionname
        (
            'confed_',  # factionname -- the enemy faction we're fighting
            0,  # numsystemsaway -- 0 means the enemy is in this system
            1,  # enemyquantity -- There's one enemy in this case
            5000,  # distancefrombase -- the enemy is spawned as the player gets within this distance
            123456.789,  # escape_distance -- not quite sure who can escape...
            0,  # creds -- presumably the reward for destroying the enemy
            False,  # defendthis -- presumably we're defending an asset
            True,  # defend_base -- presumably we're defending a base
            'merchant',  # protectivefactionname -- presumably the faction we're protecting
            (),  # jumps -- since it is in-system, this is empty (?)
            priv.name+"_mission",  # var_to_set -- probably to keep track of this mission in save games
            'Confed_AI_drone',  # dynamic_attack_fg -- name of the attacking flight group
            opponent_,  # dynamic_type -- the type of opponent
            waypoint_,  # dynamic_defend_fg -- name of the defending flight group
            0,  # waves -- how many extra waves of opponents will be spawned
            ["Mission parameters match.", "Target acquired.", "Initiating attack sequence."],  # greetingText
        ), # missionargs -- Mission arguments.
        priv.name+"_mission",  # Script to be set on completion. -1=Failure, 0=Not Accepted, 1=Succeed, 2=In progress
        rabble_speech,  # Dictionary containing what the fixer says.
        rabble_mission,  # rejectnode -- if you reject the mission twice. "None" means asking forever until you accept
        rabble_mission,  # failurenode -- if you lose the mission
        rabble_mission,  # succeednode -- if you win the mission. Usually points to the next mission
        rabble_mission,  # node -- the current mission node.
        mission_desc,  # missiondesc -- the description of the mission
    )
    debug.debug("MakeMission() call done.")
    return priv
