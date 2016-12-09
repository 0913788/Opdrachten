from Deck import *
from Players import *
import os

class Game():
    def __init__(self, amountOfPlayers, amountOfDecks):
        self.players = Players(amountOfPlayers)
        self.deck=Deck(amount=amountOfDecks)
        self.playedDeck=Deck()
        self.activePlayer=self.players.GetCurrentValue()

    #Clears the CL.
    def ClearScreen(self):
        os.system("cls")
    
    #Sets up the starting conditions of the game. (7 cards for each player and 1 played card)
    def SetStartConditions(self):
        for i in range(7):
            while(not self.players.Empty()):
                self.players.GetCurrentValue().DrawCard(self.deck.DrawCard())
                self.players.Next()
            self.players.Reset()
        self.playedDeck.AddExistingNode(self.deck.DrawCard())
    
    #TODO Prints the basic ui.
    def PrintBase(self):
        #Change the type, not the string...
        lastCard="Change me"      
        print("Last played card: " + lastCard.ToString())
        print("Active player: "+self.activePlayer.name)
        print("Your hand: ")
        self.activePlayer.hand.PrintHand()
    
    #TODO Defines player actions.
    def PlayerAction(self):
        x= input("enter to continue")
        self.ClearScreen()  

    #TODO Switches the active player to the next player in the list.
    def SwitchTurn(self):
        self.players.Next()
        #If what?
        if():
            self.players.Reset()
        self.activePlayer=self.players.GetCurrentValue()
        input("switch to player {}. Press enter to continue".format(self.activePlayer.name))
    
    #TODO Basic gameloop.
    def GameLoop(self):
        while(True):
            self.PrintBase()
            self.PlayerAction()
            self.SwitchTurn()
    
    #TODO Game "Run" function.
    def Run(self):
        self.RandomizePlayerOrder()
        self.SetStartConditions()
        self.GameLoop()
    
    #TODO Randomize the player order.
    def RandomizePlayerOrder(self): pass