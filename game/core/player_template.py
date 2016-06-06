class PlayerTemplate:
	def set_level(self, level):
			self.__level = level
			self.__hp = 100 + 50 *(self.__level - 1)
			self.__mana = self.__health
	
	def get_hp(self):
		return self.__hp