#1
a = int(input())
b = int(input())
A = a; B = b
i = 1
while A <= B:
    if i % 2 != 0:
        A += 10000
    else:
        A *= 1.07
    B *= 1.02
    i += 1
print(i - 1)

#2
N = int(input())
i = 1
result = 0
while i <= N ** (1 / 2):
    if N % i == 0:
        result += i
        if N != i * i:
            result += N / i
    i += 1
print("YES" if result == N * 2 else "NO")

#3
players = input().split()
game = [i for i in input().split()]
game_dict = {}
for i in range(len(game) - 1):
        game_dict[game[i]] = game[i + 1]
game_dict[game[-1]] = game[0]
loser = input()
N = int(input())
for i in range(N):
    loser = game_dict[loser]
print(loser)

#3
players = input().split()
game = [i for i in input().split()]
l = len(game)
first = input()
N = int(input())
f = game.index(first)
r = N % l
if r < l - f:
    print(game[f + r])
else:
    print(game[r - l + f])


#4
students = input().split()
cnt = 0
for std in students:
    if std[-1] == '고' or std[-1] == '려' or std[-1] == '대':
        cnt += 1
print(cnt)

#5
word = input()
if len(word) == len(set(word)):
    print("YES")
else:
    print("NO")