import math
def sparnadur_a_manudi(manadarGreidsla, vextir, verdbolga):
	vex = vextir / 100.0
	ver = verdbolga / 100.0
	return (manadarGreidsla * (vex + ver)) / 12


def manadarlegar_greidslur_af_lani(hofudstoll, timabil, vextir, verdbolga):
	v = (vextir + verdbolga) / 100.0
	heildarUpphaed = hofudstoll * math.pow((1 + v), (timabil / 12))
	return heildarUpphaed / timabil


def verdtryggd_Lan(hofudstoll, timabil, vextir, verdbolga):

	overdTryggt = hofudstoll / timabil
	vex = vextir / 100.0
	ver = verdbolga / 100.0
	heildarVextir = (vex + ver) / 12.0

	fasti = overdTryggt*heildarVextir
	print overdTryggt
	#print heildarVextir
	summa = 0.0
	x = 0
	while x < timabil:
		
		total = fasti + overdTryggt
		summa += total
		print int(math.ceil(total))
		overdTryggt = total
		x += 1
	print summa
verdtryggd_Lan(10000000, 240, 3, 4)
print overdtryggd_Lan(10000000, 240, 3, 4)
print overdtryggd_Lan(10000000, 240, 3, 0)

#if(verdtryggt):
	#verdtryggd_Lan
#else:
	#overdtryggd_Lan
