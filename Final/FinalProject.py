import turtle
turtle.speed(0)

screen = turtle.Screen()
screen.bgcolor("#89CFF0")


rightwing = 0
while rightwing < 2:
    turtle.forward(140)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    rightwing = rightwing+ 1

turtle.right(100)
turtle.forward(160)
#horrizontal stabilzer
turtle.left(95)
turtle.forward(80)
turtle.right(85)
#elevator
for i in range(1):
    turtle.forward(17.5)
    turtle.right(90)
    turtle.pensize(3)
    turtle.forward(190)
    turtle.backward(190)
    turtle.left(90)
    turtle.pensize(1)
    turtle.forward(17.5)
#VOR
turtle.right(85)
turtle.forward(95)
turtle.left(135)
turtle.forward(20)
turtle.backward(20)
#RUDDER
turtle.right(135)
turtle.left(85)
turtle.pensize(3)
turtle.color("Red")
turtle.forward(35)
turtle.backward(55)
for i in range(1):
    turtle.left(45)
    turtle.backward(35)
    turtle.forward(35)
for i in range(1):
    turtle.right(90)
    turtle.backward(35)
    turtle.forward(35)
    turtle.left(45)


turtle.forward(20)
turtle.color("Black")
turtle.pensize(1)

turtle.right(85)
turtle.left(45)
turtle.forward(20)
turtle.backward(20)
turtle.right(45)
turtle.right(10)
turtle.forward(95)
turtle.right(85)
turtle.forward(35)
turtle.right(85)
turtle.forward(80)
turtle.left(95)
turtle.forward(160)
turtle.left(80)

leftwing = 0
while leftwing < 2:
    turtle.forward(140)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    leftwing = leftwing+ 1


turtle.right(90)
turtle.pensize(3)
turtle.begin_fill()
for i in range(2):
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(130)
    turtle.left(90)
    #flapL = flapL + 1
turtle.end_fill()
turtle.pensize(1)

turtle.left(90)
turtle.forward(155)
for i in range(1):
    turtle.right(5)
    turtle.forward(160)
    turtle.right(85)
    turtle.forward(85)
    turtle.right(90)
    turtle.forward(174)
    turtle.right(90)
    turtle.penup()
    turtle.forward(100)
    turtle.pendown()

turtle.right(95)
turtle.forward(10)
turtle.right(85)
#alieronL
turtle.pensize(3)
for i in range(2):
    turtle.forward(30)
    turtle.left(85)
    turtle.forward(155)
    turtle.left(95)

turtle.pensize(1)
turtle.right(95)
turtle.forward(10)
turtle.left(5)
turtle.forward(140)
turtle.left(90)
turtle.penup()
turtle.forward(100)
turtle.pendown()
turtle.forward(100)

#powerplant starts here
turtle.right(85)


turtle.forward(42.5)
#angle of start of engine

turtle.left(85)
turtle.forward(10)
turtle.left(90)
turtle.forward(70)
#prop

turtle.right(90)
turtle.forward(8)
turtle.right(90)
turtle.forward(70)
#right turn to prop then spinner


turtle.left(70)
#first left
turtle.forward(15)
#prop height 15
turtle.right(140)
#prop turn right to make tip
turtle.forward(15)
#forward by 15
turtle.left(70)
#back to being center
turtle.forward(70)

turtle.right(90)
turtle.forward(8)
turtle.right(90)

turtle.forward(70)
#prop ends gonna turn left from here
turtle.left(90)
turtle.forward(10)
turtle.left(85)
turtle.forward(33)
turtle.right(85)
turtle.forward(200)
#BACK TO MIDDLE STARTING FLAPS AND ALIERON
turtle.left(90)

turtle.left(90)
turtle.pensize(3)
turtle.begin_fill()
#flapr = 0
for i in range(2):
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(130)
    turtle.right(90)
    #flapr = flapr + 1
turtle.end_fill()

turtle.pensize(1)

turtle.right(90)
turtle.forward(155)
for i in range(1):
    turtle.left(5)
    turtle.forward(160)
    turtle.left(85)
    turtle.forward(85)
    turtle.left(90)
    turtle.forward(174)
    turtle.left(90)
    turtle.forward(100)


turtle.left(95)
turtle.forward(10)
turtle.left(85)
#alieronR
turtle.pensize(3)
for i in range(2):
    turtle.forward(30)
    turtle.right(85)
    turtle.forward(155)
    turtle.right(95)

turtle.pensize(1)
turtle.left(95)
turtle.forward(10)
turtle.right(5)
turtle.forward(140)
turtle.color("white")
for i in range(2):
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
turtle.color("black")
turtle.right(90)
turtle.forward(101)
turtle.left(90)
turtle.forward(85)

turtle.left(90)

turtle.forward(101)
turtle.color("white")
turtle.left(90)
for i in range(2):
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
