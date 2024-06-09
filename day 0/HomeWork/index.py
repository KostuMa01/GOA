from turtle import *

penup()
goto(-100, -100)
pendown()

# Draw square
speed(100)
width(5)
for _ in range(4):
    forward(200)
    left(90)

# Draw door
begin_fill()
forward(70)
color("red")
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

#roof
penup()
goto(100, 100)
pendown()

begin_fill()
color("blue")
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#windows

exitonclick()
