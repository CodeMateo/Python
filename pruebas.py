import turtle

pn = turtle.Screen()
pn.title("PING PONG")
pn.bgcolor("black")
pn.setup(width=800, height=600)
pn.tracer(0)

#PUNTUACION
punt_a = 0
punt_b = 0

#JUGADOR A
jugador_a = turtle.Turtle()
jugador_a.speed(0)
jugador_a.shape("square")
jugador_a.color("white")
jugador_a.shapesize(stretch_wid=5, stretch_len=1)
jugador_a.penup()
jugador_a.goto(-350, 0)


#JUGADOR B
jugador_b = turtle.Turtle()
jugador_b.speed(0)
jugador_b.shape("square")
jugador_b.color("white")
jugador_b.shapesize(stretch_wid=5, stretch_len=1)
jugador_b.penup()
jugador_b.goto(350, 0)


#PELOTA
pelota = turtle.Turtle()
pelota.speed(0)
pelota.shape("square")
pelota.color("white")
pelota.penup()
pelota.goto(0, 0)
pelota.dx = 0.5
pelota.dy = -0.5

#MARCADOR
marcador = turtle.Turtle()
marcador.speed(0)
marcador.color("white")
marcador.penup()
marcador.hideturtle()
marcador.goto(0, 260)
marcador.write("JUGADOR A: 0 JUGADOR B: 0", align="center", font=("Courier", 20, "normal"))


#MOVIMIENTO
def jugador_a_arriba():
    y = jugador_a.ycor()
    y += 40
    jugador_a.sety(y)

def jugador_a_abajo():
    y = jugador_a.ycor()
    y -= 40
    jugador_a.sety(y)

def jugador_b_arriba():
    y = jugador_b.ycor()
    y += 40
    jugador_b.sety(y)

def jugador_b_abajo():
    y = jugador_b.ycor()
    y -= 40
    jugador_b.sety(y)


#TECLAS
pn.listen()
pn.onkeypress(jugador_a_arriba, "w")
pn.onkeypress(jugador_a_abajo, "s")

pn.onkeypress(jugador_b_arriba, "Up")
pn.onkeypress(jugador_b_abajo, "Down")


while True:
    pn.update()

    #MOVIMIENTO DE LA PELOTA
    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)
 
    #COLISIONES BORDE
    if pelota.ycor() > 290:
        pelota.sety(290)
        pelota.dy *= -1

    if pelota.ycor() < -290:
        pelota.sety(-290)
        pelota.dy *= -1
        

    if pelota.xcor() > 390:
        pelota.goto(0, 0)
        pelota.dx *= -1
        punt_a += 1
        marcador.clear()
        marcador.write("JUGADOR A: {} JUGADOR B: {}".format(punt_a, punt_b), align="center", font=("Courier", 20, "normal"))


    if pelota.xcor() < -390:
        pelota.goto(0, 0)
        pelota.dx *= -1
        punt_b += 1
        marcador.clear()
        marcador.write("JUGADOR A: {} JUGADOR B: {}".format(punt_a, punt_b), align="center", font=("Courier", 20, "normal"))


        #COLISIONES DE PELOTA Y JUGADOR
    if  pelota.xcor() < -340 and pelota.ycor() < jugador_a.ycor() + 50 and pelota.ycor() > jugador_a.ycor() - 50:
        pelota.dx *= -1

    elif pelota.xcor() > 340 and pelota.ycor() < jugador_b.ycor() + 50 and pelota.ycor() > jugador_b.ycor() - 50:
        pelota.dx *= -1

    #AUMENTO DE VELOCIDAD PELOTA
    """
    if punt_a == 1 and punt_b == 1:
        pelota.dx = 1
        pelota.dy = -1

    if punt_a == 3 and punt_b == 3:
        pelota.dx = 1.5
        pelota.dy = -1.5

    if punt_a == 5 and punt_b == 5:
        pelota.dx = 2
        pelota.dy = -2
    """
