import numpy as np
class Combat:
	
	team_red = []
	team_blue = []
	initiative_order = []
	
	def __init__(self, map_x=10, map_y=10):
		self.terrain = np.zeros(size=(map_x, map_y))
		
	def read_terrain(self):
		#Placeholder
		pass

	def add_to_team_red(self, character):
		team_red.append(character)
		
	def add_to_team_blue(self, character):
		team_blue.append(character)
	
	def roll_initiatives(self):
		#Affected by Extreme Reflexes mutation and Combat Veteran talent
		for character in team_red:
			init_score = np.random.randint(6) + character.init_bonus +  character.agility*0.01 + np.random.random_sample()*0.001
			if("Combat_Veteran" in character.talents):
				init_score_alt = np.random.randint(6) + character.init_bonus +  character.agility*0.01 + np.random.random_sample()*0.001				
				init_score = max([init_score, init_score_alt])

			initiative_order.append([character, init_score])
			
		for character in team_blue:
			init_score = np.random.randint(6) + character.init_bonus + character.agility*0.01 + np.random.random_sample()*0.001
			if("Combat_Veteran" in character.talents):
				init_score_alt = np.random.randint(6) + character.init_bonus +  character.agility*0.01 + np.random.random_sample()*0.001				
				init_score = max([init_score, init_score_alt])

			initiative_order.append([character, init_score])

		initiative_order = sorted(initiative_order, key = lambda x: x[1], reverse = True)

	def modify_initiative(character_name, amount):		
		for i in range(len(initiative_order):
			character = initiative_order[i][0]
			if(character.name == character_name):
				initiative_order[i][1] = initiative_order[i][1] + amount
				break

		initiative_order = sorted(initiative_order, key = lambda x: x[1], reverse = True)
