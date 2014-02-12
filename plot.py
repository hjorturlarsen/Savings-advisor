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
    heildarUpphaed = hofudstoll * math.pow((1 + v), (timabil / 12))
    plotData = []
    fig = plt.figure()
    for manudur in range(0, timabil+1):
        plotData.append(heildarUpphaed/timabil)
    plt.plot(plotData)
    plt.ylabel(u"Krónur")
    plt.xlabel(u"Mánuðir") 
    fig.canvas.set_window_title('Mánaðarlegar greiðslur af láni')
    plt.show()