# Bhagyesh Jethwani

# encode function which encodes password
def encode(user_password):
    encoded = ''
    for char in user_password:
        if char == '7':
            encoded += '0'
        elif char == '8':
            encoded += '1'
        elif char == '9':
            encoded += '2'
        else:
            encoded += str(int(char) + 3)
    return encoded


# decode function to be written by partner
def decode(encoded):
    pass


# main function
if __name__ == '__main__':
    exit_program = False
    encoded_password = ''
    # loop runs until user wants to exit
    while not exit_program:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")
        user_option = input("Please enter an option: ")
        # test cases for user input
        if user_option == '1':
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!\n")
        elif user_option == '2':
            decoded_password = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}")
        elif user_option == '3':
            exit_program = True
