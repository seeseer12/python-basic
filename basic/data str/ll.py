# implementing linked list in python
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
llist1=linkedlist()
llist1.head=node(1) 
second=node(2)
third=node(3)   
llist1.head.next=second
second.next=third   
llist1.printlist()
# Output:
# 1
# 2
# 3