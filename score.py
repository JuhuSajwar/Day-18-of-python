from turtle import Turtle

class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt" , mode= "r") as file:
            self.high_score=int(file.read())
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}" " " f"High Score : {self.high_score}", align="center", font= ("Arial" ,24, "normal"))
    
    
    def reset (self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt",mode= "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0    
                
    #def game_over(self):
        #self.goto(0,0)
        #self.write("GAME OVER" , align="center", font= ("Arial" ,24, "normal"))    
        
    def increase_score(self):
        self.score += 1
        self.update_score()    
        
            
    