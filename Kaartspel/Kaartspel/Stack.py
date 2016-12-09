from Node import *
from Empty import *

class Stack():
    def __init__(self, typeOfStack):
        self.items=Empty()
        self.stackType= typeOfStack
        self.headNode = self.items

    # Get the next item from the linked list.
    def Next(self): self.items = self.items.tail
 
    #TODO Adds a new node, build up from a given value, to the linked list.
    def AddNewNode(self, value):
        #Change the type, not the string...
        newNode="Change me"
        #If what?
        if():
            self.SetHeadNode(newNode)
            self.items=newNode
            self.Reset()
        else:
            tmp=self.items
            self.Reset()
            while(tmp!=self.items):
                newTmpHead=self.items
                self.Next()
            newTmpHead.tail = newNode
            self.Reset()      

    #TODO Adds an existing node to the linked list.
    def AddExistingNode(self, node): pass

    #TODO Removes the current node in the linked list.
    def RemoveCurrent(self):
        #Change the type, not the string... 
        tmp ="Change me"
        if(tmp == self.headNode):
            self.Next()
            self.SetHeadNode(self.items)
        else:
            self.items = self.headNode
            while(self.items != tmp):
                newTmpHead= self.items
                self.Next()
            newTmpHead.tail = tmp.tail         
        tmp.RemoveTail()

    #TODO Sets a new headNode (begin of the linked list)
    def SetHeadNode(self,node): pass

    #TODO Returns the current node of the linked list.
    def GetCurrentNode(self): pass

    #TODO Returrns the current value of a node within the linked list.
    def GetCurrentValue(self): pass

    #TODO Set the position of the linked list to the first node (begin)
    def Reset(self): pass
    
    #TODO Return if a node is empty.
    def Empty(self): pass

    #TODO    
    def RemoveSpecific(self, values): pass
    
    #TODO
    def Shuffle(self): pass
      
    #TODO
    def Order(self, ordering="value"): pass
    
    #TODO
    def Count(self): pass
    
    #TODO
    def SearchSpecific(self, values): 
        if(self.stackType=="card"):
            pass
        elif(self.stackType=="player"):
            pass
        else:
            pass   