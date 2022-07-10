import numpy as np
class Dice:
	def __init__(self):
		self.base_roll = None
		self.skill_roll = None
		self.gear_roll = None
		self.pushed = False

	def roll_all_dice(self, n_base, n_skill, n_gear):
		self.pushed = False
		self.base_roll = np.random.randint(6, size = n_base).tolist()
		self.skill_roll = np.random.randint(6, size = n_skill).tolist()
		self.gear_roll = np.random.randint(6, size = n_gear).tolist()

	def push_the_roll(self):
		if(self.pushed == False):
			self.pushed = True
			for i in range(len(self.base_roll)):
				if( self.base_roll[i] != 5 and self.base_roll[i] != 0):
					self.base_roll[i] = np.random.randint(6)
					
			for i in range(len(self.skill_roll)):
				if( self.skill_roll[i] != 5):
					self.skill_roll[i] = np.random.randint(6)

			for i in range(len(self.gear_roll)):
				if( self.gear_roll[i] != 5 and self.gear_roll[i] != 0):
					self.gear_roll[i] = np.random.randint(6)
		else:
			print("Pushing a roll twice not allowed!")
	
	def get_all_rolls(self):
		return(self.base_roll, self.skill_roll, self.gear_roll)

	def get_successes(self):
		return(self.base_roll.count(5) + self.skill_roll.count(5) + self.gear_roll.count(5))
		
	def get_mutation_results(self):
		return(self.base_roll.count(0))
			
	def get_gear_break(self):
		return(self.gear_roll.count(0))
