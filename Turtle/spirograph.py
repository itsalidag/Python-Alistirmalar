import turtle as t

tim = t.Turtle()

tim.speed("fastest")
for i in range(100):
    tim.circle(100)
    tim.setheading(tim.heading()+ 30)
    


screen = t.Screen()
screen.exitonclick()