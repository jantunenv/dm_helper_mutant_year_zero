import playercharacter
import mutation

def test_pc_add_session_mp():
	pc = playercharacter.PlayerCharacter(3,3,3,3)
	pc.mutations.append("")
	pc.mutations.append("")
	before = pc.MP
	pc.add_session_mp()
	after = pc.MP
	assert after == before + 2


