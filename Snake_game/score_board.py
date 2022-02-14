from turtle import Turtle


from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 20, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')  # * default color of the score board
        self.penup()
        self.goto(0, 260)
        self.write(f'Score: {self.score}', align=ALIGNMENT,
                   font=FONT)  # * font has to be in tuple
        self.hideturtle()

    def game_over(self):
        ''' This method print the Game over message at 0,0 co-ordinates in the screen'''
        self.goto(0, 0)
        self.write('Game Over', align=ALIGNMENT, font=FONT)

    def increase_score(self):
        '''This method increases the score and writes it on the window once snake eats the food'''
        self.score += 1
        self.clear()
        self.write(f'Score: {self.score}', align=ALIGNMENT,
                   font=FONT)  # * font has to be in tuple
