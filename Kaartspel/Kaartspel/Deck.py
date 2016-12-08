from Stack import *
from Card import *

class Deck(Stack):
    def __init__(self, amount=None):
        super().__init__("card")
        self.baseAmount = amount
        if(amount!=None):
            self.CreateDeck(amount)

    #TODO 
    def DrawCard(self):
        pass

    def CreateDeck(self, amount):
        types = ["Harten", "Ruiten", "Schoppen", "Klaver"]
        values = [2,3,4,5,6,7,8,9,10,"B","Q","K","A"]
        for x in range(amount):
            for i in range(len(types)):
                for j in range(len(values)):
                    #add something
                    pass
        for i in range(2):
            self.AddNewNode(Card("Joker",""))

    def PrintDeck(self):
        while(not self.Empty()):
            print(self.GetCurrentValue().ToString())
            self.Next()
        self.Reset()

    #TODO
    def ChangeDeck(self, deck): pass