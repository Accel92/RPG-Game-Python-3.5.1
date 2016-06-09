from random import randint

from .player_template import PlayerTemplate

class Enemy(object):
	
	fight_plot = "I am no plot"
	first_hit_chance_ratio = randint(0,100)
	
	def __init__(self, level, special_status = ""):
		self._level = level
		self._special = special_status
		self._name = "%s (lvl. %i)%s" % (self.__class__.__name__, self._level, self._special)
		self._player_template = PlayerTemplate(self._level)
		
		self._hp = self._player_template.get_hp()*0.7
		self._mana = self._hp
		self._exp_reward = 0
		self._skills = {
		"1. First: " : self._hp // 6,
		"2. Second: " : self._hp // 4,
		"3. Nuke: " : self._hp * 2000	# serious need for change when inherited
		}	

	def attack(self):
		'''fighting AI for all opponents, change it if you need to'''
		list_of_values = [value for (key, value) in self._skills.items()]
		list_of_values.sort()
		return list_of_values[-1]
	
	def get_hp(self):
		return self._hp
	
	def get_name(self):
		return self._name
	
	def get_exp_reward(self):
		return self._exp_reward