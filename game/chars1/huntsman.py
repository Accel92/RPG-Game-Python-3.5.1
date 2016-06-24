from ..core.new_player import my_player

class Huntsman(object):


	profession_name = "Hunstsman"

	def skillset(self):

		player_level = my_player.get_level()
		player_hp = my_player.get_hp()

		if player_level < 3:
			skills_dict = {
			"1. Shot (basic): " : player_hp // 6,
			"2. Rapid Fire: " : player_hp // 4,
			"3. Air barrage: " : player_hp // 3
			}
			return skills_dict

		elif player_level >= 6:
			skills_dict = {
			"1. Shot (basic): " : player_hp // 6,
			"2. Rapid Fire: " : player_hp // 4,
			"3. Air barrage: " : player_hp // 3
			}
			return skills_dict