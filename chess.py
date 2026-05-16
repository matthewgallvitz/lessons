import turtle
def cube(t):
    t.penup()
    t.left(145)
    t.forward(450)
    t.right(145)
    t.pendown()
def make_square1(t):
    for i in range(4):
        t.forward(size_of_square)
        t.left(90)
def make_pair_of_square(t, should_first_square_be_filled = True):
    if should_first_square_be_filled == True:
        t.begin_fill()
        make_square1(t)
        t.end_fill()
        t.forward(size_of_square)
        make_square1(t)
    else:
        make_square1(t)
        t.forward(size_of_square)
        t.begin_fill()
        make_square1(t)
        t.end_fill()

def draw_row(t, should_first_square_be_filled = True):
    for i in range(number_pair):
        make_pair_of_square(t, should_first_square_be_filled )
        t.forward(size_of_square)
#8x8 board for the chess set
screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()
t.color("blue")
t.speed(7)
cube(t)

number_pair = 4

size_of_square = 100

distance_back = size_of_square * number_pair *2

for i in range(8):
    is_even = i % 2== 0
    draw_row(t, is_even )
    t.backward(distance_back)
    t.right(90)
    t.forward(size_of_square)
    t.left(90)

    is_even = i % 2== 0


    print(i)

turtle.done()