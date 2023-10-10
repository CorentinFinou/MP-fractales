def dragoncurve(t,n,l):
    n=n*2
    l = l/10
    def x(n):
        if n==0:
            return
        x(n-1)
        t.right(90)
        y(n-1)
        t.forward(l)
    def y(n):
        if n==0:
            return
        t.forward(l)
        x(n-1)
        t.left(90)
        y(n-1)
    t.fd(l)
    x(n)