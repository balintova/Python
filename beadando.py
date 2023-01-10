import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import Canvas
import csv
import json


class Beadando:
    def __init__(self):
        #konstruktor, fő elemek felpakolása az ablakra
        self.tkinterAblak = tk.Tk()
        self.tkinterAblak.geometry('1200x800')
        self.tkinterAblak.resizable(width=False, height=False)
        self.tkinterAblak.title('Szabó Bálint Beadandó')
        #json beolvasó gomb - 0.sor
        self.jsonBeolvasoGomb = tk.Button(self.tkinterAblak, text="JSON beolvasása", command=self.jsonBeolvasas).grid(row=0, column=0)
        #csv beolvasó gomb - 1.sor
        self.csvBeolvasoGomb = tk.Button(self.tkinterAblak, text="CSV beolvasása", command=self.csvBeolvasas).grid(row=0, column=1)
        #a munkafelület ahová az adatokat rajzoljuk ki, ezt mindig reseteljük új betöltés előtt - 2.sor
        self.canvas = Canvas(self.tkinterAblak)
        self.canvas.grid(row=1)
        
        
    def jsonBeolvasas(self):
        # fájl elérési útvonalának bekérése
        fajlnev = askopenfilename()
        # fájl bináris tartalmának betöltése
        f = open(fajlnev)
        
        # fájl json-né konvertálása
        adat = json.load(f)
        # fájl olvasás lezárása
        f.close()
        # canvas tartalmának ürítése és új létrehozása
        self.canvas.destroy()
        self.canvas = Canvas(self.tkinterAblak)
        self.canvas.grid(row=1)
        # json objektum olvasható formába konvertálása
        szoveg = json.dumps(adat, indent=2)
        # scrollbar létrehozása
        self.sb = tk.Scrollbar(self.canvas)
        # json berakása text-ként
        self.txt = tk.Text(self.canvas, font="Times32")
        self.txt.grid(row=0)
        # scrollbar beállítása hogy y tengelyen görgethető legyen
        self.txt.config(yscrollcommand=self.sb.set)
        # scrollbar text elemhez kötése
        self.sb.config(command=self.txt.yview)

        # text végének beállítása a szöveg hosszára, hogy ne lehessen végtelenségig görgetni, ha már nincs tartalom
        self.txt.insert('end', szoveg)

    def csvBeolvasas(self):
        fajlnev = askopenfilename()
        #canvas ürítése
        self.canvas.destroy()
        self.canvas = Canvas(self.tkinterAblak)
        self.canvas.grid(row=1)
        # fájl megnyitása read módban
        with open(fajlnev, "r", newline="") as fajl:
            #csv readbe betöltjük a fájl tartalmát
            reader = csv.reader(fajl)
            # lista nétrehozása a beolvasott tartalomból
            csvAdat = list(reader)
        
        # beolvasott listán iterálunk
        for sorszam, sor in enumerate(csvAdat, start=0):
            #minden elem egy sor, azokon is iterálni kell, így dupla iterációt használunk
            for cellaszam, cella in enumerate(sor):
                # whitesapcek leszedése
                ertek = cella.strip()
                # első elem a fejléc ezt külön kell kezelni
                if sorszam == 0:
                    tk.Label(self.canvas, text=ertek).grid(row=2, column=cellaszam, padx=40)
                else:
                    #minden más sornál csak simán kirajzoljuk a következő sorba és cellába az értéket
                    tk.Label(self.canvas, text=ertek).grid(row=sorszam+2, column=cellaszam)
            


    def inditas(self):
        self.tkinterAblak.mainloop()


# name == main vizsgálata, hogy csak akkor fusson le ha szkriptként van indítva a fájl
if __name__ == '__main__':
    alkalmazas = Beadando()
    alkalmazas.inditas()