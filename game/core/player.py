from .choose_skill import choose_skill

class Player(object):

	
	def __init__(self):
		self._exp = 0
		self._level = 1
	
	def set_name(self, name):
		self._name = name
	
	def set_stats(self, experience):
		self._exp += experience
		self._level = (self._exp + 100)//100
		self._hp = 100 + 50 *(self._level - 1)
		self._mana = self._hp
	
	def set_spec(self, spec):
		self._spec = spec
	
	def set_skills(self):
		'''use every time at the end of fight f-tion to 
		set skills power according to newly gainsed exp'''
		self._skills = self._spec.skillset()	
		# skills_set_per_level is a f-tion of every profession
		
	def use_skill(self):
		'''method used strictly inside fight function'''
		
		number_of_skills = len(self._skills) 
		skill_keys = sorted(self._skills)
		skill_values = [value for (key, value) in sorted(self._skills.items())]
		i = 0
		while i < number_of_skills:
			print(skill_keys[i], skill_values[i], "dmg")
			i += 1
		
		what_do = choose_skill(number_of_skills)
		return skill_values[what_do - 1]	#because iteration from 0
		
		

	def get_player(self):
		print("Name: ", self._name)
		print("level: ", self._level)
		print("experience: ", self._exp)
		print("health: ", self._health)
		print("mana: ", self._mana)
		
	def get_name(self):
		return self._name

	def get_level(self):
		return self._level
		
	def get_exp(self):
		return self._exp
		
	def get_spec(self):
		return self._spec
		
	def get_skills(self):
		return self._skills
		
	def get_hp(self):
		return self._hp
		
	def get_mana(self):
		return self._mana