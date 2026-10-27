from turtle import Turtle
SEGMENTS_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_SPEED = 10
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
SNAKE_TYPE = 'square'
class Snake:
    def __init__(self):
        self.segments = []
        self.make_snake()
        self.head = self.segments[0]

    def make_snake(self):

        for position in SEGMENTS_POSITIONS:
            self.add_segment(position)

    def add_segment(self,position):
        new_seg = Turtle(SNAKE_TYPE)
        new_seg.color("white")
        new_seg.penup()
        new_seg.goto(position)
        self.segments.append(new_seg)

    def extend(self):
        self.add_segment(self.segments[-1].position())


    def move(self):

        for seg in range(len(self.segments)-1,0,-1):
            new_x = self.segments[seg-1].xcor()
            new_y = self.segments[seg-1].ycor()
            self.segments[seg].goto(new_x,new_y)
        self.head.forward(MOVE_SPEED)

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

