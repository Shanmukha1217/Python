
from turtle import Screen
from snake import Snake
from food import Food
from score_board import ScoreBoard
import time


screen = Screen()

screen.setup(width=600, height=600)  # * dimensions of the screen
screen.bgcolor('black')  # * background color of the screen
screen.title('My Snake Game')  # * title of the game
screen.tracer(0)  # * turns off the animation of the screen

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

''' listen() method allows to listen the keypress to act the functionality based on the functiion we provide '''
screen.listen()
screen.onkey(snake.move_left, 'Left')
screen.onkey(snake.move_right, 'Right')
screen.onkey(snake.move_up, 'Up')
screen.onkey(snake.move_down, 'Down')


game_is_on = True  # * game is on
while game_is_on:  # * while the game is on
    screen.update()  # * update the screen
    time.sleep(0.1)  # * sleep for 0.1 seconds
    snake.move_snake()  # * move the snake

    #* collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #* collision with the border
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        game_is_on = False
        scoreboard.game_over()

    #* collision with tail
    #* if head collides with any segment in the tail:
    #* game is over
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 15:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
