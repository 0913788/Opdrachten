class AdvancedLinkedListHandler():
    def __init__(self):
        self.list=Empty()
        self.beginNode=self.list

    #TODO set the list variable to the next element.
    def Next(self):
        self.list= self.list.tail

    #TODO set the list variable to the begin of the.  
    def Reset(self):
        pass
    
    #TODO return the isEmpty status of the list variable.
    def Empty(self):
        pass  

    #TODO return the current head of the list variable.
    def GetCurrentHead(self):
        pass
    
    #TODO return the current node of the list variable.
    def GetCurrentNode(self):
        pass

    #TODO set the given node as the Begin node of the ListHandler        
    def SetBeginNode(self, node):
        pass

    #TODO Search for a node with a specific value, if it is found return true else reset and return false.
    def SearchSpecific(self, value):
        self.Reset()
        #FIX
        while():
            #FIX
            if():
                return True
            else: 
                self.Next()
        self.Reset()
        return False
    
    #TODO Remove the current node whatever his position may be.
    def RemoveCurrentNode(self):
        #FIX
        tmp=
        #FIX
        if():
            self.Next()
            self.SetBeginNode(self.GetCurrentNode())
        else:
            self.Reset() 
            #FIX   
            while():
                if(self.GetCurrentNode()==tmp):
                    break
                else:
                    #FIX
                    tmpBeforeNode=
                    self.Next()
            #FIX
            tmpBeforeNode.tail =
        tmp.tail=None        
        self.Reset()

    #TODO add a new node to the list variable.
    def AddNewNode(self, head):
        if(self.GetCurrentNode() == self.beginNode):
            newNode=Node(head, self.beginNode)
            self.SetBeginNode(newNode)
            self.Reset()
        else:
            #FIX
            pass
    
    #TODO Add an existing node to the list variable.
    def AddExistingNode(self, node):
        if(self.GetCurrentNode() == self.beginNode):
            node.tail = self.GetCurrentNode()
            self.SetBeginNode(node)
            self.Reset()
        else:
            #FIX
            pass

    #TODO return the amount of elements within the list variable.
    def Count(self):
        pass
        
    #TODO return a node with aspecific value. if it does not exist return None
    def GetSpecificNode(self, value):
        pass

    #TODO return TRUE if a node has been removed else return FALSE
    def RemoveSpecificNode(self, value):
        pass

    #Begin misc
    def Print(self):
        self.Reset()
        print("Your list: ", end="")
        while(not self.Empty()):
            print(self.list.head, end=" ")
            self.Next()
        self.Reset()
    
    def LongPrint(self):
        print(self.list)
    #End misc
 
        
class Empty():
    def __init__(self):
        self.isEmpty = True
    
    def __str__(self):
        return "[]"

class Node():
    def __init__(self, head, tail):
        self.isEmpty = False
        self.head = head
        self.tail = tail

    def __str__(self):
        return "[Node: [Head: {}],[Tail-->{}".format(self.head, self.tail)