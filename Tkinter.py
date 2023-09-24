from tkinter import *
from turtle import *


############################################## Module Turtle ##############################################

###Définition des fonctions turtle###
frctlActuelle = "Aucune fractale choisie"
def reset():
    global isClear
    t.clear()
    t.penup()
    t.goto(390,-405)
    t.pendown()
    isClear = True


def sierpinski(n, l):
        if n == 0: 
            for _ in range(3):
                t.forward(l)
                t.left(120)
        else:
            l /= 2.0
            sierpinski(n - 1, l)  
            t.forward(l)
            sierpinski(n - 1, l)  
            t.backward(l)
            t.left(60)
            t.forward(l)
            t.right(60)
            sierpinski(n - 1, l)  
            t.left(60)
            t.backward(l)
            t.right(60)

def sierpinskiNonRec(n,l):
    global isClear
    if checkBoxClearBoolean.get() == True:
        if isClear == True:
            sierpinski(n,l)
            isClear = False
        else :
            reset()
            sierpinskiNonRec(n,l)
    else:
        sierpinski(n,l)
        


def vonKoch1(n,l):
    global isClear
    if isClear == True :
        if n == 0 :
            t.forward(l)
        else :
            vonKoch1(n-1, l/3)
            t.left(60)
            vonKoch1(n-1, l/3)
            t.left(-120)
            vonKoch1(n-1, l/3)
            t.left(60)
            vonKoch1(n-1, l/3)
    else :
        reset()
        isClear = True
        vonKoch1(n,l)

############################################## Module tkinter ##############################################

###Fenetre principale
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
labelFrctlActuelle = Label(frameLabel, text=frctlActuelle, font="Arial 20", background="#7ea0b7").grid(row=1,sticky="NWE")
frameLabel.grid_columnconfigure(0,weight=1)
frameLabel.grid_rowconfigure(0,weight=1)
frameLabel.grid_rowconfigure(1,weight=1)



###Frame 2###

#FrameConfig, contient les frames de presets et de barres de défilements (master = frame)
frameConfig = Frame(frame,highlightbackground="black", highlightthickness=1)
frameConfig.grid(row=1,sticky="NSWE")
frameConfig.grid_columnconfigure(0,weight=0)
frameConfig.grid_columnconfigure(1,weight=1)
frameConfig.grid_rowconfigure(0,weight=1)

#FramePresets, contients les boutons de presets (master = frameConfig)
framePresets = Frame(frameConfig,background="#a9cef4",highlightbackground="black", highlightthickness=1)
framePresets.grid(row=0,column=0,sticky="NSWE")
framePresets.grid_columnconfigure(0, weight=1)
labelPresets = Label(framePresets, text="Presets :",font="Arial 30 bold",background="#a9cef4",foreground="#597081").grid(row=0,sticky="NSWE")



#Boutons de presets (master = framePresets):
sierpinskiButton = Button(framePresets,text="Sierpinski",font="20",activebackground="#7ea0b7",width=40,background="#a9cef4",command= lambda: sierpinskiNonRec(3,200)).grid(row=1,sticky="NS")
vonKoch1Button = Button(framePresets,text="VonKoch 1",font="20",activebackground="#7ea0b7",width=40,background="#a9cef4",command= lambda: vonKoch1(3,200)).grid(row=2,sticky="NS")
button3 = Button(framePresets,text="preset 3",activebackground="#7ea0b7",width=40,background="#a9cef4",font="20").grid(row=3,sticky="NS")
button4 = Button(framePresets,text="preset 4",activebackground="#7ea0b7",width=40,background="#a9cef4",font="20").grid(row=4,sticky="NS")
button5 = Button(framePresets,text="preset 5",activebackground="#7ea0b7",width=40,background="#a9cef4",font="20").grid(row=5,sticky="NS")
resetButton = Button(framePresets,text="Reset",activebackground="#7ea0b7",width=40,background="#a9cef4",font="20",command=reset).grid(row=6,sticky="NS")
for i in range (len(framePresets.winfo_children())-1):
    framePresets.grid_rowconfigure(i+1,weight=1)
#print(len(framePresets.winfo_children()))



#FrameBarres
frameBarres = Frame(frameConfig,highlightbackground="black", highlightthickness=1)
frameBarres.grid(row=0,column=1,sticky="NSWE")
frameBarres.grid_columnconfigure(0,weight=1)

#CheckBox de Clear (master : frameBarres)
checkBoxClearBoolean = BooleanVar()
checkBoxClear = Checkbutton(frameBarres, text="Clear à chaque fois : ", variable=checkBoxClearBoolean,onvalue=True,offvalue=False,)
checkBoxClear.grid(row=0,sticky="NSWE")
checkBoxClear.select()#set la checkBox sur cochée de base


#Frame Turtle
turtleCanvas = Canvas(fenetre)
turtleCanvas.grid(row=0,column=1,sticky="NSWE")
t = RawTurtle(turtleCanvas)










t.speed('fastest')
reset()


fenetre.mainloop()