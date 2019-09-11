import turtle
scn = turtle.Screen()
scn.bgcolor("yellow")

alice = turtle.Turtle()
bob = turtle.Turtle()
cindy = turtle.Turtle()

bob.shape("turtle")
cindy.shape("square")

bob.fillcolor("white")

alice.forward(200)
bob.right(75)
bob.forward(150)
bob.pencolor("blue")
bob.begin_fill()
bob.circle(150)
bob.end_fill()

scn.exitonclick()
