import Base
import debug
import sys
import planet_lib
time_of_day='_night'
debug.info("calling planet_lib.MakePlanet (time_of_day='%s'" % (time_of_day))
room = planet_lib.MakePlanet (time_of_day)
