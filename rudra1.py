import turtle
import random
import time

# Set up the screen
screen = turtle.Screen()
screen.title("RUDHRA Logo")
screen.bgcolor("black")
screen.tracer(0)  # Disable automatic screen updates for smoother animation

# Create a turtle for background animation
bg_turtle = turtle.Turtle()
bg_turtle.speed(0)
bg_turtle.hideturtle()

# Animate a dynamic background pattern with rotating circles
colors = ["red", "blue", "green", "yellow", "purple", "orange"]
for i in range(100):
    bg_turtle.color(random.choice(colors))
    bg_turtle.circle(100 + i)  # Increasing circle size for a spiral effect
    bg_turtle.right(10)
    screen.update()
    time.sleep(0.05)

# Create a turtle for animating the logo text
logo_text = "RUDHRA"
logo_turtle = turtle.Turtle()
logo_turtle.hideturtle()
logo_turtle.color("white")
logo_turtle.penup()
logo_turtle.goto(0, -50)

# Animate the text appearance letter by letter
for i in range(1, len(logo_text) + 1):
    logo_turtle.clear()
    logo_turtle.write(logo_text[:i], align="center", font=("Arial", 48, "bold"))
    time.sleep(0.5)

# Keep the window open until it is closed by the user
screen.mainloop()
