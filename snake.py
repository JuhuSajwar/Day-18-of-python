from turtle import Turtle
import random
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
SNAKE_COLOR_CHOICE = ["red", "green", "blue", "yellow", "orange", "purple"]

class Snake:
    
    def __init__(self):
        self.segment = []
        self.create_snake()
      
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
            
    def add_segment(self, position):        
        tom = Turtle("square")
        tom.color(random.choice(SNAKE_COLOR_CHOICE))
        tom.penup()
        tom.goto(position)
        self.segment.append(tom)
        
    def reset(self):
        for seg in self.segment:
            seg.goto(1000,1000)
        self.segment.clear()
        self.create_snake()
        self.segment[0]    
        
    def extend_seg(self):
        self.add_segment(self.segment[-1].position())       
    
    
    def move(self):
        for seg_num in range(len(self.segment) -1, 0 , -1 ):
            new_x = self.segment[seg_num -1].xcor()
            new_y = self.segment[seg_num -1].ycor()
            self.segment[seg_num].goto(new_x,new_y)
        self.segment[0].forward(MOVE_DISTANCE)
        
    def up(self):
        if self.segment[0].heading() != DOWN:
            self.segment[0].setheading(UP)
        
    def down(self):
        if self.segment[0].heading() != UP:
            self.segment[0].setheading(DOWN)
    
    def left(self):
        if self.segment[0].heading() != RIGHT:
            self.segment[0].setheading(LEFT)
    
    def right(self):
        if self.segment[0].heading() != LEFT:                            
            self.segment[0].setheading(RIGHT)