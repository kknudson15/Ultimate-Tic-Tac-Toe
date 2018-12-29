class Player:

    def __init__(self):
        self.marker = 'x'
    def make_move(self):
        return int(input("what space would you like to move to (1-9)"))
    def set_marker(self, marker):
        self.marker = marker
    def get_marker(self):
        return self.marker
