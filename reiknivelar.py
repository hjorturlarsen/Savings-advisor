import math
import matplotlib.pyplot as plt

def framtidarvirdi(eign, timabil, vextir):
    vaxtabrot = vextir/100.0
    end = timabil
    plottari = []
    for manudur in range(0, end)
        plottari.Append(eign*(math.pow((1+vaxtabrot), manudur)))

    plt.plot(plottari)
    plt.ylabel("ble")
    plt.show()
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
