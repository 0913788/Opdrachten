from Hand import *

class Player():
    def __init__(self, name):
        self.hand = Hand()
        self.name = name

    def ToString(self): return self.name
    
    #TODO
    def DrawCard(self, node): pass
    
    #TODO
    def PlayCard(self): pass
