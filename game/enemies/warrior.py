#from ..core import PlayerTemplate
from .enemy import Enemy

from random import randint

class Warrior(Enemy):
	
	fight_plot = "Enemy Warrior appears in front of you.\nYou need to fight!"
	first_hit_chance_ratio = 30
	
	def __init__(self, level, special_status = ""):
		super(Warrior, self).__init__(level, special_status)
		self._exp_reward = 100 + 50* self._level
		#del player_template
		if self._level < 3:
			self._skills = {
			"1. Charge: " : self._hp // 4,
			}	
		elif self._level >= 6:
			self._skills = {
			"1. Charge: " : self._hp // 4,
			"2. SpinSlash: " : self._hp // 3,
			}