# recursion Tree:




# memoization(top-down approach)
# def fib(n,dp={}):
#     if n == 0 or n == 1:
#         return n
    
#     if n in dp:
#         return dp[n]
#     dp[n] = fib(n-1,dp) + fib(n-2, dp)
#     return dp[n]


# tabulation (bottom up approach)
"""
This method basically removes the recursion and we calculate from smaller to lager ones

"""


# def fib(n):
#     a,b = 0, 1
#     print(0, end=" ")
#     for i in range(n):
#         a,b = b, a+b
#         print(a, end=" ")

# fib(6)
    


# count number of digits

def count_digits(n):
    if n == 0:
        return 0
    return (n%10) + count_digits(n//10)

# dry run

# n = 589
#  count_digits(589)
#         [  condition ]
#      return 3

#  count_digits(58)
#         [  condition ]
#      return 2


#  count_digits(5)
#         [  condition ]
#      return 1

#  count_digits(0)
#         [  condition True]
                # return 0



