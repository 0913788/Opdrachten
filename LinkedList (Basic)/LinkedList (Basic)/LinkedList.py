class BasicLinkedListHandler():
    def __init__(self):
        self.list=Empty()
        self.beginNode=self.list

    #TODO set the list variable to the next element.
    def Next(self):
        pass

    #TODO set the list variable to the begin of the.  
    def Reset(self):
        pass
    
    #TODO return the isEmpty status of the list variable.
    def Empty(self):
        pass
    
    #TODO Repair the method; Add a new node to the "top" of the list. (list = 1|-> 2|->[] 
    #                                                                  list.AddNewNode(4)  = 4|-> 1|-> 2|->[])
    def AddNewNode(self, head):
        #FIX Change the newNode into something more usefull.
        newNode="change me"
        self.SetBeginNode(newNode)
        self.Reset()

    #TODO get the current head of the list variable.
    def GetCurrentHead(self):
        pass

    #TODO set the given node as the beginNode variable        
    def SetBeginNode(self, node):
        pass
    
    #TODO Check if a given value is present within the list variable.
    def PresentCheck(self, value):
        #FIX While what?
        while():
            #FIX If .. ==value?
            if(==value):
                print("{} is present within the list.".format(value))
                return
            self.Next()
        print("{} is not present within the list".format(value))
        #FIX Dont forget to...
        self.

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