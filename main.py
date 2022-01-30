from turtle import Screen, Turtle
from turtles import Turtles
from food import Food
from scoreboard import Scoreboard
import time  # this module is for making the moments slow as they are very fast when we run the code

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("yellow")
screen.title("Pk's Turtle Game")
screen.tracer(0)

turtles = Turtles()  # creating an object of class turtles
food = Food()
screen.listen()
scoreboard = Scoreboard()
# linked with turtles class
screen.onkey(turtles.up, "Up")
screen.onkey(turtles.down, "Down")
screen.onkey(turtles.left, "Left")
screen.onkey(turtles.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()  # placing this method here because it will only update after all the segments have moved and no gap
    # no gap is visible between the movement of pieces of turtle
    time.sleep(0.1)  # the delay will be done after complete movement of segments, but also it lets segments move faster
    turtles.move()
    # Detect collision with food
    if turtles.head.distance(food)< 15: # as the len of food is ten by ten we can set 15 as it reaches near it collides
        food.refresh()  # this obj ref calls refresh method as soon as it collides with the food and position changes
        turtles.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if turtles.head.xcor() > 280 or turtles.head.xcor() < -280 or turtles.head.ycor() > 280 or turtles.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    for segment in turtles.segments[1:]:  # [1:] means other than the first segment loop through the other segments
        if turtles.head.distance(segment)<10:
            game_is_on = False
            scoreboard.game_over()



screen.exitonclick()
