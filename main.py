from turtle import *
screen = Screen()
screen.setworldcoordinates(-1200,-800,800,800)
screen.bgcolor("black")
x_axis = 120
y_axis = 120
# forward(50)
# goto(0,0)
# goto(800,600)

# goto(x_axis, y_axis)
# pendown()
# circle(100)

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

# ndivhu weird circle
def nd_weird_circle(sides, size, angle, sides_multiplier, turn_angle,
                    loop_range):
    penup()
    pendown()
    begin_fill()
    fillcolor("red")
    circle(size*0.8)
    end_fill()
    for i in range(loop_range):
        begin_fill()
        if i % 2 == 0:
            fillcolor("#4e6e81")

        create_weirdcircle(sides, size, angle, sides_multiplier, turn_angle)
        end_fill()
        print(i)


# circle(100 / 2, 180)
#x_coord = -800 OG
#x_coord =-750
x_coord = -12000
#y_coord = -400 OG
y_coord = -800

speed(0)
print(x_coord, y_coord)
radius_big = 210
radius_small = 45
penup()
goto(x_coord, y_coord)
pendown()
counter = 0
for n in range(5):
    penup()
    x_coord = -1800
    goto(x_coord, y_coord)
    pendown()
    for i in range(0,15,1):
        print(i)
        if counter == 0:
            penup()
            goto(x_coord, y_coord)
            pendown()
            begin_fill()
            fillcolor("#480607")
            circle(radius_big / 2, 180)
            circle(radius_big)
            end_fill()
            penup()
            goto(x_coord, y_coord)

            circle(radius_small / 2, 180)
            pendown()
            nd_weird_circle(1, radius_big/2.1, 50, 1, 90, 19)
            counter += 1
            penup()
        else:
            counter -= 1
        x_coord += 250
        # if i % 2 != 0:
        #     x_coord += 250
        # else :
        #     x_coord += 250
        

    y_coord += 650
    #x_coord = -800 OG
    #x_coord =-750
    x_coord =-100



# goto(x_axis, y_axis*1.7)
done()
