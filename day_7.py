# arrays 
'''
--> Data-structure
--> continuous
--> same type of data saved 
'''


'''
arr = [4,5,6]
arr = [using indexing] --> 0 to len(arr)-1
'''


# # accessing elements of an array
# arr = [4,5,6]
# for i in range(len(arr)):   
#     print(arr[i])

# problem 1: find the sum of all the elements of the array
# arr = [10,20,30,40,50]

# total = 0
# for i in range(len(arr)):
#     total = total + arr[i]

# print(f"sum of elements: {total}")

# Problem 2: find the largest element in the array

# arr = [80,10,50,490,150]
# largest = arr[0]

# for i in range(len(arr)):
#     if largest < arr[i]:
#         largest = arr[i]
#     else:
#         pass

# print(f"the largest number in the array is {largest}")

# Problem 3: count even numbers in an array
# arr = [1,2,3,4,5,6,7,8,9,10]
# count = 0

# for i in range(len(arr)):
#     if arr[i] % 2 == 0:
#         count += 1


# print(f"Total even numbers in the array is {count}")

# # Problem 4: reverse the array
# arr = [1,2,3,4,5,6,7,8,9,10]
# count = len(arr)-1
# i = 0
# while i < count:
#     temp = arr[i]
#     arr[i] = arr[count]
#     arr[count] = temp
#     i += 1
#     count -= 1

# print(arr)

# Problem 5: find an element from the array
# arr = [4,8,2,9]
# target = 2
# found = 0
# for i in range(len(arr)):
#     if arr[i] == target:
#         print(f"Found your target at index {i}")
#         found = 1
#         break
#     else:
#         pass

# if found == 0:
#     print("Cant Found the Element its not there in the array")

