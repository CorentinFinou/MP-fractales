def vonKoch1(t,n,l):
        if n == 0 :
            t.forward(l)
        else :
            vonKoch1(t,n-1, l/3)
            t.left(60)
            vonKoch1(t,n-1, l/3)
            t.left(-120)
            vonKoch1(t,n-1, l/3)
            t.left(60)
            vonKoch1(t,n-1, l/3)