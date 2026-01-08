class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head=None

    def append(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            print(f"Node {new_node.data} added as head at beginning")
            return
        last=self.head
        while last.next:
            last=last.next
        last.next=new_node
        print(f"Node {new_node.data} appended to the list")


    def show(self):
        current=self.head
        while current:
            print(current.data,end=" -> ")
            current=current.next
        print("None")

    def length(self):
        count=0
        length=self.head
        while length:
            count+=1
            length=length.next
        return count
    
    def delete(self,position):
        if self.head is None:
            print("List is empty, nothing to delete")
            return
        temp=self.head
        if position==0:
            self.head=temp.next
            temp=None
            print("Head node deleted")
            return
        for i in range(position-1):
            temp=temp.next
            if temp is None:
                break
        if temp is None or temp.next is None:
            print("Position out of bounds, nothing to delete")
            return
        next_node=temp.next.next
        temp.next=None
        temp.next=next_node
        print(f"Node at position {position} deleted")
    

       



l1=LinkedList()
l1.append(10)
l1.append(20)
l1.append(30)
l1.append(40)
l1.append(50)
l1.show()
l1.show()
print("Length of linked list:", l1.length())
l1.delete(0)
l1.show()
l1.delete(3)
l1.show()