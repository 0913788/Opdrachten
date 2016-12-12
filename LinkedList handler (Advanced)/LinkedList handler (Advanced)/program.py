from LinkedList import *

l =AdvancedLinkedListHandler()

l.AddNewNode(5)
l.AddNewNode(1)
l.LongPrint()
print(l.Count())
print(l.RemoveSpecificNode(1))
l.RemoveSpecificNode(4)
print(l.GetSpecificNode(5).head)
l.LongPrint()