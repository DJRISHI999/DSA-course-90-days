# Backtracking -> Recursion + choices + all possible answers

# 1. password finding -> 0 / 1, 3 digit, all possible combinations using recursion
# Normal Human Brain: _ _ _
# position 1 : 0/1
# position 2 : 0/1
# position 3 : 0/1

# 1
# 1
# 0


# 110



"""
def binary(n,ans):
    if n == 0:
        print(ans)
        return
    binary(n-1,ans+"0")
    binary(n-1,ans+"1")    
    

binary(3,"")
"""


# subset of strings
# "abc" --> abc, ab, bc, ac, a, b ,c
# normal human:
# a
# 
# 


"""def subsets(s,i,curr):
    if i == len(s):
        print(curr)
        return
    
    subsets(s,i+1,curr+s[i])
    subsets(s,i+1,curr)
    
subsets("abc",0,"")"""



# permutation "abc"
# c
# 0,n-1
# [start:end-1]
# if i = 0, permute(s[:0]+s[1:], ""+s[0])
"""def permute(s,ans):
    if len(s)==0:
        print(ans)
        return
    
    for i in range(len(s)):
        permute(s[:i]+s[i+1:], ans+s[i])

permute("abc","")
"""

# THE MAZE

maze = [

    [1,1,0],
    [1,1,0],
    [0,1,1]
]

def solve_maze(i,j,path):
    if i == len(maze)-1 and j == len(maze[0])-1:
        print(path)
        return

    if i>=len(maze) or j>=len(maze[0]) or maze[i][j] == 0:
        return
    
    # visited
    maze[i][j] = 0

    # move down
    solve_maze(i+1,j,path+"D")

    # move right
    solve_maze(i,j+1,path+"R")

    # Backtrack: mark cell as unvisited for other parts
    maze[i][j] = 1

solve_maze(0,0,"")