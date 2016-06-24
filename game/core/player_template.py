class PlayerTemplate:
	
	def __init__(self, level):
		self._level = level
		self._hp = 100 + 50 *(self._level - 1)
		self._mana = self._hp
	
	def get_hp(self):
		return self._hp