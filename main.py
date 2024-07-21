from turtle import Screen 
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=680,height=680)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

#Create snake body

starting_postion = [(0,0),[-20,0],[-40,0]]


segments= []


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    #detect collision with food
    if snake.head.distance(food)< 15:
      food.refresh()
      snake.extend()
      scoreboard.increase_score()


    #DETECT COLLISION WITH WALL

    if snake.head.xcor() >300 or snake.head.xcor( ) < -300 or snake.head.ycor()> 300 or snake.head.ycor()< -300:
        game_is_on = False
        scoreboard.game_over()


    #detect collision with tail
    for segment in snake.segments[1:]:
        if segment == snake.head:
           passs
        elif snake.head.distance(segment) < 10:
           game_is_on = False
           scoreboard.game_over()
        
















screen.exitonclick()