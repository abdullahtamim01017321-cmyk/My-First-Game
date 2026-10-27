from turtle import Screen, Turtle
import snake
import time
import food
import scoreboard
SPEED_SNAKE = 0.1
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My First Game")
screen.tracer(0)

border = Turtle()
border.hideturtle()
border.speed(0)
border.penup()
border.color("green")
border.pensize(10)

border.goto(-295, 295)
border.pendown()

border.goto(295, 295)
border.goto(295, -295)
border.goto(-295, -295)
border.goto(-295, 295)

border.penup()


snake = snake.Snake()
food = food.Food()
scoreboard = scoreboard.Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(SPEED_SNAKE)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    if snake.head.xcor()> 280 or snake.head.xcor()< -280 or snake.head.ycor()> 280 or snake.head.ycor()< -280:
        is_game_on = False
        scoreboard.game_over()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 9.5:
            is_game_on = False
            scoreboard.game_over()
            break


screen.exitonclick()