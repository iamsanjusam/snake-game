from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)
screen.title("Snake Game")


snake = Snake()
food = Food()
score = ScoreBoard()

game_on = True

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_on:
    screen.update()
    time.sleep(0.1)

    # Detect Collision with the Food.
    if snake.head.distance(food) < 15:
        food.refresh()
        score.update_score()
        snake.extend()

    # Detect Collision with the Wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        score.game_over()

    # Detect Collision with the tail.
    for seg in snake.snakes [1:]:
        if snake.head.distance(seg) < 10:
            game_on = False
            score.game_over()

    snake.move()

screen.exitonclick()
