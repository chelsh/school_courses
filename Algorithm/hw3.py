#1
def g(n):
    if n <= 1:
        return n
    else:
        return 5 * g(n-1) - 6 * g(n - 2)



#2
import math
def i(y, z):
    if z == 0:
        return 0
    elif z % 2 == 1:
        return i(2*y, math.floor(z/2)) + y
    else:
        return i(2*y, math.floor(z/2))
    
for j in range(10):
    for k in range(10):
        print(j , k, i(j,k))




# def i(y, z):
#     try:
#         if z == 0:
#             return 0
#         elif z % 2 == 1:
#             if math.floor(z / 2) + y == z:
#                 return 1111
#             return i(2*y, math.floor(z / 2) + y)
#         else:
#             return i(2*y, math.floor(z / 2))
#     except:
#         return 1111
    
    
# for j in range(10):
#     for k in range(10):
#         res = i(j,k)
#         print(res)
#         if not res:
#             print(j ,k, res)

# print(i(5,4))




#3
import sys 

N = int(sys.stdin.readline())  
nums = [] 
for n in range(N):
    nums.append(sys.stdin.readline())

small = []
large = []


def minmax(L):
    pass