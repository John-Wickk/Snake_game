import turtle
import time
import random

delay = 0.1

#score
score = 0
high_score = 0

#set up the screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0) # turns off the screen updates

# snake head
head = turtle.Turtle()
head.speed(0)
head.shape('circle')
head.color('green')
head.penup()
head.goto(0,0)
head.direction = 'stop'

#snake food

food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
food.goto(0,100)

# function
def go_up():
    if head.direction !="down":
        head.direction = "up"

def go_down():
    if head.direction !="up":
        head.direction = "down"

def go_left():
    if head.direction !="right":
        head.direction = "left"

def go_right():
    if head.direction !="left":
        head.direction = "right"


def move():
    if head.direction =='up':
        y=head.ycor()
        head.sety(y + 20)
    if head.direction =='down':
        y=head.ycor()
        head.sety(y - 20)
    if head.direction =='left':
        x=head.xcor()
        head.setx(x - 20)
    if head.direction =='right':
        x=head.xcor()
        head.setx(x + 20)

# keyword bindings
wn.listen()
wn.onkeypress(go_up, 'w')
wn.onkeypress(go_down, 's')
wn.onkeypress(go_left, 'a')
wn.onkeypress(go_right, 'd')



segments = []

#pen

pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("score: 0 high score: 0", align="center", font=('courier', 25, "normal"))










wn.mainloop()
