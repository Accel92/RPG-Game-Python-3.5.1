from . import Welcome
from . import AryanBunker
from . import Boss


class Map(object):
	
	first_location = Welcome()
	last_location = Boss()
	
	locations = { 
	#'redhead_jew' : RedheadJew(),
	'aryan' : AryanBunker(),
	#'nigga' : NiggaPoopHut(),
	#'gypsy' : GypsyWagon(),
	#'muslim' : KebabMasterChef()
	#'boss' = Boss()
	}
	
	def get_first_location(self):
		return self.first_location
	
	def get_last_location(self):
		return self.last_location
	
	def next_location(self, location):
		loc = Map.locations.get(location)
		return loc