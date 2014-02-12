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
    if(hofudstoll < 0 or timabil < 0):
        return
    # Ekki haegt ad hafa strengi sem input
    if(isinstance(hofudstoll, str) or isinstance(timabil, str) or isinstance(verdbolga, str) or isinstance(vextir, str)):
        return
    v = (vextir + verdbolga) / 100.0
    heildarUpphaed = hofudstoll * math.pow((1 + v), (timabil / 12.0))
    return heildarUpphaed / timabil

def verdtryggt(strengur):
    if(strengur == u'Já'):
        return True
    else:
        return False
        
print framtidarvirdi("sss",2.0,4)
print framtidarvirdi(-1000,2.2,4.3)
print framtidarvirdi(1000,-0.4,-4.3)
print framtidarvirdi(1000,2,0)
print framtidarvirdi(-1000,2,0)
print "----------------------"
print reglulegurspar(-1000,2,3)
print reglulegurspar(1000.0,-2,3)
print reglulegurspar(1000.45,2.0,-3)
print reglulegurspar(-1000,-2,-3)
print reglulegurspar(1000.45,2.45,3.45)
print "----------------------"
print sparnadar_takmark(-10000, 15000, 2, 4)
print sparnadar_takmark(-100000, 15000, 2, 4)
print sparnadar_takmark(10000, -15000, 2, 4)
print sparnadar_takmark(10000, 15000, "ssdf", 4.34)
print sparnadar_takmark(10000, 15000, -2, -4)
print "----------------------"
print sparnadar_timi(-100000, -1000, 4)
print sparnadar_timi(100000, -1000, 4)
print sparnadar_timi(-100000, 1000, 4)
print sparnadar_timi("100000", 1000, 4)
print sparnadar_timi(100000, 100.20, 4)
print "----------------------"
print sparnadur_a_manudi(1000, 3, 5)
print sparnadur_a_manudi(1000, 3, 5)
print sparnadur_a_manudi(1000, 3, 5)
print sparnadur_a_manudi(1000, 3, 5)
print sparnadur_a_manudi(1000, 3, 5)
print "----------------------"
print manadarlegar_greidslur_af_lani(100000, -3, 4, 4)
print manadarlegar_greidslur_af_lani(100000, 3, -4, 4)
print manadarlegar_greidslur_af_lani(-100000, 3, 4, 4)
print manadarlegar_greidslur_af_lani("sdsadw", 3, -4, 4)
print manadarlegar_greidslur_af_lani(100000, 3, 0, 0)
print manadarlegar_greidslur_af_lani(100000, 3, -4.0, -7.3)