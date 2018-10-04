from t03 import num_of_dividers

inp_num = int(input("Input your number: "))

if len(num_of_dividers(inp_num)) == 4:
    print("This number is prime")
else:
    print("This number is not prime")
