# sorting
# sorting ke types : 
# 1. Comparison based 
# 2. Non-comparison based

# sorting ke more types:
# 1. In-place
# 2. Out-place

# Comparision based:
'''
1. Bubble Sort
2. Selection
3. Insertion
4. Merge
5. Quick
6. Heap

'''
# Non-comparison:
'''
1. Count Sort
2. Radix Sort
3. Bucket Sort

'''

# In-place:
'''
1. Bubble
2. Selection
3. Insertion
4. Quick
5. Heap

'''

# Out-place
'''
Radix
Count
Merge

'''

# Count Sort

# arr = [1,3,2,3,1]

# # range dekho
# min = 1
# max = 3

# # Count array banao jisme har element ka index ke hisaab se count rakho
# index : 0 1 2 3
# count : 0 2 1 2

# # sorted array
# 1 -> 2 times
# 2 -> 1 time 
# 3 -> 2 times

# sorted_arr = [1,1,2,3,3]

# def count_sort(arr):
#     min = 0
#     max = 0

#     for i in range(len(arr)):
#         if arr[i] >= min:
#             pass
#         else:
#             min = arr[i]
    
#     for j in range(len(arr)):
#         if arr[j] <= max:
#             pass
#         else:
#             max = arr[j]

#     count = [0] * (max+1) #count = [0,0,0,0]

#     for num in arr:
#         count[num] = count[num] + 1

#     traversing_counter = 0
#     sorted_arr = [0,0,0,0,0]
#     for i in range(len(count)):
#         while count[i] > 0:
#             print(f"traversing_counter {traversing_counter}")
#             print(f"value of count at {i}th index: {count[i]}")
#             sorted_arr[traversing_counter] = i
#             traversing_counter = traversing_counter + 1
#             count[i] = count[i]-1

#     return sorted_arr
        
# arr = [1,3,2,3,1]
# print(count_sort(arr))



# # Radix sort : non - comparison and outplace 

# arr = [170,45,75,90,802]

# # ones place:
# '''
# 170 --> 0
# 45 ---> 5
# 75 ---> 5
# 90 ---> 0
# 802 --> 2
# '''

# # grouping numbers with same digit

# '''
# 0 --> 170, 90
# 2 --> 802   
# 5 --> 45, 75
# '''

# pass_one_arr = [170,90,802,45,75]

# # Tens place:
# '''
# 170 --> 7
# 90 ---> 9
# 802 ---> 0
# 45 ---> 4
# 75 --> 7
# '''

# # grouping now basis of tens place

# '''
# 0 --> 802
# 4 --> 45
# 7 --> 170, 75
# 9 --> 90
# '''

# pass_two_arr = [802,45,170,75,90]

# # hundred place
# '''
# 802 --> 8
# 45 ---> 0
# 170 --> 1
# 75 ---> 0
# 90 ---> 0
# '''

# # grouping with hundred place

# '''
# 0 --> 45, 75, 90
# 1 --> 170
# 8 --> 802
# '''

# pass_three_arr = [45,75,90,170,802]


# Program of Radix sort

# def get_max(arr):
#     max_val = arr[0]
#     for i in range(1,len(arr)-1):
#         if arr[i] > max_val:
#             max_val = arr[i]
#         else:
#             pass

#     return max_val

# 50 = 50 // 10 = 
# 5 % 10 = 5 


# 5418412 = 5418412 // 100000 = 54 % 10 = 4

# def count_sort(arr,exp):
#     n = len(arr)
#     output = [0] * n
#     count = [0] * 10
    
#     for i in range(0,n):
#         digit = (arr[i] // exp) % 10
#         count[digit] += 1

#         # [2,0,1,0,0,2,0,0,0,0]

# # count = [2,3,3,3,5,5,5,5,5]

#     for j in range(1,10):
#         count[j] = count[j] + count[j-1]
#     # # arr = [170,45,75,90,802]
#     k = n-1
#     while k >= 0:
#         digit = (arr[k] // exp)%10
#         output[count[digit]-1] = arr[k]
#         count[digit] = count[digit] - 1
#         k = k-1

#     for i in range(0,len(arr)):
#         arr[i] = output[i]


# def radix_sort(arr):
#     max_num = get_max(arr)
#     exp = 1
#     while max_num // exp > 0:
#         count_sort(arr,exp)
#         exp = exp * 10
    
#     return arr


# arr = [170,45,75,90,802]
# print(f"this is your sorted Array : {radix_sort(arr)}")


# Bucket Sort
'''
Range based sorting technique
elements ko chhote grp(buckets) ke andr baat dete h 
har bucket ke andr individually sort krte h
last me sab buckets ko combine kr dete h

'''

# Use case
'''
1. Data uniformly distributed
2. Floating numbers/small range ho
3. faster avg performance

'''
# maano ki 0-100 ki range h

# Aur hamne iss range ko 10 ke grps(bucket) me baat diya 0-9, 10-19, 20-29 ... 90-100

# bucket count = size of array
# bucket range  = ((max-min+1) // bucket_count) +1
# bucket index = (value-min_value)//bucket_range

# arr = [0.42,0.32,0.33,0.52,0.37,0.47,0.51]
# n = 7

# B0 B1 B2 B3 B4 B5 B6

# index = 0.42 * 7 = 2.94 --> 2
# 2,2,2,3,2,3,3

# B2 -> [0.42,0.32,0.33,0.37]
# B3 -> [0.52,0.47,0.51]

# B2 -> [0.32.0.33,0.37,0.42]
# B3 -> [0.47,0.51,0.52]


# sorted_arr = B2 + B3
# ->  [0.32.0.33,0.37,0.42,0.47,0.51,0.52]

# insertion sort

# hath me cards -> 7,3,5,2

# Rules:
# 1. Left part hmesha sorted rakhte
# 2. Right side se ek element uthate hai
# 3. usko correct position pr insert kr dete h

# arr -> [8,3,5,2]
#  [8 | 3,5,2]
#  [3,8 | 5,2]
#  [3,5,8 | 2]
#  [2,3,5,8] --> Sorted 


# def insertion_sort(arr):
#     n = len(arr)

#     for i in range(1,n): # 1,2,3
#         key = arr[i] # key = 2
#         j = i-1 # j = 2
#         while j >= 0 and arr[j] > key: # yes and yes --> yes
#             arr[j+1] = arr[j] # arr[1] --> 3
#             j = j-1 # -1

#         arr[j+1] = key # arr[0] = 2 , arr = 2,3,5,8

#     return arr

# # Bucket sort ka code

# def bucket_sort(arr):
#     n = len(arr)
#     min_val = arr[0]
#     max_val = arr[0]
    
#     for i in range(n):
#         if min_val>arr[i]:
#             min_val = arr[i]
#         if max_val<arr[i]:
#             max_val = arr[i]
    

#     print(f"max value {max_val}")
#     print(f"min value {min_val}")


#     bucket_count = n
#     buckets = [[] for _ in range(bucket_count)]
#     # Normalize index calculation for any range
#     for i in range(n):
#         # Avoid division by zero if all elements are the same
#         if max_val == min_val:
#             index = 0
#         else:
#             index = int(((arr[i] - min_val) / (max_val - min_val)) * (bucket_count - 1))
#         buckets[index].append(arr[i])

#     for k in range(bucket_count):
#         buckets[k] = insertion_sort(buckets[k])

#     idx = 0
#     for i in range(bucket_count):
#         for j in range(len(buckets[i])):
#             arr[idx] = buckets[i][j]
#             idx += 1

#     return arr


# arr = [0.42,0.32,0.33,0.52,0.37,0.47,0.51]

# print(f"sorted array is {bucket_sort(arr)}")

# stable sorting : [3,1,1,5]


# Bubble Sort: [5,3,4,1]
# 5 > 3 : Swap --> [3,5,4,1]
# 5 > 4 : Swap --> [3,4,5,1]
# 5 > 1 : Swap --> [3,4,1,5]

# Through loop
# def Bubble_Sort(arr): # arr = [5,3,4,1]
#     n = len(arr) # 4

#     for i in range(n): # 0,1,2,3
#         swapped = False # False

#         for j in range(0,n-i-1): # 0
#             if arr[j] > arr[j+1]: # True
#                 temp = arr[j] 
#                 arr[j] = arr[j+1]
#                 arr[j+1] = temp # [1, 3, 4, 5]
#                 swapped = True # True

#         if swapped == False:
#             break

#     return arr

# arr = [5,3,4,1]
# print(f"your sorted array is : {Bubble_Sort(arr)}")


# Through recursion
# def Bubble_Sort(arr,n):
    
#     if n == 1:
#         return arr
    
#     i = 0
#     while(i<n-1):
#         if arr[i] > arr[i+1]:
#             temp = arr[i]
#             arr[i] = arr[i+1]
#             arr[i+1] = temp

#         i = i+1

#     return Bubble_Sort(arr,n-1)

# arr = [5,3,4,1]
# print(f"your sorted array is : {Bubble_Sort(arr,len(arr))}")

# Selection sort:

# base idea: har pass me poore unsorted part se sabse chhota chuno aur shuru me rakh do

# arr = [5,3,4,1]
# pass 1 --> [1,5,3,4]
# pass 2 --> [1,3,5,4]
# pass 3 --> [1,3,4,5]

# start with loop

# def selection_sort(arr):
#     n = len(arr)

#     for i in range(n):
#         min_index = i
#         for j in range(i+1,n):
#             if arr[j] < arr[min_index]:
#                 min_index = j
            

#         if min_index != i:
#             temp = arr[i]
#             arr[i] = arr[min_index]
#             arr[min_index] = temp

#     return arr

# arr = [5,3,4,1]
# print(f"your sorted array is : {selection_sort(arr)}")


# Recursion:

# def selection_sort(arr,n,start):
#     if start == n-1:
#         return arr
    
#     min_index = start

#     j = start+1
#     while(j<n):
#         if arr[j] < arr[min_index]:
#             min_index = j
#         j = j+1

#     if min_index != start:
#         temp = arr[start]
#         arr[start] = arr[min_index]
#         arr[min_index] = temp

#     return selection_sort(arr,n,start+1) 

# arr = [8,2,4,9]
# print(f"your sorted arr is {selection_sort(arr,len(arr),0)}")  


# Quick Sort:


# arr = [10,80,30,90,40,50,70]


# def partition(arr,low,high):
#     mid = low + (high-low) // 2

#     pivot = arr[mid]

#     i = low
#     j = high

#     while i <= j:

#         while arr[i] < pivot:
#             i = i + 1

#         while arr[j] > pivot:
#             j = j - 1

#         if i <= j:
#             arr[i], arr[j] = arr[j], arr[i]
#             i = i+1
#             j = j-1


#     return i

# def quick_sort(arr,low,high):
#     if low < high:
#         index = partition(arr,low,high)

#         quick_sort(arr,low,index-1)

#         quick_sort(arr,index,high)

#     return arr


# arr = [10,80,30,90,40,50,70]
# result = quick_sort(arr,0,len(arr)-1)

# print(f"sorted arr is {result}")


# time complexity : n(logn)
        
# ::::Merge Sort::::

# def merge_sort(arr,left,right):
#     print(f"Left is {left} = {arr[left]} and Right is {right} = {arr[right]}")
#     if left<right:
#         mid = left + (right-left) // 2
#         print(f"mid = {mid}")

#         # left part
#         merge_sort(arr,left,mid)
        
#         # right part
#         merge_sort(arr,mid+1,right)

#         # Merge both parts
#         merge(arr,left,mid,right)


# def merge(arr,left,mid,right):
#     n1 = mid-left+1 # [9,5,1] 
#     print(f"length of left sub-array = {n1}")
#     n2 = right - mid # [8,6,4] 
#     print(f"length of right sub-array = {n2}")

#     L = [0] * n1
#     print(f"initialized left sub-array: {L}")
#     R = [0] * n2
#     print(f"initialized right sub-array: {R}")

#     for i in range(n1):
#         print(f"indexing starts with left = {left}, i = {i}, index = arr[left+1] = arr[{left+i}] = {arr[left+i]}")
#         L[i] = arr[left+i]
#         print(f"at index {i} of Left subarray  = {L[i]}")

#     for j in range(n2):
#         print(f"indexing starts with right = {right}, j = {j}, index = arr[mid+1+j] = arr[{mid+1+j}] = {arr[mid+1+j]}")
#         R[j] = arr[mid+1+j]
#         print(f"at index {j} of Right subarray  = {R[j]}")

#     i = 0
#     j = 0
#     k = left
#     print(f"here k is {left}")

#     while i<n1 and j<n2:
#         print(f"now we start comparing and filling data in original arr")
#         if L[i] <= R[j]:
#             print(f"L[{i}] <= R[{j}] means {L[i]} <= {R[j]}")
#             arr[k] = L[i]
#             print(f"so at index {k} of arr we have L[{i}] means at arr[{k}] = {L[i]}")
#             i = i+1

#         else:
#             print(f"L[{i}] > R[{j}] means {L[i]} > {R[j]}")
#             arr[k] = R[j]
#             print(f"so at index {k} of arr we have R[{j}] means at arr[{k}] = {R[j]}")
#             j = j+1

#         k = k+1


#     while i < n1:
#         print(f"so we have remaining part of Left Subarray as {i} < {n1}")
#         arr[k] = L[i]
#         print(f"so at index {k} of arr we have L[{i}] means at arr[{k}] = {L[i]}")
#         i = i+1
#         k = k+1

#     while j<n2:
#         arr[k] = R[j]
#         print(f"so at index {k} of arr we have R[{j}] means at arr[{k}] = {R[j]}")
#         k = k+1


# arr = [9,5,1,8,6,4]

# print(f"your unsorted array is {arr}")

# merge_sort(arr,0,len(arr)-1)

# print(f"your sorted array is {arr}")

