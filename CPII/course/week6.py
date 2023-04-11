# 버블 정렬
def bubble_sort(L):
    i = 1
    length = len(L)

    while (i < length):
        j = 0
        while (j < length - 1):
            if (L[i] < L[j]):
                L[i], L[j] = L[j], L[i]
            j += 1
        i += 1
    





 




# numbers = [8, 3, 4, 2, 6, 1, 9, 5, 7]
# i = 1
# length = len(numbers)
# while i < length:
#     j = 0
#     while j < length - i:
#         if numbers[j] > numbers[j + 1]:
#             numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
#         j += 1
#     i += 1
#     print(numbers)