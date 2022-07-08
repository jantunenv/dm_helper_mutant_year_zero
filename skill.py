class skill:
	
	def __init__ (self, name, attribute):
		assert attribute in ["Strength", "Agility", "Wits", "Empathy"]
		self.name = name
		self.attribute = attribute

class SpecialistSkill(Skill):
	def __init__ (self, name, attribute, class_name):
		assert class_name in ["Enforcer", "Gearhead", "Stalker", "Fixer", "Dog_Handler", "Chronicler", "Boss", "Grunt"]
		Skill.__init__(self, name, attribute)
		self.class_name = class_name

class skill_list:
	
	def __init__ (self):
		
		self.skills = {"Endure": Skill("Endure", "Strength"),
						"Force": Skill("Force", "Strength"),
						"Fight": Skill("Fight", "Strength"),
						"Sneak": Skill("Sneak", "Agility"),
						"Move": Skill("Move", "Agility"),
						"Shoot": Skill("Shoot", "Agility"),
						"Scout": Skill("Scout", "Wits"),
						"Comprehend": Skill("Comprehend", "Wits"),
						"Know_the_Zone": Skill("Know_the_Zone", "Wits"),
						"Sense_Emotion": Skill("Sense_Emotion", "Empathy"),
						"Manipulate": Skill("Manipulate", "Empathy"),
						"Heal": Skill("Heal", "Empathy"),
						"Intimidate": SpecialistSkill("Intimidate", "Strength", "Enforcer"),
						"Jury-Rig": SpecialistSkill("Jury-Rig", "Wits", "Gearhead"),
						"Find_the_Path": SpecialistSkill("Find_the_Path", "Agility", "Stalker"),
						"Make_a_Deal": SpecialistSkill("Make_a_Deal", "Empathy", "Fixer"),
						"Sic_a_Dog": SpecialistSkill("Sic_a_Dog", "Agility", "Dog_Handler"),
						"Inspire": SpecialistSkill("Inspire", "Empathy", "Chronicler"),
						"Command": SpecialistSkill("Command", "Wits", "Boss"),
						"Shake_It_Off": SpecialistSkill("Shake_It_Off", "Strength", "Grunt"),	
						}

		
