from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=1000, height=800)
screen.title("Snake game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
screen.listen()
food = Food()
scoreboard = Scoreboard()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.15)
    snake.move()

    if snake.head.xcor() > 480 or snake.head.xcor() < -480 or snake.head.ycor() > 392 or snake.head.ycor() < -395:
        snake.hide_turtle()
        scoreboard.reset_score()
        snake.reset_snake()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        scoreboard.increase()

    for t in snake.turtles[1:]:
        if snake.head.distance(t) < 10:
            snake.hide_turtle()
            scoreboard.reset_score()
            snake.reset_snake()

screen.exitonclick()
