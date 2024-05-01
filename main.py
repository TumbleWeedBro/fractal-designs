from turtle import *

shape("turtle")
speed(0)


def pattern(size, levels, angle):
    if levels ==0:
        return
    forward(size)
    right(angle)

    pattern(size * 0.8, levels - 1, angle)

    left(angle * 2)

    pattern(size * 0.8, levels - 1, angle)

    right(angle)
    backward(size)


pattern(200, 10, 60)
mainloop()
