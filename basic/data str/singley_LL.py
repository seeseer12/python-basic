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
    
    # def delete(self,index):
    #     delete=self.head
    #     count=0
    #     if delete is None:
    #         print("List is empty, nothing to delete")
    #         return
    #     if index==0:
    #         self.head=self.head.next
    #         delete=None
    #         return
            
    #     while index is not count:
    #         prev=delete
    #         delete=delete.next
    #         count+=1    
    #     prev.next=delete.next
    #     delete=None
    #     return

       



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
l1.delete(2)
l1.show()