from turtle import *
import random

shape("turtle")
speed(0)
width(10)
bgcolor("orange")
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


def create_weirdcircle(sides, size, angle, sides_multiplier, turn_angle):
    penup()
    goto(random.randint(-200, 200), random.randint(-200, 200))
    pendown()
    for _ in range(sides * sides_multiplier):
        snowflake_side(size, sides)
        right(angle / sides)
    penup()
    right(turn_angle)
    # forward(size * 2)
    pendown()
# line_with_humps(100, 3, 30)

def weird_circle(sides, size, angle, sides_multiplier, turn_angle, loop_range):
    for i in range(loop_range):
        create_weirdcircle(sides, size, angle, sides_multiplier, turn_angle)
        print(i)

# spider circle
# weird_circle(3, 100, 200, 1, 90,35)
weird_circle(3,135,338,1,261,57)

size = random.randint(100,200)
angle = random.randint(1,360)
sides_multiplier = random.randint(1,10)
turn_angle = random.randint(200,400)
loop_range = random.randint(1,100)

print(f"size: {size} angle: {angle} sizes_multiplier: {sides_multiplier} turn_angle: {turn_angle} loop_range: {loop_range}")

# weird_circle(3, size, angle, sides_multiplier, turn_angle, loop_range)

mainloop()
