class Engine(object):
	
	def __init__(self, a_map):
		self.map = a_map
		
	def play(self):
		current_scene = self.map.get_first_location()
		last_scene = self.map.get_last_location()
		
		while True:
			try: 
				next_scene_return = current_scene.start()
			except AttributeError:
				print("WATCH OUT: We go with last scene")
				last_scene.start()
				break
			current_scene = self.map.next_location(next_scene_return)
			
'''class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.start()
            current_scene = self.scene_map.next_scene(next_scene_name)'''