from turtle import *

shape("turtle")
speed(0)

def pattern(size, levels, angle):
    if levels ==0:
        return
    forward(size)
    right(angle)

    pattern(size*0.9, levels - 1, angle)

    left(angle * 2)

    pattern(size*0.9 , levels - 1, angle)

    right(angle)
    backward(size)


def move():
    left(90)
    for i in range(4):
        left(90)
        pattern(40, 5, 60)

    penup()
    for i in range(4):
        forward(60)
    pendown()

for i in range(4):
    move()

mainloop()
