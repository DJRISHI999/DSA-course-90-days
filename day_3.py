# RECURSION:

# RULE : BASE CONDITION

'''
def function_name(n):
    if base_condition:
        return
    function_name(smaller_size)


'''

# n = 20
# fun(20)
# fun(19)
# fun(18)
# .
# .
# .

# if n == 1:
#     return 
# fun(1)
# print(n)




# 1->20

# def fun(n):
#     if n==0:
#         return
#     fun(n-1)

# fun(3)

# fun(3)
# fun(2)
# fun(1)
# fun(0) --> stop



# def fun(n):
#     if n==0:
#         return
#     fun(n-1)
#     print(n, end=" ")



# def fun(n):
#     if n == 0:
#         return 1
#     return n * fun(n-1)


# def fun(n):
#     if n == 0:
#         return 0
#     return n + fun(n-1)


# 0 1 1 2 3 .... 

# def fun(n):
#     if n == 0 or n == 1:
#         return n
#     return fun(n-1) + fun(n-2)
    
     
# n = 6
# print(fun(n))

'''
fun(6) ---> return fun(5) + fun(4)

fun(2) ---> return fun(0) + fun(1) ---> return 1

'''