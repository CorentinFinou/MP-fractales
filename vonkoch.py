def vonKoch(t,n,l):
        if n == 0 :
            t.forward(l)
        else :
            vonKoch(t,n-1, l/3)
            t.left(60)
            vonKoch(t,n-1, l/3)
            t.left(-120)
            vonKoch(t,n-1, l/3)
            t.left(60)
            vonKoch(t,n-1, l/3)