from ..core.new_player import my_player

class Mage(object):


	profession_name = "Mage"

	def skillset(self):
		
		player_level = my_player.get_level()
		player_hp = my_player.get_hp()
		
		if player_level < 3:
			skills_dict = {
			"1. Arcane Bolt (basic):" : player_hp  //6,
			"1. Fireball: " : player_hp //4,
			"2. Scorched Earth: " : player_hp //3
			}	
			return skills_dict
			
		elif player_level >= 6:
			skills_dict = {
			"1. Arcane Bolt (basic): " : player_hp //6,
			"2. Fireball (basic): " : player_hp //4,
			"3. Scorched Earth: " : player_hp //3,
			"4. Nuke: " : player_hp * 3
			}
			return skills_dict