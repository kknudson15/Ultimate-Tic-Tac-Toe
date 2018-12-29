import random 

class Computer:
    def __init__(self):
        self = self
    def set_marker(self, marker):
        self.marker = marker
    def get_marker(self):
        return self.marker
    def make_move(self):
        move = self.random_move()
        return move
        
    def random_move(self):
        return random.randint(1,9)
    def smart_move(self):
        pass
    def minimax(self):
        pass
    def SEF(self):
        pass