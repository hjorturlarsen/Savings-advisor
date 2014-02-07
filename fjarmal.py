
# fjarmal.py

##LALALALALALALALALALALALAL

import wx
import Tabs

class MyNote(wx.Notebook):
    def __init__(self, parent):
        wx.Notebook.__init__(self, parent, id=wx.ID_ANY, style=wx.BK_DEFAULT)

        tabOne = Tabs.Tab1(self)
        self.AddPage(tabOne, u"Skrá lán")
        tabTwo = Tabs.Tab2(self)
        self.AddPage(tabTwo, u"Reglulegur sparnaður")
        tabThree = Tabs.Tab3(self)
        self.AddPage(tabThree, u"Framtíðarvirði")
        tabFour = Tabs.Tab4(self)
        self.AddPage(tabFour, u"Sparnaðartakmark")
        tabFive = Tabs.Tab5(self)
        self.AddPage(tabFive, u"Sparnaðartími")



class MyFrame(wx.Frame):

    def __init__(self):

        wx.Frame.__init__(self, None, wx.ID_ANY, u"Lánayfirlit", size=(1200,700))
        panel = wx.Panel(self)
        notebook = MyNote(panel)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(notebook, 1, wx.ALL|wx.EXPAND, 5)
        panel.SetSizer(sizer)
        self.Layout()
        self.SetBackgroundColour(wx.BLACK)
        self.Show()

app = wx.App(False)
frame = MyFrame()
app.MainLoop()
