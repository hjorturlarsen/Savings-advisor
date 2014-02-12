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