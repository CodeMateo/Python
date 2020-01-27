import turtle
import os

wn = turtle.Screen()
wn.title("GUERRA MORTAL")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

score_a = 0
score_b = 0

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("blue")
ball.penup()
ball.shapesize(stretch_wid=1.5, stretch_len=1.5)
ball.goto(-200, 0)

ball1 = turtle.Turtle()
ball1.speed(0)
ball1.shape("square")
ball1.color("green")
ball1.penup()
ball1.shapesize(stretch_wid=1.5, stretch_len=1.5)
ball1.goto(200, 0)

"""
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("VERDE: 0  AZUL: 0", align="center", font=("Arial", 24, "normal"))
"""

def muñeco_up():
    y = ball.ycor()
    y += 20
    ball.sety(y)

def muñeco_down():
    y = ball.ycor()
    y -= 20
    ball.sety(y)

def muñeco_derecha():
    x = ball.xcor()
    x += 20
    ball.setx(x)

def muñeco_izquierda():
    x = ball.xcor()
    x -= 20
    ball.setx(x)

#-----------------------------------------------------------

def muñeco_up1():
    y = ball1.ycor()
    y += 20
    ball1.sety(y)

def muñeco_down1():
    y = ball1.ycor()
    y -= 20
    ball1.sety(y)

def muñeco_derecha1():
    x = ball1.xcor()
    x += 20
    ball1.setx(x)

def muñeco_izquierda1():
    x = ball1.xcor()
    x -= 20
    ball1.setx(x)


wn.listen()
wn.onkeypress(muñeco_up, "w")
wn.onkeypress(muñeco_down, "s")
wn.onkeypress(muñeco_derecha, "d")
wn.onkeypress(muñeco_izquierda, "a")


wn.onkeypress(muñeco_up1, "Up")
wn.onkeypress(muñeco_down1, "Down")
wn.onkeypress(muñeco_derecha1, "Right")
wn.onkeypress(muñeco_izquierda1, "Left")

while True:
    wn.update()

    if ball.ycor() > 270:
        ball.sety(270)

    if ball.ycor() < -270:
        ball.sety(-270)

    if ball.xcor() > 360:
        ball.setx(360)

    if ball.xcor() < -360:
        ball.setx(-360)


    if ball1.ycor() > 270:
        ball1.sety(270)

    if ball1.ycor() < -270:
        ball1.sety(-270)

    if ball1.xcor() > 360:
        ball1.setx(360)

    if ball1.xcor() < -360:
        ball1.setx(-360)

    if ball.xcor() == ball1.xcor() and ball.ycor() == ball1.ycor():
        ball.goto(-200, 0)
        ball1.goto(200, 0)
        """
        score_a += 1
        pen.clear()
        pen.write("VERDE: {}".format(score_a), align="center", font=("Arial", 24, "normal"))
        """

    if ball1.xcor() == ball.xcor() and ball1.ycor() == ball.ycor():
        ball.goto(-200, 0)
        ball1.goto(200, 0)
        """
        score_b += 1
        pen.clear()
        pen.write("AZUL: {}".format(score_b), align="center", font=("Arial", 24, "normal"))
        """