from turtle import Turtle,Screen, clearscreen, resetscreen

tim = Turtle()

def forward():
    tim.forward(15)
def backward():
    tim.backward(15)
def right():
    tim.right(15)
def left():
    tim.left(15)



screen = Screen()
screen.listen()
screen.onkey(fun=forward, key="w")
screen.onkey(fun=backward, key="s")
screen.onkey(fun=right, key="d")
screen.onkey(fun=left, key="a")
screen.onkey(fun=clearscreen, key="c")
screen.onkey(fun=resetscreen, key="c")
screen.exitonclick()