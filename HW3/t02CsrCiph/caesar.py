from HW3.t02CsrCiph.caesar_logic import encrypt, decrypt
from termcolor import colored

if __name__ == '__main__':
    cipher_flag = input("Do you want encrypt or decrypt your message?\nPress(e/d): ")
    user_text = input("Input text: ")
    user_offset = int(input("Input offset: "))

    if cipher_flag == 'e':
        print("The encryption of your text is " + colored(encrypt(user_offset, user_text), 'yellow', attrs=['bold']))
    elif cipher_flag == 'd':
        print("The decryption of your text is " + colored(decrypt(user_offset, user_text), 'yellow', attrs=['bold']))
