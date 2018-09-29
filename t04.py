a = int(input("Input your number: "))
ans = [i for i in range(-abs(a + 1), abs(a + 1)) if i != 0 and a % i == 0]
if len(ans) == 4:
    print("THis number is prime")
else:
    print("This number is not prime")