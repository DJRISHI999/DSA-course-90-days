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

def get_max(arr):
    max_val = arr[0]
    for i in range(1,len(arr)-1):
        if arr[i] > max_val:
            max_val = arr[i]
        else:
            pass

    return max_val

# 50 = 50 // 10 = 
# 5 % 10 = 5 


# 5418412 = 5418412 // 100000 = 54 % 10 = 4

def count_sort(arr,exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    
    for i in range(0,n):
        digit = (arr[i] // exp) % 10
        count[digit] += 1

        # [2,0,1,0,0,2,0,0,0,0]

# count = [2,3,3,3,5,5,5,5,5]

    for j in range(1,10):
        count[j] = count[j] + count[j-1]
    # # arr = [170,45,75,90,802]
    k = n-1
    while k >= 0:
        digit = (arr[k] // exp)%10
        output[count[digit]-1] = arr[k]
        count[digit] = count[digit] - 1
        k = k-1

    for i in range(0,len(arr)):
        arr[i] = output[i]


def radix_sort(arr):
    max_num = get_max(arr)
    exp = 1
    while max_num // exp > 0:
        count_sort(arr,exp)
        exp = exp * 10
    
    return arr


arr = [170,45,75,90,802]
print(f"this is your sorted Array : {radix_sort(arr)}")