a = int(input("Input your number: "))
ans = [i for i in range(1, a + 1) if a % i == 0]
print(ans)
