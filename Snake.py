import turtle
import time
import random

posponer = 0.1

# Marcador
score = 0
high_score = 0

# Configuracion de la ventana
window = turtle.Screen()  # crear pantalla
window.title("Snake")  # nombre pantalla
window.bgcolor("black")  # color fondo
window.setup(width=600, height=600)  # dimensiones pantalla
window.tracer(0)

# Cabeza serpiente
cabeza = turtle.Turtle()  # crear cabeza
cabeza.speed(0)  # velocidad incial de la cabeza
cabeza.shape("square")  # forma de la cabeza
cabeza.color("blue")  # color de la cabeza
cabeza.penup()  # para que no deje rastro
cabeza.goto(0, 0)  # posicion inical(0,0) = centro
cabeza.direction = "stop"  # direccion incial de la cabeza

# Comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0, 100)

# Cuerpo serpiente
cuerpo = []

# Texto marcador
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0, 260)
texto.write("Marcador= 0       Record= 0", align="center",
            font=("Courier", 20, "normal"))

# Texto game over
game_over = turtle.Turtle()
game_over.speed(0)
game_over.color("red")
game_over.penup()
game_over.hideturtle()
game_over.goto(0, 0)


# Funciones


def arriba():
    cabeza.direction = "up"
    game_over.clear()


def abajo():
    cabeza.direction = "down"
    game_over.clear()


def derecha():
    cabeza.direction = "right"
    game_over.clear()


def izquierda():
    cabeza.direction = "left"
    game_over.clear()


def movimiento():
    y = cabeza.ycor()  # indicar cual es la posicion del eje y
    x = cabeza.xcor()  # indicar cual es la posicion del eje x

    # arriba
    if cabeza.direction == "up":
        cabeza.sety(y + 20)  # actualizar valor e incrementar +20

    # abajo
    if cabeza.direction == "down":
        cabeza.sety(y - 20)

    # derecha
    if cabeza.direction == "right":
        cabeza.setx(x + 20)

    # izquierda
    if cabeza.direction == "left":
        cabeza.setx(x - 20)


# Teclado
window.listen()
window.onkeypress(arriba, "Up")
window.onkeypress(abajo, "Down")
window.onkeypress(derecha, "Right")
window.onkeypress(izquierda, "Left")

window.onkeypress(arriba, "w")
window.onkeypress(abajo, "s")
window.onkeypress(derecha, "d")
window.onkeypress(izquierda, "a")

window.onkeypress(arriba, "W")
window.onkeypress(abajo, "S")
window.onkeypress(derecha, "D")
window.onkeypress(izquierda, "A")

# Bucle principal
while True:
    window.update()  # refresque todo el rato la pantalla

    # Colisiones bordes
    if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < - 280:
        game_over.write("GAME OVER", align="center",
                        font=("Courier", 36, "normal"))
        time.sleep(1)
        cabeza.goto(0, 0)
        cabeza.direction = "stop"

        # Esconder cuerpo
        for parte_cuerpo in cuerpo:
            parte_cuerpo.goto(1000, 1000)

        # Limpiar lista de segmentos
        cuerpo.clear()

        # Poner marcador a 0
        score = 0

        texto.clear()
        texto.write("Marcador= {}       Record= {}".format(score, high_score), align="center",
                    font=("Courier", 20, "normal"))

    # Colisiones cuerpo
    for parte_cuerpo in cuerpo:
        if parte_cuerpo.distance(cabeza) < 20:
            game_over.write("GAME OVER", align="center",
                            font=("Courier", 36, "normal"))
            time.sleep(1)
            cabeza.goto(0, 0)
            cabeza.direction = "stop"

            # Esconder cuerpo
            for parte_cuerpo in cuerpo:
                parte_cuerpo.goto(1000, 1000)

            # Limpiar lista de segmentos
            cuerpo.clear()

            # Poner marcador a 0
            score = 0

            texto.clear()
            texto.write("Marcador= {}       Record= {}".format(score, high_score), align="center",
                        font=("Courier", 20, "normal"))

    # Colisiones comida
    if cabeza.distance(comida) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        comida.goto(x, y)

        nuevo_cuerpo = turtle.Turtle()
        nuevo_cuerpo.speed(0)
        nuevo_cuerpo.shape("square")
        nuevo_cuerpo.color("blue")
        nuevo_cuerpo.penup()
        nuevo_cuerpo.goto(0, 100)
        cuerpo.append(nuevo_cuerpo)

        # Aumentar marcador
        score += 10
        if score > high_score:
            high_score = score

        texto.clear()
        texto.write("Marcador= {}       Record= {}".format(score, high_score), align="center",
                    font=("Courier", 20, "normal"))

    # Mover el cuerpo de la serpiente
    total_cuerpo = len(cuerpo)
    for index in range(total_cuerpo - 1, 0, -1):
        x = cuerpo[index - 1].xcor()
        y = cuerpo[index - 1].ycor()
        cuerpo[index].goto(x, y)

    if total_cuerpo > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        cuerpo[0].goto(x, y)

    movimiento()
    time.sleep(posponer)  # para que el programa no se ejecute tan rapido
