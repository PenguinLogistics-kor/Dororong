import turtle
import random
import time

screen = turtle.Screen()
screen.title("달리기 경기")
screen.bgcolor("white")

turtle.register_shape("dororong.gif")
turtle.register_shape("scarlet.gif")

track = turtle.Turtle()
track.speed(0)
track.penup()
track.goto(-120, 40)
track.pendown()
track.forward(240)
track.penup()
track.goto(-120, -40)
track.pendown()
track.forward(240)

track.penup()
track.goto(0, 40)
track.right(90)
track.pendown()
track.forward(80)
track.hideturtle()

t1 = turtle.Turtle()
t1.shape("dororong.gif")  
t1.penup()
t1.goto(-120, 20)

t2 = turtle.Turtle()
t2.shape("scarlet.gif")  
t2.penup()
t2.goto(-120, -20)

while t1.xcor() < 120 and t2.xcor() < 120:
    t1.forward(random.randint(1, 5))
    t2.forward(random.randint(1, 5))
    time.sleep(0.05)

winner = None
if t1.xcor() >= 120 and t2.xcor() >= 120:
    winner = "무승부!"
elif t1.xcor() >= 120:
    winner = "도로롱 승!"
else:
    winner = "홍북이 승!"
    
result = turtle.Turtle()
result.hideturtle()
result.penup()
result.goto(0, 60)
result.write(winner, align="center", font=("Arial", 16, "bold"))

turtle.done()
