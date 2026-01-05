# sliding window


# Fixed Window Type 

# arr = [5,2,8,9,7,0,88,51,23,78]
# window_size = 3
# Left <---> Rght, [ _ , _ , _ ]
# [5,2,8]
#   [2,8,9]
#     [8,9,7]...

# Problem 1: Maximum sum of subarray of size K
# arr = [2,1,5,1,3,2]
# k = 3

# brute force

# arr = [2,1,5,1,3,2]
# k = 3

# max_sum = 0
# for i in range(len(arr)-(k+1)): # i=0,1,2
#     cur_sum = 0
#     for j in range(i,i+k): #(0,3), (1,4), (2,5)
#         cur_sum = cur_sum + arr[j] 
#     if max_sum < cur_sum:
#         max_sum = cur_sum
#     else:
#         pass

# print(max_sum)


# sliding window 

# arr = [2,1,5,1,3,2]
# k = 3
# window_sum = 0

# for i in range(k):
#     window_sum = window_sum + arr[i]

# max_sum = 0

# for j in range(k,len(arr)):
#     window_sum += arr[j]
#     window_sum -= arr[j-k]
#     if max_sum < window_sum:
#         max_sum = window_sum
#     else:
#         pass

# print(max_sum)


# Problem2: average of subarray of size k

# arr = [1,3,2,6,-1,4,1,8,2]
# k = 5

# window_sum = 0
# for i in range(k):
#     window_sum += arr[i]

# for j in range(k,len(arr)+1):
#     print(f"avg : {window_sum/k}")
#     if j < len(arr):
#         window_sum += arr[j]
#         window_sum -= arr[j-k]





#  Variable Sliding Window
# at least, at most, smallest/longest subarray, sum>= k , distinct characters, no repetition

# Problem 3 : Smallest Subarray with sum >= Target

# arr = [2,1,5,2,3,2]
# target = 7

# start = 0
# window_sum = 0
# min_len = len(arr)+1

# for i in range(len(arr)):
#     window_sum += arr[i]

#     while window_sum >= target:
#         if (min_len > i-start+1): # 5-3+1 = 3
#             min_len = i-start+1
#         window_sum = window_sum - arr[start]
#         start += 1

# print(min_len)


# Problem 4: Longest Subarray with sum<=k