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










wn.mainloop()
