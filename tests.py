import playercharacter
import mutation
import dice
import pytest

def test_pc_add_session_mp():
	pc = playercharacter.PlayerCharacter(3,3,3,3)
	pc.mutations.append("")
	pc.mutations.append("")
	before = pc.MP
	pc.add_session_mp()
	after = pc.MP
	assert after == before + 2

def test_dice_throwing_and_consistency():
	d = dice.Dice()
	d.roll_all_dice(4,3,3)
	results = d.get_all_rolls()
	
	cnt1 = 0
	cnt2 = 0
	cnt3 = 0
	for die in results[0]:
		if(die == 5):
			cnt1 += 1
		elif(die == 0):
			cnt2 +=1
	
	for die in results[1]:
		if(die == 5):
			cnt1 += 1

	for die in results[2]:
		if(die == 5):
			cnt1 += 1
		elif(die == 0):
			cnt3 +=1

	assert(cnt1 == d.get_successes() and cnt2 == d.get_mutation_results() and cnt3 == d.get_gear_break())

@pytest.mark.parametrize('execution_number', range(5))
def test_push_roll(execution_number):
	d = dice.Dice()
	d.roll_all_dice(4,3,3)
	results = d.get_all_rolls()	
	cnt1 = d.get_successes()
	cnt2 = d.get_mutation_results()
	cnt3 = d.get_gear_break()
	d.push_the_roll()
	cnt1 -= d.get_successes()
	cnt2 -= d.get_mutation_results()
	cnt3 -= d.get_gear_break()
	assert(cnt1 <= 0 and cnt2 <= 0 and cnt3 <= 0)
