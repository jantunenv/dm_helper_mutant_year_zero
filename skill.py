class skill:
	
	def __init__ (self, name, attribute, combat = False, action = True, level = 0):
		assert attribute in ["Strength", "Agility", "Wits", "Empathy"]
		self.level = level
		self.name = name
		self.attribute = attribute
		self.combat_skill = combat
		self.consumes_action = action

	def set_level(self, level):
		self.level = level

class SpecialistSkill(Skill):
	def __init__ (self, name, attribute, class_name):
		assert class_name in ["Enforcer", "Gearhead", "Stalker", "Fixer", "Dog_Handler", "Chronicler", "Boss", "Grunt"]
		Skill.__init__(self, name, attribute)
		self.class_name = class_name

class Skill_list:
	def __init__ (self):
		self.skills = {"Endure": Skill("Endure", "Strength"),
						"Force": Skill("Force", "Strength", True),
						"Fight": Skill("Fight", "Strength", True),
						"Sneak": Skill("Sneak", "Agility"),
						"Move": Skill("Move", "Agility", True),
						"Shoot": Skill("Shoot", "Agility", True),
						"Scout": Skill("Scout", "Wits"),
						"Comprehend": Skill("Comprehend", "Wits"),
						"Know_the_Zone": Skill("Know_the_Zone", "Wits"),
						"Sense_Emotion": Skill("Sense_Emotion", "Empathy"),
						"Manipulate": Skill("Manipulate", "Empathy", True),
						"Heal": Skill("Heal", "Empathy", True),
						"Intimidate": SpecialistSkill("Intimidate", "Strength", "Enforcer", True),
						"Jury-Rig": SpecialistSkill("Jury-Rig", "Wits", "Gearhead"),
						"Find_the_Path": SpecialistSkill("Find_the_Path", "Agility", "Stalker"),
						"Make_a_Deal": SpecialistSkill("Make_a_Deal", "Empathy", "Fixer"),
						"Sic_a_Dog": SpecialistSkill("Sic_a_Dog", "Agility", "Dog_Handler", True),
						"Inspire": SpecialistSkill("Inspire", "Empathy", "Chronicler", True),
						"Command": SpecialistSkill("Command", "Wits", "Boss"),
						"Shake_It_Off": SpecialistSkill("Shake_It_Off", "Strength", "Grunt", True, False),	
						}
