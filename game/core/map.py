from .welcome import Welcome
from .second_location import SecondLocation
from .third_location import ThirdLocation
from .boss import Boss

from .castle import Castle
from .wizard_tower import WizardTower
from .shadow1 import ShadowOne
from .copse import Copse


class Map(object):
	
	first_location = Welcome()
	last_location = Boss()
	
	locations = { 
	'castle' : Castle(),
	'wizard_tower' : WizardTower(),
	'shadow_one' : ShadowOne(),
	'copse' : Copse(),
	'second location' : SecondLocation(),
	'third location' : ThirdLocation()
	}
	
	def get_first_location(self):
		return self.first_location
	
	def get_last_location(self):
		return self.last_location
	
	def next_location(self, location):
		loc = Map.locations.get(location)
		return loc
		
		
'''
class Map(object):

    scenes = {
	'castle' : Castle(),
	'wizard_tower' : WizardTower(),
	'shadow_one' : ShadowOne(),
	'copse' : Copse(),
	'second location' : SecondLocation(),
	'third location' : ThirdLocation()
	}

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)'''