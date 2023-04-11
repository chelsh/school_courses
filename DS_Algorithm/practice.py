# #삽입
# from itertools import count
# from typing import List
# N = 7
# def insert(data: List[int], location : int, value : int):
#     global count
#     if location > N - 1 or count > N:
#         raise IndexError
#     for i in range(N - 1, location, -1):
#         data[i] = data[i - 1]
#     data[location] = value
#     count += 1

# def delete(data : List[int], location ; int):
#     global count
#     if location > N - 1 or 


n = int(input())

for i in range(n):
    for j in range(i * i):
        n += n

