import pylab as pl
import tkinter as tk
from pylab import plot, pi
from os.path import basename, splitext
from tkinter import IntVar, StringVar

class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Graf"

    def __init__(self):

        super().__init__(className=self.name)
        self.geometry("300x500")

    
        self.var_entryFre = tk.IntVar()
        self.var_entryAmp = tk.IntVar()    
        self.var_entryPer = tk.IntVar()
        
        self.var_entryTit = tk.StringVar()
        self.var_entryXLabel = tk.StringVar()
        self.var_entryYLabel = tk.StringVar()

        self.var_entryFre.set(1)
        self.var_entryAmp.set(1)
        self.var_entryPer.set(1)
        self.var_entryTit.set("Title")
        self.var_entryXLabel.set("X label")
        self.var_entryYLabel.set("Y label")
    
        vcmd = (self.register(self.callback))

        self.title(self.name)

        self.lbl1 = tk.Label(self, text="Frekvence")
        self.lbl1.grid(row=0,column=0)
        self.entryFre = tk.Entry(self, validate="all", validatecommand=(vcmd, '%P'), textvariable = self.var_entryFre)
        self.entryFre.grid(row=1,column=0)

        self.lbl2 = tk.Label(self, text="Amplituda")
        self.lbl2.grid(row=2,column=0)
        self.entryAmp = tk.Entry(self, validate="all", validatecommand=(vcmd, '%P'), textvariable = self.var_entryAmp)
        self.entryAmp.grid(row=3,column=0)

        self.lbl3 = tk.Label(self, text="Počet period")
        self.lbl3.grid(row=4,column=0)
        self.entryPer = tk.Entry(self, validate="all", validatecommand=(vcmd, '%P'), textvariable = self.var_entryPer)
        self.entryPer.grid(row=5,column=0)

        self.lbl4 = tk.Label(self, text="Title")
        self.lbl4.grid(row=6,column=0)
        self.EntryTit = tk.Entry(self, textvariable = self.var_entryTit)
        self.EntryTit.grid(row=7,column=0)

        self.lbl5 = tk.Label(self, text="XLabel")
        self.lbl5.grid(row=8,column=0)
        self.EntryXLabel = tk.Entry(self, textvariable = self.var_entryXLabel)
        self.EntryXLabel.grid(row=9,column=0)

        self.lbl6 = tk.Label(self, text="YLabel")
        self.lbl6.grid(row=10,column=0)
        self.EntryYLabel = tk.Entry(self, textvariable = self.var_entryYLabel)
        self.EntryYLabel.grid(row=11,column=0)    

        self.btnZhodnot = tk.Button(self, text="Načti graf ze zadaných hodnot", command=self.Zhodnot)
        self.btnZhodnot.grid(row=12,column=0)

        self.btnNacti = tk.Button(self, text="Načti graf ze souboru", command=self.Zesouboru)
        self.btnNacti.grid(row=13,column=0)

        self.btn = tk.Button(self, text="Ukonči program", command=self.quit)
        self.btn.grid(row=14,column=0)
                
    
    def Zhodnot(self):
        self.fre = self.var_entryFre.get()
        self.amp = self.var_entryAmp.get()
        self.per = self.var_entryPer.get()

        self.tit = self.var_entryTit.get()
        self.xlabel = self.var_entryXLabel.get()
        self.ylabel = self.var_entryYLabel.get()

        t = pl.linspace(0, self.per/self.fre, self.fre*10000)
        y = self.amp * (pl.cos(2*pi*self.fre*t ))

        pl.plot(t,y)

        pl.title(self.tit)
        pl.xlabel(self.xlabel)
        pl.ylabel(self.ylabel)
        pl.show()

    def Zesouboru(self):
        f = open("soubor-win.txt", "r")
        x = []
        y = []
        while True:
            radek = f.readline()
            if radek =="":
                break
            cisla = radek.split()
            x.append(float(cisla[0]))
            y.append(float(cisla[1]))
        f.close()
        pl.figure()
        pl.plot(x,y)
        pl.grid(True)
        pl.show()

    def callback(self, P):
        if str.isdigit(P) or P == "":
            return True
        else:
            return False

    def quit(self, event=None):
        super().quit()

app = Application()
app.mainloop()