# Simple Queue

# Working :
# Insert -> pichhhe se (rear)
# Delete -> Aage se    (front)

# Problems :
# enqueue -> [_ , _ , 30, 20] <- dequeue 
# space waste


# printer queue, Task Scheduling, BFS(conceptually)


# Type 2 Queue (Circular Queue)

# [_ , _ , 30, 20] -> [30,20, _ , _ ]

# (rear + 1) % size
# Conditions 
# Full ---> (rear+1)%size == front
# Empty --> front == -1

# CPU scheduling
# Memory management
# Streaming buffer

# Code

class CircularQueue:
    def __init__(self,size):
        self.arr = [0]*size
        self.size = size
        self.front = -1
        self.rear = -1

    def enqueue(self,x):
        if (self.rear+1) % self.size == self.front:
            print("Queue is full")
            return
        
        if self.front == -1:
            self.front = 0

        self.rear = (self.rear + 1) % self.size
        self.arr[self.rear] = x


    def dequeue(self):
        if self.front == -1:
            print("Queue is Empty")
            return
        
        val = self.arr[self.front]

        if self.front == self.rear:
            self.front = self.rear = -1

        else:
            self.front = (self.front+1) % self.size

        return val


# DE-QUEUE ( Double Ended queue):

# Type : 
# 1. Input Restricted : input ek hi end jayeaga aur output dono taraf se nikalenge
# 2. Output Restricted : output ek hi trf se niklega aur input dono trf se jaa skta h

# Operations: 
#  1. insertFront 
#  2. insertRear
#  3. deleteFront
#  4. deleteRear

# Use cases: 
# Sliding Window
# Undo/Redo
# Palindrome checking


class Dequeue:
    def __init__(self,size):
        self.arr = [0] * size
        self.size = size
        self.front = -1
        self.rear = -1

    
    def insert_front(self,x):
        if (self.front == 0 and self.rear == self.size-1) or (self.front == self.rear+1):
            print("DEQUEUE IS FULL")
            return
        
        if self.front == -1:
            self.front = self.rear = 0

        elif self.front == 0:
            self.front = self.size - 1

        else:
            self.front -= 1

        self.arr[self.front] = x


    def insert_rear(self,x):
        if (self.front == 0 and self.rear == self.size-1) or (self.front == self.rear+1):
            print("DEQUEUE IS FULL")
            return
        
        if self.rear == -1:
            self.rear = self.front = 0

        elif self.rear == self.size-1:
            self.rear = 0

        else:
            self.rear += 1

        self.arr[self.rear] = x

    def delete_front(self):
        if (self.front == -1):
            print("DEQUEUE IS EMPTY")
            return
        
        val = self.arr[self.front]

        if self.front == self.rear:
            self.front = self.rear = -1

        elif self.front == self.size-1:
            self.front = 0
        
        else:
            self.front += 0

        return val
    

    def delete_rear(self):
        if (self.rear == -1):
            print("DEQUEUE IS EMPTY")
            return
        val = self.arr[self.rear]
        if self.rear == self.front:
            self.rear = self.front = -1

        elif self.rear == 0:
            self.rear = self.size-1

        else:
            self.rear -= 1

        return val