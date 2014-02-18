import math
import matplotlib.pyplot as plt
import numpy
import reiknivelar

def plot_framtidarvirdi(eign, timabil, vextir):
    vaxtabrot = vextir/100.0
    plotData = []
    fig1 = plt.figure()
    for manudur in range(0,timabil+1):
        plotData.append(eign*(math.pow((1+vaxtabrot), manudur)))
    plt.plot(plotData, linewidth=2, color='r')
    plt.ylabel(u"Krónur")
    plt.xlabel(u"Ár")
    fig1.canvas.set_window_title(u'Framtíðarvirði')
    plt.show()

def plot_reglulegurspar(greidsla, timabil, vextir):
    v = vextir/100.0
    vex = v/12.0
    plotData = []
    fig2 = plt.figure()
    for manudur in range(0, timabil+1):
        plotData.append((greidsla / vex)*((math.pow((1 + vex), manudur)) - 1))
    plt.plot(plotData,linewidth=2, color='r')
    plt.ylabel(u"Krónur")
    plt.xlabel(u"Mánuðir") 
    fig2.canvas.set_window_title('Reglulegur sparnaður')
    plt.show()

def plot_hofudstols_ryrnun(hofudstoll, timabil, vextir, verdbolga, manadarGreidsla, fjoldiManadarGreidslna):
    plotData1 = reiknivelar.hofudstols_ryrnun_an_sparnadar(hofudstoll, timabil, vextir, verdbolga)
    plotData2 = reiknivelar.hofudstols_ryrnun_med_sparnadi(hofudstoll, timabil, vextir, verdbolga, manadarGreidsla, fjoldiManadarGreidslna)
    fig3 = plt.figure()
    line1, = plt.plot(plotData1, linewidth=2, color='r')
    line2, = plt.plot(plotData2, linewidth=2, color='b')
    plt.ylabel(u"Krónur")
    plt.xlabel(u"Mánuðir")
    fig3.canvas.set_window_title("Greiðsla af láni")
    fig3.legend([line1, line2], [u'Niðugreiðsla án sparnaðar', u'Niðurgreiðsla með sparnaði'], bbox_to_anchor=[0.5, 0.955], loc='center', ncol=2)
    plt.show()