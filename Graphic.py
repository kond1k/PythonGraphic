import turtle
import random
import math


def go_to_xy(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


def draw_fill_circle(x, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(x)
    turtle.end_fill()


turtle.speed(15)
go_to_xy(0, 0)
turtle.circle(80)
go_to_xy(0, 160)
draw_fill_circle(5, 'red')
answer = ''



phi = 360 / 7
r = 50
phi_rad = 0
start = 0

for i in range(0, 7):
    phi_rad = phi * i * math.pi / 180.0
    go_to_xy(math.sin(phi_rad) * r, math.cos(phi_rad) * r + 60)
    draw_fill_circle(22, "white")

while answer != 'N':
    answer = turtle.textinput("Играть?", "Y/N")
    if answer == 'Y':
        for i in range(start, random.randrange(7, 100)):
            phi_rad = phi * i * math.pi / 180.0
            go_to_xy(math.sin(phi_rad) * r, math.cos(phi_rad) * r + 60)
            draw_fill_circle(22, "brown")
            draw_fill_circle(22, "white")

    go_to_xy(math.sin(phi_rad) * r, math.cos(phi_rad) * r + 60)
    draw_fill_circle(22, "brown")

    start = i % 7
    if i % 7 == 0:
        go_to_xy(-150, 250)
        turtle.write("Вы проиграли", font=("Arial", 18, "normal"))
else:
    pass
