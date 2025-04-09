# Create the CRC card.
class PlayerMovement:
    def __init__(self, player_name, player_move): # What is this? | In this case, a method called __init__ is being defined, in which the paren. rep. attributes that go into the function. For example, f(x) - a function is a label that takes x as an input, and generate an output.
        self.player_name = player_name
        self.player_move = player_move
    # GOAL: Abstract the functions for player movement (up,down,left,right) into methods that can be used as part of this class.
    def player_up(self):
        return self.player_name + " is moving up."
    def player_down(self):
        return self.player_name + " is moving down."
    def player_left(self):
        return self.player_name + " is moving left."
    def player_right(self):
        return self.player_name + " is moving right."