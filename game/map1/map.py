from . import Welcome
from . import SecondLocation
from . import ThirdLocation
from . import Boss


class Map(object):
	
	first_location = Welcome()
	last_location = Boss()
	
	locations = { 
	'second_location' : SecondLocation(),
	'third_location' : ThirdLocation()
	}
	
	def get_first_location(self):
		return self.first_location
	
	def get_last_location(self):
		return self.last_location
	
	def next_location(self, location):
		loc = Map.locations.get(location)
		return loc
		
		
		
'''class Map(object):	alternative

    scenes = {
        'welcome': Welcome(),
        'second_location': SecondLocation(),
        'finished': Boss(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)'''
