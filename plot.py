import math
import matplotlib.pyplot as plt
import numpy

def plot_framtidarvirdi(eign, timabil, vextir):
    vaxtabrot = vextir/100.0
    plotData = []
    fig = plt.figure()
    for manudur in range(0,timabil+1):
        plotData.append(eign*(math.pow((1+vaxtabrot), manudur)))
    plt.plot(plotData)
    plt.ylabel(u"Krónur")
    plt.xlabel(u"Ár")
    fig.canvas.set_window_title(u'Framtíðarvirði')
    plt.show()

def plot_reglulegurspar(greidsla, timabil, vextir):
    v = vextir/100.0
    vex = v/12.0
    plotData = []
    fig = plt.figure()
    for manudur in range(0, timabil+1):
        plotData.append((greidsla / vex)*((math.pow((1 + vex), manudur)) - 1))
    plt.plot(plotData)
    plt.ylabel(u"Krónur")
    plt.xlabel(u"Mánuðir") 
    fig.canvas.set_window_title('Reglulegur sparnaður')
    plt.show()


def plot_manadarlegar_greidslur_af_lani(hofudstoll, timabil, vextir, verdbolga):
    v = (vextir + verdbolga) / 100.0
    manadarGreidsla = 10000
    heildarUpphaed = hofudstoll * math.pow((1 + v), (timabil / 12))
    plotData = []
    plotData2 = []
    fig = plt.figure()
    for manudur in range(0, timabil+1):
        plotData.append(heildarUpphaed/timabil)
        plotData2.append(heildarUpphaed/timabil - 1000)
    plt.plot(plotData)
    plt.plot(plotData2)
    plt.ylim([0,100000])
    plt.ylabel(u"Krónur")
    plt.xlabel(u"Mánuðir") 
    fig.canvas.set_window_title('Mánaðarlegar greiðslur af láni')
    plt.show()

plot_manadarlegar_greidslur_af_lani(1000000, 25, 4, 5)