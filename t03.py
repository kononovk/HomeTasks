a = int(input("Input your number: "))
ans = [i for i in range(-abs(a), abs(a) + 1) if i != 0 and a % i == 0]
for i in ans:
    print(i, end=' ')
