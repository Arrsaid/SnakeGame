from turtle import Turtle
UP, DOWN, LEFT, RIGHT = 90, 270, 180, 0
POSITION = [(0, 0), (-20, 0), (-40, 0), (-60, 0)]


class Snake:
    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]

    def create_snake(self):
        for position in POSITION:
            self.add_turtle(position)

    def add_turtle(self, position):
        tommy = Turtle(shape="square")
        tommy.penup()
        tommy.color("white")
        tommy.goto(position)
        self.turtles.append(tommy)

    def extend_snake(self):
        self.add_turtle(self.turtles[-1].position())

    def reset_snake(self):
        self.turtles = []
        self.create_snake()
        self.extend_snake()
        self.head = self.turtles[0]

    def move(self):
        for num in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[num - 1].xcor()
            new_y = self.turtles[num - 1].ycor()
            self.turtles[num].goto(new_x, new_y)
        self.head.forward(20)

    def hide_turtle(self):
        for turtle in self.turtles:
            turtle.hideturtle()

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)
