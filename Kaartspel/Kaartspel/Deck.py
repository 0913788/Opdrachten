from Stack import *
from Card import *

class Deck(Stack):
    def __init__(self, amount=None):
        super().__init__("card")
        self.baseAmount = amount
        if(amount!=None):
            self.CreateDeck(amount)

    #TODO returns the top node (card) of a deck.
    def DrawCard(self):
        pass

    #TODO Creates cards and adds these to the linked list.
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
    
    #Prints the whole deck to the console.
    def PrintDeck(self):
        while(not self.Empty()):
            print(self.GetCurrentValue().ToString())
            self.Next()
        self.Reset()

    #TODO
    def ChangeDeck(self, deck): pass