# searching :

# Types : 1. Linear
#         2. Binary

# Lamen searching/ Linear search/ brute-force

# when to use:
# 1. unsorted
# 2. small input
# 3. simple logic

# arr = [4,2,7,1,9],  target = 7
#       ---> ^

# Linear search Program: 

# def linear_Search(arr,target):
#     for i in range(0,len(arr)):
#         if arr[i] == target:
#             return i
#         else:
#             pass
#     return -1

# arr = [4,2,7,1,9]
# target = 7
# result = linear_Search(arr,target)
# if result != -1:
#     print(f"We found the element at {result}")
# else:
#     print(f"{target} Not Found !!")

# Best case complexity: O(1)
# Worst case : O(n)


# Binary search : 
# 1. Sorted Array

# Logic: 
# "Middle element dekho"
# 1. Agr chhota hai -> right jao
# 2. Agr bada hai to -> left jao

# def binary_search(arr,target):
#     low = 0
#     high = len(arr)-1

#     while low<=high:
#         mid = (low+high)//2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             low = mid+1
#         else:
#             high = mid-1
#     return -1


# arr = [1,3,5,7,9,11]
# target = 7

# result = binary_search(arr,target)
# if result != -1:
#     print(f"We found the element at {result}")
# else:
#     print(f"{target} Not Found !!")

# Problem 1: Binary search recursive
# Problem 2: Count the occurences of element
# Problem 3: First and last occurence of an element

# Best case of Binary Search: O(1)
# Worst case of Binary Search: O(log n)


# recursion se binary search

def binary_search(arr,target,low,high):
    
    if low > high:
        return -1
    
    mid = low + (high-low) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr,target,mid+1,high)
    else:
        return binary_search(arr,target,low,mid-1)

arr = [1,3,5,7,9,11]
target = 7

print(binary_search(arr,target,0,len(arr)-1))
