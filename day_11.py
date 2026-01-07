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

def count_sort(arr):
    min = 0
    max = 0

    for i in range(len(arr)):
        if arr[i] >= min:
            pass
        else:
            min = arr[i]
    
    for j in range(len(arr)):
        if arr[j] <= max:
            pass
        else:
            max = arr[j]

    count = [0] * (max+1) #count = [0,0,0,0]

    for num in arr:
        count[num] = count[num] + 1

    traversing_counter = 0
    sorted_arr = [0,0,0,0,0]
    for i in range(len(count)):
        while count[i] > 0:
            print(f"traversing_counter {traversing_counter}")
            print(f"value of count at {i}th index: {count[i]}")
            sorted_arr[traversing_counter] = i
            traversing_counter = traversing_counter + 1
            count[i] = count[i]-1

    return sorted_arr
        
arr = [1,3,2,3,1]
print(count_sort(arr))