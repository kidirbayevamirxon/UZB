import turtle

window=turtle.Screen()
window=turtle.setup(1000, 600)
window.bgcolor("white")

turtle.speed(4)
turtle.penup()
turtle.goto(-960, 370)
turtle.pendown()

hight_main=140
width_main=1920

def draw_rectangle( color, hight):
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(width_main)
        turtle.right(90)
        turtle.forward(hight)
        turtle.right(90)
    turtle.end_fill()
    turtle.right(90)
    turtle.forward(hight)
    turtle.left(90)

draw_rectangle("#0099B5", hight_main)
draw_rectangle("#CE1126",10)
draw_rectangle("white", hight_main)
draw_rectangle("#CE1126",10)
draw_rectangle("#1EB53A", hight_main)


def hilal(size):
    turtle.color("white")
    turtle.right(90)
    turtle.penup()
    turtle.goto(-500, 300)
    turtle.pendown()
    turtle.fillcolor("white")
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(-470, 300)
    turtle.fillcolor("#0099B5")
    turtle.begin_fill()
    turtle.circle(size-8)
    turtle.end_fill()
    turtle.letf(90)

hilal(40)

def yildiz(size):
    turtle.penup()
    turtle.goto(-370, 328)
    turtle.pendown()
    for j in range(12):
        if j==3:
            turtle.penup()
            turtle.goto(-400, 298)
            turtle.pendown()
        elif j==7:
            turtle.penup()
            turtle.goto(-430, 268)
            turtle.pendown()
        turtle.fillcolor("white")
        turtle.begin_fill()
        turtle.begin_fill()
        turtle.forward(size)
        turtle.left(72)
        turtle.forward(size)
        turtle.right(144)
        turtle.forward(size)
        turtle.left(72)
        turtle.forward(size)
        turtle.right(144)
        turtle.forward(size)
        turtle.left(72)
        turtle.forward(size)
        turtle.right(144)
        turtle.forward(size)
        turtle.left(72)
        turtle.forward(size)
        turtle.right(144)
        turtle.forward(size)
        turtle.left(72)
        turtle.forward(size)
        turtle.right(144)

        turtle.end_fill()
        turtle.penup()
        turtle.forward(30)
        turtle.pendown()

yildiz(5)


turtle.hideturtle()
turtle.done()

