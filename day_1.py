
# for i in range(n): # i ---> 
#     for j in range(m): # j -----> 1,2,3,4,5
#         print(j)

# n = 5, m = 5

# i ---> 1 to 5

# i -> 1 , j ----> 5 + 5 + 5 + 5 + 5

# i = 1
# n = 4
# count = 0
# while i<n:
#     count += 1
#     print(count)
#     i = i*2 


# 2^x = 16
# n
# operations = log2(16)


# i = 729
# count = 0
# while i>1:
#     count += 1
#     print(count)
#     i = i//3

#  i ---> 8 divide 2 = 4
#  i ---> 4 divide 2 = 2
#  i ---> 2 divide 2 = 1


# constant time complexity
# O(1)

# O(100n) and O(5n)
# O(n)

# 10

# 100*100 = 10000

# 5*100 = 500

def copy(arr):
    new = []
    for x in arr:
        new.append(x)


i = 1
count = 0
n = 81
while i<= n:
    i = i*3
    count += 1
    print(count)
# time complexity = ?
# How many steps for n = 81?

def f(n):
    if n==1:
        return
    f(n-1)
# Time ?
# Space ?
