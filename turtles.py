from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


# Each time we call this call via object it will create 3 new turtle shapes using starting positions
class Turtles:
    # We should always use self when working with the class
    def __init__(self):
        self.segments = []  # Creating an empty list to store the values added to the var 'new_segment' from for loop
        # later
        # -later after iteration
        self.create_turtle()
        self.head = self.segments[0]

    def create_turtle(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)


    def add_segment(self,position):
        new_segment = Turtle("turtle")
        new_segment.color("red")
        new_segment.penup()  # This won't let the turtles draw a line when moving to a new line
        new_segment.goto(position)
        self.segments.append(
            new_segment)  # Each new segment which is created is appended to the list called segments

    def extend(self):
        self.add_segment(self.segments[-1].position()) # The position() is an in built turtle method


    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            # here we got hold of the last 2
            new_x = self.segments[seg_num - 1].xcor()  # getting hold of the second-last position into the new_x var
            new_y = self.segments[seg_num - 1].ycor()  # getting hold of the last segment
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:  # Turtle has a heading method which will give directions in terms of degrees
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
