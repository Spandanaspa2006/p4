class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Circullarll:
    def __init__(self):
        self.head=Node(None)
        self.head.next=self.head
    def append(self,data):
        newnode=Node(data)
        if (self.head == None):
            self.head = newnode
            newnode.next = self.head
            return
        else:
            temp = self.head
            while (temp.next != self.head):
                temp = temp.next
            temp.next = newnode
            newnode.next = self.head
    def display(self):
        current=self.head
        if self.head is None:
            print("List is Empty")
            return
        else:
            print("Node in Linkedlist are")
            while (current.next!=self.head):
                current=current.next
                print (current.data)
    def deletenode(self, key):
        temp = self.head
        if temp.next is not temp:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        while temp.next is not self.head:
            if temp.data is key:
                break
            prev = temp
            temp = temp.next
        if temp == self.head:
            return
        prev.next = temp.next
a=Circullarll()
a.append(1)
a.append(3)
a.append(4)
a.display()
a.append(2)
a.deletenode(2)
print("After deleting the element")
a.display()