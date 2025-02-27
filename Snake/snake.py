from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]
        
    def create_snake(self):
        for i in range(3):
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(x=-20 * i, y=0)
            self.segment.append(new_segment)
        return self.segment
      
    def move(self):
        for seg_num in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg_num - 1].xcor()
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(x=new_x, y=new_y)
        self.segment[0].forward(MOVE_DISTANCE)
        
    def up(self):
        if self.head.heading() != DOWN:
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
            
            
        
              