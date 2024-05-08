import turtle

screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(0)
t.pensize(20)
colors = ["red", "blue"]

def draw_rectangle(side_length, color):
    t.color(color)
    for _ in range(4):
        t.forward(side_length)
        t.right(90)

def draw_nested_square(num_rectangles, side_length):
    for i in range(num_rectangles):
        draw_rectangle(side_length, colors[i % len(colors)])
        t.penup()
        t.goto(t.xcor() + 20, t.ycor() - 20)
        t.pendown()
        side_length -= 40

def draw_multiple_nested_squares(num_patterns, num_rectangles, side_length, spacing, num_rows):
    start_x = t.xcor()
    y_coordinate = -300
    for _ in range(num_rows):
        y_coordinate += 100
        for _ in range(num_patterns):
            draw_nested_square(num_rectangles, side_length)
            t.penup()
            t.goto(start_x + side_length + spacing, y_coordinate)
            t.pendown()
            start_x = t.xcor()

num_rows = 2
num_patterns = 4
num_rectangles = 5
side_length = 200
spacing = 10

total_width = (num_patterns * side_length) + ((num_patterns - 1) * spacing)
start_x = -(total_width / 2)

t.penup()
t.goto(start_x, 0)
t.pendown()

draw_multiple_nested_squares(num_patterns, num_rectangles, side_length, spacing, num_rows)
screen.exitonclick()
