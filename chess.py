import turtle
c = turtle.Turtle()

def draw():
    for i in range(4):
        c.forward(30)
        c.left(90)
    c.forward(30)

if __name__=="__main__":
    c.speed(100)
    for i in range(8):
        c.up()
        c.setpos(-100,30*i)
        c.down()
        for j in range(8):
            if(i+j)%2 == 0:
                col = "Black"

            else:
                col ="white"
            c.fillcolor(col)
            c.begin_fill()
            draw()
            c.end_fill()
    c.hideturtle()
    turtle.done()
        
