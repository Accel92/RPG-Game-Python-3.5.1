import random
import time

from ..core.fight import Fight
from ..enemies.warrior import Warrior

class WizardTower(object):

	def start(self):
		print("You enter a WIZARD TOWER and encounter taunted Bull, I'm afraind")
		print("that only thing left to do is fight")
		my_enemy = Warrior(1, "[Boss]")
		print("ME BE PRINTING")
		fight1 = Fight(my_enemy)
		fight1.fight()
		time.sleep(2)
		return 'third_location'
		#return 0