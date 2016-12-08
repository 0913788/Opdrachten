from Deck import *
from Players import *
import os

class Game():
    def __init__(self, amountOfPlayers, amountOfDecks):
        self.players = Players(amountOfPlayers)
        self.deck=Deck(amount=amountOfDecks)
        self.playedDeck=Deck()
        self.activePlayer=self.players.GetCurrentValue()

    def ClearScreen(self):
        os.system("cls")

    def SetStartConditions(self):
        for i in range(7):
            while(not self.players.Empty()):
                self.players.GetCurrentValue().DrawCard(self.deck.DrawCard())
                self.players.Next()
            self.players.Reset()
        self.playedDeck.AddExistingNode(self.deck.DrawCard())
    
    #TODO
    def PrintBase(self):
        #Change the type, not the string...
        lastCard="Change me"      
        print("Last played card: " + lastCard.ToString())
        print("Active player: "+self.activePlayer.name)
        print("Your hand: ")
        self.activePlayer.hand.PrintHand()
    
    #TODO 
    def PlayerAction(self):
        x= input("enter to continue")
        self.ClearScreen()  

    #TODO
    def SwitchTurn(self):
        self.players.Next()
        #If what?
        if():
            self.players.Reset()
        self.activePlayer=self.players.GetCurrentValue()
        input("switch to player {}. Press enter to continue".format(self.players.GetCurrentValue().name))
    
    #TODO
    def GameLoop(self):
        while(True):
            self.PrintBase()
            self.PlayerAction()
            self.SwitchTurn()
    
    #TODO
    def Run(self):
        self.RandomizePlayerOrder()
        self.SetStartConditions()
        self.GameLoop()
    
    #TODO
    def RandomizePlayerOrder(self): pass