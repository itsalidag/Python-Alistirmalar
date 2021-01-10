from turtle import Turtle, Screen

tim = Turtle()
tim.speed(1)
tim.shape("turtle")
# TODO make turtle move with dashed lines.
# TODO draw üçgen, kare, 5 gen altıgane 7 gen 8gen
move = True
while move:
    for i in range(3):
        tim.pencolor("red")
        tim.right(120)
        tim.forward(80)
    for i in range(4):
        tim.pencolor("blue")
        tim.right(90)
        tim.forward(80)
    for i in range(5):
        tim.pencolor("yellow")
        tim.right(360/5)
        tim.forward(80)
    for i in range(6):
        tim.pencolor("green")
        tim.right(360/6)
        tim.forward(80)
    tim.write("I'm done boss. ", True, align="left")
    move = False




screen = Screen()
screen.exitonclick()
