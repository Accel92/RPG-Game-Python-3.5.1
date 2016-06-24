import random
import time

from ..core import Fight
from ..enemies.warrior import Warrior

class Castle(object):

	def start(self):
		print("""
		You stand up and walk around the room. It's small with some furnitures
		and a lamp on wooden table. You dress up in the linen clothes that have been
		left for you and. You look through a big castle window in your room.
		You see part of fortification and a cliff. Further ahead there is a Winter Forest.
		You recognize it for



		""")
		print("that only thing left to do is fight")
		my_enemy = Warrior(1, "[Boss]")
		print("ME BE PRINTING")
		fight1 = Fight(my_enemy)
		fight1.fight()
		time.sleep(2)
		return 'third_location'
		#return 0