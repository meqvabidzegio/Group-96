from turtle import *


#we want to paint a house

#step 1: draw a square
speed(20)

width(7)
color("orange")
forward (200)
left(90)

forward (200)
left(90)

forward (200)
left(90)

forward (200)
left(90)
#end of square

#drawing a door

forward(70)
color("brown")
left(90)
forward(90)     #height of the door
right(90)
forward(60) 
right(90)
forward(90)

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()


penup()
goto(200, 170)
pendown()
color("orange")
right(60)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
penup()
goto(0, 0)
pendown()
left(90)
forward(120)
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
right(180)
forward(25)
right(90)
forward(50)
penup()
goto(0, 0)
pendown()
left(180)
forward(145)
right(90)
forward(50)
penup()
forward(100)
pendown()
forward(50)
left(90)
forward(25)
left(90)
forward(25)
left(90)
forward(50)
penup()
goto(0, 0)
exitonclick()     