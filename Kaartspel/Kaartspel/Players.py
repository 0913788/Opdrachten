from Stack import *
from Player import *

class Players(Stack):
    def __init__(self, amount):
        super().__init__("player")
        self.CreatePlayer(amount)
    
    #TODO    
    def CreatePlayer(self, amount):
        for i in range(amount):
            #Create a player
            pass
        