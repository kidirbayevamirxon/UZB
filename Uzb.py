import turtle

# Ekranni sozlash
window = turtle.Screen()
window.setup(1000, 600)
window.bgcolor("white")

# Turtle sozlamalarini boshlash
turtle.speed(4)
turtle.penup()
turtle.goto(-960, 370)
turtle.pendown()

# Flagning o'lchamlari
hight_main = 140
width_main = 1920

def draw_rectangle(color, height):
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(width_main)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()
    turtle.right(90)
    turtle.forward(height)
    turtle.left(90)

# Flagni chizish, yuqori qismini ochish uchun
# Aslida yuqori qismni bo'sh qilib chizamiz
draw_rectangle("#0099B5", hight_main)  # Ko'k
draw_rectangle("#CE1126", 10)           # Qizil chiziq
draw_rectangle("white", hight_main)     # Oq
draw_rectangle("#CE1126", 10)           # Qizil chiziq
draw_rectangle("#1EB53A", hight_main)   # Yashil

# Flagning yuqori qismi ochiq bo'lishi uchun:
# Bu yerda yuqoridagi qismni bo'sh qoldirish yoki boshqa xususiyatlar qo'shish mumkin

# Hilal (oy) chizish funksiyasi
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
    turtle.circle(size - 8)
    turtle.end_fill()
    turtle.left(90)

# Hilalni chizish
hilal(40)

# Yulduz (yildiz) chizish funksiyasi
def yildiz(size):
    turtle.penup()
    turtle.goto(-370, 328)
    turtle.pendown()
    for j in range(12):
        if j == 3:
            turtle.penup()
            turtle.goto(-400, 298)
            turtle.pendown()
        elif j == 7:
            turtle.penup()
            turtle.goto(-430, 268)
            turtle.pendown()
        
        turtle.fillcolor("white")
        turtle.begin_fill()

        for _ in range(5):  # Yulduz chizish uchun 5 marta oldinga borish va burilish
            turtle.forward(size)
            turtle.right(144)  # Yulduzning burchagi

        turtle.end_fill()
        turtle.penup()
        turtle.forward(30)
        turtle.pendown()

# Yulduzlarni chizish
yildiz(5)

# Turtle kursorini yashirish
turtle.hideturtle()

# Chizishni yakunlash
turtle.done()
