import VS
import Director
import directions_mission

class ambush(directions_mission.directions_mission):
	def privateSetupPlayer(self):
		self.timer=0
		self.inescapable=0
		self.havelaunched=0
		self.terminated=0

	def __init__(self, savevar, systems, delay, faction, numenemies, dyntype='', fgname='', greetingText=["Hello there, smuggler. Prepare to die!", "The price on your head is big enough that I missed my lunch."], directions=[], destination='', AdjustFaction=True):
		directions_mission.directions_mission.__init__ (self, savevar, directions, destination)
		print 'Ambush: Starting'
		if type(faction)!=tuple and type(faction)!=list:
			self.faction=(faction,)
		else:
			self.faction=faction
		if type(systems)!=tuple and type(systems)!=list:
			self.systems=(systems,)
		else:
			self.systems=systems
		if type(numenemies)!=tuple and type(numenemies)!=list:
			self.numenemies=(numenemies,)
		else:
			self.numenemies=numenemies
		if type(dyntype)!=tuple and type(dyntype)!=list:
			self.dyntype=(dyntype,)
		else:
			self.dyntype=dyntype
		if type(fgname)!=tuple and type(fgname)!=list:
			self.fgname=(fgname,)
		else:
			self.fgname=fgname
		self.greetingText=greetingText
		self.cp=VS.getCurrentPlayer()
		self.delay=delay
		self.privateSetupPlayer()
		if type(AdjustFaction)!=tuple and type(AdjustFaction)!=list:
			self.AdjustFaction=(AdjustFaction,)
		else:
			self.AdjustFaction=AdjustFaction
	def setupPlayer(self,cp):
		print "ambush setting player up"
		directions_mission.directions_mission.setupPlayer(self,cp)
		self.privateSetupPlayer()

	def Launch(self,you):
		if (self.havelaunched==0):
			for i in range (len(self.faction)):
				faction=self.faction[i]
				if len(self.numenemies) > i:
					numenemies=self.numenemies[i]
				else:
					numenemies=self.numenemies[0]
				if type(self.AdjustFaction) != bool:
					try:
						if len(self.AdjustFaction) > i:
							self.AdjustFaction=self.AdjustFaction[i]
						else:
							self.AdjustFaction=self.AdjustFaction[0]
					except:
						AjdustFaction = True
				if len(self.fgname) > i:
					fgname=self.fgname[i]
				else:
					fgname=self.fgname[0]
				if fgname=="":
					fgname="Shadow"
				if len(self.dyntype) > i:
					dyntype=self.dyntype[i]
				else:
					dyntype=self.dyntype[0]
				for z in range(numenemies):
					print 'Ambush: Launch ships!'
					self.havelaunched=1
					import launch
					L=launch.Launch()
					L.fg=fgname
					L.dynfg="" # dynfg tells launch to load flightgroup from SaveString
					if (dyntype==""):
						import faction_ships
						dyntype=faction_ships.getRandomFighter(faction)
					L.type=dyntype
					L.num=1
					if z == 0:
						L.fgappend=""
					else:
						L.fgappend="_"+str(z)
					L.minradius=6000
					L.maxradius=8000
					try:
						import faction_ships
						L.minradius*=faction_ships.launch_distance_factor
						L.maxradius*=faction_ships.launch_distance_factor
					except:
						pass
					L.faction=faction
					import universe		
					enemy=L.launch(you)
					lead=enemy.getFlightgroupLeader()
					enemy.SetTarget(you)
					if (lead):
						lead.SetTarget(you)
					else:
						enemy.setFlightgroupLeader(enemy)
					enemy.setFgDirective("A.")
					self.enemy=lead			
					rel=VS.GetRelation(faction,"privateer")
					if (self.AdjustFaction and rel>=0):
						VS.AdjustRelation(faction,"privateer",-.02-rel,1.0)
						rel=VS.GetRelation("privateer",faction)
						VS.AdjustRelation("privateer",faction,-.02-rel,1.0)
					if (i==0 and z==0):
						universe.greet(self.greetingText,enemy,you)
					print 'Ambush: Ships have been launched. Exiting...'
	def terminate(self):
		self.terminated=1#VS.terminateMission(0)
	def Execute(self):
		directions_mission.directions_mission.Execute(self)
		if (self.terminated==1):
			return
		you=VS.getPlayerX(self.cp)
		if you.isNull():
			return
		sys=you.getUnitSystemFile()
		if(not self.inescapable):
			for i in self.systems:
				where=sys.find(i)
				if (where>0):
					if (sys[where-1]=='/'):
						where=0
				if (where==0):
					#print 'Ambush: wait before launching ship...'
					self.inescapable=1
					self.timer=VS.GetGameTime()
		if (self.inescapable and ((self.delay==0) or (VS.GetGameTime()-self.timer>=self.delay))):
			self.Launch(you)
			self.terminate()
#					print "it's unavoidable, my young apprentice... in "+str(self.delay)+" seconds from "+str(self.timer)
			
