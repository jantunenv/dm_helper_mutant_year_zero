class PlayerCharacter:
	
	gear_dice = 0
	MP = 0
	mutations = []
	skills = []
	talents = []
	
	def __init__(self, strength = 3, agility = 3, wits = 3, empathy = 3):
		self.strength = strength
		self.agility = agility
		self.wits = wits
		self.empathy = empathy

	def add_session_mp(self):
		self.MP += len(self.mutations)
