from turtle import Turtle, Screen
screen= Screen()
screen.setup(width=500, height=400)
colors = ["red","orange","yellow","blue","purple","green"]
t1 =Turtle(shape="turtle")
t1.penup()
t1.goto(x=-230,y=-100)
t2=Turtle(shape="turtle")
t2.penup()
t2.goto(x=-230,y=-50)
t3=Turtle(shape="turtle")
t3.penup()
t3.goto(x=-230,y=0)
t4=Turtle(shape="turtle")
t4.penup()
t4.goto(x=-230,y=50)
t5=Turtle(shape="turtle")
t5.penup()
t5.goto(x=-230,y=100)
t6 = Turtle(shape="turtle")
t6.penup()
t6.goto(x=-230,y = 150)

screen= Screen()

userbet = screen.textinput("make your bet", "which turtle will win the race? (color)")
