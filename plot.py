import math
import matplotlib.pyplot as plt

def plot_framtidarvirdi(eign, timabil, vextir):
    vaxtabrot = vextir/100.0
    plotData = []
    for manudur in range(0,timabil+1):
        plotData.append(eign*(math.pow((1+vaxtabrot), manudur)))
    plt.plot(plotData)
    plt.ylabel("Kronur")
    plt.xlabel("Ar")
    plt.show()

def plot_reglulegurspar(greidsla, timabil, vextir):
    v = vextir/100.0
    vex = v/12.0
    plotData = []
    for manudur in range(0, timabil+1):
        plotData.append((greidsla / vex)*((math.pow((1 + vex), manudur)) - 1))
    plt.plot(plotData)
    plt.ylabel("Kronur")
    plt.xlabel("Manudir")
    plt.show()

#def plot_sparnadar_takmark(upphaed, eign, timabil, vextir):
#    vex = vextir / 100.0
#    plotData = []
#    for manudur in range(1,timabil+1):
#        efra = ((upphaed - eign * math.pow(1 + (vex / 12), (12 * manudur))) * vex / 12)
#        nedra = math.pow(1 + (vex / 12), 12 * manudur) - 1
#        plotData.append(round(efra/nedra))
#    plt.plot(plotData)
#    plt.ylabel("Kronur")
#    plt.xlabel("Ar")
#    plt.show()

#def plot_sparnadar_timi(markmid, upphaed, vextir):
#    vex = vextir / 100.0
#    efra = math.log10(((markmid * (vex / 12)) / upphaed) + 1)
#    nedra = math.log10(1 + (vex / 12)) * 12
#	
#    total = efra / nedra
#    ar = int(total)
#    manudir = math.ceil((total - ar) * 12)
#    return ar, manudir