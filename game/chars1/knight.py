from ..core import my_player

class Knight(object):
	
	
	profession_name = "Knight"
	
	def skillset(self):
		
		player_level = my_player.get_level()
		player_hp = my_player.get_hp()
		
		if player_level < 3:
			skills_dict = {
			"1. Slash (basic): " : player_hp // 6,
			"2. Heavy Strike: " : player_hp // 5
			}	
			return skills_dict
			
		elif player_level >= 6:
			skills_dict = {
			"1. Slash (basic): " : player_hp // 6,
			"2. Heavy Slash: " : player_hp // 5,
			"3. Atomic Punch: " : player_hp
			}
			return skills_dict