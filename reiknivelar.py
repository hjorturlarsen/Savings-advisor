import math

#Haegt ad hafa negativ-a vexti og tapa thannig sma saman pening
def framtidarvirdi(eign, timabil, vextir):
    if (eign < 0 or timabil < 0):
        return
    # Ekki haegt ad hafa strengi sem input
    if(isinstance(eign, str) or isinstance(timabil, str) or isinstance(vextir, str)):
        return
    vaxtabrot = vextir/100.0
    return eign*(math.pow((1 + vaxtabrot), timabil))

#Haegt ad hafa negativ-a vexti
def reglulegurspar(greidsla, timabil, vextir):
    if(greidsla < 0 or timabil < 0):
        return
    # Ekki haegt ad hafa strengi sem input
    if(isinstance(greidsla, str) or isinstance(timabil, str) or isinstance(vextir, str)):
        return
    v = vextir/100.0
    vex = v/12.0
    return (greidsla / vex)*((math.pow((1 + vex), timabil)) - 1)

#Eign getur verid neikvaed t.d. ef thu skuldar 10.000
#tha tharftu ad leggja meira fyrir a manudi en ella.
#Einnig geta vextir verid neikvaedir
def sparnadar_takmark(upphaed, eign, timabil, vextir):
    if(upphaed < 0 or timabil < 0):
        return
    # Ekki haegt ad hafa strengi sem input
    if(isinstance(eign, str) or isinstance(timabil, str) or isinstance(vextir, str) or isinstance(upphaed, str)):
        return
    vex = vextir / 100.0
    efra = ((upphaed - eign * math.pow(1 + (vex / 12), (12 * timabil))) * vex / 12)
    nedra = math.pow(1 + (vex / 12), 12 * timabil) - 1
    return round(efra / nedra)

#Vextir geta verid negativ
def sparnadar_timi(markmid, upphaed, vextir):
    if(markmid < 0 or upphaed < 0):
        return 
    # Ekki haegt ad hafa strengi sem input
    if(isinstance(markmid, str) or isinstance(upphaed, str) or isinstance(vextir, str)):
        return
    vex = vextir / 100.0
    efra = math.log10(((markmid * (vex / 12)) / upphaed) + 1)
    nedra = math.log10(1 + (vex / 12)) * 12
    
    total = efra / nedra
    ar = int(total)
    manudir = math.ceil((total - ar) * 12)
    return ar, manudir

#Vextir og verdbolga geta her verid negative
def sparnadur_a_manudi(manadarGreidsla, vextir, verdbolga):
    if(manadarGreidsla < 0):
        return
    # Ekki haegt ad hafa strengi sem input
    if(isinstance(manadarGreidsla, str) or isinstance(verdbolga, str) or isinstance(vextir, str)):
        return
    vex = vextir / 100.0
    ver = verdbolga / 100.0
    return (manadarGreidsla * (vex + ver)) / 12

#Vextir og verdbolga geta verid negative sem er snilld fyrir lantakendur 
def manadarlegar_greidslur_af_lani(hofudstoll, timabil, vextir, verdbolga):
    if(hofudstoll < 0 or timabil < 0 or vextir < 0):
        return
    # Ekki haegt ad hafa strengi sem input
    if(isinstance(hofudstoll, str) or isinstance(timabil, str) or isinstance(verdbolga, str) or isinstance(vextir, str)):
        return
    v = (vextir + verdbolga) / 100.0
    heildarUpphaed = hofudstoll * math.pow((1 + v), (timabil / 12.0))
    return heildarUpphaed / timabil

def hofudstols_ryrnun_an_sparnadar(hofudstoll, timabil, vextir, verdbolga):
    stada = []
    stada.append(hofudstoll)
    greidsla = manadarlegar_greidslur_af_lani(hofudstoll, timabil, vextir, verdbolga)
    while(hofudstoll > 1):
        if(greidsla > hofudstoll):
            greidsla = hofudstoll
        hofudstoll = hofudstoll - greidsla
        stada.append(hofudstoll)
    return stada

def hofudstols_ryrnun_med_sparnadi(hofudstoll, timabil, vextir, verdbolga, manadarGreidsla):
    stada = []
    stada.append(hofudstoll)
    #breytan greidsla er manadargreidsla af lani a manudi að vidbaettri theirri upphaed
    #sem notandi er tilbuinn ad greida inn a hofudstolinn a manudi. (Vextir dregnir fra theirri upphaed)
    greidsla = manadarlegar_greidslur_af_lani(hofudstoll, timabil, vextir, verdbolga) + (manadarGreidsla -sparnadur_a_manudi(manadarGreidsla, vextir, verdbolga))
    while(hofudstoll > 1):
        if(greidsla > hofudstoll):
            greidsla = hofudstoll
        hofudstoll = hofudstoll - greidsla
        stada.append(hofudstoll)
    return stada


def verdtryggt(strengur):
    if(strengur == u'Já'):
        return True
    else:
        return False
