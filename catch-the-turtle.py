import turtle
import time
import random

#? ayarlamalar
screen = turtle.Screen()
screen.screensize(600,600,"lightblue")
screen.bgcolor("light blue")
screen.title("Turtle Game")
turtle_object = turtle.Turtle() #! kalem nesnesi -->  turtle_object  <-- kalem nesnesi
turtle_score = turtle.Turtle()
turtle_time = turtle.Turtle()
turtle_finish = turtle.Turtle()
turtle_finish.hideturtle()
screen.listen()

#? değişkenler
score = 0
remaining_time = 15

#? skor ve time yazıları
def score_tablo():
    turtle_score.undo()
    turtle_score.speed(0)
    turtle_score.penup()
    turtle_score.goto(0,280)
    turtle_score.hideturtle()
    turtle_score.color("green")
    turtle_score.write(f"Score: {score} ", font=("Arial",28,"normal"),align="center")



def time_tablo():
    turtle_time.undo()
    turtle_time.speed(0)
    turtle_time.penup()
    turtle_time.goto(0,240)
    turtle_time.hideturtle()
    turtle_time.color("black")
    turtle_time.write(f"Time: {remaining_time}", font=("Arial",26,"normal"),align="center")

#?-------------------------------------------------------------------------------------------------------

#? rastgele yer değiştirme
def change_location():
    turtle_object.shape("turtle")
    turtle_object.penup()
    turtle_object.pencolor("lightblue")
    turtle_object.speed(0)
    turtle_object.shapesize(stretch_wid=2, stretch_len=2, outline=1)
    turtle_object.goto(random.randint(-250,300),random.randint(-250,250))


#? skor ekleme fonksiyonu
def score_add(x , y):
    global score
    score += 1
    change_location()
    score_tablo()

#? süre fonksiyonu
def sayac():
    global remaining_time
    time.sleep(1)
    remaining_time -= 1
    time_tablo()


while remaining_time > 0:
    sayac()    
    score_tablo()
    time_tablo()
    time.sleep(0.3)
    change_location()
    turtle_object.onclick(score_add)
    # if remaining_time <= 0:
    #     score = tuple(score)

if remaining_time <= 0:
    turtle_object.hideturtle()
    turtle_finish.hideturtle()
    turtle_finish.color("black")
    turtle_finish.write("Game Over !", font=("Arial",30,"normal"),align="center")

turtle.done()

