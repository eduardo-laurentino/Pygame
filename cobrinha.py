# pacotes...
import turtle
import random
import time





# criando a tela...
screen = turtle.Screen()
screen.title("SNAKE GAME IN PYTHON")
screen.setup(width=700, height=700)
screen.tracer(0)
screen.bgcolor("#1d1d1d")

# criando borda da tela...
turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.goto(-310, 250)
turtle.pendown()
turtle.color("red")
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.penup()
turtle.hideturtle()

# score...
score = 0;
turtle.delay = 0.1

# snake
snake = turtle.Turtle()
snake.speed(50)
snake.shape("circle")
snake.color("blue")
snake.penup()
snake.goto(0, 0)
snake.direction = 'stop'

# comida...
fruit = turtle.Turtle()
fruit.speed(0)
fruit.shape("circle")
fruit.color("green")
fruit.penup()
fruit.goto(30, 30)

old_fruit = []

# tela final...
scoring = turtle.Turtle()
scoring.speed(0)
scoring.color("white")
scoring.penup()
scoring.hideturtle()
scoring.goto(0, 300)
scoring.write("Score: ", align="center", font=("Courier", 24, "bold"))


# função para movimento
def snake_go_up():
    if snake.direction != "up":
        snake.direction = "up"

def snake_go_down():
    if snake.direction != "up":
        snake.direction = "down"

def snake_go_left():
    if snake.direction != "right":
        snake.direction = "left"

def snake_go_right():
    if snake.direction != "left":
        snake.direction = "right"

def move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)
    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)
    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)
    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)



# configurando teclado...
screen.listen()
screen.onkeypress(snake_go_up, "Up")
screen.onkeypress(snake_go_down, "Down")
screen.onkeypress(snake_go_left, "Left")
screen.onkeypress(snake_go_right, "Right")

# main loop...
while True:
    screen.update()

    if snake.distance(fruit) < 20:
        x = random.randint(-290, 270)
        y = random.randint(-240, 240)
        fruit.goto(x, y)
        scoring.clear()
        score += 1
        scoring.write("Score: {}".format(score), align="center", font=("Courier", 24, "bold"))
        turtle.delay -= 0.0001

        new_fruit = turtle.Turtle()
        new_fruit.speed(0)
        new_fruit.shape("circle")
        new_fruit.color("blue")
        new_fruit.penup()
        old_fruit.append(new_fruit)

    
    for index in range(len(old_fruit) -1, 0, -1):
        a = old_fruit[index -1].xcor()
        b = old_fruit[index -1].ycor()

        old_fruit[index].goto(a, b)


    if len(old_fruit) > 0:
        a = snake.xcor()
        b = snake.ycor()
        old_fruit[0].goto(a, b)
    move()


    if snake.xcor() > 280 or snake.xcor() < -300 or snake.ycor() > 240 or snake.ycor() < -240:
        time.sleep(1)
        screen.clear()
        screen.bgcolor("green")
        scoring.goto(0, 0)
        scoring.write("Game Over \n seu score é {}".format(score), align="center", font=("Courier", 40, "bold"))



    for food in old_fruit:
        if food.distance(snake) < 20:
            time.sleep(1)
            screen.clear()
            screen.bgcolor("green")
            scoring.goto(0, 0)
            scoring.write("Fim de Jogo! Sua Pontuação: {}".format(score), align="center", font=("Courier", 35, "bold"))

    time.sleep(turtle.delay)

turtle.Terminator()