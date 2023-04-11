#Exercise 1
L = []
result = []
while True:
    std = input()
    if std == "END":
        break
    else:
        L.append(std.split())
for i in range(len(L)):
    if int(L[i][0][:4]) >= 2020:
        result.append(L[i][1])
print(result)

#Exercise 2
print([int(int(i) / 2) for i in input().split()])

#Exercise 3
S = list(input());C = input()
n = 0
for i in S:
    if i == C:
        n += 1
print(n)

#Exercise 4
scores = [int(n) for n in input().split()]
for i in scores:
    if i <= min(scores):
        scores.remove(i)
print(scores)

#Exercise 5
S = input().split()
result = []
for i in range(len(S)):
    if S[i][-1] == ',' or S[i][-1] == '.':
        S[i] = S[i][:-1]
        result.append(S[i])
    elif S[i] != 'a' or S[i] != 'an' or S[i] != 'the':
        result.append(S[i])
print(" ".join(result))