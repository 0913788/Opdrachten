from NodeAndEmpty import *

def opdracht1(a):
    r = []
    while(a>0):
        if(a%2==0):
            r.append(a)
        a=a-1
    return r
opd1 = opdracht1(5)

def opdracht2(a):
    r = []
    for i in range(len(a)):
        if(a[i]%2==0):
            r.append(a[i])
    return r
opd2 = opdracht2([0,1,2,3,4]) 

def opdracht3(a):
    r = Empty()
    while(not a.isEmpty):
        if(a.head%2==0):
            r = Node(a.head, r)
    return r
opdracht3(Node(2, Node(5, Node(86, Node(101,Empty())))))

def opdracht4(a,f):
    if(not a.isEmpty):
        if(f(a.head)):
            return Node(a.head, opdracht4(a.tail, f))
        return opdracht4(a.tail,f)   
    return a
opd4=opdracht4(Node(2, Node(5, Node(86, Node(101,Empty())))), lambda x: x%2==0)