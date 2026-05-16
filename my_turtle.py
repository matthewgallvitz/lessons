import turtle
def make_square2(t):
    for i in range(4):
        t.forward(100)
        t.left(90)

def make_triangle(t):
    t.forward(100)
    t.right(120)
    t.forward(100)
    t.right(120)
    t.forward(100)

screen = turtle.Screen()
screen.bgcolor("white")

t = turtle.Turtle()
t.color("blue")
t.speed(1)

make_square2(t)
t.penup()
t.left(180)
t.forward(200)
input()
t.left(180)
t.pendown()
make_square2(t)
t.left(180)
input()
t.penup()
t.forward(100)
input()
t.pendown()

#make_square(t)

make_triangle(t)


turtle.done()