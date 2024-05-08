from turtle import *
import random

shape("turtle")
speed(0.1)
width(5)
bgcolor("black")
goto(0,0)
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

# first shape
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


def create_snowflake(sides, length):
    # normal snowflake
    for _ in range(sides):
        snowflake_side(length, sides)
        right(360 / sides)
# create a snowflakes
# create_snowflake(3,100)

def create_weirdcircle(sides, size, angle, sides_multiplier, turn_angle):
    penup()
    # goto(random.randint(-200, 200), random.randint(-200, 200))
    pendown()
    for _ in range(sides * sides_multiplier):
        snowflake_side(size, sides)
        right(angle / sides)
    penup()
    right(turn_angle)
    forward(size * 2)
    pendown()
# line_with_humps(100, 3, 30)


def weird_circle(sides, size, angle, sides_multiplier, turn_angle, loop_range):
    for i in range(loop_range):

        create_weirdcircle(sides, size, angle, sides_multiplier, turn_angle)
        print(i)

# ndivhu weird circle
def nd_weird_circle(sides, size, angle, sides_multiplier, turn_angle,
                    loop_range, x, y):
    penup()
    goto(x, y)
    pendown()
    begin_fill()
    fillcolor("red")
    circle(size*0.8)
    end_fill()
    for i in range(loop_range):
        begin_fill()
        if i % 2 == 0:
            fillcolor("purple")

        create_weirdcircle(sides, size, angle, sides_multiplier, turn_angle)
        end_fill()
        print(i)


# spider circle
# penup()
# goto(0, -150)
# pendown()
# weird_circle(2, 90, 200, 1, 90,38)
# other weird circle
# weird_circle(2, 200, 50, 1, 90, 19)

# Main program
if __name__ == "__main__":

    x = 130
    y = 150
    x_axis = 0
    y_at_axis = 0
    circles = 0
    while circles < 3:

        for i in range(5):
            penup()
            if i == 0:
                goto(x_axis+30, y_at_axis+20)
                nd_weird_circle(1, 60, 50, 1, 90, 19, x_axis, y_at_axis)
                weird_circle(1, 60, 50, 1, 90, 19)
            else:
                if i % 2 == 0:
                    y *= -1
                else:
                    x *= -1
                goto(x, y)
                pendown()
                nd_weird_circle(1, 40, 50, 1, 90, 19, x, y)
                weird_circle(1, 40, 50, 1, 90, 19)  
        circles += 1
        x += 50
        y += 100
        x_axis += 200


# weird_circle(3,135,338,1,261,57)

# size = random.randint(100,200)
# angle = random.randint(1,360)
# sides_multiplier = random.randint(1,10)
# turn_angle = random.randint(200,400)
# loop_range = random.randint(1,100)

# print(f"size: {size} angle: {angle} sizes_multiplier: {sides_multiplier} turn_angle: {turn_angle} loop_range: {loop_range}")

# weird_circle(3, size, angle, sides_multiplier, turn_angle, loop_range)

mainloop()
