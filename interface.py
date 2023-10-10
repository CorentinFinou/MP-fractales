from tkinter import *
from turtle import *
from tkinter import colorchooser

def init():
    global t,fenetre,framePresets,fractaleIntermediateFctn,curseurOrdre,curseurRotation,curseurTaille,turtleColor,couleurButton
    def reset():
        global isClear
        curseurTaille.set(200)
        curseurOrdre.set(4)
        curseurRotation.set(0)
        t.clear()
        t.penup()
        t.goto(0,0)
        t.goto(turtleCanvas.winfo_screenmmwidth()/2,-turtleCanvas.winfo_screenmmwidth()/2)
        #print(turtleCanvas.winfo_screenmmwidth()/2,-turtleCanvas.winfo_screenmmwidth()/2)
        t.pendown()
        isClear = True
    #

    def getSourisPos(eventSpec):
        t.penup()
        t.goto(eventSpec.x-191,-eventSpec.y+134)#pas toucher, a tester sur plus grand écran
        t.pendown()
    
    def fractaleIntermediateFctn(nomFractale,n,l,r,c):
        global isClear
        if checkBoxClearBoolean.get() == True:
            if isClear == True:
                t.color(c)
                t.setheading(r)
                nomFractale(t,n,l)
                isClear = False
            else :
                reset()
                fractaleIntermediateFctn(nomFractale,n,l,r,c)
        else:
            t.color(c) 
            t.setheading(r)
            nomFractale(t,n,l)

    def choose_color():
        global turtleColor,couleurButton
        turtleColor = colorchooser.askcolor(title ="Choose color")[1]
        couleurButton.config(foreground=turtleColor)

    fenetre = Tk()
    fenetre.title("Fractales")
    fenetre.attributes("-fullscreen",True)
    isClear = True


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
    frctlActuelle = "Aucune fractale choisie"
    labelFrctlActuelle = Label(frameLabel, text=frctlActuelle, font="Arial 20", background="#7ea0b7").grid(row=1,sticky="NWE")
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



    #Boutons de presets (master = framePresets):
    #sierpinskiButton = Button(framePresets,text="Sierpinski",font="20",activebackground="#7ea0b7",background="#a9cef4",command= lambda: fractaleIntermediateFctn(sierpinski,curseurOrdre.get(),curseurTaille.get(),curseurRotation.get(),turtleColor)).grid(row=1,sticky="NSWE")
    #vonKoch1Button = Button(framePresets,text="VonKoch 1",font="20",activebackground="#7ea0b7",background="#a9cef4",command= lambda: fractaleIntermediateFctn(vonKoch1,curseurOrdre.get(),curseurTaille.get(),curseurRotation.get(),turtleColor)).grid(row=2,sticky="NSWE")
    #button3 = Button(framePresets,text="preset 3",activebackground="#7ea0b7",background="#a9cef4",font="20").grid(row=3,sticky="NSWE")
    #button4 = Button(framePresets,text="preset 4",activebackground="#7ea0b7",background="#a9cef4",font="20").grid(row=4,sticky="NSWE")
    #button5 = Button(framePresets,text="preset 5",activebackground="#7ea0b7",background="#a9cef4",font="20").grid(row=5,sticky="NSWE")
    resetButton = Button(framePresets,text="Reset",activebackground="#7ea0b7",background="#a9cef4",font="Arial 17",command=reset).grid(row=100,sticky="NSWE") #100 histoire d'être sûr que le bouton reset sera toujours en bas
    framePresets.grid_rowconfigure(100,weight=1)
    #for i in range (len(framePresets.winfo_children())-1):
        #framePresets.grid_rowconfigure(i+1,weight=1)
    #print(len(framePresets.winfo_children()))



    #FrameBarres
    frameBarres = Frame(frameConfig,highlightbackground="black", highlightthickness=1)
    frameBarres.grid(row=0,column=1,sticky="NSWE")
    frameBarres.grid_columnconfigure(0,weight=1)
    labelParamètres = Label(frameBarres, text="Paramètres :",font="Arial 40 bold",background="#a9cef4",foreground="#597081").grid(row=0,sticky="NSWE")



    #Barres (ou curseurs)

    #Ordre
    labelOrdre = Label(frameBarres, text="Ordre :").grid(row=2,sticky="NSWE")
    curseurOrdre = Scale(frameBarres,from_=1,to=6,orient="horizontal")
    curseurOrdre.grid(row=3,sticky="NSWE")
    curseurOrdre.set(4)
    labelTaille = Label(frameBarres,text="Taille :").grid(row=4,sticky="NSWE")
    curseurTaille = Scale(frameBarres,from_=10,to=300,orient="horizontal")
    curseurTaille.grid(row=5,sticky="NSWE")
    curseurTaille.set(200)
    labelRotation = Label(frameBarres,text="Rotation (antihoraire) :").grid(row=6,sticky="NSWE")
    curseurRotation = Scale(frameBarres,from_=0,to=360,orient="horizontal")
    curseurRotation.grid(row=7,sticky="NSWE")
    turtleColor = "black"
    couleurButton = Button(frameBarres, text="Couleur",command=choose_color,foreground=turtleColor,font="Arial 20")
    couleurButton.grid(row=8,sticky="NSWE")
    randomButton = Button(frameBarres, text="Random",font="Arial 20")
    randomButton.grid(row=9,sticky="NSWE")

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
    Button(framePresets,text=name,activebackground="#7ea0b7",background="#a9cef4",font="Arial 17",command= lambda: fractaleIntermediateFctn(fctn,curseurOrdre.get(),curseurTaille.get(),curseurRotation.get(),turtleColor)).grid(row=len(framePresets.winfo_children())-1,sticky="NSWE")
    framePresets.grid_rowconfigure(len(framePresets.winfo_children())-1,weight=1)

def start():
    fenetre.mainloop()