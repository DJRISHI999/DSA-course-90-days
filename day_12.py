# Stack and Queue

## Stack :
#  Properties: 1. behaves like continuous memory 
#              2. Pointer is on top elemnt always
#              3. basically it follows LIFO or FILO
#              4. Only one element can be accessed to put in or to put out at a time


# Operations: 
# 1. Push: add only one element at a time on the top
# 2. Pop: remove only one element at a time from the top
# 3. Seek/peek/top: it sees top element
# 4. isEmpty: it sees that stack is empty or not


# Keywords : 
# 1. Stack Overflow : agr ham ek full stack me ek aur element add krna chahte h to hame ek error milta h jisme ham "Stack OverFlow" kehte h.

# 2. Stack underflow : agr ham ek empty stack me jabardasti ek aur element nikalana chahte h to wo hame ek error deta hai jiska naam hai "Stack Underflow".

class Stack:
    def __init__(self,size):
        self.stack = [0] * size
        self.top = -1
        self.size = size

    def push(self,value):
        if self.top == self.size-1:
            print(f"Bhai Stack Overflow hai")
            return
        self.top = self.top+1
        self.stack[self.top] = value

    def pop(self):
        if self.top == -1:
            print("Bhai stack underflow hai means khali hai already")
            return
        
        value = self.stack[self.top]
        self.top = self.top-1
        return value
    
    def peek(self):
        if self.top == -1:
            return None
        
        return self.stack[self.top]
    
    def isEmpty(self):
        return self.top == -1
    


stack = Stack(5)

stack.push("N")
stack.push("e")
stack.push("e")
stack.push("l")
stack.push("u")
stack.push("LOL") # Stack overflow


print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.peek())

print(stack.isEmpty())


# Queue : Line A->B->C->D

#  Properties: 1. behaves like continuous memory 
#              2. Pointer is on top and last
#              3. basically it follows FIFO or LILO
#              4. Only one element can be accessed to put in or to put out at a time


# Operations: 
# 1. Enqueue: Adds one element in the last of the queue
# 2. Dequeue: Removes fisrt element from the queue
# 3. Front: sees the very first element of the queue
# 4. Rear: sees the last element of the queue
# 5. isEmpty: checks if queue is empty


# Keywords : 
# 1. Queue Overflow : agr ham ek full queue me ek aur element add krna chahte h to hame ek error milta h jisme ham "Queue Overflow" kehte h.

# 2. Queue Underflow : agr ham ek empty queue me jabardasti ek aur element nikalana chahte h to wo hame ek error deta hai jiska naam hai "Queue Underflow".



# class Queue:
#     def __init__(self,size):
#         self.queue = [0] * size
#         self.front = 0
#         self.rear = -1
#         self.size = size
#         self.count = 0

#     def enqueue(self,value):
#         if self.count == self.size:
#             print("Bhai jagah nhi hai baad me aana ")
#             return
        
#         self.rear += 1
#         self.queue[self.rear] = value
#         self.count += 1


#     def dequeue(self):
#         if self.count == 0:
#             print("Queue is underflow")
#             return
        
#         value = self.queue[self.front]
#         self.front += 1
#         self.count -= 1
#         return value
    

#     def isEmpty(self):
#         return self.count == 0
    

# shadi_ki_line = Queue(5)

# shadi_ki_line.enqueue("Akash")
# shadi_ki_line.enqueue("sneha")
# shadi_ki_line.enqueue("Dhruv")
# shadi_ki_line.enqueue("Anjali")
# shadi_ki_line.enqueue("Nilu")
# shadi_ki_line.enqueue("Nilu ki roommate")


# print(shadi_ki_line.dequeue())
# print(shadi_ki_line.dequeue())
# print(shadi_ki_line.dequeue())
# print(shadi_ki_line.dequeue())


# print(shadi_ki_line.queue[shadi_ki_line.front])






