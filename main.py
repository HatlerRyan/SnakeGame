import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)

scoreboard = Scoreboard()
snake = Snake()
food = Food()
screen.listen()
screen.onkey(snake.up, "w",)
screen.onkey(snake.left, "a",)
screen.onkey(snake.down, "s",)
screen.onkey(snake.right, "d",)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()

    # If snake gets food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.add_point()
        # print(scoreboard.score)
        scoreboard.re_score()

    # if snake runs into wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    #     if snake hits it's own tail
    for segment in snake.segments:
        if snake.head == segment:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()



screen.exitonclick()
