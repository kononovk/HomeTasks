def num_of_dividers(inp_num):
    dividers = [i for i in range(-abs(inp_num), abs(inp_num) + 1) if i != 0 and inp_num % i == 0]
    return dividers


if __name__ == '__main__':
    num = int(input("Input your number: "))
    print(num_of_dividers(num))
