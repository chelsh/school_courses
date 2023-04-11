# if __name__ == '__main__':
#     ary = []
#     d_ary = []
#     for i in range(10):
#         ary.append(i + 10)
#         print("{:3d}".format(ary[i]), end = " ")
#     print("_____________________________________")
#     for i in range(3):
#         d_ary.append([])
#         for j in range(5):
#             d_ary[i].append(i + j)
#             print("{:3d}".format(d_ary[i][j]), end = " ")
#         print()

# # typing 모듈
# from typing import *
# def repeat(message: str, times: Optional[int] = None) -> list:    # Optional !!
#     if times:
#         return [message] * times
#     else:
#         print("else")
#         return [message]

# print(repeat("Hello!", 5))



# def multi(L):
#     lL = []
#     rL = []
#     result = []
#     n = 1
#     for i in range(len(L)):
#         n *= L[i]
#         lL.append(n)
#     n = 1
#     for i in range(len(L) - 1, -1, -1):
#         n *= L[i]
#         rL.append(n)
#     rL.reverse()

#     for i in range(len(L)):
#         if i == 0:
#             result.append(rL[i + 1])
#         elif i == len(L) - 1:
#             result.append(lL[i - 1])
#         else:
#             result.append(lL[i - 1] * rL[i + 1])
#     return result

# numList = [int(i) for i in input().split()]
# print(multi(numList))



# def push(stack,item):
#     stack.append(item)
# def pop(stack):
#     if len(stack) != 0:
#         item = stack.pop(-1)# stack.pop()
#         return item
#     else:
#         empty()
# def empty():
#     print("Stack is Empty")
# def top(stack):
#     if len(stack) != 0:
#         return stack[-1]
#     else:
#         empty()
# if __name__ == '__main__':
#     me = []
#     pop(me)
#     push(me,'apple')
#     push(me,'orange')
#     push(me,'cherry')
#     print(me)
#     print(top(me))
#     pop(me)
#     print(me)



