def sierpinski(t,n, l):
        if n == 0: 
            for _ in range(3):
                t.forward(l)
                t.left(120)
        else:
            l /= 2.0
            sierpinski(t,n - 1, l)  
            t.forward(l)
            sierpinski(t,n - 1, l)  
            t.backward(l)
            t.left(60)
            t.forward(l)
            t.right(60)
            sierpinski(t,n - 1, l)  
            t.left(60)
            t.backward(l)
            t.right(60)