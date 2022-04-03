import pylab as pl
import tkinter as tk

from pylab import *
from os.path import basename, splitext
from tkinter import *



class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Graf"

    def __init__(self):

        super().__init__(className=self.name)
        self.geometry("300x200")

        self.var_entryFre = tk.IntVar()
        self.var_entryAmp = tk.IntVar()     
        self.title(self.name)
        self.lbl1 = tk.Label(self, text="Frekvence")
        self.lbl1.pack()
        self.entryFre  = tk.Entry(self, textvariable = self.var_entryFre)
        self.entryFre.pack()
        self.lbl2 = tk.Label(self, text="Amplituda")
        self.lbl2.pack()
        self.entryAmp  = tk.Entry(self, textvariable = self.var_entryAmp)
        self.entryAmp.pack()
        self.btnZhodnot = tk.Button(self, text="Načti graf ze zadaných hodnot", command=self.Zhodnot)
        self.btnZhodnot.pack()
        self.btnVypsat = tk.Button(self, text="Načti graf ze souboru", command=self.Zesouboru)
        self.btnVypsat.pack()
        self.btn = tk.Button(self, text="Ukonči program", command=self.quit)
        self.btn.pack()
        
    def quit(self, event=None):
        super().quit()
    
    def Zhodnot(self):
        self.fre = self.var_entryFre.get()
        self.a = self.var_entryAmp.get()
        t = pl.linspace(0, 10/self.fre, self.fre*10000)
        y = self.a * (pl.cos(2*pi*self.fre*t ))
        pl.plot(t,y)

        pl.title("výkon")
        pl.xlabel("t[s]")
        pl.ylabel("u[V],i[A], p[W]")
        pl.show()

    def Zesouboru(self):
        f = open("soubor-win.txt", "r")
        x = []
        y = []
        while 1:
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

app = Application()
app.mainloop()