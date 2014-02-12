import math

def framtidarvirdi(eign, timabil, vextir):
    vaxtabrot = vextir/100.0
    return eign*(math.pow((1 + vaxtabrot), timabil))

def reglulegurspar(greidsla, timabil, vextir):
    v = vextir/100.0
    vex = v/12.0
    return (greidsla / vex)*((math.pow((1 + vex), timabil)) - 1)

def sparnadar_takmark(upphaed, eign, timabil, vextir):
    vex = vextir / 100.0
    efra = ((upphaed - eign * math.pow(1 + (vex / 12), (12 * timabil))) * vex / 12)
    nedra = math.pow(1 + (vex / 12), 12 * timabil) - 1
    return round(efra / nedra)

def sparnadar_timi(markmid, upphaed, vextir):
    vex = vextir / 100.0
    efra = math.log10(((markmid * (vex / 12)) / upphaed) + 1)
    nedra = math.log10(1 + (vex / 12)) * 12
	
    total = efra / nedra
    ar = int(total)
    manudir = math.ceil((total - ar) * 12)
    return ar, manudir

def sparnadur_a_manudi(manadarGreidsla, vextir, verdbolga):
	vex = vextir / 100.0
	ver = verdbolga / 100.0
	return (manadarGreidsla * (vex + ver)) / 12

def manadarlegar_greidslur_af_lani(hofudstoll, timabil, vextir, verdbolga):
	v = (vextir + verdbolga) / 100.0
	heildarUpphaed = hofudstoll * math.pow((1 + v), (timabil / 12))
	return heildarUpphaed / timabil

def verdtryggt(strengur):
    if(strengur == u'Já'):
        return True
    else:
        return False
