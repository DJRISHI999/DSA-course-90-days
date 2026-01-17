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

# class Stack:
#     def __init__(self,string):
#         self.size = len(string)
#         self.stack = [0]*self.size
#         self.top = -1
#         self.string = string


#     def push(self):
#         if self.top == self.size-1:
#             return
#         self.top += 1
#         self.stack[self.top] = self.string[self.top]


#     def pop(self):
#         if self.top == -1:
#             return
#         value = self.stack[self.top]
#         self.top = self.top-1
#         return value
    

# def isBalanced(string):
#     pair = {
#         "{": "}",
#         "[" : "]",
#         "(": ")"
#     }

#     if len(string) % 2 != 0:
#         return False
#     else:
#         abc = Stack(string)
#         for i in range(abc.size // 2):
#             abc.push()

#         mid = abc.size // 2 - 1

#         for j in range(mid+1,abc.size):
#             char = abc.pop()
#             if pair.get(char) != string[j]:
#                 return False
#         return True
    

# print(isBalanced("{[()]}"))  # True
# print(isBalanced("{[(])}"))  # False
# print(isBalanced("{{[[(())]]}}"))  # True


# Q3 Evaluate a postfix expression using stack
#  Input : "23*54*+9-"
#  OutPut : 17


class Stack:
    def __init__(self,expression):
        self.size = len(expression)
        self.stack = [0] * self.size
        self.top = -1
        self.exp = expression
        self.count = 0
        self.operands = ["*","+","/","-"]

    def push(self):
        if self.top == self.size-1:
            return
        
        self.top += 1
        self.stack[self.top] = self.exp[self.count]
        self.count += 1
        print(f"Pushed: {self.exp[self.count-1]}, Stack: {self.stack[:self.top+1]}")

    
    def peek(self):
        if self.stack[self.top] in self.operands:
            return True
        else:
            return False
        
    def push_after_operation(self,value):
        self.top += 1
        self.stack[self.top] = value
        print(f"Pushed after operation: {value}, Stack: {self.stack[:self.top+1]}")

    

    def pop(self):
        if self.top == -1:
            return
        value = self.stack[self.top]
        print(f"Popped: {value}, Stack before pop: {self.stack[:self.top+1]}")
        self.top -= 1
        return value
    


def Calucate(exp):
    stack = Stack(exp)
    
    while stack.count < stack.size:
        stack.push()
        
        if stack.peek():
            print(f"\nFound operator: {stack.stack[stack.top]}")
            operation = stack.pop()
            operand2 = int(stack.pop())
            operand1 = int(stack.pop())
            print(f"Calculating: {operand1} {operation} {operand2}")
            
            if operation == "+":
                result = operand1 + operand2
            elif operation == "-":
                result = operand1 - operand2
            elif operation == "*":
                result = operand1 * operand2
            elif operation == "/" and operand2 != 0:
                result = operand1 / operand2
            else:
                result = 0
            
            print(f"Result: {result}")
            stack.push_after_operation(result)
    
    final_result = stack.pop()
    print(f"\nFinal Answer: {final_result}")
    return final_result



print(Calucate("23*54*+9-"))



# Stack Span Problem:
# Prices: [100 80 60 70 60 75 85]
# Span:   [1    1  1  2  1  4  6] 