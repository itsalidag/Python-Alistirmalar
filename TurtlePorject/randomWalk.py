import turtle as t
import random

colors = ["light pink","wheat","lavender","dark sea green","gainsboro","powder blue","brown","navajo white"]
tim = t.Turtle()
tim.hideturtle()
tim.pensize(10)
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)
#TODO move 50, rotate random (90,0,270) move 50 again.
for i in range(15):
    ancles = [0,90,180,270]
    pos = random.choice(ancles)
    tim.color(random_color())
    tim.setheading(random.choice(ancles))
    tim.forward(50)

screen= t.Screen()
screen.exitonclick()