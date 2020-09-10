#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
PC02_GRAFFITI - ETHAN FRIER - GRAD - ETFR1107
Turtle starter code
ATLS 1300
Author: Dr. Z  - May 29, 2020
Author: Ethan Frier - Spetember 8, 2020
'''

from turtle import * #import the library of commands that you'd like to use

colormode(255)

# Create a panel to draw on. 
panel = Screen()
w = 743 # width of panel
h = 495 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======

t = Turtle() 
t.speed(10) 

# draw eyes
t.penup()
t.goto(-18,111)
t.pendown()
t.dot(10, "red")
t.penup()
t.goto(41,120)
t.pendown()
t.dot(10, "red")
t.penup()

# draw finger ray gun
t.goto(110, -90)
t.dot(10, "red")
t.setheading(350)
t.pendown()
t.pencolor(255, 0, 0)
t.pensize(10)
t.forward(100)
curPos = t.pos()
t.goto(curPos)
t.dot(20, "orange")
t.goto(110, -90)
t.dot(20, "orange")
t.setheading(350)
t.pendown()
t.pencolor(255, 165, 0)
t.pensize(20)
t.forward(100)
curPos = t.pos()
t.goto(curPos)
t.dot(30, "yellow")
t.goto(110, -90)
t.dot(30, "yellow")
t.setheading(350)
t.pendown()
t.pencolor(255, 255, 0)
t.pensize(30)
t.forward(100)
curPos = t.pos()

# draw moneyspolsion
t.goto(curPos)
t.color("green")
t.dot(50,)
t.dot(60)
t.dot(70)
t.dot(80)
t.dot(90)
t.dot(100)
t.dot(120)
t.dot(140)
t.dot(160)
t.dot(180)
t.dot(200)
t.dot(250)
t.dot(300)
t.dot(400)
t.dot(500)
t.dot(600)
t.dot(700)
t.dot(800)
t.dot(900)
t.dot(1000)

# re-draw eyes bigger
t.color("black")
t.penup()
t.goto(-18,111)
t.pendown()
t.dot(15, "red")
t.penup()
t.goto(41,115)
t.pendown()
t.dot(15, "red")
t.penup()
t.goto(-18,111)
t.pendown()
t.dot(25, "red")
t.penup()
t.goto(41,115)
t.pendown()
t.dot(25, "red")
t.penup()

# draw smile
t.goto(-10,50)
t.begin_fill()
t.fillcolor("red")
t.goto(40,55)
t.goto(35,45)
t.goto(18,37)
t.goto(-2,42)
t.goto(-10,50)
t.end_fill()
t.hideturtle()

done()

