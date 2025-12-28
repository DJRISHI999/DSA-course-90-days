# # last class h/w solutions

# i = 1
# count = 0
# n = 81
# while i<= n:
#     i = i*3
#     count += 1
#     print(count)
# # time complexity = ?
# # How many steps for n = 81?

# # i = 1, n = 81
# # 1st iteration ---> 3
# # 2nd iteration ---> 3*3
# # 3rd iteration ---> 3*3*3
# # 4th iteration ---> 3*3*3*3
# # 5th iteration ---> 3*3*3*3*3
# # output ---> i = 243, total iterations = 5, time complexity = O(logn)


# def f(n):
#     if n==1:
#         return
#     f(n-1)
# # Time ?
# # Space ?

# # n = 5
# # f(5) and function stops at n = 1
# # f(5)--->f(4)-->f(3)--->f(2)--->f(1) <break>


# modulo %

# condition check before every iteration = n > 0

# 1st iteration:
# 487 % 10 = 7
# 487 // 10 = 48

# 2nd iteration:
# 48 % 10 = 8
# 48 // 10 = 4

# 3rd iteration:
# 4 % 10 = 4
# 4 // 10 = 0
# iterate the digits in a given
# n = 487
# while n > 0:
#     digit = n%10
#     print(digit)
#     # trimming
#     n = n // 10
# prime number = 1 or itself
# check if a number prime or not = 1>i and i<n

# n = 20
# for i in range(2,n): # 2 -> 19
#     if n % i == 0:
#         print("imposter spotted... IT is not a PRIME")
#         break
#     else:
#         print("NO IMPOSTER TILL NOW")
#         continue

n = a X b
96 = 1,2,3,4,6,8,|9|,12,16,24,48,96





# prime number = 1 or itself
# check if a number prime or not = 1>i and i<n
n = 97
for i in range(2,math.sqrt(n)):
    if n % i == 0:
        print("number is not prime")
        break
    else:
        print("yes its prime")
        continue

O(n)
O()
# n = a X b
# _/n
# 16 = 1,2,4,8,16
# 96 = 1,2,3,4,6,8,|9|,12,16,24,48,96
# 7 = 1 |2| 7



# GCD achha logic
# gcd(a,b) = max(factor of a , factors of b)

# 2->_/n
# another_pair = n // i

gcd = 0
a = [1,2,4,8]
b = [1,2,4,8,16]
if gcd < i:


# example = 8,16
# 16 % 8 = 2
# gcd(a,b) = gcd(b,a%b)

# gcd(48,18)
# 48 % 18 = 12 -> gcd(18,12)
# 18 % 12 = 6 -> gcd(12,6)
# 12 % 6 = 0 -> gcd = 6

# def gcd(a,b):
#     while b!=0:
#         a,b = b,a%b
#     return a

# print(gcd(356,712))

'''
LCM X GCD = a X b
6,9
LCM = 18
GCD = 3

LCM X GCD = 54
6 X 9 = 54

=> LCM X GCD = a X b
=> LCM = (a X b) / GCD
'''
"""
def gcd(a,b):
    while b!=0:
        a,b = b,a%b
    return a

def lcm(a,b):
    product = a*b
    return product//gcd(a,b)

print(lcm(6,9))

"""
i <= _/n
i*i <= n
for(int i =0;i*i <= n;i++){

}


# print all prime numbers b/w 1 to N
# given a number n, count total divisors
"""
for(int i=1; i*i<=n; i++){
    if(n%i==0){
        //some work is done here
    }
}

time complexity = ?
 """

'''
why Euclid Algorithm is O(log n) and not O (_/n)?

'''









'''







'''









