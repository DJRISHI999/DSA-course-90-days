# LinkedList : 
#  first Node (head) -> Second Node -> Third Node -> ... -> Last Node -> Null/None

# Node ke andr : Data + next ka address

# Types:
#  1. Singly Linked List
#  2. Doubly Linked List


# Singly linked List

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


    def insertAtBegin(self,data):
        new_node = Node(data) 

        new_node.next = self.head

        self.head = new_node


    def insertEnd(self,data):
        
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.next = new_node


    def insertAtPosition(self,data,pos):
        new_node = Node(data)

        if pos == 0:
            self.insertAtBegin(data)
            return
        
        temp = self.head
        i = 0
        while temp is not None and i < pos-1:
            temp = temp.next
            i += 1

        if temp is None:
            print("Position Out of Range")
            return
        
        new_node.next = temp.next
        temp.next = new_node


    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end = " -> ")
            temp = temp.next

        print("None")

    def deleteStart(self):
        if self.head is None:
            print("No element in LL")
            return 
        
        temp = self.head
        self.head = temp.next

        return self.head
    

    def deleteEnd(self):
        if self.head is None:
            print("No element in LL")
            return 
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next

        value = temp.next
        temp.next = None

        return value
    

    def deleteAtPosition(self,pos):
        if self.head is None:
            print("No element in LL")
            return 
        
        if pos == 0:
            self.deleteStart()

        temp = self.head
        i = 0
        while temp.next is not None and i < pos-1:
            temp = temp.next
            i += 1


        if  temp.next is None:
            print("position out of range")
            return
        
        value = temp.next
        temp.next = temp.next.next
        return value


ll = LinkedList()

ll.insertEnd(20)
ll.insertEnd(30)

ll.insertAtBegin(10)

ll.insertAtPosition(15,3)

ll.display()

ll.deleteAtPosition(2)
ll.deleteEnd()
ll.deleteStart()

ll.display()




# Deletion from LinkedList

