from turtle import *

x_axis = 120
y_axis = 120
# forward(50)

# goto(x_axis, y_axis)
# pendown()
# circle(100)

# circle(100 / 2, 180)
#x_coord = -800 OG
x_coord =-650
#y_coord = -400 OG
y_coord = -250
speed(0)
print(x_coord, y_coord)
radius_big = 110
radius_small = 30
penup()
goto(x_coord, y_coord)
pendown()
for n in range(3):
    penup()
    goto(x_coord, y_coord)
    pendown()
    for i in range(6):
        goto(x_coord, y_coord)
        circle(radius_big / 2, 180)
        circle(radius_big)
        goto(x_coord, y_coord)
        circle(radius_small / 2, 180)
        circle(radius_small)
        #x_coord += 250
    y_coord += 250
    x_coord = -800


# goto(x_axis, y_axis*1.7)
done()
