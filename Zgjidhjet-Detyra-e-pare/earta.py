import turtle

h = turtle.Turtle()
h.pencolor("black")

h.right(90)
h.forward(50)
h.penup()
h.forward(10)
h.pendown()
h.forward(50)
h.left(90)
h.penup()
h.forward(50)
h.left(90)
h.pendown()
h.forward(50)
h.right(90)
h.penup()
h.forward(50)
h.right(90)
h.pendown()
h.forward(50)
h.left(90)
h.penup()
h.forward(25)
h.left(90)
h.pendown()
h.forward(50)
h.penup()
h.forward(10)
h.pendown()
h.forward(50)
h.penup()
h.backward(25)
h.left(90)
h.forward(40)
h.pendown()
h.forward(20)
h.penup()
h.backward(60)
h.right(90)
h.forward(60)
h.left(90)

for i in range(4):
    h.forward(15)
    h.pendown()
    h.forward(15)
    h.penup()

h.forward(5)
h.right(90)
h.penup()
h.forward(30)
h.pendown()
h.right(30)
h.forward(50)
h.penup()
h.forward(10)
h.pendown()
h.forward(50)
h.penup()
h.right(60)
h.forward(10)
h.right(60)
h.pendown()
h.forward(50)
h.penup()
h.forward(10)
h.pendown()
h.forward(50)

 
turtle.done()