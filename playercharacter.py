class Character:
	MP = 0
	mutations = []
	skills = []
	talents = []
	init_bonus = 0

	def __init__(self, name, strength = 3, agility = 3, wits = 3, empathy = 3):
		self.strength = strength
		self.agility = agility
		self.wits = wits
		self.empathy = empathy
		self.name = name

	
class PlayerCharacter(Character):
	def __init__(self, strength = 3, agility = 3, wits = 3, empathy = 3):
		Character.__init__(self, strength, agility, wits, empathy)

	def add_session_mp(self):
		self.MP += len(self.mutations)
