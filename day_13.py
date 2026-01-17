# Stack problems???

# Q1. Reverse a given string using stack

class stack:
    def __init__(self,string):
        self.size = len(string)
        self.stack = [0]*self.size
        self.top = -1
        self.string = string
        
    
    def push(self):
        if self.top == self.size-1:
            return
        self.top += 1
        self.stack[self.top] = self.string[self.top]

    def pop(self):
        if self.top == -1:
            return
        value = self.stack[self.top]
        self.top = self.top-1
        return value
    
    

                
def reverseString(string):
        reversed = ""
        abc = stack(string)
        for i in range(abc.size):
            abc.push()
        for j in range(abc.size):
            char = abc.pop()
            reversed += char
        return reversed

print(reverseString("Neelu"))


# Q2. Check for balanced parentheses in an expression

class Stack:
    def __init__(self,string):
        self.size = len(string)
        self.stack = [0]*self.size
        self.top = -1
        self.string = string


    def push(self):
        if self.top == self.size-1:
            return
        self.top += 1
        self.stack[self.top] = self.string[self.top]


    def pop(self):
        if self.top == -1:
            return
        value = self.stack[self.top]
        self.top = self.top-1
        return value
    

def isBalanced(string):
    pair = {
        "{": "}",
        "[" : "]",
        "(": ")"
    }

    if len(string) % 2 != 0:
        return False
    else:
        abc = Stack(string)
        for i in range(abc.size // 2):
            abc.push()

        mid = abc.size // 2 - 1

        for j in range(mid+1,abc.size):
            char = abc.pop()
            if pair.get(char) != string[j]:
                return False
        return True
    

print(isBalanced("{[()]}"))  # True
print(isBalanced("{[(])}"))  # False
print(isBalanced("{{[[(())]]}}"))  # True
