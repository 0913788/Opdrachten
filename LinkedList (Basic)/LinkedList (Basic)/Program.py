#uit bestand "LinkedList" importeer alles (*)
from LinkedList import *
#uit het bestand "random" importeer alleen "randint"
from random import randint

#Vult een linked list handler met random getallen
def FillHandler(l):
    printString = "Adding order: "
    for i in range(4):
        x=randint(10,30)
        printString+="{} ".format(x)
        l.AddNewNode(x)
    print(printString)

#Main program
basicLinedkList = BasicLinkedListHandler()
FillHandler(basicLinedkList)
print("")
basicLinedkList.Print()
print("\n")
print("Detailed info:")
basicLinedkList.LongPrint()
print("")
print("Checking some numbers:")
for i in range(3):
    basicLinedkList.PresentCheck(randint(10,30))