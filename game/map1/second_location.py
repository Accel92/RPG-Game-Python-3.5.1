import random
import time

from ..core import Fight
from ..chars1 import SpiderLv1

class SecondLocation(object):
	
	def start(self):
		print("You enter a location and encounter taunted Bull, I'm afraind\
		that only thing left to do is fight")
		#spider = SpiderLv1()
		fight1 = Fight()
		fight1.fight(Bull, 1, "Boss")
		time.sleep(2)
		return 0