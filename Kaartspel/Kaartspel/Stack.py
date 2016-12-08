from Node import *
from Empty import *

class Stack():
    def __init__(self, typeOfStack):
        self.items=Empty()
        self.stackType= typeOfStack
        self.headNode = self.items

    def Next(self): self.items = self.items.tail
 
    #TODO
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

    #TODO    
    def AddExistingNode(self, node): pass

    #TODO
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

    #TODO
    def SetHeadNode(self,node): pass

    #TODO    
    def GetCurrentNode(self): pass

    #TODO    
    def GetCurrentValue(self): pass

    #TODO
    def Reset(self): pass
    
    #TODO
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