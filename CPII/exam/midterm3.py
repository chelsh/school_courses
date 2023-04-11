word = input()
answer = input()
result = []

for i in range(len(word)):
    if answer[i] == word[i]:
        result.append('O')
    
    elif answer[i] in word:
        result.append('?')

    else:
        result.append('X')

for i in range(len(word)):
    print(result[i], end = "")