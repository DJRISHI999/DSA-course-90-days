# Two Pointer Approach
# ---------->
# [5,8,7,2,10]
#  ^        ^
#  |        |
# start    end

# # Problem 1: reverse the array
# arr = [1,2,3,4,5,6,7,8,9,10]
# end = len(arr)-1
# start = 0
# while start<end:
#  arr[start], arr[end] = arr[end], arr[start]
#     start += 1
#     end -= 1
# print(arr)

# Problem 2: Check palindrome

# MOM -> MOM (palindrome)

# arr = [1,2,3,2,1]

# # pointer
# start = 0
# end = len(arr)-1

# is_palindrome = True

# while start<end:
#     if arr[start] != arr[end]:
#         is_palindrome = False
#         break
#     else:
#         pass
#     start += 1
#     end -= 1

# if is_palindrome:
#     print("Yes it is a palindrome")
# else:
#     print("No its not")


# Problem3 : Count pairs with given sum
# given : sorted array, target sum
# arr = [0,2,3,5,6]
# target = 7
# count = 0
# start = 0
# end = len(arr)-1

# while start<end:
#     if arr[start] + arr[end] == target:
#         count = count + 1
#         start += 1
#         end -= 1
#     elif arr[start] + arr[end] < target:
#         start += 1
#     else:
#         end -= 1

# print(f"there are {count} number of pairs for {target} as sum")

# PROBLEM 4: Seperate even and odd
# PROBLEM 5: Move all zeros to the end of the array










