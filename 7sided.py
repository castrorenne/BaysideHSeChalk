import turtle

boo = turtle.Turtle()
boo.speed(0)

for y in ['red','blue','green','cyan','magenta']:
    boo.fillcolor(y)
    for x in range(7):
        boo.begin_fill()
        boo.forward(100)
        boo.right(360 / 7)
        boo.pensize(x)
        boo.end_fill()
    boo.left(360 / 5)
    

turtle.done()
