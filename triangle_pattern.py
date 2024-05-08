import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a Turtle object
afro_turtle = turtle.Turtle()
afro_turtle.speed(0)
afro_turtle.color("yellow")

# Use afro_turtle consistently for penup and pendown operations
x_coord = -800
y_coord = 200
afro_turtle.penup()
afro_turtle.goto(x_coord, y_coord)
afro_turtle.pendown()

# Function to draw a triangle
def draw_triangle(size, color, direction):
    afro_turtle.color(color)
    afro_turtle.begin_fill()
    if direction == 'up':
        for _ in range(3):
            afro_turtle.forward(size)
            afro_turtle.right(120)
    elif direction == 'down':
        for _ in range(3):
            afro_turtle.forward(size)
            afro_turtle.left(120)
    afro_turtle.end_fill()

# Draw multiple rows of alternating triangles
def draw_alternating_triangles():
    colors = ["red", "blue", "green"]
    size = 50

    for row_index in range(10):
        for col_index in range(10):
            if row_index % 2 == 0:
                draw_triangle(size, colors[col_index % 3], 'up')
            else:
                draw_triangle(size, colors[col_index % 3], 'down')
            afro_turtle.penup()
            afro_turtle.forward(size * 1.5)
            afro_turtle.pendown()

        afro_turtle.penup()
        if row_index % 2 == 0:
            afro_turtle.goto(x_coord + 30, afro_turtle.ycor() - size * 2 + 40)
        else:
            afro_turtle.goto(x_coord, afro_turtle.ycor() - size * 2 + 40)
        afro_turtle.pendown()

# Call the draw_alternating_triangles function to draw rows of triangles
draw_alternating_triangles()

# Hide the turtle and display the result
afro_turtle.hideturtle()
screen.exitonclick()
