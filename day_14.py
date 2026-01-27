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

# 