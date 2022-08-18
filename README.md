Privateer: Wing Commander Universe
==================================

  Privateer: Wing Commander Universe (Priv:WCU) is a mod for the
Open Source VegaStrike game. It is patterned after the 1994 Privateer
game set in Chris Robert's Wing Commander universe.

  While Priv:WCU aims to include a faithful representation of the
orginal Privateer campaign, it also aims to give the player access
to the wider Wing Commander Universe and not just the Gemini sector
of the original game.

  Similarly, the aim is to include and allow the purchase of ships
not available for purchase in the original Privateer game.  The
rationale is that if a ship is seen flying around in the wider Wing
Commander Universe, it should be available for purchase -- at the
right price (which may include doing someone a personal favour).

  It should be noted that Privateer: Wing Commander Universe is
basically a rebranded version of Privateer: Parallel Universe.

  I (ermo) am under the impression that I have the blessing of the
former maintainer (who goes by the nick 'Chuck Starchaser') to
continue the development of his baby.  Sadly, the SVN repository
of Privateer: Parallel Universe and its development forum appears
to be lost to the bit gods.

  If you want to participate in the Priv:WCU development discussion,
check out the development thread on the Vega Strike forums:

  http://forums.vega-strike.org/viewtopic.php?p=133438#p133438

How to get Privateer: Wing Commander Universe running
-----------------------------------------------------

  Priv:WCU is developed on top of the latest stable git branch version
of the VegaStrike engine. It is not presently in a state suitable for
end-users.

  It is worth noting that Priv:WCU is developed and tested primarily on
Linux.
  
### Windows:

  Priv:WCU is not currently tested under Windows, but the VegaStrike
engine should now be running on Windows.

### Linux:

  Instructions on how to fetch and compile the newest VegaStrike
engine can be found here:

  https://github.com/vegastrike/Vega-Strike-Engine-Source#compiling-vegastrike

  The Priv:WCU codebase has been ported to py3. Python-3.4 and up is
supported since the 0.8.x branch of the Vega-Strike-Engine-Source project.
  
  Python-2.7 is no longer supported.

### Creating symlinks to the VegaStrike binaries ###

  Create a bin/ directory in the root Priv:WCU folder and create
symbolic links to the `vegastrike-engine` and `vegasettings` binaries respectively.

On my system, it looks like this:


    ermo@dante:~/repos/privateer_wcu/bin [master* +0 ~1 -0 !]
    $ ls -l
    total 0
    lrwxrwxrwx 1 ermo ermo 48 Aug 18 18:14 vegasettings -> ../../Vega-Strike-Engine-Source/bin/vegasettings
    lrwxrwxrwx 1 ermo ermo 53 Aug 18 18:14 vegastrike-engine -> ../../Vega-Strike-Engine-Source/bin/vegastrike-engine


To start Priv:WCU in development mode, navigate to the Priv:WCU `bin/` folder
and type `./vegastrike-engine -D../` `<ENTER>`

To change the Priv:WCU configuration options, navigate to the Priv:WCU `bin/` folder
and type `./vegasettings --target ../` `<ENTER>`


Forking
-------

  I humbly ask that you do not fork this project (Priv:WCU) to make
competing projects until such time as it is clear that I (ermo) am no
longer making any attempt to update it.  You are however welcome to
fork the project if the intent is to contribute content or bugfixes. :)

Please use only `https://github.com/pwcu/privateer_wcu` as the fork origin.

History
-------

  Privateer: Wing Comander Universe has its roots in the Privateer:
Parallel Universe mod (which itself is a continuation of the
Privateer Remake project, the history of which is too long to include
here), but also includes content from the Privateer: Gemini Gold mod
(as close to a 1:1 remake of the original Privateer on the VegaStrike
engine as one is likely to get) and the Wing Commander Universe project,
which itself spawned the Privateer Remake project.

Wing Commander: Universe can be found at http://wcu.solsector.net/

Privateer: Gemini Gold can be found at http://privateer.sourceforge.net/

Confused yet?


Credits
-------

- Chuck Starchaser (Privateer: Parallel Universe lead)
- John Cordell (Privateer: Gemini Gold lead)
- [DMJC](https://github.com/DMJC) (Wing Commander: Universe lead)
- (to be filled in as I learn more about the long history this project)
