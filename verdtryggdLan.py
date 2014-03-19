import math
def sparnadur_a_manudi(manadarGreidsla, vextir, verdbolga):
	vex = vextir / 100.0
	ver = verdbolga / 100.0
	return (manadarGreidsla * (vex + ver)) / 12

def manadarlegar_greidslur_af_lani(hofudstoll, timabil, vextir, verdbolga):
	v = (vextir + verdbolga) / 100.0
	heildarUpphaed = hofudstoll * math.pow((1 + v), (timabil / 12))
	return heildarUpphaed / timabil
