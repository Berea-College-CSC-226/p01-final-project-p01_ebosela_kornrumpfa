# Create the CRC card.
class PlayerMovement:
    def __init__(self, x=0, y=0, speed=0):# What is this? | In this case, a method called __init__ is being defined, in which the paren. rep. attributes that go into the function. For example, f(x) - a function is a label that takes x as an input, and generate an output.
        self.x = x
        self.y = y
        self.speed = speed
    # GOAL: Abstract the functions for player movement (up,down,left,right) into methods that can be used as part of this class.

    def player_up(self):
         self.y += self.speed

    def player_down(self):
         self.y -= self.speed

    def player_left(self):
         self.x += self.speed

    def player_right(self):
         self.y -= self.speed

    def player_position(self):
        return(self.x, self.y)

player1 = PlayerMovement()
player1.player_up()
print(player1.player_position)


