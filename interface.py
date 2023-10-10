from tkinter import *
from turtle import *
from tkinter import colorchooser
from random import randint

def init():
    global t,fenetre,framePresets,fractaleIntermediateFctn,curseurOrdre,curseurRotation,curseurTaille,turtleColor,couleurButton,curseurWidth
    def reset():
        global isClear
        curseurTaille.set(200)
        curseurOrdre.set(4)
        curseurRotation.set(0)
        curseurWidth.set(1)
        t.clear()
        t.penup()
        t.goto(0,0)
        t.goto(turtleCanvas.winfo_screenmmwidth()/2,-turtleCanvas.winfo_screenmmwidth()/2)
        t.pendown()
        isClear = True

    def getSourisPos(eventSpec):
        t.penup()
        t.goto(eventSpec.x-191,-eventSpec.y+134)
        t.pendown()

    
    def fractaleIntermediateFctn(nomFractale,n,l,r,c,L):
        global isClear
        if checkBoxClearBoolean.get() == True:
            if isClear == True:
                try:
                    t.color(c)
                    t.setheading(r)
                    t.pensize(L)
                    nomFractale(t,n,l)
                    isClear = False
                except TypeError: #pour, si besoin, affichage de formes simples (sans variable ordre)
                    nomFractale(t,l)
                except : # c n'est parfois pas au bon format (rare) pour des raisons inconnues --> turtle.TurtleGraphicsError: bad color string:,           exception inconnue : pas de spécifaction a l'except, recommence tant que c est au bon format
                    print("Couleur au mauvais format, nouvelle tentative.")
                    c = "#"+hex(randint(0,2**24))[2:]
                    fractaleIntermediateFctn(nomFractale,n,l,r,c,L)
            else :
                t.clear()
                isClear = True
                fractaleIntermediateFctn(nomFractale,n,l,r,c,L)
        else:
            t.color(c) 
            t.setheading(r)
            t.pensize(L)
            nomFractale(t,n,l)

    def choose_color():
        global turtleColor,couleurButton
        turtleColor = colorchooser.askcolor(title ="Choose color")[1]
        print(turtleColor)
        couleurButton.config(foreground=turtleColor)

    def random():
        global turtleColor
        curseurTaille.set(randint(10,300))
        curseurOrdre.set(randint(1,10))
        curseurRotation.set(randint(0,360))
        curseurWidth.set(randint(1,10))
        turtleColor = "#"+hex(randint(0,2**24))[2:]

    fenetre = Tk()
    fenetre.title("Fractales")
    fenetre.attributes("-fullscreen",True)

    ###Frame 1###
    #Contient les labels et les commandes

    frame = Frame(fenetre,background="white",highlightbackground="black", highlightthickness=1)
    frame.grid(sticky="NSWE") #s'étendra dans toutes les directions (points cardinaux)

    #Définition des ratios de grandeurs
    fenetre.grid_columnconfigure(0,weight=1)
    fenetre.grid_columnconfigure(1,weight=2)
    fenetre.grid_rowconfigure(0,weight=1)
    frame.grid_columnconfigure(0,weight=1)
    frame.grid_rowconfigure(0,weight=1)
    frame.grid_rowconfigure(1,weight=2)

    #Label Fractale (master = frame)
    frameLabel = Frame(frame,background="#7ea0b7",highlightbackground="black", highlightthickness=1)
    frameLabel.grid(row=0,sticky="NSWE")
    labelTitre = Label(frameLabel, text="Fractales",font="Arial 30",background="#7ea0b7").grid(row=0,sticky="SWE")
    frameLabel.grid_columnconfigure(0,weight=1)
    frameLabel.grid_rowconfigure(0,weight=1)
    frameLabel.grid_rowconfigure(1,weight=1)



    ###Frame 2###

    #FrameConfig, contient les frames de presets et de barres de défilements (master = frame)
    frameConfig = Frame(frame,highlightbackground="black", highlightthickness=1)
    frameConfig.grid(row=1,sticky="NSWE")
    frameConfig.grid_columnconfigure(0,weight=1)
    frameConfig.grid_columnconfigure(1,weight=1)
    frameConfig.grid_rowconfigure(0,weight=1)

    #FramePresets, contients les boutons de presets (master = frameConfig)
    framePresets = Frame(frameConfig,background="#a9cef4",highlightbackground="black", highlightthickness=1)
    framePresets.grid(row=0,column=0,sticky="NSWE")
    framePresets.grid_columnconfigure(0, weight=1)
    labelPresets = Label(framePresets, text="Presets :",font="Arial 30 bold",background="#a9cef4",foreground="#597081").grid(row=0,sticky="NSWE")
    resetButton = Button(framePresets,text="Reset",activebackground="#7ea0b7",background="#a9cef4",font="Arial 17",command=reset).grid(row=100,sticky="NSWE") #100 histoire d'être sûr que le bouton reset sera toujours en bas
    framePresets.grid_rowconfigure(100,weight=1)



    #FrameBarres
    frameBarres = Frame(frameConfig,highlightbackground="black", highlightthickness=1)
    frameBarres.grid(row=0,column=1,sticky="NSWE")
    frameBarres.grid_columnconfigure(0,weight=1)
    labelParamètres = Label(frameBarres, text="Paramètres :",font="Arial 40 bold",background="#a9cef4",foreground="#597081").grid(row=0,sticky="NSWE")



    #Barres (ou curseurs)

    #Ordre
    labelOrdre = Label(frameBarres, text="Ordre :").grid(row=2,sticky="NSWE")
    curseurOrdre = Scale(frameBarres,from_=1,to=10  ,orient="horizontal")
    curseurOrdre.grid(row=3,sticky="NSWE")
    curseurOrdre.set(4)
    labelTaille = Label(frameBarres,text="Taille :").grid(row=4,sticky="NSWE")
    curseurTaille = Scale(frameBarres,from_=10,to=300,orient="horizontal")
    curseurTaille.grid(row=5,sticky="NSWE")
    curseurTaille.set(200)
    labelRotation = Label(frameBarres,text="Rotation (antihoraire) :").grid(row=6,sticky="NSWE")
    curseurRotation = Scale(frameBarres,from_=0,to=360,orient="horizontal")
    curseurRotation.grid(row=7,sticky="NSWE")
    labelWidth = Label(frameBarres,text="Largeur :").grid(row=8,sticky="NSWE")
    curseurWidth = Scale(frameBarres,from_=1,to=10,orient="horizontal")
    curseurWidth.grid(row=9,sticky="NSWE")
    curseurWidth.set(1)
    turtleColor = "black"
    couleurButton = Button(frameBarres, text="Couleur",command=choose_color,foreground=turtleColor,font="Arial 20")
    couleurButton.grid(row=10,sticky="NSWE")
    randomButton = Button(frameBarres, text="Random",font="Arial 20",command=random)
    randomButton.grid(row=11,sticky="NSWE")

    #CheckBox de Clear (master : frameBarres)
    checkBoxClearBoolean = BooleanVar()
    checkBoxClear = Checkbutton(frameBarres, text="Clear à chaque fois : ", variable=checkBoxClearBoolean,onvalue=True,offvalue=False)
    checkBoxClear.grid(row=1,sticky="NWE")
    checkBoxClear.select()#set la checkBox sur cochée de base



    #Frame Turtle
    turtleCanvas = Canvas(fenetre)
    turtleScreen = TurtleScreen(turtleCanvas)
    turtleCanvas.grid(row=0,column=1,sticky="NSWE")
    t = RawTurtle(turtleScreen)



    turtleCanvas.bind("<Button>",getSourisPos)

    t.speed('fastest')
    reset()


def add(fctn,name):
    Button(framePresets,text=name,activebackground="#7ea0b7",background="#a9cef4",font="Arial 17",command= lambda: fractaleIntermediateFctn(fctn,curseurOrdre.get(),curseurTaille.get(),curseurRotation.get(),turtleColor,curseurWidth.get())).grid(row=len(framePresets.winfo_children())-1,sticky="NSWE")
    framePresets.grid_rowconfigure(len(framePresets.winfo_children())-1,weight=1)

def start():
    fenetre.mainloop()