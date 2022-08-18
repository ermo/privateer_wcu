"""
    It is important to build in some intelligence in the ship upgrade
    process.  Otherwise, ships will become overpowered very quickly.

    The goal is to maintain a relatively 'fast and fun' type of gameplay.

    This outlines the class of upgrades which will be available to
    various ships.

    rabble = no ECM, no extra armor, no extra shields, weaker weapons, (Troy at the beginning)
    normal = no ECM, no extra armor, no extra shields, normal weapons
    experienced = ECM Level 1, plasteel armor, no extra shields, normal weapons, possibility of lowest repair bot
    hardcore = ECM Level 2, tungsten armor, no extra shields, normal weapons, possibility of up to 2nd lowest repair bot

    So essentially, survivability (and therefore damage dealt over time)
    of the opponents goes up as difficulty level increases.

    Ships ordered after reactor level for the non-blank version in question:

    light_1 = ["tarsus", "fireblade"]
    light_2 = ["dralthi", "salthi", "demon", "gladius", "talon", "tarsusMk2", "sparrowhawk", "hornet", "hornetCVL", "sartha", "ferret", "ferretCVL"]
    medium_3 = ["galaxy", "kukhri", "krant", "scimitar", ]
    medium_4 = ["gothri", "centurion", "galaxyhk", "raptor", "sabre" ]
    heavy_5 = ["broadsword", "orion", "orionMk2", "orionMk2b", "orionMk2H", "grikath"]
    heavy_6 = ["galaxygs", ]
    capship = ["kamekh", "paradigm", "freetrader"]

    The current interface for the unit upgrade function is something like this:
    unit.upgrade(upgrade_filename : string, mountoffset : int, subunitoffset : int, force : bool, loop_through_mounts : bool)

    
"""
import VS
import debug
import vsrandom


def GetDiffInt(diff):
    """Convert difficulty (float) to an integer value"""
    ch = 0
    if (diff <= 0.1):
        ch = 0
    elif (diff <= 0.3):
        ch = 1 - vsrandom.randrange(0, 2)
    elif (diff <= 0.5):
        ch = 2 - vsrandom.randrange(0, 3)
    elif (diff <= 0.7):
        ch = 3 - vsrandom.randrange(0, 4)
    elif (diff <= 0.9):
        ch = 4 - vsrandom.randrange(0, 5)
    else:
        ch = 5 - vsrandom.randrange(0, 6)
    return ch


def GetDiffCargo(diff, base_category, all_category, use_all, dont_use_all=0):
    """ This function makes a string based on the difficulty.

        In this way it can be restricted to light or medium mounts
        when the difficulty is low, avoiding unaffordable weapons

    """
    cat = all_category
    ch = dont_use_all
    #this makes ch only 1
    if (diff <= 0.2):
        ch = 1
    elif (diff <= 0.4):
        ch = 2 - vsrandom.randrange(dont_use_all, 3)
    elif ((diff <= 0.7) or use_all):
        ch = 3 - vsrandom.randrange(dont_use_all, 4)
    # ch is 0 if it is any upgrades/Weapon
    # otherwise it could be light, medium or heavy or some random set
    # between Light and X (light, medium, heavy)
    if (ch == 1):
        cat = "%sLight" % (base_category)
    elif (ch == 2):
        cat = "%sMedium" % (base_category)
    elif (ch == 3):
        cat = "%sHeavy" % (base_category)
    debug.debug("Category: %s" % (cat))
    return cat


def getItem(cat, parentcat=None):
    """Get a random cargo item listed on the master part list"""
    cargo_item = VS.getRandCargo(1, cat)  # try to get a cargo from said category
    if (cargo_item.GetQuantity() <= 0):  # if no such cargo exists in this cateogry
        if (parentcat is not None):
            debug.debug("UpgradeError: Can't find %s"
                        " -- using %s instead" % (cat, parentcat))
            # get it from the parent category
            cargo_item = VS.getRandCargo(1, parentcat)
        if (cargo_item.GetQuantity() <= 0):  # otherwise get cargo from upgrades category
            debug.debug("UpgradeError: terrible error lasers instead")
            # this always succeeds
            cargo_item = VS.getRandCargo(1, "upgrades")
    debug.debug("getItem: %s" % (cargo_item.GetContent()))
    return cargo_item


def GetRandomWeapon(diff):
    """Get a random beam or mounted gun from master part list"""
    rndnum = vsrandom.random()
    cat = "upgrades"
    if (rndnum < 0.5):
        cat = GetDiffCargo(diff, "upgrades/Weapons/Beam_Arrays_", "upgrades/Weapons", 1)
    else:
        cat = GetDiffCargo(diff, "upgrades/Weapons/Mounted_Guns_", "upgrades/Weapons", 1)
    debug.debug("Getting item: %s" % (str(cat)))
    item = getItem(cat, "upgrades/Weapons")
    return item


def getRandIncDec(type):
    """Return a clamped random increase of 'type'"""
    type_ = type
    type += vsrandom.randrange(-1, 2, 2)
    if (type < 0):
        type = 0
    elif (type > 5):
        type = 5
    debug.debug("%.3f upgraded to %.3f" % (type_, type))
    return type


def GetShieldLevelZero(faces):
    return "shield_%d" % (faces)


def GetRandomShield(faces, type):
    """Get a random shield system from master part list"""
    type = getRandIncDec(type)
    if type == 0:
        return GetShieldLevelZero(faces)
    cat = "shield_%d_Level%d" % (faces, type)
    debug.debug("Got Shield: %s" % (cat))
    return cat


def GetRandomAfterburner(diff):
    """Get a random afterburner from master part list"""
    cat = GetDiffCargo(diff, "upgrades/Engines/Engine_Enhancements_", "upgrades/Engines", 0, 1)
    item = getItem(cat, "upgrades/Engines")
    return item


def getRandomRadar():
    """Get a random radar from master part list"""
    myint = vsrandom.randrange(0, 3)
    item = "SkyScope_Beta"
    if (myint <= 0):
        item = "StarScanner_2545"
    elif (myint == 1):
        item = "Hawkeye_ZX-86"
    debug.debug("Got Radar: %s" % (item))
    return item


def UpgradeRadar(un):
    """Upgrades radar (based on difficulty)"""
    cat = getRandomRadar()
    temp = un.upgrade(cat, 0, 0, 1, 0)
    debug.debug("Upgrading Radar %s percent %.3f" % (cat, temp))


def UpgradeAfterburner(un, diff):
    """Upgrades afterburner based on difficulty"""
    i = 0
    while (i < diff*3.0):
        cat = GetRandomAfterburner(diff)
        temp = un.upgrade(cat.GetContent(), 0, 0, 1, 0)
        debug.debug("Upgrading Afterburner %s percent %.3f" % (cat.GetContent(), temp))
        i = i+1


def getRandomEngine(diff):
    """Calculate random engine and reactor multipliers based on difficulty"""
    myint = GetDiffInt(diff)
    cat = "engine_level_%d" % (myint)
    debug.debug("Got %s" % (cat))
    dog = "reactor_level_%d" % (myint)
    debug.debug("Got %s" % (dog))
    return (myint, cat, dog)


def UpgradeEngine(un, diff):
    """Upgrades engine, reactor and shields based on difficulty level"""
    (type, cat, dog) = getRandomEngine(diff)
    if (type != 0):
        temp = un.upgrade(cat, 0, 0, 1, 0)
        temp = un.upgrade(dog, 0, 0, 1, 0)
        debug.debug("Upgrading Engine %s percent %f" % (cat, temp))
        if (temp > 0.0):
            cat = GetRandomShield(2, type)
            temp = un.upgrade(cat, 0, 0, 1, 0)
            debug.debug("Upgrading Shield %s percent %f" % (cat, temp))
            cat = GetRandomShield(4, type)
            temp = un.upgrade(cat, 0, 0, 1, 0)
            debug.debug("Upgrading Shield4 %s percent %f" % (cat, temp))
            return True
    cat = GetShieldLevelZero(2)
    temp = un.upgrade(cat, 0, 0, 1, 0)
    debug.debug("Upgrading Shield2 level 0... percent=%s" % (temp))
    cat = GetShieldLevelZero(4)
    temp = un.upgrade(cat, 0, 0, 1, 0)
    debug.debug("Upgrading Shield4 level 0... percent=%s" % (temp))
    return False


def GetRandomHull():
    item = getItem("upgrades/Hull_Upgrades")
    return item


def GetRandomTurret():
    item = getItem("upgrades/Weapons/Turrets", "upgrades/Weapons")
    return item


def GetRandomArmor():
    item = getItem("upgrades/Armor_Modification", "upgrades/Hull_Upgrades")
    return item


def GetRandomAmmo():
    item = getItem("upgrades/Ammunition/3pack", "upgrades/Ammunition")
    return item


def GetRandomRepairSys():
    item = getItem("upgrades/Repair_Systems/Research", "upgrades/Repair_Systems")
    return item


def basicUnit(un, diff):
    """This sets up a blank unit with the basic upgrades needed for any sort of figthing"""
    i = 0
    while (i < 2):  # two lasers
        percent = un.upgrade("laser", i, i, 0, 1)
        i = i + 1
    UpgradeEngine(un, diff)
    UpgradeRadar(un)
    if ((vsrandom.random() < 0.9) and (vsrandom.random() < (diff * 5.0))):
        UpgradeAfterburner(un, diff)
        if ((vsrandom.random() < 0.9) and (vsrandom.random() < (diff * 5.0))):
            percent = un.upgrade("jump_drive", i, i, 0, 1)
    else:
        percent = un.upgrade("jump_drive", i, i, 0, 1)
    # and after some careful review of the code in question,
    # it appears upgrades below are already offered by default on blank ships
    # ...only need to give 'em a pair of guns
    #some engines
    #    percent=un.upgrade("engine_level_0",0,0,0,0)
    #    percent=un.upgrade("shield_2",0,0,0,0)
    #both shield 2 and 4 depending on ship type!
    #    percent=un.upgrade("shield_4",0,0,0,0)
    #some dumb armor
    #    percent=un.upgrade("plasteel",0,0,0,0)
    #and at least a few hitpoints
    #    percent=un.upgrade("hull",0,0,0,0)


def upgradeHelper(un, mycargo, curmount, creds, force, cycle):
    """This does the dirty work of the upgrade unit function.

        Given the list that contains a piece of cargo, it upgrades it,
        subtracts the price, and slaps it on your ship,
        and returns the new number of creds the computer player has.

        It may well be negative because we thought that these guys may
        go into debt or something

    """
    newcreds = 0.0
    if (mycargo.GetQuantity() <= 0):  # if somehow the cargo isn't there
        debug.debug("UpgradeError: cargo not found")
        return 0.0  # and terminate the enclosing loop by saying we're out of cash
    else:
        str = mycargo.GetContent()  # otherwise our name is the GetQuantity() function
        newcreds = mycargo.GetPrice()  # and the price is the GetPrice() function
        newcreds = newcreds * un.upgrade(str, curmount, curmount, force, cycle)
        creds = creds - newcreds  # we added some newcreds and subtracted them from credit ammt
    return creds  # return new creds


def upgradeUnit(un, diff):
    """Handle the actual upgrading process on a unit based on difficulty"""
    creds = 0.0
    curmount = 0
    mycargo = VS.Cargo("", "", 0, 0, 0, 0)
    str = ""
    debug.debug("Calling basicUnit(%s, %.2f)" % (un.getName(), float(diff)))
    basicUnit(un, diff)
    debug.debug("'- basicUnit returned")
    mycargo = GetRandomHull()  # ok now we get some hull upgrades
    creds = upgradeHelper(un, mycargo, 0, creds, 1, 0)
    mycargo = GetRandomArmor()  # and some random armor
    creds = upgradeHelper(un, mycargo, 0, creds, 1, 0)
    inc = 0
    rndnum = vsrandom.random() * 2
    if (rndnum < diff):
        # there is a small chance that you will get a repair system.
        mycargo = GetRandomRepairSys()
        creds = upgradeHelper(un, mycargo, 0, creds, 1, 0)
    turretz = un.getSubUnits()
    turretcount = 0
    while (not turretz.isDone()):
        turretcount += 1
        turretz.advance()
    #turretcount -= 1
    debug.debug("Iterating through turrets...")
    for i in range(turretcount):
        for j in range(4):
            mycargo = GetRandomTurret()  # turrets as 3rd...
            creds = upgradeHelper(un, mycargo, i, creds, 0, 0)
    debug.debug("'- Done iterating through turrets.")
    turretcount = diff*50
    if (turretcount > 24):
        turretcount = 24
    elif (turretcount < 3):
        turretcount = 3
    debug.debug("Iterating through difficulty-based turretcount...")
    for i in range(int(turretcount)):
        for j in range(10):
            if (vsrandom.random() < 0.66):
                # weapons go on as first two items of loop
                mycargo = GetRandomWeapon(diff)
            else:
                mycargo = GetRandomAmmo()
            cont = mycargo.GetContent()
            if (cont.find('tractor') == -1 and cont.find('repulsor') == -1 and cont.find("steltek_gun") == -1):
                creds = upgradeHelper(un, mycargo, curmount, creds, 0, 1)  # we pass this in to the credits...and we only loop through all mounts if we're adding a weapon
                break
        curmount += 1  # increase starting mounts hardpoint
    debug.debug("'- Done iterating through difficulty-based turretcount.")


def get_info(un):
    """ Show the configuration of a ship unit

        unit_name : string
        reactor : string (N/A)
        shield : string (N/A)
        hull : string (N/A)
        armor : string (N/A)
        ecm : string (N/A)
        repair_droid : string (N/A)
        radar : string (N/A)
        missiles : string
        guns : string
        turrets : string (N/A)
    """
    num_mounts = un.getNumMounts()
    info = "\n >>> current unit: %s (%s), %d mounts\n" % (un.getName(), un.getFactionName(), num_mounts)
    for i in range(num_mounts):
        if "weapon_info" in un.GetMountInfo(i):
            info += "     '- mount %d: %s\n" % (i, un.GetMountInfo(i)["weapon_info"]["name"])
        else:
            info += "     '- mount %d: %s\n" % (i, un.GetMountInfo(i))
    debug.debug(info)


def match_and_upgrade_weapons(un, upgrade_maps):
    """This function adjusts mounts according to the supplied upgrade maps

       An upgrade map is a list with tuples of the form ('Laser','mass_driver')
    """
    matches = False
    num_mounts = un.getNumMounts()
    for i in range(num_mounts):
        for umap in upgrade_maps:
            _match, _new = umap
            if "weapon_info" in un.GetMountInfo(i):
                current_mount = un.GetMountInfo(i)["weapon_info"]["name"]
                if current_mount == _match:
                    un.upgrade(_new, i, 0, 1, 0)
                    matches = True
                    #debug.debug("\n >>> '- matched %s and swapped for %s (mount: %d)" % (_match, _new, i))
    return matches


def adjust_upgrades(un):
    """This is the master function for custom upgrade rules"""

    upgraded = False
    current_system = VS.getSystemName()
    player_ship = VS.getPlayer().getName()
    this_unit = un.getName()
    this_unit_faction = un.getFactionName()

    s = "\n >>> current_system: %s\n     player_ship = %s\n" % (current_system, player_ship)
    s += "     '- attempting to upgrade: %s (%s)...\n" % (this_unit, this_unit_faction)
    debug.debug(s)
    get_info(un)
    # BEGIN custom upgrade rules

    pirate_rabble_talon_weapons = [("MassDriver", "laser"),
                                   ("Particle", "mass_driver")]
    if (current_system == "Troy"
    and "tarsus" in player_ship
    and "pirates" in this_unit_faction
    and "talon" in this_unit):
        upgraded = match_and_upgrade_weapons(un, pirate_rabble_talon_weapons)

    # END custom upgrade rules
    if upgraded:
        s = "\n >>> '- adjustments made to %s (%s)! :-)\n" % (this_unit, this_unit_faction)
        debug.debug(s)
        get_info(un)
    else:
        s = "\n --- '- no adjustments made to %s (%s).\n" % (this_unit, this_unit_faction)
        debug.debug(s)


