a = int(input("Input your number: "))
ans = ['±' + str(i) for i in range(1, abs(a + 1)) if a % i == 0]
for i in ans:
    print(i, end=' ')


# The same code but with repeating divisors which annoy me
"""
a = int(input("Input your number: "))
ans = [i for i in range(-abs(a + 1), abs(a + 1)) if i != 0 and a % i == 0]
for i in ans:
    print(i, end=' ')
"""
