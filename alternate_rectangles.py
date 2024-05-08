import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a Turtle object
t = turtle.Turtle()
t.speed(5)
t.color("blue")

# Function to draw a rectangle
def draw_rectangle(width, height):
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)

# draw vertical rectangles
rectangle_width = 20
rectangle_height = 110
for _ in range(5):
    draw_rectangle(rectangle_width, rectangle_height)
    t.penup()
    t.forward(rectangle_width+7)  # Move to the right for the next rectangle
    t.pendown()

# Move to draw vertically
t.penup()
t.goto(0, -120)  # Position to start drawing vertically
t.pendown()

# Draw 3 rectangles horizontally
rectangle_width = 130
rectangle_height = 20
for _ in range(3):
    draw_rectangle(rectangle_width, rectangle_height)
    t.penup()
    t.forward(0)  # Stay in the same column
    t.right(90)
    t.forward(rectangle_height+7)  # Move down for the next rectangle
    t.left(90)
    t.pendown()

# Hide the turtle and display the result
t.hideturtle()
screen.exitonclick()
