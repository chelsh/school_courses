first = 1
while True:
    user = input()
    if user == "END":
        break

    else:
        if first == 1:
            print("C")
            first = 0
            post = user
        else:
            print(post)
            post = user