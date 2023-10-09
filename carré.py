def carre(t,l) :
    for _ in range(4) :
        t.forward(l)
        t.left(90)

def imbrique(t,n,l) :
    if n > 0 :
        carre(t,l)
        t.penup() 
        t.forward(l//2) 
        t.left(45) 
        t.pendown()
        imbrique(t,n-1,l/2**0.5)