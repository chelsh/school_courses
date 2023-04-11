# page 6
# def twoSum(data, target):
#     var_key = {}
#     for i, var in enumerate(data):
#         var_key[var] = i
#     for v in var_key.keys():
#         numToFind = target - v
#         if numToFind in var_key.keys():
#             return [var_key[v], var_key[numToFind]]

# nums = [1,5,4,9,13,3,8,7,6,10,14,16,2,11]
# print(twoSum(nums, 19))




# page 7

# def palindrome(data: str) -> bool:
#     strList = []
#     for char in data:
#         if char.isalpha():
#             strList.append(char.lower())
#     while len(strList) > 1:
#         if strList.pop(0) != strList.pop(-1):
#             return False
#     return True

# if __name__ == "__main__":
#     data = input()
#     print(f"isPalindrome -> {palindrome(data)}")

 