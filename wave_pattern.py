import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(0)  # Set the drawing speed to the fastest
screen = turtle.Screen()

screen.bgcolor("orange")

# Function to draw a circle with a given radius
def draw_circle(radius):
    t.circle(radius, 180)

# Draw 5 circles in a row
num_circles = 20  # Adjust the number of circles as needed
radius = 50  # Adjust the radius of the circles as needed
x_coord = -800
y_coord = 200
headT = 90  # Initial heading
t.pensize(10)


def wave(headT):
    for i in range(2):
        t.penup()
        t.goto(x_coord, y_coord)
        t.pendown()
        if i % 2 == 0:
            headT *= -1  # Reverse the heading every other circle
        else:
            headT *= -1
        t.setheading(headT)

        draw_circle(radius)
        t.penup()
        t.forward(radius * 2)  # Move forward to prepare for the next circle
        t.pendown()


for _ in range(6):

    if _ % 3 == 0:
        t.pencolor("red")
    elif _ % 3 == 1:
        t.pencolor("green")
    elif _%3 == 2:
         t.pencolor("black")
    y_coord += 12
    x_coord = -800
    for _ in range(5):
        wave(headT)
        x_coord += 200
    # Hide the turtle and display the result
t.hideturtle()
turtle.done()
