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
        new_node.next = self.head


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
    
    def find_middle(self):
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow.data
    

    def find_cycle(self):
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return "Cycle Found !!!!"
            
        return "Cycle not found"
    

    def find_cycle_start_point(self):
        slow = self.head
        fast = self.head
        # detect cycle 
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break # instead of returning that cycle is detected we will break loop and let the pointers be there 

        else: 
            return None # this is when we couldn't detect cycle
        

        slow = self.head # move slow pointer to head and fast pointer will be there at meet point

        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow.data
    

    def loop_length(self):
        slow = self.head
        fast = self.head
        # detect cycle 
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break # instead of returning that cycle is detected we will break loop and let the pointers be there 

        else: 
            return None # this is when we couldn't detect cycle
        

        slow = self.head # move slow pointer to head and fast pointer will be there at meet point

        while slow != fast:
            slow = slow.next
            fast = fast.next

        fast = fast.next
        length = 1
        while slow != fast:
            fast = fast.next
            length += 1

        return length
        


ll = LinkedList()

ll.insertAtBegin(10)

ll.insertEnd(20)

ll.insertAtPosition(15,3)

# ll.display()

# print(ll.find_middle())

print(ll.find_cycle())
print(ll.find_cycle_start_point())
print(ll.loop_length())

# ll.deleteAtPosition(2)
# ll.deleteEnd()
# ll.deleteStart()

# ll.display()



# Fast and Slow pointer :

# ham head se start krenge dono ko 
#  dono aage badte jayenge 
# Fast wala thoda fast aage badega maan lo 2 steps at one time and Slow wala dheere dheere badega maan lo 1 step at a time 

# ideally singly linked list me fast poninter hmesha aage rhega Slow pointer ke.
# but agr linkedlist ke andr cycle present h to Fast pointer kabhi na kabhi Slow pointer ko catch kr lega and tabhi hame pata chal jayega ki cycle present h

# Use cases:
'''
1. Middle of LinkedList dhundh skte h 
2. Cycle find krna
3. Cycle ka starting point
4. Palindrome
5. loop length 
'''



# palindrome...




