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

def flocon(t,n,l) :
	for _ in range(3) :
		vonKoch(t,n,l)
		t.left(-120)