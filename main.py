from turtle import *

shape("turtle")
speed(5)
width(10)
bgcolor("orange")
# color("orange")
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

# for i in range(4):
#     move()

width(2)
def line_with_humps(size, level, angle):
    if level == 0:
        return
    forward(size / 3)
    left(angle)
    forward(size / 3)
    right(angle * 2)
    forward(size / 3)
    left(angle)
    forward(size / 3)

    line_with_humps(size, level-1, angle)


def snowflake_side(length, levels):
    if levels == 0:
        forward(length)
        return
    length /= 3
    snowflake_side(length, levels - 1)
    left(60)
    snowflake_side(length, levels - 1)
    right(120)
    snowflake_side(length, levels - 1)
    left(60)
    snowflake_side(length, levels - 1)



# line_with_humps(100, 3, 30)

snowflake_side(200, 2)
mainloop()
