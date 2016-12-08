from Stack import *

class Hand(Stack):
    def __init__(self):
        super().__init__("cards")
    
    def PrintHand(self):
        while(not self.Empty()):
            print(self.GetCurrentValue().ToString())
            self.Next()
        self.Reset()
            
    #TODO        
    def PlayCard(self, type, value): pass
    
    