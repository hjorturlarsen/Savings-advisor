import reiknivelar
import wx
import Reikningar
import plot

lan = []

class Tab1(wx.Panel):
    def __init__(self, parent):

        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY, size=(0,0))
        hbox  = wx.BoxSizer(wx.HORIZONTAL)
        vbox1 = wx.BoxSizer(wx.VERTICAL)
        vbox2 = wx.BoxSizer(wx.VERTICAL)
        vbox3 = wx.GridSizer(6,2,0,0)
        vbox4 = wx.GridSizer(4,2,0,0)
        pnl1 = wx.Panel(self, -1, style=wx.SIMPLE_BORDER)
        pnl2 = wx.Panel(self, -1, style=wx.SIMPLE_BORDER)
        self.lc = wx.ListCtrl(self, -1, style=wx.LC_REPORT)
        self.lc.InsertColumn(0, u'Nafn')
        self.lc.InsertColumn(1, u'Vextir')
        self.lc.InsertColumn(2, u'Verðtryggt')
        self.lc.InsertColumn(3, u'Höfudstoll')
        self.lc.InsertColumn(4, u'Lengd i mánuðum')
        self.lc.SetColumnWidth(0, 140)
        self.lc.SetColumnWidth(1, 130)
        self.lc.SetColumnWidth(2, 130)
        self.lc.SetColumnWidth(3, 150)
        self.lc.SetColumnWidth(4, 170)

        yesno = [u'Já', 'Nei']

        vbox1.Add(pnl1, 1, wx.EXPAND | wx.ALL, 3)
        vbox1.Add(pnl2, 1, wx.EXPAND | wx.ALL, 3)
        vbox2.Add(self.lc, 1, wx.EXPAND)
        self.tc1 = wx.TextCtrl(pnl1, -1)
        self.tc2 = wx.TextCtrl(pnl1, -1)
        self.tc3 = wx.ComboBox(pnl1, -1, size=(110,-1), choices=yesno)
        self.tc4 = wx.TextCtrl(pnl1, -1)
        self.tc5 = wx.TextCtrl(pnl1, -1)
        vbox3.AddMany([ (wx.StaticText(pnl1, -1, u'Nafn:'),0, wx.ALIGN_CENTER| wx.TOP, 0),
                        (self.tc1, 0, wx.ALIGN_LEFT|wx.ALIGN_CENTER| wx.TOP, 0),
                        (wx.StaticText(pnl1, -1, u'Vextir:'),0, wx.ALIGN_CENTER| wx.TOP, 0),
                        (self.tc2,0, wx.ALIGN_LEFT|wx.ALIGN_CENTER| wx.TOP, 0),
                        (wx.StaticText(pnl1, -1, u'Verdtryggt:'),0, wx.ALIGN_CENTER| wx.TOP, 0),
                        (self.tc3, 0, wx.ALIGN_LEFT|wx.ALIGN_CENTER| wx.TOP, 0),
                        (wx.StaticText(pnl1, -1, u'Höfuðstóll:'),0, wx.ALIGN_CENTER| wx.TOP, 0),
                        (self.tc4, 0, wx.ALIGN_LEFT|wx.ALIGN_CENTER| wx.TOP, 0),
                        (wx.StaticText(pnl1, -1, u'Lengd i mánuðum:'),0, wx.ALIGN_CENTER| wx.TOP, 0),
                        (self.tc5, 0, wx.ALIGN_LEFT|wx.ALIGN_CENTER| wx.TOP, 0),
                        (wx.Button(pnl1, 10, u'Bæta við'),   0, wx.ALIGN_CENTER| wx.TOP, 0),
                        (wx.Button(pnl1, 12, u'Hreinsa'), 0, wx.ALIGN_CENTER| wx.TOP, 0)])
        pnl1.SetSizer(vbox3)

        self.tc6 = wx.TextCtrl(pnl2, -1)
        self.tc7 = wx.TextCtrl(pnl2, -1)
        self.tc8 = wx.TextCtrl(pnl2, -1)
        
        vbox4.Add(wx.StaticText(pnl2, -1, u'Upphæð:'),0,  wx.ALIGN_CENTER| wx.TOP, 0)
        vbox4.Add(self.tc6, 0,  wx.ALIGN_CENTER| wx.TOP, 0)
        vbox4.Add(wx.StaticText(pnl2, -1, u'Tími:'),0,  wx.ALIGN_CENTER| wx.TOP, 0)
        vbox4.Add(self.tc7, 0,  wx.ALIGN_CENTER| wx.TOP, 0)
        vbox4.Add(wx.StaticText(pnl2, -1, u'Mesta binding:'),0,  wx.ALIGN_CENTER| wx.TOP, 0)
        vbox4.Add(self.tc8, 0,  wx.ALIGN_CENTER| wx.TOP, 0)
        vbox4.Add(wx.Button(pnl2, 13, u'Finna'),   0, wx.ALIGN_CENTER| wx.TOP, 0)

        self.lc2 = wx.ListCtrl(self, -1, style=wx.LC_REPORT)
        self.lc2.InsertColumn(0, u'Nafn')
        self.lc2.InsertColumn(1, u'Vextir')
        self.lc2.InsertColumn(2, u'Verðtryggt')
        self.lc2.InsertColumn(3, u'Binding i mánuðum')
        self.lc2.InsertColumn(4, u'Innistæðuhækkun vaxta')
        self.lc2.SetColumnWidth(0, 200)
        self.lc2.SetColumnWidth(1, 100)
        self.lc2.SetColumnWidth(2, 100)
        self.lc2.SetColumnWidth(3, 120)
        self.lc2.SetColumnWidth(4, 120)
        vbox2.Add(self.lc2, 1, wx.EXPAND)

        for i in range(len(Reikningar.Reikningar)):
            self.lc2.InsertStringItem(i, Reikningar.Reikningar[i][0])
            self.lc2.SetStringItem(i, 1, Reikningar.Reikningar[i][1])
            self.lc2.SetStringItem(i, 2, Reikningar.Reikningar[i][2])
            self.lc2.SetStringItem(i, 3, Reikningar.Reikningar[i][3])
            self.lc2.SetStringItem(i, 4, Reikningar.Reikningar[i][4])
    
    
        pnl2.SetSizer(vbox4)
        self.Bind (wx.EVT_BUTTON, self.OnAdd, id=10)
        #self.Bind (wx.EVT_BUTTON, self.OnRemove, id=11)
        self.Bind (wx.EVT_BUTTON, self.OnClear, id=12)
        self.Bind (wx.EVT_BUTTON, self.OnFind, id=13)
        hbox.Add(vbox1, 1, wx.EXPAND)
        hbox.Add(vbox2, 1, wx.EXPAND)
        self.SetSizer(hbox)

    def OnAdd(self, event):
        if not self.tc1.GetValue() or not self.tc2.GetValue() or not self.tc3.GetValue() or not self.tc4.GetValue() or not self.tc5.GetValue():
            return
        num_items = self.lc.GetItemCount()
        self.lc.InsertStringItem(num_items, self.tc1.GetValue())
        self.lc.SetStringItem(num_items, 1, self.tc2.GetValue())
        self.lc.SetStringItem(num_items, 2, self.tc3.GetValue())
        self.lc.SetStringItem(num_items, 3, self.tc4.GetValue())
        self.lc.SetStringItem(num_items, 4, self.tc5.GetValue())
        l = [self.tc1.GetValue(),float(self.tc2.GetValue()),self.tc3.GetValue(),
             int(self.tc4.GetValue()),int(self.tc5.GetValue())]
        lan.append(l)
        print(lan)
        self.tc1.Clear()
        self.tc2.Clear()
        self.tc4.Clear()
        self.tc5.Clear()

    def OnRemove(self, event):
        index = self.lc.GetFocusedItem()
        self.lc.DeleteItem(index)

    def OnClear(self, event):
        self.lc.DeleteAllItems()

    def OnFind(self, event):
        if not self.tc6.GetValue() or not self.tc7.GetValue() or not self.tc8.GetValue():
            return

        
        u = int(self.tc6.GetValue())
        t = int(self.tc7.GetValue())
        m = float(self.tc8.GetValue())
        
        a = ''
        p = 0

        
        for i in range(len(lan)):
            if reiknivelar.verdtryggt(lan[i][2]):
                temp = float(lan[i][1]) + 5.0
                temp2 = reiknivelar.reglulegurspar(u, t, temp)
                if(p < temp2):
                    p = temp2
                    a = lan[i][0]
            else:
                temp = float(lan[i][1])
                temp2 = reiknivelar.reglulegurspar(u, t, temp)
                if(p < temp2):
                    p = temp2
                    a = lan[i][0]


        for j in range(len(Reikningar.Reikningar)):
            R = float(Reikningar.Reikningar[j][3])
            minsta = Reikningar.Reikningar[j][4]
            if R <= m:
                if(minsta == u'Nei'):
                    if(reiknivelar.verdtryggt(Reikningar.Reikningar[j][2])):
                        temp = float(Reikningar.Reikningar[j][1]) + 5.0
                        temp2 = reiknivelar.reglulegurspar(u, t, temp)
                        if(p<temp2):
                            p = temp2
                            a = Reikningar.Reikningar[j][0]
                    else:
                        temp = float(Reikningar.Reikningar[j][1])
                        temp2 = reiknivelar.reglulegurspar(u, t, temp)
                        if(p<temp2):
                            p = temp2
                            a = Reikningar.Reikningar[j][0]

                #elif minsta == u'Já':

                #--- Hér kemur útreikningur fyrir reikninga með breytilega vexti
                #--- eftir innistæðu
                    

        print(a)

                
        msg = u'Hagstæðast er að borga inn á: "'+ a + '"'
        dc = wx.MessageDialog(None, msg)
        dc.ShowModal()


class Tab2(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
        hbox  = wx.BoxSizer(wx.VERTICAL)
        vbox1 = wx.BoxSizer(wx.VERTICAL)
        vbox2 = wx.BoxSizer(wx.VERTICAL)
        vbox3 = wx.GridSizer(7,3,0,0)
        vbox4 = wx.BoxSizer(wx.VERTICAL)
        pnl1 = wx.Panel(self, -1, style=wx.SIMPLE_BORDER)
        pnl2 = wx.Panel(self, -1, style=wx.SIMPLE_BORDER)
        self.lc = wx.ListCtrl(self, -1, style=wx.LC_REPORT)
        
        vbox1.Add(pnl1, 1, wx.EXPAND | wx.ALL, 3)
        vbox1.Add(pnl2, 1, wx.EXPAND | wx.ALL, 3)
        vbox2.Add(self.lc, 1, wx.EXPAND | wx.ALL, 3)
        self.tc1 = wx.TextCtrl(pnl1, -1)
        self.tc2 = wx.TextCtrl(pnl1, -1)
        self.tc3 = wx.TextCtrl(pnl1, -1)
        self.tc4 = wx.TextCtrl(pnl1, -1, style=wx.TE_READONLY)
        
        vbox3.AddMany([ (wx.StaticText(pnl1, -1, ''),0, wx.ALIGN_CENTER| wx.TOP, 45),
                        (wx.StaticText(pnl1, -1, u'Reiknaðu út hvað regluleg mánaðarleg greiðsla verður orðin mikil eftir ákveðinn tíma og ávöxtun.'),0, wx.ALIGN_CENTER| wx.TOP, 45),
                        (wx.StaticText(pnl1, -1, ''),0, wx.ALIGN_CENTER| wx.TOP, 45),
                        (wx.StaticText(pnl1, -1, u'Mánaðarleg greiðsla:'),0, wx.ALIGN_CENTER| wx.TOP, 45),
                        (self.tc1, 0, wx.ALIGN_LEFT|wx.ALIGN_CENTER| wx.TOP, 45),
                        (wx.StaticText(pnl1, -1, u'krónur. Fjárhæð sem er lögð inn á hverjum mánuði.       '),0, wx.ALIGN_CENTER| wx.TOP, 45),
                        (wx.StaticText(pnl1, -1, u'Lengd timabils:'),0, wx.ALIGN_CENTER| wx.TOP, 40),
                        (self.tc2,0, wx.ALIGN_LEFT|wx.ALIGN_CENTER| wx.TOP, 40),
                        (wx.StaticText(pnl1, -1, u'mánuðir. Lengd sparnaðartímabils.'),0, wx.ALIGN_CENTER| wx.TOP, 45),
                        (wx.StaticText(pnl1, -1, u'Vextir:'),0, wx.ALIGN_CENTER| wx.TOP, 35),
                        (self.tc3, 0, wx.ALIGN_LEFT|wx.ALIGN_CENTER| wx.TOP, 35),
                        (wx.StaticText(pnl1, -1, u'%. Vextir á sparnaðartímabili.'),0, wx.ALIGN_CENTER| wx.TOP, 45),
                        (wx.StaticText(pnl1, -1, ''),0, wx.ALIGN_CENTER| wx.TOP, 35),
                        (wx.Button(pnl1, 10, u'Reikna'), 0, wx.ALIGN_CENTER| wx.TOP, 30),
                        (wx.StaticText(pnl1, -1, ''),0, wx.ALIGN_CENTER| wx.TOP, 45),
                        (wx.StaticText(pnl1, -1, u'Þú munt eiga:'),0, wx.ALIGN_CENTER| wx.TOP, 20),
                        (self.tc4, 0, wx.ALIGN_LEFT|wx.ALIGN_CENTER| wx.TOP, 20),
                        (wx.StaticText(pnl1, -1, u'krónur.'),0, wx.ALIGN_CENTER| wx.TOP, 45),
                        (wx.StaticText(pnl1, -1, ''),0, wx.ALIGN_CENTER| wx.TOP, 35),
                        (wx.Button(pnl1, 11, u'Myndrænt'), 0, wx.ALIGN_CENTER| wx.TOP, 30)])
        pnl1.SetSizer(vbox3)
        pnl2.SetSizer(vbox4)
        self.Bind (wx.EVT_BUTTON, self.OnAdd, id=10)
        self.Bind (wx.EVT_BUTTON, self.OnPlot, id=11)
        hbox.Add(vbox1, 1, wx.EXPAND)
        hbox.Add(vbox2, 1, wx.EXPAND)
        self.SetSizer(hbox)


    def OnAdd(self, event):
        if not self.tc1.GetValue() or not self.tc2.GetValue() or not self.tc3.GetValue():
            return
        self.tc4.Clear()
        greidsla = int(self.tc1.GetValue())
        timabil = int(self.tc2.GetValue())
        vextir = float(self.tc3.GetValue())
        nidurstada = reiknivelar.reglulegurspar(greidsla, timabil, vextir)
        nidurstada = int(nidurstada)
        self.tc4.AppendText(str(nidurstada))
        print nidurstada

    def OnPlot(self, event):
        greidsla = int(self.tc1.GetValue())
        timabil = int(self.tc2.GetValue())
        vextir = float(self.tc3.GetValue())
        plot.plot_reglulegurspar(greidsla, timabil, vextir)
        



class Tab3(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
        hbox  = wx.BoxSizer(wx.VERTICAL)
        vbox1 = wx.BoxSizer(wx.VERTICAL)
        vbox2 = wx.BoxSizer(wx.VERTICAL)
        vbox3 = wx.GridSizer(7,3,0,0)
        vbox4 = wx.BoxSizer(wx.VERTICAL)
        pnl1 = wx.Panel(self, -1, style=wx.SIMPLE_BORDER)
        pnl2 = wx.Panel(self, -1, style=wx.SIMPLE_BORDER)
        self.lc = wx.ListCtrl(self, -1, style=wx.LC_REPORT)
        
        vbox1.Add(pnl1, 1, wx.EXPAND | wx.ALL, 3)
        vbox1.Add(pnl2, 1, wx.EXPAND | wx.ALL, 3)
        vbox2.Add(self.lc, 1, wx.EXPAND | wx.ALL, 3)
        self.tc1 = wx.TextCtrl(pnl1, -1)
        self.tc2 = wx.TextCtrl(pnl1, -1)
        self.tc3 = wx.TextCtrl(pnl1, -1)
        self.tc4 = wx.TextCtrl(pnl1, -1, style=wx.TE_READONLY)
        
        vbox3.AddMany([ (wx.StaticText(pnl1, -1, ''),0, wx.ALIGN_CENTER| wx.TOP, 45),
                        (wx.StaticText(pnl1, -1, u'Reiknaðu út hvað eign þín verður orðin mikil eftir ákveðinn tíma og ávöxtun.'),0, wx.ALIGN_CENTER| wx.TOP, 45),
                        (wx.StaticText(pnl1, -1, ''),0, wx.ALIGN_CENTER| wx.TOP, 45),
                        (wx.StaticText(pnl1, -1, u'Upphafleg eign:'),0, wx.ALIGN_CENTER| wx.TOP, 45),
                        (self.tc1, 0, wx.ALIGN_LEFT|wx.ALIGN_CENTER| wx.TOP, 45),
                        (wx.StaticText(pnl1, -1, u'krónur. Fjárhæð sem til er fyrir sparnað.       '),0, wx.ALIGN_CENTER| wx.TOP, 45),
                        (wx.StaticText(pnl1, -1, u'Lengd timabils:'),0, wx.ALIGN_CENTER| wx.TOP, 40),
                        (self.tc2,0, wx.ALIGN_LEFT|wx.ALIGN_CENTER| wx.TOP, 40),
                        (wx.StaticText(pnl1, -1, u'ár. Lengd sparnaðartímabils.'),0, wx.ALIGN_CENTER| wx.TOP, 45),
                        (wx.StaticText(pnl1, -1, u'Vextir:'),0, wx.ALIGN_CENTER| wx.TOP, 35),
                        (self.tc3, 0, wx.ALIGN_LEFT|wx.ALIGN_CENTER| wx.TOP, 35),
                        (wx.StaticText(pnl1, -1, u'%. Vextir á sparnaðartímabili.'),0, wx.ALIGN_CENTER| wx.TOP, 45),
                        (wx.StaticText(pnl1, -1, ''),0, wx.ALIGN_CENTER| wx.TOP, 35),
                        (wx.Button(pnl1, 10, u'Reikna'), 0, wx.ALIGN_CENTER| wx.TOP, 30),
                        (wx.StaticText(pnl1, -1, ''),0, wx.ALIGN_CENTER| wx.TOP, 45),
                        (wx.StaticText(pnl1, -1, u'Þú munt eiga:'),0, wx.ALIGN_CENTER| wx.TOP, 20),
                        (self.tc4, 0, wx.ALIGN_LEFT|wx.ALIGN_CENTER| wx.TOP, 20),
                        (wx.StaticText(pnl1, -1, u'krónur.'),0, wx.ALIGN_CENTER| wx.TOP, 45),
                        (wx.StaticText(pnl1, -1, u''),0, wx.ALIGN_CENTER| wx.TOP, 45),
                        (wx.Button(pnl1, 11, u'Myndrænt'), 0, wx.ALIGN_CENTER| wx.TOP, 30)])
        pnl1.SetSizer(vbox3)
        pnl2.SetSizer(vbox4)
        self.Bind (wx.EVT_BUTTON, self.OnAdd, id=10)
        self.Bind (wx.EVT_BUTTON, self.OnPlot, id=11)
        hbox.Add(vbox1, 1, wx.EXPAND)
        hbox.Add(vbox2, 1, wx.EXPAND)
        self.SetSizer(hbox)

    def OnAdd(self, event):
        if not self.tc1.GetValue() or not self.tc2.GetValue() or not self.tc3.GetValue():
            return

        self.tc4.Clear()
        eign = int(self.tc1.GetValue())
        timabil = int(self.tc2.GetValue())
        vextir = float(self.tc3.GetValue())
        nidurstada = reiknivelar.framtidarvirdi(eign, timabil, vextir)
        nidurstada = int(nidurstada)
        self.tc4.AppendText(str(nidurstada))
        print nidurstada

    def OnPlot(self, event):
        eign = int(self.tc1.GetValue())
        timabil = int(self.tc2.GetValue())
        vextir = float(self.tc3.GetValue())
        plot.plot_framtidarvirdi(eign, timabil, vextir)

class Tab4(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
        
        hbox  = wx.BoxSizer(wx.VERTICAL)
        vbox1 = wx.BoxSizer(wx.VERTICAL)
        vbox2 = wx.BoxSizer(wx.VERTICAL)
        vbox3 = wx.GridSizer(7,3,0,0)
        vbox4 = wx.BoxSizer(wx.VERTICAL)
        pnl1 = wx.Panel(self, -1, style=wx.SIMPLE_BORDER)
        pnl2 = wx.Panel(self, -1, style=wx.SIMPLE_BORDER)
        self.lc = wx.ListCtrl(self, -1, style=wx.LC_REPORT)
        
        vbox1.Add(pnl1, 1, wx.EXPAND | wx.ALL, 3)
        vbox1.Add(pnl2, 1, wx.EXPAND | wx.ALL, 3)
        vbox2.Add(self.lc, 1, wx.EXPAND | wx.ALL, 3)
        self.tc1 = wx.TextCtrl(pnl1, -1)
        self.tc2 = wx.TextCtrl(pnl1, -1)
        self.tc3 = wx.TextCtrl(pnl1, -1)
        self.tc4 = wx.TextCtrl(pnl1, -1, style=wx.TE_READONLY)
        self.tc5 = wx.TextCtrl(pnl1, -1)
        
        vbox3.AddMany([ (wx.StaticText(pnl1, -1, ''),0, wx.ALIGN_CENTER| wx.TOP, 45),
                        (wx.StaticText(pnl1, -1, u'Reiknar út hvað þú þarft að leggja fyrir á mánuði til að ná óskaupphæðinni þinni eftir ákveðinn tíma'),0, wx.ALIGN_CENTER| wx.TOP, 45),
                        (wx.StaticText(pnl1, -1, ''),0, wx.ALIGN_CENTER| wx.TOP, 45),
                        (wx.StaticText(pnl1, -1, u'Óskaupphæð:'),0, wx.ALIGN_CENTER| wx.TOP, 45),
                        (self.tc1, 0, wx.ALIGN_LEFT|wx.ALIGN_CENTER| wx.TOP, 45),
                        (wx.StaticText(pnl1, -1, u'krónur. Fjárhæð sem þú vilt eiga i lok sparnaðar.       '),0, wx.ALIGN_CENTER| wx.TOP, 45),
                        (wx.StaticText(pnl1, -1, u'Upphafleg eign:'),0, wx.ALIGN_CENTER| wx.TOP, 40),
                        (self.tc2,0, wx.ALIGN_LEFT|wx.ALIGN_CENTER| wx.TOP, 40),
                        (wx.StaticText(pnl1, -1, u'krónur. Fjárhæð sem til er í upphafi sparnaðar.'),0, wx.ALIGN_CENTER| wx.TOP, 45),
                        (wx.StaticText(pnl1, -1, u'Tímabil:'),0, wx.ALIGN_CENTER| wx.TOP, 35),
                        (self.tc3, 0, wx.ALIGN_LEFT|wx.ALIGN_CENTER| wx.TOP, 35),
                        (wx.StaticText(pnl1, -1, u'ár. Lengd sparnaðartímabils í árum.'),0, wx.ALIGN_CENTER| wx.TOP, 45),
                        (wx.StaticText(pnl1, -1, u'Vextir:'),0, wx.ALIGN_CENTER| wx.TOP, 35),
                        (self.tc5, 0, wx.ALIGN_LEFT|wx.ALIGN_CENTER| wx.TOP, 35),
                        (wx.StaticText(pnl1, -1, u'%. Vextir á sparnaðartímabili.'),0, wx.ALIGN_CENTER| wx.TOP, 35),
                        (wx.StaticText(pnl1, -1, ''),0, wx.ALIGN_CENTER| wx.TOP, 35),
                        (wx.Button(pnl1, 10, u'Reikna'), 0, wx.ALIGN_CENTER| wx.TOP, 30),
                        (wx.StaticText(pnl1, -1, ''),0, wx.ALIGN_CENTER| wx.TOP, 45),
                        (wx.StaticText(pnl1, -1, u'Þú þarft að leggja:'),0, wx.ALIGN_CENTER| wx.TOP, 20),
                        (self.tc4, 0, wx.ALIGN_LEFT|wx.ALIGN_CENTER| wx.TOP, 20),
                        (wx.StaticText(pnl1, -1, u'krónur fyrir á mánuði.'),0, wx.ALIGN_CENTER| wx.TOP, 45)])
        pnl1.SetSizer(vbox3)
        pnl2.SetSizer(vbox4)
        self.Bind (wx.EVT_BUTTON, self.OnAdd, id=10)
        hbox.Add(vbox1, 1, wx.EXPAND)
        hbox.Add(vbox2, 1, wx.EXPAND)
        self.SetSizer(hbox)


    def OnAdd(self, event):
        if not self.tc1.GetValue() or not self.tc2.GetValue() or not self.tc3.GetValue() or not self.tc5.GetValue():
            return
        self.tc4.Clear()
        upphaed = int(self.tc1.GetValue())
        eign = int(self.tc2.GetValue())
        timabil = int(self.tc3.GetValue())
        vextir = float(self.tc5.GetValue())
        nidurstada = reiknivelar.sparnadar_takmark(upphaed, eign, timabil, vextir)
        nidurstada = int(nidurstada)
        self.tc4.AppendText(str(nidurstada))
        print nidurstada

class Tab5(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
        hbox  = wx.BoxSizer(wx.VERTICAL)
        vbox1 = wx.BoxSizer(wx.VERTICAL)
        vbox2 = wx.BoxSizer(wx.VERTICAL)
        vbox3 = wx.GridSizer(7,3,0,0)
        vbox4 = wx.BoxSizer(wx.VERTICAL)
        pnl1 = wx.Panel(self, -1, style=wx.SIMPLE_BORDER)
        pnl2 = wx.Panel(self, -1, style=wx.SIMPLE_BORDER)
        self.lc = wx.ListCtrl(self, -1, style=wx.LC_REPORT)
        
        vbox1.Add(pnl1, 1, wx.EXPAND | wx.ALL, 3)
        vbox1.Add(pnl2, 1, wx.EXPAND | wx.ALL, 3)
        vbox2.Add(self.lc, 1, wx.EXPAND | wx.ALL, 3)
        self.tc1 = wx.TextCtrl(pnl1, -1)
        self.tc2 = wx.TextCtrl(pnl1, -1)
        self.tc3 = wx.TextCtrl(pnl1, -1)
        self.tc4 = wx.TextCtrl(pnl1, -1, style=wx.TE_READONLY)
        self.tc5 = wx.TextCtrl(pnl1, -1, style=wx.TE_READONLY)
        
        vbox3.AddMany([ (wx.StaticText(pnl1, -1, ''),0, wx.ALIGN_CENTER| wx.TOP, 45),
                        (wx.StaticText(pnl1, -1, u'Reiknar út hversu lengi það tekur þig að spara vissa upphæð ef þú leggur ákveðna upphæð fyrir á mánuði.'),0, wx.ALIGN_CENTER| wx.TOP, 45),
                        (wx.StaticText(pnl1, -1, ''),0, wx.ALIGN_CENTER| wx.TOP, 45),
                        (wx.StaticText(pnl1, -1, u'Upphæð:'),0, wx.ALIGN_CENTER| wx.TOP, 45),
                        (self.tc1, 0, wx.ALIGN_LEFT|wx.ALIGN_CENTER| wx.TOP, 45),
                        (wx.StaticText(pnl1, -1, u'krónur. Fjárhæð sem á að spara fyrir.       '),0, wx.ALIGN_CENTER| wx.TOP, 45),
                        (wx.StaticText(pnl1, -1, u'Sparnaður á mánuði:'),0, wx.ALIGN_CENTER| wx.TOP, 40),
                        (self.tc2,0, wx.ALIGN_LEFT|wx.ALIGN_CENTER| wx.TOP, 40),
                        (wx.StaticText(pnl1, -1, u'krónur.'),0, wx.ALIGN_CENTER| wx.TOP, 45),
                        (wx.StaticText(pnl1, -1, u'Vextir:'),0, wx.ALIGN_CENTER| wx.TOP, 35),
                        (self.tc3, 0, wx.ALIGN_LEFT|wx.ALIGN_CENTER| wx.TOP, 35),
                        (wx.StaticText(pnl1, -1, u'%. Vextir á sparnaðartímabili.'),0, wx.ALIGN_CENTER| wx.TOP, 45),
                        (wx.StaticText(pnl1, -1, ''),0, wx.ALIGN_CENTER| wx.TOP, 35),
                        (wx.Button(pnl1, 10, u'Reikna'), 0, wx.ALIGN_CENTER| wx.TOP, 30),
                        (wx.StaticText(pnl1, -1, ''),0, wx.ALIGN_CENTER| wx.TOP, 45),
                        (wx.StaticText(pnl1, -1, u'Það tekur þig:'),0, wx.ALIGN_CENTER| wx.TOP, 20),
                        (self.tc4, 0, wx.ALIGN_LEFT|wx.ALIGN_CENTER| wx.TOP, 20),
                        (wx.StaticText(pnl1, -1, u'ár'),0, wx.ALIGN_CENTER| wx.TOP, 20),
                        (wx.StaticText(pnl1, -1, u'og'),0, wx.ALIGN_CENTER| wx.TOP, 45),
                        (self.tc5, 0, wx.ALIGN_LEFT|wx.ALIGN_CENTER| wx.TOP, 20),
                        (wx.StaticText(pnl1, -1, u'mánuði.'),0, wx.ALIGN_CENTER| wx.TOP, 45)])
        pnl1.SetSizer(vbox3)
        pnl2.SetSizer(vbox4)
        self.Bind (wx.EVT_BUTTON, self.OnAdd, id=10)
        hbox.Add(vbox1, 1, wx.EXPAND)
        hbox.Add(vbox2, 1, wx.EXPAND)
        self.SetSizer(hbox)

    def OnAdd(self, event):
        if not self.tc1.GetValue() or not self.tc2.GetValue() or not self.tc3.GetValue():
            return

        self.tc4.Clear()
        self.tc5.Clear()
        markmid = int(self.tc1.GetValue())
        upphaed = int(self.tc2.GetValue())
        vextir = float(self.tc3.GetValue())
        ar = reiknivelar.sparnadar_timi(markmid, upphaed, vextir)[0]
        ar = int(ar)
        self.tc4.AppendText(str(ar))
        man = reiknivelar.sparnadar_timi(markmid, upphaed, vextir)[1]
        man = int(man)
        self.tc5.AppendText(str(man))



            
