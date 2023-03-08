# Bhagyesh Jethwani


def encode(user_password):
    encoded = ''
    for char in user_password:
        encoded += str(int(char) + 3)
    print("Your password has been encoded and stored!")
    return encoded


def decode():
    pass


if __name__ == '__main__':
    exit_program = False
    while not exit_program:
        print("Menu")
        print("---------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")
        user_option = input("Please enter an option: ")
        if user_option == '1':
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
        elif user_option == '2':
            decode()
        elif user_option == '3':
            exit_program = True

