<<<<<<< HEAD
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
=======
﻿import math
import matplotlib.pyplot as plt

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
    
>>>>>>> 7174126a1058d8fb778212ae57bbb0c094d961c5
