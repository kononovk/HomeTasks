a = int(input("Input your number: "))
for i in range(2, int(a**0.5) + 1):
    if a % i == 0:
        print('{} is not prime'.format(a))
        exit(0)
print('{} is prime'.format(a))


