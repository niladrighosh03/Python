import turtle

# Set up the screen
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("white")

# Create a turtle for drawing
pen = turtle.Turtle()
pen.speed(2)
pen.color("blue")
pen.pensize(3)

# Draw the face
pen.up()
pen.goto(0, -100)
pen.down()
pen.circle(100)

# Draw the eyes
pen.up()
pen.goto(-40, 40)
pen.down()
pen.circle(15)
pen.up()
pen.goto(40, 40)
pen.down()
pen.circle(15)

# Draw the nose
pen.up()
pen.goto(0, 10)
pen.down()
pen.right(90)
pen.forward(30)

# Draw the mouth
pen.up()
pen.goto(-40, -40)
pen.down()
pen.circle(40, 180)

# Draw the beard
pen.up()
pen.goto(-60, -100)
pen.down()
pen.goto(60, -100)

# Write Dhoni's name
pen.up()
pen.goto(-80, 150)
pen.down()
pen.write("MS Dhoni", font=("Arial", 16, "bold"))

# Hide the turtle
pen.hideturtle()

# Exit on click
turtle.done()
