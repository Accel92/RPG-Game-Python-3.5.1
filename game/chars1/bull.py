from ..core import PlayerTemplate
from random import randint

class Bull(object):
	
	fight_plot = "Bull appears in front of you.\n You need to fight!"
	first_hit_chance_ratio = 30
	
	def __init__(self, level, special_status = ""):
		self.__level = level
		self.__special = special_status
		self.__name = "Bull (lvl. %i)%s" % (self.level, self.special)
		player_template = PlayerTemplate()
		player_template.set_level(self.level)
		self.__hp = player_template.get_hp()*0.7
		self.__mana = self.__hp
		self.__exp_reward = 100 + 50* self_level
		
		del player_template
	
	def skillset(self):
		
		if self.level < 3:
			skills_dict = {
			"1. Charge: " : self.hp * 1/6,
			}	
			return skills_dict
			
		elif self.level >= 6:
			skills_dict = {
			"1. Charge: " : self.hp * 1/6,
			"2. Trample: " : self.hp * 1/5,
			}
			return skills_dict
	
	def attack(self):
		attacks = skillset()
		if len(attacks) = 1:
			return attacks.value["1"]
		else:
			return attacks.value[randint(1:2)]
			
	def get_hp(self):
		return self.__hp
	
	def get_name(self):
		return self.__name
	
	def get_exp_reward(self):
		return self.__exp_reward