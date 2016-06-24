from ..core.new_player import my_player

class Shadow(object):


	profession_name = "Shadow"

	def skillset(self):

		player_level = my_player.get_level()
		player_hp = my_player.get_hp()

		if player_level < 3:
			skills_dict = {
			"1. Slash (basic):" : player_hp  //6,
			"2. Shadow Step: " : player_hp // 4,
			"3. Ambush: " : player_hp // 3
			}
			return skills_dict

		elif player_level >= 6:
			skills_dict = {
			"1. Slash (basic): " : player_hp //6,
			"2. Shadow Step (basic): " : player_hp //4,
			"3. Ambush: " : player_hp // 3,
			"4. Trap: " : player_hp * 3
			}
			return skills_dict