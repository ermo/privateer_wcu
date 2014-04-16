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
rationale is that all ships flying around in the wider Wing
Commander Universe should be available for purchase.

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

  Priv:WCU is developed on top of the latest SVN version of the
VegaStrike engine. It is not presently in a state suitable for
end-users.

  It is worth noting that Priv:WCU is developed on Linux.
  
### Windows:

  Priv:WCU does not currently run under Windows.  Last I checked, the 
VegaStrike development binaries for Windows did not work with the
Priv:WCU code base. 

### Linux:

  Instructions on how to fetch and compile the newest VegaStrike
engine can be found here:

  http://wiki.vega-strike.org/HowTo:Compile_from_SVN_on_Linux

  At present, Priv:WCU depends on the Python 2.7 branch of the VS
source code (this is the default).  It will likely not work on the new
Python 3.x branch.


### Creating symlinks to the VegaStrike binaries ###

  Create a bin/ directory in the root Priv:WCU folder and create
symbolic links to the vegastrike and vssetup binaries respectively.

On my system, it looks like this:


    [privateer_wcu/]$ ls -la bin/
    total 8
    drwx------  2 ermo ermo 4096 Sep 25 16:16 .
    drwxrwxr-x 26 ermo ermo 4096 Sep 25 16:12 ..
    lrwxrwxrwx  1 ermo ermo   39 Sep  5 00:46 vegastrike -> ../../trunk/vegastrike/build/vegastrike
    lrwxrwxrwx  1 ermo ermo   42 Sep  5 00:46 vssetup -> ../../trunk/vegastrike/build/setup/vssetup
    [privateer_wcu/]$


To start Priv:WCU, navigate to the root Priv:WCU folder and type bin/vegastrike <ENTER>

To change the Priv:WCU configuration options, navigate to the root Priv:WCU folder
and type bin/vssetup <ENTER>


Forking
-------

  I humbly ask that you do not fork this project (Priv:WCU) to make
competing projects until such time as it is clear that I (ermo) am no
longer making any attempt to update it.  You are however welcome to
fork the project if the intent is to contribute content or bugfixes. :)


History
-------

  Privateer: Wing Comander Universe has its roots in the Privateer:
Parallel Universe mod (which itself is a continuation of the
Privateer Remake project, the history of which is too long to include
here), but also includes content from the Privateer: Gemini Gold mod
(as close to a 1:1 remake of the original Privateer on the VegaStrike
engine as one is likely to get) and the Wing Commander Universe project,
which itself spawned the Privateer Remake project.

Wing Commander Universe can be found at http://wcu.solsector.net/

Privateer: Gemini Gold can be found at http://privateer.sourceforge.net/

Confused yet?


Credits
-------

* Chuck Starchaser (Privateer: Parallel Universe lead)
* John Cordell (Privateer: Gemini Gold lead)
* (to be filled in as I learn more about the long history this project)
