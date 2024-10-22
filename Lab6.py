# Graham Johnston

def encode(password: str) -> str:
    encoded_password = ''.join(str((int(d) + 3) % 10) for d in password)

    return encoded_password

def decode():
    pass

if __name__ == '__main__':
    # Print looping menu
    while True:
        print('\nMenu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')

        # Prompt for menu option
        menu_option = input('\nPlease enter an option: ')

        if menu_option == '1':
            password = input('Please enter your password to encode: ')
            encoded_password = encode(password)
            print('Your password has been encoded and stored!')
            print(encoded_password)

        if menu_option == '2':
            pass

        if menu_option == '3':
            break