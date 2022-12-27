from turtle import *
import turtle
import random
import time

txt_open = open('text.txt', 'r')

width = 1200
height = 800
win = turtle.Screen()
win.setup(width, height)
win.bgcolor("sky blue")
win.title("Новогодняя открытка")

sb_rate = 1, 3
sb_size = 5, 15
wind_change = 1, 5
max_wind = 3


def make_circle(turtle_name, x, y, size, colour):
    turtle_name.color(colour)
    turtle_name.penup()
    turtle_name.setposition(x, y)
    turtle_name.dot(size)


list_of_sbs = []


# Механика снега
def make_sb():
    sb = turtle.Turtle()
    sb.color("white")
    sb.penup()
    sb.setposition(random.randint(-2 * width, width / 2), height / 2)
    sb.hideturtle()
    sb.size = random.randint(*sb_size)
    list_of_sbs.append(sb)


def move_sb(turtle_name, falling_speed=4, wind=0):
    turtle_name.clear()
    turtle_name.sety(turtle_name.ycor() - falling_speed)
    if wind:
        turtle_name.setx(turtle_name.xcor() + wind)
    turtle_name.dot(turtle_name.size)


# Земля
ground = turtle.Turtle()
ground.fillcolor("white")  # forest green
ground.penup()
ground.setposition(-width / 2, -height / 2)
ground.begin_fill()
for _ in range(2):
    ground.forward(width)
    ground.left(90)
    ground.forward(100)
    ground.left(90)
ground.end_fill()

# Елка
circle = turtle.Turtle()
circle.shape('circle')
circle.color('red')
circle.speed('fastest')
circle.up()

square = turtle.Turtle()
square.shape('square')
square.color('green')
square.speed('fastest')
square.up()

circle.goto(0, 280)
circle.stamp()

k = 0
for i in range(1, 17):
    y = 30 * i
    for j in range(i - k):
        x = 30 * j
        square.goto(x, -y + 280)
        square.stamp()
        square.goto(-x, -y + 280)
        square.stamp()

    if i % 4 == 0:
        x = 30 * (j + 1)
        circle.color('red')
        circle.goto(-x, -y + 280)
        circle.stamp()
        circle.goto(x, -y + 280)
        circle.stamp()
        k += 2

    if i % 4 == 3:
        x = 30 * (j + 1)
        circle.color('yellow')
        circle.goto(-x, -y + 280)
        circle.stamp()
        circle.goto(x, -y + 280)
        circle.stamp()

square.color('brown')
for i in range(17, 20):
    y = 30 * i
    for j in range(3):
        x = 30 * j
        square.goto(x, -y + 280)
        square.stamp()
        square.goto(-x, -y + 280)
        square.stamp()

# конец елки

# Генерация снега
ground = turtle.Turtle()
for x in range(int(-width / 2), int(width / 2), int(width / 200)):
    make_circle(ground, x, -290, random.randint(5, 55), "white")

# Снеговик
sm = turtle.Turtle()
x_position = -300  # позиция X
y_positions = -1, -80, -200  # позиция Y
size = 85  # общий размер
for y in y_positions:
    make_circle(sm, x_position, y, size, "white")
    size = size * 1.5

button_seperation = 22  # расстояние между пуговицами
button_y_positions = [y_positions[1] - button_seperation,
                      y_positions[1],
                      y_positions[1] + button_seperation]

# пуговицы (характеристики)
for y in button_y_positions:
    make_circle(sm, x_position, y, 10, "black")
    make_circle(sm, x_position, y, 5, "white")

y_offset = 10
x_seperation = 15
# глаза
for x in x_position - x_seperation, x_position + x_seperation:
    make_circle(sm, x, y_positions[0] + y_offset, 20, "green")
    make_circle(sm, x, y_positions[0] + y_offset, 10, "black")
    make_circle(sm, x, y_positions[0] + y_offset, 5, "white")

# Нос
sm.color("orange")
sm.setposition(x_position - 10, y_positions[0] - y_offset)
sm.shape("triangle")
sm.setheading(200)
sm.turtlesize(0.5, 2.5)

txt = turtle.Turtle()
txt.color("Purple")
txt.penup()
txt.setposition(-350, 290)
txt.write(txt_open.readline(), font=("purple", 30, "bold"), align="center")
txt.setposition(-170, 250)
txt.color("green")
txt.write("Поздравляю всех ", font=("blue", 30, "bold"), align="right")
txt.color("red")
txt.setx(10)
txt.setposition(290, 110)
txt.write("С Новым Годом!", font=("red", 30, "normal"), align="center")

# txt.write("from", font=("Apple Chancery", 20, "bold"), align="right")
txt.hideturtle()

# Генерация снега на фоне
win.tracer(0)
time_delay = 0
start_time = time.time()
wind = 0
wind_delay = 5
wind_timer = time.time()
wind_step = 0.1
while True:
    if time.time() - start_time > time_delay:
        make_sb()
        start_time = time.time()
        time_delay = random.randint(*sb_rate) / 10

    for sb in list_of_sbs:
        move_sb(sb, wind=wind)
        if sb.ycor() < -height / 2:
            sb.clear()
            list_of_sbs.remove(sb)

    if time.time() - wind_timer > wind_delay:
        wind += wind_step
        if wind >= max_wind:
            wind_step = -wind_step
        elif wind <= 0:
            wind_step = abs(wind_step)

        wind_timer = time.time()
        wind_delay = random.randint(*wind_change) / 10

    win.update()

turtle.done()
