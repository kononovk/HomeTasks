from hw4.t01.smile_logic import bracket_correct

if __name__ == '__main__':
    if bracket_correct(input("Input your string: ")):
        print("String is correct")
    else:
        print("String is  incorrect")
